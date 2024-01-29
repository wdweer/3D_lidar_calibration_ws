cmake_minimum_required(VERSION 3.0.2)
project(hokuyo_gazebo)

# Find catkin and any catkin packages
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  gazebo_ros
)

# Declare a catkin package
catkin_package(
  # CATKIN_DEPENDS roscpp rospy gazebo_ros
)

# Specify additional locations of header files
include_directories(
  ${catkin_INCLUDE_DIRS}
)

# Mark other files for installation (e.g. launch and bag files, etc.)
install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

