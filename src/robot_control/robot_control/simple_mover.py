import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

class SimpleMover(Node):
    def __init__(self):
        super().__init__('simple_mover')
        
        self.publisher_ = self.create_publisher(
            JointTrajectory, 
            '/scaled_joint_trajectory_controller/joint_trajectory', 
            10
        )
        
        self.get_logger().info('Simple Mover Node Started! Waiting 2 seconds...')
        
        self.timer = self.create_timer(2.0, self.move_robot)

    def move_robot(self):
        msg = JointTrajectory()
        
        msg.joint_names = [
            'shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 
            'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint'
        ]
        
        point = JointTrajectoryPoint()
        
        point.positions = [0.0, -1.57, 0.0, -1.57, 0.0, 0.0]
        
        point.time_from_start.sec = 5
        
        msg.points.append(point)
        
        self.publisher_.publish(msg)
        self.get_logger().info('Message Published! Robot should be moving.')
        
        self.timer.cancel()

def main(args=None):
    rclpy.init(args=args)
    node = SimpleMover()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()