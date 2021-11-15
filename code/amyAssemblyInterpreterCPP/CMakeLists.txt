cmake_minimum_required(VERSION 3.10)

# set the project name
project(amyasm)

# add the executable
add_executable(amyasm amyAssemblyInterpreter.cpp lexer.cpp util.cpp memory.cpp)