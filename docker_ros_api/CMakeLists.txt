cmake_minimum_required(VERSION 2.8.3)
project(docker_ros_api)

find_package(catkin REQUIRED COMPONENTS
     rospy
     docker_ros_api_msgs
)

catkin_python_setup()

catkin_package(
    INCLUDE_DIRS
    
    LIBRARIES

    CATKIN_DEPENDS
    rospy
    docker_ros_api_msgs

    )


#############
## Install ##
#############


install(DIRECTORY launch/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
  )

install(PROGRAMS scripts/docker_compose_ros_api_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
  )

install(DIRECTORY src/
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}/scripts/
  )
