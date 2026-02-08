cmake_minimum_required(VERSION 3.20)
project(HelloWebGPU)

set(CMAKE_CXX_STANDARD 17)

# Include the WebGPU-distribution subdirectory
add_subdirectory(webgpu)

add_executable(hello_gpu main.cpp)

# Link the WebGPU targets provided by distribution
target_link_libraries(hello_gpu
    wgpu_static
)