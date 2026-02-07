cmake_minimum_required(VERSION 3.28)
project(
    LearnWebGPU # name of the project, which will also be the name of the visual studio solution if you use it
    VERSION 0.1.0 # any version number
    LANGUAGES CXX C # programming languages used by the project
)

# Create the target
add_executable(App main.cpp)

# Set C++23 standard with proper target properties
target_compile_features(App PRIVATE cxx_std_23)

# Ensure the standard is required, not optional
set_target_properties(App PROPERTIES
    CXX_STANDARD 23
    CXX_STANDARD_REQUIRED ON
    CXX_EXTENSIONS OFF)

# For GNU (MinGW) toolchains, prefer static linking of libstdc++/libgcc
if(CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
    # Copy required MinGW runtime DLLs into the target directory after build
    get_filename_component(MINGW_BIN_DIR ${CMAKE_CXX_COMPILER} DIRECTORY)
    add_custom_command(TARGET App POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy_if_different
            "${MINGW_BIN_DIR}/libstdc++-6.dll" "$<TARGET_FILE_DIR:App>"
        COMMAND ${CMAKE_COMMAND} -E copy_if_different
            "${MINGW_BIN_DIR}/libgcc_s_seh-1.dll" "$<TARGET_FILE_DIR:App>"
        COMMAND ${CMAKE_COMMAND} -E copy_if_different
            "${MINGW_BIN_DIR}/libwinpthread-1.dll" "$<TARGET_FILE_DIR:App>"
    )
endif()
