#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
from create_msgs.msg import MotorSetpoint

class RoombaSmoothTeleop(Node):
    def __init__(self):
        super().__init__('roomba_smooth_teleop')
        
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.vacuum_pub = self.create_publisher(MotorSetpoint, '/vacuum_motor', 10)
        self.brush_pub = self.create_publisher(MotorSetpoint, '/main_brush_motor', 10)
        self.side_brush_pub = self.create_publisher(MotorSetpoint, '/side_brush_motor', 10)
        
        self.joy_sub = self.create_subscription(Joy, '/joy', self.joy_callback, 10)
        
        # Timer do publikacji - 20Hz (co 0.05s)
        self.timer = self.create_timer(0.05, self.publish_twist)
        
        # Stan sterowania
        self.current_twist = Twist()
        self.is_l1_pressed = False
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

        self.get_logger().info("SMOOTH TELEOP READY - Interwał 20Hz")

    def joy_callback(self, msg):
        # Sprawdzamy L1
        self.is_l1_pressed = bool(msg.buttons[self.BTN_L1])
        
        if self.is_l1_pressed:
            self.current_twist.linear.x = msg.axes[self.AXIS_RIGHT_Y] * self.current_max_speed
            self.current_twist.angular.z = msg.axes[self.AXIS_RIGHT_X] * 1.5
        else:
            self.current_twist = Twist() # Zera

        # Biegi i silniki (pozostają na zdarzeniach, bo nie wymagają ciągłości)
        if msg.buttons[self.BTN_R1] == 1 and self.last_buttons[self.BTN_R1] == 0:
            self.current_max_speed = min(self.current_max_speed + 0.1, 0.8)
        if msg.buttons[self.BTN_R2] == 1 and self.last_buttons[self.BTN_R2] == 0:
            self.current_max_speed = max(self.current_max_speed - 0.1, 0.1)

        if msg.buttons[self.BTN_TRIANGLE] == 1 and self.last_buttons[self.BTN_TRIANGLE] == 0:
            self.is_vacuum_on = not self.is_vacuum_on
            self.vacuum_pub.publish(MotorSetpoint(duty_cycle=float(self.is_vacuum_on)))

        if msg.buttons[self.BTN_CROSS] == 1 and self.last_buttons[self.BTN_CROSS] == 0:
            self.is_brush_on = not self.is_brush_on
            m = MotorSetpoint(duty_cycle=float(self.is_brush_on))
            self.brush_pub.publish(m)
            self.side_brush_pub.publish(m)

        self.last_buttons = list(msg.buttons)

    def publish_twist(self):
        # Ta funkcja wysyła komendę co 0.05s, nawet jeśli pad milczy
        # To "karmi" failsafe sterownika i eliminuje żabkowanie
        self.cmd_vel_pub.publish(self.current_twist)

def main():
    rclpy.init()
    rclpy.spin(RoombaSmoothTeleop())
    rclpy.shutdown()

if __name__ == '__main__':
    main()