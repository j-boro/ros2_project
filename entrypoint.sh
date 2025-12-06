#!/bin/bash

set -e
source /opt/ros/jazzy/setup.bash
source /app/ros2_project/install/setup.bash

exec "$@"