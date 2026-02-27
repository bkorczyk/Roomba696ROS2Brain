#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry, Path
from geometry_msgs.msg import PoseStamped, Point
from visualization_msgs.msg import Marker
from create_msgs.msg import Bumper # Upewnij się, że paczka jest dostępna

class RoombaBumpMapper(Node):
    def __init__(self):
        super().__init__('roomba_bump_mapper')
        
        # Subskrypcje
        self.odom_sub = self.create_subscription(Odometry, '/odom', self.odom_callback, 10)
        self.bump_sub = self.create_subscription(Bumper, '/bumper', self.bump_callback, 10)
        
        # Publishery dla RViz
        self.path_pub = self.create_publisher(Path, '/roomba_path', 10)
        self.marker_pub = self.create_publisher(Marker, '/wall_markers', 10)
        
        # Dane do mapowania
        self.path = Path()
        self.path.header.frame_id = "odom"
        self.wall_id = 0
        self.last_pose = None

        self.get_logger().info("BUMP-MAPPER URUCHOMIONY. Oczekiwanie na dane z /odom i /bumper...")

    def odom_callback(self, msg):
        # 1. Tworzenie mapy pokrycia (Ścieżka)
        self.last_pose = msg.pose.pose
        new_pose = PoseStamped()
        new_pose.header = msg.header
        new_pose.pose = msg.pose.pose
        
        # Ograniczamy gęstość punktów ścieżki (co 5cm), by nie zapchać pamięci
        if len(self.path.poses) == 0 or self.get_distance(self.path.poses[-1].pose, new_pose.pose) > 0.05:
            self.path.poses.append(new_pose)
            self.path.header.stamp = self.get_clock().now().to_msg()
            self.path_pub.publish(self.path)

    def bump_callback(self, msg):
        # 2. Mapowanie przeszkód
        if (msg.is_left_pressed or msg.is_right_pressed) and self.last_pose:
            self.publish_wall_marker(self.last_pose.position)
            side = "LEWY" if msg.is_left_pressed else "PRAWY"
            self.get_logger().warn(f"KOLIZJA! [{side}] Zaznaczam ścianę na mapie.")

    def publish_wall_marker(self, position):
        marker = Marker()
        marker.header.frame_id = "odom"
        marker.header.stamp = self.get_clock().now().to_msg()
        marker.ns = "walls"
        marker.id = self.wall_id
        marker.type = Marker.CUBE
        marker.action = Marker.ADD
        marker.pose.position = position
        marker.scale.x = 0.1
        marker.scale.y = 0.1
        marker.scale.z = 0.1
        marker.color.a = 1.0 # Nieprzezroczystość
        marker.color.r = 1.0 # Czerwony
        
        self.marker_pub.publish(marker)
        self.wall_id += 1

    def get_distance(self, p1, p2):
        import math
        return math.sqrt((p1.position.x - p2.position.x)**2 + (p1.position.y - p2.position.y)**2)

def main():
    rclpy.init()
    rclpy.spin(RoombaBumpMapper())
    rclpy.shutdown()

if __name__ == '__main__':
    main()