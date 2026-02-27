#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from create_msgs.msg import Bumper
import random
import time

class RoombaAutoLogic(Node):
    def __init__(self):
        super().__init__('roomba_auto_logic')
        
        # Publisher do sterowania
        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        
        # Subskrypcja zderzaka
        self.bump_sub = self.create_subscription(Bumper, '/bumper', self.bump_callback, 10)
        
        # Timer logiki (20Hz)
        self.timer = self.create_timer(0.05, self.control_loop)
        
        # Stan maszyny
        self.state = "SPIRAL"
        self.spiral_time = 0.0
        self.recovery_start_time = 0.0
        self.is_bumped = False
        
        self.get_logger().info("TRYB AUTO: URUCHOMIONO. Rozpoczynam sprzątanie spiralne.")

    def bump_callback(self, msg):
        if (msg.is_left_pressed or msg.is_right_pressed) and self.state != "RECOVERY":
            self.get_logger().warn("KOLIZJA! Przechodzę w tryb RECOVERY.")
            self.state = "RECOVERY"
            self.recovery_start_time = time.time()
            self.is_bumped = True

    def control_loop(self):
        twist = Twist()
        now = time.time()

        if self.state == "SPIRAL":
            # Zwiększamy promień spirali w czasie
            self.spiral_time += 0.05
            twist.linear.x = 0.2  # Stała prędkość do przodu
            # Zmniejszająca się prędkość obrotowa = rosnący promień
            twist.angular.z = max(0.1, 1.5 - (self.spiral_time * 0.02))
            
        elif self.state == "RECOVERY":
            elapsed = now - self.recovery_start_time
            if elapsed < 0.8:
                # Krok 1: Wycofaj się
                twist.linear.x = -0.1
                twist.angular.z = 0.0
            elif elapsed < 2.0:
                # Krok 2: Obróć się o losowy kąt
                twist.linear.x = 0.0
                twist.angular.z = 1.2 if random.random() > 0.5 else -1.2
            else:
                # Powrót do sprzątania
                self.get_logger().info("Przeszkoda ominięta. Nowa spirala.")
                self.state = "SPIRAL"
                self.spiral_time = 0.0
                self.is_bumped = False

        self.cmd_pub.publish(twist)

def main():
    rclpy.init()
    node = RoombaAutoLogic()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.cmd_pub.publish(Twist()) # Stop
    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    main()