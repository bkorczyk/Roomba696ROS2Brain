#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
import socket
import time

class RoombaBruteforce(Node):
    def __init__(self):
        super().__init__('roomba_bruteforce')
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.joy_sub = self.create_subscription(Joy, '/joy', self.joy_callback, 10)
        
        self.esp_ip = "192.168.88.103"
        self.esp_port = 8888
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.is_vacuum_on = False
        self.is_brush_on = False
        self.current_max_speed = 0.25 
        self.last_buttons = [0] * 20 

        # Mapowanie
        self.AXIS_RIGHT_X = 3  
        self.AXIS_RIGHT_Y = 4  
        self.BTN_L1 = 4        
        self.BTN_R1 = 5        
        self.BTN_R2 = 7        
        self.BTN_TRIANGLE = 2  
        self.BTN_CROSS = 0     

        try:
            self.sock.connect((self.esp_ip, self.esp_port))
            self.get_logger().info("POŁĄCZONO. Próbuję wybudzić silniki w trybie FULL...")
            # Sekwencja budzenia: START (128) -> FULL (132)
            self.send_roi([128, 132])
            time.sleep(0.2)
        except Exception as e:
            self.get_logger().error(f"Błąd socketu: {e}")

    def send_roi(self, data):
        try:
            self.sock.sendall(bytearray(data))
        except:
            pass

    def joy_callback(self, msg):
        # Jazda
        twist = Twist()
        if len(msg.buttons) > self.BTN_L1 and msg.buttons[self.BTN_L1] == 1:
            twist.linear.x = msg.axes[self.AXIS_RIGHT_Y] * self.current_max_speed
            twist.angular.z = msg.axes[self.AXIS_RIGHT_X] * 1.5
        self.cmd_vel_pub.publish(twist)

        # Biegi
        if msg.buttons[self.BTN_R1] == 1 and self.last_buttons[self.BTN_R1] == 0:
            self.current_max_speed = min(self.current_max_speed + 0.1, 0.6)
        if msg.buttons[self.BTN_R2] == 1 and self.last_buttons[self.BTN_R2] == 0:
            self.current_max_speed = max(self.current_max_speed - 0.1, 0.1)

        # Silniki - Przełączanie
        if (msg.buttons[self.BTN_TRIANGLE] == 1 and self.last_buttons[self.BTN_TRIANGLE] == 0) or \
           (msg.buttons[self.BTN_CROSS] == 1 and self.last_buttons[self.BTN_CROSS] == 0):
            
            if msg.buttons[self.BTN_TRIANGLE]: self.is_vacuum_on = not self.is_vacuum_on
            if msg.buttons[self.BTN_CROSS]: self.is_brush_on = not self.is_brush_on
            
            self.apply_motors_bruteforce()

        self.last_buttons = list(msg.buttons)

    def apply_motors_bruteforce(self):
        mask = 0
        if self.is_vacuum_on: mask |= 2
        if self.is_brush_on: mask |= 5 
        
        self.get_logger().info(f"WYSYŁAM STRZAŁ DO SILNIKÓW: Mask={mask}")
        
        # Próbujemy "wstrzelić" komendę kilka razy z rzędu (Bruteforce)
        for _ in range(3):
            self.send_roi([128, 132]) # Wymuś FULL
            time.sleep(0.02)
            self.send_roi([138, mask]) # Ustaw silniki
            time.sleep(0.02)
        
        # Pikanie na potwierdzenie
        self.send_roi([140, 1, 1, 80, 8, 141, 1])

def main():
    rclpy.init()
    rclpy.spin(RoombaBruteforce())
    rclpy.shutdown()

if __name__ == '__main__':
    main()