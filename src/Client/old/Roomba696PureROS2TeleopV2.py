#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

class RoombaPrecisionTeleop(Node):
    def __init__(self):
        super().__init__('roomba_precision_teleop')
        
        # Publisher do standardowego topica jazdy
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        
        # Subskrypcja pada podpiętego lokalnie do Rolling
        self.joy_sub = self.create_subscription(Joy, '/joy', self.joy_callback, 10)
        
        # Ustawienia czułości
        self.max_linear_speed = 0.3  # m/s
        self.max_angular_speed = 1.5 # rad/s

        # Mapowanie dla PS3 na ROS2 Rolling (joy_linux_node)
        self.BTN_L1 = 4
        self.AXIS_RIGHT_X = 2  # Prawy analog Lewo/Prawo
        self.AXIS_RIGHT_Y = 5  # Prawy analog Przód/Tył

        self.print_status()

    def print_status(self):
        print("\n" + "="*40)
        print("      ROOMBA PRECISION TELEOP")
        print("="*40)
        print(" STEROWANIE: Prawy Analog")
        print(" BEZPIECZNIK: L1 (Musi być wciśnięty)")
        print(" SILNIKI: Wyłączone w kodzie")
        print("="*40 + "\n")

    def joy_callback(self, msg):
        twist = Twist()

        # Sprawdzenie przycisku bezpieczeństwa L1
        # msg.buttons[4] == 1 oznacza, że trzymasz przycisk
        if len(msg.buttons) > self.BTN_L1 and msg.buttons[self.BTN_L1] == 1:
            # Pobieramy wartości z prawego analoga
            # Często osie analogów mają odwróconą polaryzację, więc dodajemy '-' jeśli trzeba
            twist.linear.x = msg.axes[self.AXIS_RIGHT_Y] * self.max_linear_speed
            twist.angular.z = msg.axes[self.AXIS_RIGHT_X] * self.max_angular_speed
            
            self.get_logger().info(f"Jazda aktywna | X: {twist.linear.x:.2f} | Z: {twist.angular.z:.2f}", throttle_duration_sec=0.5)
        else:
            # Jeśli L1 nie jest wciśnięty, wysyłamy wymuszone zero (bezpieczeństwo)
            twist.linear.x = 0.0
            twist.angular.z = 0.0

        self.cmd_vel_pub.publish(twist)

def main():
    rclpy.init()
    node = RoombaPrecisionTeleop()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        # Failsafe przy wyjściu
        stop_twist = Twist()
        node.cmd_vel_pub.publish(stop_twist)
        print("\nZatrzymano sterowanie.")
    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    main()