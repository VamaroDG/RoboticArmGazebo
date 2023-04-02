cmake_minimum_required(VERSION 2.8.3)
project(my_robot_description)


find_package(catkin REQUIRED COMPONENTS
    roscpp
    rospy
    ros_utils
    std_msgs
    sensor_msgs
    tf
	tf2
	tf2_geometry_msgs
	tf2_ros
	urdf
	xacro
	roslaunch
)
	

catkin_package(
    INCLUDE_DIRS
        include
    LIBRARIES
        ${PROJECT_NAME}_lib
    CATKIN_DEPENDS
    	roscpp
    	rospy
    	ros_utils
    	std_msgs
    	sensor_msgs
    	tf
		tf2
		tf2_geometry_msgs
		tf2_ros
		urdf
		xacro
		roslaunch
)

#include_directories(
#    include
#    ${catkin_INCLUDE_DIRS}
#)
#
#add_executable(
#    ${PROJECT_NAME}_node
#    src/${PROJECT_NAME}_node.cpp
#    src/My_robot_description.cpp
#    include/${PROJECT_NAME}/My_robot_description.hpp
#)

#target_link_libraries(
#    ${PROJECT_NAME}_node
#    ${catkin_LIBRARIES}
#)


