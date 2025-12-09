# UR5 control

## Installation
Since this repo uses the Universal Robots driver as a submodule, remember to clone using:

    git clone --recursive https://github.com/j-boro/ros2_project.git

Then navigate to the main project directory and run:

    docker compose up

This should build the whole image and run both RViz to visualize the robot and the teach pendant to control it. You can see that [here](http://localhost:6080/vnc.html).

## External control

The <code>*default.installation*</code> file sets the network up automatically, so to run external commands you only need to start the robot and run a program with the <code>*External Control*</code> command block on it.