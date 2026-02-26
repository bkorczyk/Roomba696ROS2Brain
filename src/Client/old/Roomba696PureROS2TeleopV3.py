#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
import socket
import time

class RoombaFinalFix(Node):
    def __init__(self):
        super().__init__('roomba_final_fix')
        
        # Komunikacja
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.joy_sub = self.create_subscription(Joy, '/joy', self.joy_callback, 10)
        
        # Bezpośrednie połączenie do ESP32 dla silników i trybów
        self.esp_ip = "192.168.88.103"
        self.esp_port = 8888
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Stan
        self.is_vacuum_on = False
        self.is_brush_on = False
        self.max_speed = 0.3

        # DIAGNOSTYKA MAPOWANIA (Zmień te indeksy jeśli pad reaguje inaczej)
        self.AXIS_RIGHT_X = 3  # Próbujemy 3 zamiast 2
        self.AXIS_RIGHT_Y = 4  # Próbujemy 4 zamiast 5
        self.BTN_L1 = 4        # Przycisk bezpieczeństwa

        try:
            self.sock.connect((self.esp_ip, self.esp_port))
            self.get_logger().info("POŁĄCZONO Z ESP32")
            self.print_legend()
        except Exception as e:
            self.get_logger().error(f"Błąd socketu: {e}")

    def print_legend(self):
        print("\n" + "!"*40)
        print(" L1 (Trzymaj) : BEZPIECZNIK JAZDY")
        print(" Prawy Analog : JAZDA")
        print(" Trójkąt      : ODKURZACZ")
        print(" Krzyżyk      : SZCZOTKI")
        print("!"*40 + "\n")

    def send_roi(self, data):
        try: self.sock.sendall(bytearray(data))
        except: pass

    def joy_callback(self, msg):
        # 1. JAZDA (L1 + Prawy Analog)
        twist = Twist()
        # Sprawdzamy czy L1 jest wciśnięty (jako button lub oś)
        l1_pressed = msg.buttons[self.BTN_L1] == 1
        
        if l1_pressed:
            # Pobieramy osie prawego analoga
            # Jeśli nadal nie działa, sprawdź ros2 topic echo /joy i ruszaj prawą gałką
            twist.linear.x = msg.axes[self.AXIS_RIGHT_Y] * self.max_speed
            twist.angular.z = msg.axes[self.AXIS_RIGHT_X] * 1.5
        else:
            twist.linear.x = 0.0
            twist.angular.z = 0.0
        
        self.cmd_vel_pub.publish(twist)

        # 2. SILNIKI (Symbole - mapowanie PS3: Cross=0, Triangle=2)
        if msg.buttons[2]: # Trójkąt
            self.is_vacuum_on = not self.is_vacuum_on
            self.update_motors()
            time.sleep(0.3)
            
        if msg.buttons[0]: # Krzyżyk
            self.is_brush_on = not self.is_brush_on
            self.update_motors()
            time.sleep(0.3)

    def update_motors(self):
        mask = 0
        if self.is_vacuum_on: mask |= 2
        if self.is_brush_on: mask |= 5 
        self.send_roi([128, 131, 138, mask]) # Budzimy i ustawiamy silniki
        self.get_logger().info(f"MOTORY: Vac:{self.is_vacuum_on} Brush:{self.is_brush_on}")

def main():
    rclpy.init()
    rclpy.spin(RoombaFinalFix())
    rclpy.shutdown()

if __name__ == '__main__':
    main()