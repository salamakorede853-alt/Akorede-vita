cmake_minimum_required(VERSION 3.22.1)
project(akorede_vita_android LANGUAGES CXX)

add_subdirectory(${CMAKE_CURRENT_LIST_DIR}/../../../../../shared shared)

add_library(akorede_vita_android SHARED android_bridge.cpp)

target_link_libraries(akorede_vita_android PRIVATE akorede_vita_engine_bridge)
