project(PackageTest CXX)
cmake_minimum_required(VERSION 3.1.2)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_executable(Arg_Printer Arg_Printer.cpp)
conan_target_link_libraries(Arg_Printer)

# CTest is a testing tool that can be used to test your project.
#enable_testing()
#add_test(NAME Arg_Printer
#         WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
#         COMMAND Arg_Printer)

