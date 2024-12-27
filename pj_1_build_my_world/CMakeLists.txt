cmake_minimum_required(VERSION 2.8.3 FATAL_ERROR)

find_package(gazebo REQUIRED)

include_directories(${GAZEBO_INCLUDE_DIRS})
link_directories(${GAZEBO_LIBRARY_DIRS})
list(APPEND CMAKE_CXX_FLAGS "${GAZEBO_CXX_FLAGS}")

add_library(world_plugin SHARED script/welcome_message.cpp)
target_link_libraries(world_plugin ${GAZEBO_LIBRARIES})
