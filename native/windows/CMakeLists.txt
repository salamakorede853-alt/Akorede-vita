cmake_minimum_required(VERSION 3.22)
project(AkoredeVitaWindows VERSION 0.1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

find_package(Qt6 REQUIRED COMPONENTS Widgets)

add_subdirectory(../shared shared)

qt_standard_project_setup()

qt_add_executable(AkoredeVitaWindows
    src/main.cpp
)

target_link_libraries(AkoredeVitaWindows
    PRIVATE
        Qt6::Widgets
        akorede_vita_engine_bridge
)
