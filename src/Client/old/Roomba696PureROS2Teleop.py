#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty

class RoombaPureTeleop(Node):
    def __init__(self):
        super().__init__('roomba_pure_teleop')
        
        # Publishery do jazdy i silników
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.vacuum_pub = self.create_publisher(Empty, '/vacuum_motor', 10)
        self.main_brush_pub = self.create_publisher(Empty, '/main_brush_motor', 10)
        self.side_brush_pub = self.create_publisher(Empty, '/side_brush_motor', 10)
        
        # Subskrypcja pada
        self.joy_sub = self.create_subscription(Joy, '/joy', self.joy_callback, 10)
        
        # Parametry
        self.max_linear_speed = 0.25 
        self.max_angular_speed = 1.2
        self.speed_multiplier = 1.0

        # Mapowanie osi i przycisków (Rolling/PS3)
        self.L1 = 4
        self.R1 = 5
        self.R2 = 7
        self.TRIANGLE = 2
        self.CROSS = 0
        self.AXIS_RIGHT_X = 2 # Skręcanie
        self.AXIS_RIGHT_Y = 5 # Przód/Tył

        self.print_legend()

    def print_legend(self):
        print("\n" + "="*45)
        print("   ROOMBA 696 PURE ROS2 TELEOP - LEGENDA")
        print("="*45)
        print(" L1 (Trzymaj)    : GAZ")
        print(" Prawy Analog    : JAZDA (Góra/Dół) + SKRĘT (L/P)")
        print(" R1 / R2         : +/- PRĘDKOŚĆ")
        print(" Trójkąt         : TOGGLE ODKURZACZ (Vacuum)")
        print(" Krzyżyk         : TOGGLE SZCZOTKI (Main & Side)")
        print("="*45 + "\n")

    def joy_callback(self, msg):
        # 1. JAZDA PRZEZ /cmd_vel
        twist = Twist()
        if msg.buttons[self.L1]:
            twist.linear.x = msg.axes[self.AXIS_RIGHT_Y] * self.max_linear_speed * self.speed_multiplier
            twist.angular.z = msg.axes[self.AXIS_RIGHT_X] * self.max_angular_speed
        self.cmd_vel_pub.publish(twist)

        # 2. BIEGI
        if msg.buttons[self.R1]: 
            self.speed_multiplier = min(self.speed_multiplier + 0.1, 2.0)
            self.get_logger().info(f"Mnożnik prędkości: {self.speed_multiplier:.1f}")
        if msg.buttons[self.R2]: 
            self.speed_multiplier = max(self.speed_multiplier - 0.1, 0.5)
            self.get_logger().info(f"Mnożnik prędkości: {self.speed_multiplier:.1f}")

        # 3. SILNIKI PRZEZ DEDYKOWANE TOPIKI
        # W create_driver wysłanie Empty na te topiki zazwyczaj przełącza stan (Toggle)
        if msg.buttons[self.TRIANGLE]:
            self.vacuum_pub.publish(Empty())
            self.get_logger().info("Przełączam Odkurzacz")
            
        if msg.buttons[self.CROSS]:
            self.main_brush_pub.publish(Empty())
            self.side_brush_pub.publish(Empty())
            self.get_logger().info("Przełączam Szczotki")

def main():
    rclpy.init()
    node = RoombaPureTeleop()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    main()