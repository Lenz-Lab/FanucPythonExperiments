#!/bin/bash

# source ros2 humble
source /opt/ros/$ROS_DISTRO/setup.bash

# source pymoveit2 ws 
source $PYMOVEIT/install/local_setup.bash

# source fanuc packages in current ws
source install/local_setup.bash

/home/$USER/.local/bin/jupyter-notebook