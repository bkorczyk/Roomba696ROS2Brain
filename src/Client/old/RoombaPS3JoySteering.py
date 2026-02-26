#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
import std_msgs.msg

class RoombaTeleopNode(Node):
    def __init__(self):
        super().__init__('roomba_teleop_node')
        
        # Publisher do standardowego topica jazdy
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        
        # Subskrypcja pada
        self.joy_sub = self.create_subscription(Joy, '/joy', self.joy_callback, 10)
        
        # Parametry
        self.max_linear_speed = 0.2  # m/s (200mm/s)
        self.max_angular_speed = 1.0 # rad/s
        self.speed_multiplier = 1.0

        self.get_logger().info("ZALADOWANO CZYSZTY TELEOP ROS2")
        self.get_logger().info("Sterowanie: L1 (Gaz) + Lewy Analog (Kierunek)")

    def joy_callback(self, msg):
        twist = Twist()
        
        # Sprawdzamy L1 (Deadman Switch) - zazwyczaj indeks 4
        # Jeśli L1 jest wciśnięty, przekazujemy wartości z analoga na cmd_vel
        if msg.buttons[4]:
            # Lewy analog góra/dół (indeks 1)
            twist.linear.x = msg.axes[1] * self.max_linear_speed * self.speed_multiplier
            # Lewy analog lewo/prawo (indeks 0)
            twist.angular.z = msg.axes[0] * self.max_angular_speed
            
            self.get_logger().info(f"Publikuje na /cmd_vel: x={twist.linear.x:.2f}, z={twist.angular.z:.2f}")
        else:
            # Jeśli puścisz L1, Twist() domyślnie ma zera (STOP)
            pass
            
        self.cmd_vel_pub.publish(twist)

        # Obsługa biegów (R1 zwiększa mnożnik, R2 zmniejsza)
        if msg.buttons[5]: self.speed_multiplier = min(self.speed_multiplier + 0.1, 2.5)
        if msg.buttons[7]: self.speed_multiplier = max(self.speed_multiplier - 0.1, 0.5)

def main():
    rclpy.init()
    node = RoombaTeleopNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()