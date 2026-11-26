cmake_minimum_required(VERSION 3.22)
project(akorede_vita_shared LANGUAGES CXX)

add_library(akorede_vita_engine_bridge STATIC
    src/engine_status.cpp
)

target_include_directories(akorede_vita_engine_bridge
    PUBLIC
        ${CMAKE_CURRENT_SOURCE_DIR}/include
)

target_compile_features(akorede_vita_engine_bridge PUBLIC cxx_std_17)

set_target_properties(akorede_vita_engine_bridge PROPERTIES
    POSITION_INDEPENDENT_CODE ON
)
