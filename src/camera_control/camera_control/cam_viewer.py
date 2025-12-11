#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class CameraViewer(Node):
    def __init__(self):
        super().__init__('camera_viewer')
        self.subscription = self.create_subscription(Image, 'image_raw', self.listener_callback, 10)
        self.br = CvBridge()
        self.get_logger().info("Camera Viewer Started")

    def listener_callback(self, data):
        current_frame = self.br.imgmsg_to_cv2(data, "bgr8")
        cv2.imshow("camera_feed", current_frame)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    node = CameraViewer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()