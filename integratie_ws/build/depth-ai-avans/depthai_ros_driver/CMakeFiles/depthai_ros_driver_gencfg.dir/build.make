# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/student/Git-projects/robot_project/integratie_ws/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/student/Git-projects/robot_project/integratie_ws/build

# Utility rule file for depthai_ros_driver_gencfg.

# Include the progress variables for this target.
include depth-ai-avans/depthai_ros_driver/CMakeFiles/depthai_ros_driver_gencfg.dir/progress.make

depth-ai-avans/depthai_ros_driver/CMakeFiles/depthai_ros_driver_gencfg: /home/student/Git-projects/robot_project/integratie_ws/devel/include/depthai_ros_driver/parametersConfig.h
depth-ai-avans/depthai_ros_driver/CMakeFiles/depthai_ros_driver_gencfg: /home/student/Git-projects/robot_project/integratie_ws/devel/lib/python2.7/dist-packages/depthai_ros_driver/cfg/parametersConfig.py


/home/student/Git-projects/robot_project/integratie_ws/devel/include/depthai_ros_driver/parametersConfig.h: /home/student/Git-projects/robot_project/integratie_ws/src/depth-ai-avans/depthai_ros_driver/cfg/parameters.cfg
/home/student/Git-projects/robot_project/integratie_ws/devel/include/depthai_ros_driver/parametersConfig.h: /opt/ros/melodic/share/dynamic_reconfigure/templates/ConfigType.py.template
/home/student/Git-projects/robot_project/integratie_ws/devel/include/depthai_ros_driver/parametersConfig.h: /opt/ros/melodic/share/dynamic_reconfigure/templates/ConfigType.h.template
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/student/Git-projects/robot_project/integratie_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating dynamic reconfigure files from cfg/parameters.cfg: /home/student/Git-projects/robot_project/integratie_ws/devel/include/depthai_ros_driver/parametersConfig.h /home/student/Git-projects/robot_project/integratie_ws/devel/lib/python2.7/dist-packages/depthai_ros_driver/cfg/parametersConfig.py"
	cd /home/student/Git-projects/robot_project/integratie_ws/build/depth-ai-avans/depthai_ros_driver && ../../catkin_generated/env_cached.sh /home/student/Git-projects/robot_project/integratie_ws/build/depth-ai-avans/depthai_ros_driver/setup_custom_pythonpath.sh /home/student/Git-projects/robot_project/integratie_ws/src/depth-ai-avans/depthai_ros_driver/cfg/parameters.cfg /opt/ros/melodic/share/dynamic_reconfigure/cmake/.. /home/student/Git-projects/robot_project/integratie_ws/devel/share/depthai_ros_driver /home/student/Git-projects/robot_project/integratie_ws/devel/include/depthai_ros_driver /home/student/Git-projects/robot_project/integratie_ws/devel/lib/python2.7/dist-packages/depthai_ros_driver

/home/student/Git-projects/robot_project/integratie_ws/devel/share/depthai_ros_driver/docs/parametersConfig.dox: /home/student/Git-projects/robot_project/integratie_ws/devel/include/depthai_ros_driver/parametersConfig.h
	@$(CMAKE_COMMAND) -E touch_nocreate /home/student/Git-projects/robot_project/integratie_ws/devel/share/depthai_ros_driver/docs/parametersConfig.dox

/home/student/Git-projects/robot_project/integratie_ws/devel/share/depthai_ros_driver/docs/parametersConfig-usage.dox: /home/student/Git-projects/robot_project/integratie_ws/devel/include/depthai_ros_driver/parametersConfig.h
	@$(CMAKE_COMMAND) -E touch_nocreate /home/student/Git-projects/robot_project/integratie_ws/devel/share/depthai_ros_driver/docs/parametersConfig-usage.dox

/home/student/Git-projects/robot_project/integratie_ws/devel/lib/python2.7/dist-packages/depthai_ros_driver/cfg/parametersConfig.py: /home/student/Git-projects/robot_project/integratie_ws/devel/include/depthai_ros_driver/parametersConfig.h
	@$(CMAKE_COMMAND) -E touch_nocreate /home/student/Git-projects/robot_project/integratie_ws/devel/lib/python2.7/dist-packages/depthai_ros_driver/cfg/parametersConfig.py

/home/student/Git-projects/robot_project/integratie_ws/devel/share/depthai_ros_driver/docs/parametersConfig.wikidoc: /home/student/Git-projects/robot_project/integratie_ws/devel/include/depthai_ros_driver/parametersConfig.h
	@$(CMAKE_COMMAND) -E touch_nocreate /home/student/Git-projects/robot_project/integratie_ws/devel/share/depthai_ros_driver/docs/parametersConfig.wikidoc

depthai_ros_driver_gencfg: depth-ai-avans/depthai_ros_driver/CMakeFiles/depthai_ros_driver_gencfg
depthai_ros_driver_gencfg: /home/student/Git-projects/robot_project/integratie_ws/devel/include/depthai_ros_driver/parametersConfig.h
depthai_ros_driver_gencfg: /home/student/Git-projects/robot_project/integratie_ws/devel/share/depthai_ros_driver/docs/parametersConfig.dox
depthai_ros_driver_gencfg: /home/student/Git-projects/robot_project/integratie_ws/devel/share/depthai_ros_driver/docs/parametersConfig-usage.dox
depthai_ros_driver_gencfg: /home/student/Git-projects/robot_project/integratie_ws/devel/lib/python2.7/dist-packages/depthai_ros_driver/cfg/parametersConfig.py
depthai_ros_driver_gencfg: /home/student/Git-projects/robot_project/integratie_ws/devel/share/depthai_ros_driver/docs/parametersConfig.wikidoc
depthai_ros_driver_gencfg: depth-ai-avans/depthai_ros_driver/CMakeFiles/depthai_ros_driver_gencfg.dir/build.make

.PHONY : depthai_ros_driver_gencfg

# Rule to build all files generated by this target.
depth-ai-avans/depthai_ros_driver/CMakeFiles/depthai_ros_driver_gencfg.dir/build: depthai_ros_driver_gencfg

.PHONY : depth-ai-avans/depthai_ros_driver/CMakeFiles/depthai_ros_driver_gencfg.dir/build

depth-ai-avans/depthai_ros_driver/CMakeFiles/depthai_ros_driver_gencfg.dir/clean:
	cd /home/student/Git-projects/robot_project/integratie_ws/build/depth-ai-avans/depthai_ros_driver && $(CMAKE_COMMAND) -P CMakeFiles/depthai_ros_driver_gencfg.dir/cmake_clean.cmake
.PHONY : depth-ai-avans/depthai_ros_driver/CMakeFiles/depthai_ros_driver_gencfg.dir/clean

depth-ai-avans/depthai_ros_driver/CMakeFiles/depthai_ros_driver_gencfg.dir/depend:
	cd /home/student/Git-projects/robot_project/integratie_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/student/Git-projects/robot_project/integratie_ws/src /home/student/Git-projects/robot_project/integratie_ws/src/depth-ai-avans/depthai_ros_driver /home/student/Git-projects/robot_project/integratie_ws/build /home/student/Git-projects/robot_project/integratie_ws/build/depth-ai-avans/depthai_ros_driver /home/student/Git-projects/robot_project/integratie_ws/build/depth-ai-avans/depthai_ros_driver/CMakeFiles/depthai_ros_driver_gencfg.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : depth-ai-avans/depthai_ros_driver/CMakeFiles/depthai_ros_driver_gencfg.dir/depend

