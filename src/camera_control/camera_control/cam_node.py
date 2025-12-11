#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import cv2
import numpy as np

def map_range(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

class CameraInteractor(Node):
    def __init__(self):
        super().__init__('camera_interactor')
        self.window_name = "Robot Control Interface"
        
        self.subscription = self.create_subscription(
            Image, 'image_raw', self.listener_callback, 10
        )
        
        self.publisher_ = self.create_publisher(
            JointTrajectory, 
            '/scaled_joint_trajectory_controller/joint_trajectory', 
            10
        )
        
        self.point = None
        self.get_logger().info("Click anywhere in the window to move the robot!")

    def listener_callback(self, image_data):
        cv_image = np.zeros((512, 700, 3), np.uint8)
        
        cv2.putText(cv_image, "X-Axis: Base Pan | Y-Axis: Elbow", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        if self.point is not None:
            cv2.rectangle(cv_image, self.point, (self.point[0]+100, self.point[1]+100), (0, 255, 0), 3)
            
        cv2.imshow(self.window_name, cv_image)
        cv2.waitKey(25)
        cv2.setMouseCallback(self.window_name, self.mouse_callback)

    def mouse_callback(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.point = (x, y)
            self.move_robot(x, y)

    def move_robot(self, x, y):
        base_target = map_range(x, 0, 700, 2.1, -1.5) 
        
        elbow_target = map_range(y, 0, 512, -0.5, -2.5)

        self.get_logger().info(f"Click at ({x},{y}) -> Moving Base to {base_target:.2f}, Elbow to {elbow_target:.2f}")

        msg = JointTrajectory()
        
        msg.header.stamp.sec = 0
        msg.header.stamp.nanosec = 0
        
        msg.joint_names = [
            'shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 
            'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint'
        ]
        
        point = JointTrajectoryPoint()
        
        point.positions = [base_target, -1.72, elbow_target, -0.81, 1.6, -0.03]
        
        point.time_from_start.sec = 2
        
        msg.points.append(point)
        
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = CameraInteractor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
