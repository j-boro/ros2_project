# UR5e control

This dockerized ROS2 project allows the user to control a virtual Universal Robots UR5e robot both using it's simulated teach pendant and an *almost* camera based point-and-click system.

## Installation
Since this repo uses the Universal Robots driver as a submodule, remember to clone using:

    git clone --recursive https://github.com/j-boro/ros2_project.git

Navigate to the main project directory and run:

    docker compose up

This should build the whole image and run both RViz to visualize the robot and the teach pendant to control it. You can see the pendant [here](http://localhost:6080/vnc.html).

## External control

The <code>*default.installation*</code> file sets the network up automatically, so to run external commands you only need to start the robot and run a program with the <code>*External Control*</code> command block in it.

## Testing

To make sure everything is running correctly, run this in a secondary terminal:

    docker exec -it ros_robot bash -c "source /opt/ros/jazzy/setup.bash && source /app/ros2_project/install/setup.bash && ros2 run robot_control simple_mover"

The robot should home itself. Then you can run:

    docker exec -it ros_robot bash -c "source /opt/ros/jazzy/setup.bash && source /app/ros2_project/install/setup.bash && ros2 launch ur_robot_driver test_scaled_joint_trajectory_controller.launch.py"

This is a test file provided by UR.

## Operation

Since launch files were created, these two commands can open the required nodes for controlling the robot:

Just the control pad:

    docker exec -it ros_robot bash -c "source /opt/ros/jazzy/setup.bash && source /app/ros2_project/install/setup.bash && ros2 launch camera_control camera_system.launch.py"

Both the control pad and the actual camera feed.

    docker exec -it ros_robot bash -c "source /opt/ros/jazzy/setup.bash && source /app/ros2_project/install/setup.bash && ros2 launch camera_control all_nodes.launch.py"

