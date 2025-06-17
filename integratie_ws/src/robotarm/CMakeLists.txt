cmake_minimum_required(VERSION 3.0.2)
project(robotarm)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  moveit_ros_planning_interface
  rospy
  std_msgs
  std_srvs
  tf2_ros
  xarm_msgs

  # Voeg deze toe voor action en message generation
  actionlib
  actionlib_msgs
  message_generation
)

################################################
## Declare ROS messages, services and actions ##
################################################

## Actie bestanden
add_action_files(
  FILES
  manipulator.action
)

## Genereer berichten en acties
generate_messages(
  DEPENDENCIES
  std_msgs
  actionlib_msgs
)

###################################
## catkin specific configuration ##
###################################
catkin_package(
  CATKIN_DEPENDS
    geometry_msgs
    moveit_ros_planning_interface
    rospy
    std_msgs
    std_srvs
    tf2_ros
    xarm_msgs
    actionlib
    actionlib_msgs
    message_runtime
)

###########
## Build ##
###########

include_directories(
  ${catkin_INCLUDE_DIRS}
)

# Hier kan je targets toevoegen als je C++ code hebt
# add_executable(...)
# target_link_libraries(...)

#############
## Install ##
#############

# Voeg hier install regels toe als je wilt

#############
## Testing ##
#############

# Tests indien nodig

