#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty

class CrossVersionTeleop(Node):
    def __init__(self):
        super().__init__('cross_version_teleop')
        
        # Publishery - będą publikować w sieć, Humble je odbierze
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.vacuum_pub = self.create_publisher(Empty, '/vacuum_motor', 10)
        self.brush_pub = self.create_publisher(Empty, '/main_brush_motor', 10)
        
        self.joy_sub = self.create_subscription(Joy, '/joy', self.joy_callback, 10)
        
        self.linear_limit = 0.3
        self.angular_limit = 1.0

        print("--- TELEOP ROLLING -> HUMBLE READY ---")
        print("Kierowanie: PRAWY ANALOG | Gaz: L1")

    def joy_callback(self, msg):
        # 1. JAZDA (L1 + Prawy Analog)
        # Na Rolling PS3: Prawy X = axes[2], Prawy Y = axes[5]
        twist = Twist()
        if msg.buttons[4]: # L1
            twist.linear.x = msg.axes[5] * self.linear_limit
            twist.angular.z = msg.axes[2] * self.angular_limit
        self.cmd_vel_pub.publish(twist)

        # 2. SILNIKI (Humble Topics)
        if msg.buttons[2]: # Triangle
            self.vacuum_pub.publish(Empty())
            self.get_logger().info("Wysłano: Toggle Vacuum")
            
        if msg.buttons[0]: # Cross
            self.brush_pub.publish(Empty())
            self.get_logger().info("Wysłano: Toggle Brushes")

def main():
    rclpy.init()
    rclpy.spin(CrossVersionTeleop())
    rclpy.shutdown()

if __name__ == '__main__':
    main()