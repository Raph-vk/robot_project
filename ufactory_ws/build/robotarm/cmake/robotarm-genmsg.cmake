# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "robotarm: 7 messages, 0 services")

set(MSG_I_FLAGS "-Irobotarm:/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg;-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg;-Iactionlib_msgs:/opt/ros/melodic/share/actionlib_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(robotarm_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorGoal.msg" NAME_WE)
add_custom_target(_robotarm_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "robotarm" "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorGoal.msg" ""
)

get_filename_component(_filename "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionGoal.msg" NAME_WE)
add_custom_target(_robotarm_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "robotarm" "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionGoal.msg" "robotarm/manipulatorGoal:actionlib_msgs/GoalID:std_msgs/Header"
)

get_filename_component(_filename "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorFeedback.msg" NAME_WE)
add_custom_target(_robotarm_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "robotarm" "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorFeedback.msg" ""
)

get_filename_component(_filename "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorResult.msg" NAME_WE)
add_custom_target(_robotarm_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "robotarm" "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorResult.msg" ""
)

get_filename_component(_filename "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorAction.msg" NAME_WE)
add_custom_target(_robotarm_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "robotarm" "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorAction.msg" "robotarm/manipulatorGoal:actionlib_msgs/GoalID:actionlib_msgs/GoalStatus:robotarm/manipulatorFeedback:robotarm/manipulatorActionGoal:robotarm/manipulatorActionResult:std_msgs/Header:robotarm/manipulatorResult:robotarm/manipulatorActionFeedback"
)

get_filename_component(_filename "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionFeedback.msg" NAME_WE)
add_custom_target(_robotarm_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "robotarm" "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionFeedback.msg" "robotarm/manipulatorFeedback:actionlib_msgs/GoalID:actionlib_msgs/GoalStatus:std_msgs/Header"
)

get_filename_component(_filename "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionResult.msg" NAME_WE)
add_custom_target(_robotarm_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "robotarm" "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionResult.msg" "actionlib_msgs/GoalID:actionlib_msgs/GoalStatus:robotarm/manipulatorResult:std_msgs/Header"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(robotarm
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robotarm
)
_generate_msg_cpp(robotarm
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorGoal.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robotarm
)
_generate_msg_cpp(robotarm
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robotarm
)
_generate_msg_cpp(robotarm
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robotarm
)
_generate_msg_cpp(robotarm
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorAction.msg"
  "${MSG_I_FLAGS}"
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorGoal.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorFeedback.msg;/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionGoal.msg;/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionResult.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorResult.msg;/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionFeedback.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robotarm
)
_generate_msg_cpp(robotarm
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorFeedback.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robotarm
)
_generate_msg_cpp(robotarm
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorResult.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robotarm
)

### Generating Services

### Generating Module File
_generate_module_cpp(robotarm
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robotarm
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(robotarm_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(robotarm_generate_messages robotarm_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorGoal.msg" NAME_WE)
add_dependencies(robotarm_generate_messages_cpp _robotarm_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionGoal.msg" NAME_WE)
add_dependencies(robotarm_generate_messages_cpp _robotarm_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorFeedback.msg" NAME_WE)
add_dependencies(robotarm_generate_messages_cpp _robotarm_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorResult.msg" NAME_WE)
add_dependencies(robotarm_generate_messages_cpp _robotarm_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorAction.msg" NAME_WE)
add_dependencies(robotarm_generate_messages_cpp _robotarm_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionFeedback.msg" NAME_WE)
add_dependencies(robotarm_generate_messages_cpp _robotarm_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionResult.msg" NAME_WE)
add_dependencies(robotarm_generate_messages_cpp _robotarm_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(robotarm_gencpp)
add_dependencies(robotarm_gencpp robotarm_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS robotarm_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(robotarm
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robotarm
)
_generate_msg_eus(robotarm
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorGoal.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robotarm
)
_generate_msg_eus(robotarm
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robotarm
)
_generate_msg_eus(robotarm
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robotarm
)
_generate_msg_eus(robotarm
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorAction.msg"
  "${MSG_I_FLAGS}"
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorGoal.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorFeedback.msg;/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionGoal.msg;/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionResult.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorResult.msg;/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionFeedback.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robotarm
)
_generate_msg_eus(robotarm
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorFeedback.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robotarm
)
_generate_msg_eus(robotarm
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorResult.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robotarm
)

### Generating Services

### Generating Module File
_generate_module_eus(robotarm
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robotarm
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(robotarm_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(robotarm_generate_messages robotarm_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorGoal.msg" NAME_WE)
add_dependencies(robotarm_generate_messages_eus _robotarm_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionGoal.msg" NAME_WE)
add_dependencies(robotarm_generate_messages_eus _robotarm_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorFeedback.msg" NAME_WE)
add_dependencies(robotarm_generate_messages_eus _robotarm_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorResult.msg" NAME_WE)
add_dependencies(robotarm_generate_messages_eus _robotarm_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorAction.msg" NAME_WE)
add_dependencies(robotarm_generate_messages_eus _robotarm_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionFeedback.msg" NAME_WE)
add_dependencies(robotarm_generate_messages_eus _robotarm_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionResult.msg" NAME_WE)
add_dependencies(robotarm_generate_messages_eus _robotarm_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(robotarm_geneus)
add_dependencies(robotarm_geneus robotarm_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS robotarm_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(robotarm
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robotarm
)
_generate_msg_lisp(robotarm
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorGoal.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robotarm
)
_generate_msg_lisp(robotarm
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robotarm
)
_generate_msg_lisp(robotarm
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robotarm
)
_generate_msg_lisp(robotarm
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorAction.msg"
  "${MSG_I_FLAGS}"
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorGoal.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorFeedback.msg;/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionGoal.msg;/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionResult.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorResult.msg;/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionFeedback.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robotarm
)
_generate_msg_lisp(robotarm
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorFeedback.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robotarm
)
_generate_msg_lisp(robotarm
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorResult.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robotarm
)

### Generating Services

### Generating Module File
_generate_module_lisp(robotarm
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robotarm
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(robotarm_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(robotarm_generate_messages robotarm_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorGoal.msg" NAME_WE)
add_dependencies(robotarm_generate_messages_lisp _robotarm_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionGoal.msg" NAME_WE)
add_dependencies(robotarm_generate_messages_lisp _robotarm_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorFeedback.msg" NAME_WE)
add_dependencies(robotarm_generate_messages_lisp _robotarm_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorResult.msg" NAME_WE)
add_dependencies(robotarm_generate_messages_lisp _robotarm_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorAction.msg" NAME_WE)
add_dependencies(robotarm_generate_messages_lisp _robotarm_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionFeedback.msg" NAME_WE)
add_dependencies(robotarm_generate_messages_lisp _robotarm_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionResult.msg" NAME_WE)
add_dependencies(robotarm_generate_messages_lisp _robotarm_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(robotarm_genlisp)
add_dependencies(robotarm_genlisp robotarm_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS robotarm_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(robotarm
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robotarm
)
_generate_msg_nodejs(robotarm
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorGoal.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robotarm
)
_generate_msg_nodejs(robotarm
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robotarm
)
_generate_msg_nodejs(robotarm
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robotarm
)
_generate_msg_nodejs(robotarm
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorAction.msg"
  "${MSG_I_FLAGS}"
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorGoal.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorFeedback.msg;/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionGoal.msg;/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionResult.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorResult.msg;/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionFeedback.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robotarm
)
_generate_msg_nodejs(robotarm
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorFeedback.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robotarm
)
_generate_msg_nodejs(robotarm
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorResult.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robotarm
)

### Generating Services

### Generating Module File
_generate_module_nodejs(robotarm
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robotarm
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(robotarm_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(robotarm_generate_messages robotarm_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorGoal.msg" NAME_WE)
add_dependencies(robotarm_generate_messages_nodejs _robotarm_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionGoal.msg" NAME_WE)
add_dependencies(robotarm_generate_messages_nodejs _robotarm_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorFeedback.msg" NAME_WE)
add_dependencies(robotarm_generate_messages_nodejs _robotarm_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorResult.msg" NAME_WE)
add_dependencies(robotarm_generate_messages_nodejs _robotarm_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorAction.msg" NAME_WE)
add_dependencies(robotarm_generate_messages_nodejs _robotarm_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionFeedback.msg" NAME_WE)
add_dependencies(robotarm_generate_messages_nodejs _robotarm_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionResult.msg" NAME_WE)
add_dependencies(robotarm_generate_messages_nodejs _robotarm_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(robotarm_gennodejs)
add_dependencies(robotarm_gennodejs robotarm_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS robotarm_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(robotarm
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robotarm
)
_generate_msg_py(robotarm
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorGoal.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robotarm
)
_generate_msg_py(robotarm
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robotarm
)
_generate_msg_py(robotarm
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robotarm
)
_generate_msg_py(robotarm
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorAction.msg"
  "${MSG_I_FLAGS}"
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorGoal.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorFeedback.msg;/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionGoal.msg;/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionResult.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorResult.msg;/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionFeedback.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robotarm
)
_generate_msg_py(robotarm
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorFeedback.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robotarm
)
_generate_msg_py(robotarm
  "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorResult.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robotarm
)

### Generating Services

### Generating Module File
_generate_module_py(robotarm
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robotarm
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(robotarm_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(robotarm_generate_messages robotarm_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorGoal.msg" NAME_WE)
add_dependencies(robotarm_generate_messages_py _robotarm_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionGoal.msg" NAME_WE)
add_dependencies(robotarm_generate_messages_py _robotarm_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorFeedback.msg" NAME_WE)
add_dependencies(robotarm_generate_messages_py _robotarm_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorResult.msg" NAME_WE)
add_dependencies(robotarm_generate_messages_py _robotarm_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorAction.msg" NAME_WE)
add_dependencies(robotarm_generate_messages_py _robotarm_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionFeedback.msg" NAME_WE)
add_dependencies(robotarm_generate_messages_py _robotarm_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/student/ufactory_ws/devel/.private/robotarm/share/robotarm/msg/manipulatorActionResult.msg" NAME_WE)
add_dependencies(robotarm_generate_messages_py _robotarm_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(robotarm_genpy)
add_dependencies(robotarm_genpy robotarm_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS robotarm_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robotarm)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robotarm
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(robotarm_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()
if(TARGET actionlib_msgs_generate_messages_cpp)
  add_dependencies(robotarm_generate_messages_cpp actionlib_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robotarm)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robotarm
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(robotarm_generate_messages_eus std_msgs_generate_messages_eus)
endif()
if(TARGET actionlib_msgs_generate_messages_eus)
  add_dependencies(robotarm_generate_messages_eus actionlib_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robotarm)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robotarm
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(robotarm_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()
if(TARGET actionlib_msgs_generate_messages_lisp)
  add_dependencies(robotarm_generate_messages_lisp actionlib_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robotarm)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robotarm
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(robotarm_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()
if(TARGET actionlib_msgs_generate_messages_nodejs)
  add_dependencies(robotarm_generate_messages_nodejs actionlib_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robotarm)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robotarm\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robotarm
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(robotarm_generate_messages_py std_msgs_generate_messages_py)
endif()
if(TARGET actionlib_msgs_generate_messages_py)
  add_dependencies(robotarm_generate_messages_py actionlib_msgs_generate_messages_py)
endif()
