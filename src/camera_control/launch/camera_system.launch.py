from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='camera_control',
            executable='publisher',
            name='main_camera_publisher',
            output='screen'
        ),
        
        Node(
            package='camera_control',
            executable='interactor',
            name='main_camera_interactor',
            output='screen'
        ),
    ])