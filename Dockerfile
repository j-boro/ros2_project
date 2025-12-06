FROM osrf/ros:jazzy-desktop

SHELL ["/bin/bash", "-c"]

WORKDIR /app

COPY src ros2_project/src

RUN apt-get update && rosdep update && rosdep install -i --from-paths ros2_project/src --rosdistro jazzy -y

RUN cd ros2_project && source /opt/ros/jazzy/setup.bash && colcon build

COPY entrypoint.sh /

ENTRYPOINT [ "/entrypoint.sh" ]

CMD ["bash"]