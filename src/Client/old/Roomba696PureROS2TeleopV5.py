#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
from create_msgs.msg import MotorSetpoint # Wymaga zbudowanego create_msgs na Rolling!
import time

class RoombaPureROS2(Node):
    def __init__(self):
        super().__init__('roomba_pure_ros2_teleop')
        
        # Publishery do sterownika
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.vacuum_pub = self.create_publisher(MotorSetpoint, '/vacuum_motor', 10)
        self.main_brush_pub = self.create_publisher(MotorSetpoint, '/main_brush_motor', 10)
        self.side_brush_pub = self.create_publisher(MotorSetpoint, '/side_brush_motor', 10)
        
        # Subskrypcja Joy (lokalna na Rolling)
        self.joy_sub = self.create_subscription(Joy, '/joy', self.joy_callback, 10)
        
        # Parametry
        self.is_vacuum_on = False
        self.is_brush_on = False
        self.current_max_speed = 0.25
        self.last_buttons = [0] * 20 

        # Mapowanie osi i przycisków (Rolling/PS3)
        self.AXIS_RIGHT_X = 3  
        self.AXIS_RIGHT_Y = 4  
        self.BTN_L1 = 4        
        self.BTN_R1 = 5        
        self.BTN_R2 = 7        
        self.BTN_TRIANGLE = 2  
        self.BTN_CROSS = 0     

        self.get_logger().info("URUCHOMIONO TRYB PURE ROS 2 (ROLLING -> HUMBLE)")

    def joy_callback(self, msg):
        # 1. JAZDA
        twist = Twist()
        if len(msg.buttons) > self.BTN_L1 and msg.buttons[self.BTN_L1] == 1:
            twist.linear.x = msg.axes[self.AXIS_RIGHT_Y] * self.current_max_speed
            twist.angular.z = msg.axes[self.AXIS_RIGHT_X] * 1.5
        self.cmd_vel_pub.publish(twist)

        # 2. BIEGI (R1 / R2)
        if msg.buttons[self.BTN_R1] == 1 and self.last_buttons[self.BTN_R1] == 0:
            self.current_max_speed = min(self.current_max_speed + 0.1, 0.7)
            self.get_logger().info(f"PRĘDKOŚĆ: {self.current_max_speed:.2f}")

        if msg.buttons[self.BTN_R2] == 1 and self.last_buttons[self.BTN_R2] == 0:
            self.current_max_speed = max(self.current_max_speed - 0.1, 0.1)
            self.get_logger().info(f"PRĘDKOŚĆ: {self.current_max_speed:.2f}")

        # 3. SILNIKI (Przełączanie przez MotorSetpoint)
        if msg.buttons[self.BTN_TRIANGLE] == 1 and self.last_buttons[self.BTN_TRIANGLE] == 0:
            self.is_vacuum_on = not self.is_vacuum_on
            self.publish_motor_state('vacuum', self.is_vacuum_on)

        if msg.buttons[self.BTN_CROSS] == 1 and self.last_buttons[self.BTN_CROSS] == 0:
            self.is_brush_on = not self.is_brush_on
            self.publish_motor_state('brushes', self.is_brush_on)

        self.last_buttons = list(msg.buttons)

    def publish_motor_state(self, motor_type, state):
        val = 1.0 if state else 0.0
        msg = MotorSetpoint(duty_cycle=val)
        
        if motor_type == 'vacuum':
            self.vacuum_pub.publish(msg)
            self.get_logger().info(f"Odkurzacz: {val}")
        elif motor_type == 'brushes':
            self.main_brush_pub.publish(msg)
            self.side_brush_pub.publish(msg)
            self.get_logger().info(f"Szczotki: {val}")

def main():
    rclpy.init()
    node = RoombaPureROS2()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    main()