#! /bin/bash

# AmyScript tools installer 
# Author: Amy Burnett

# this folder's path
AMY_DIR=$PWD

# Build compiler
echo "Building AmyScript Compiler"
cd amyc
./build.sh
cd ..

# Add compiler to path
# Currently this is temporary
if [[ ":$PATH:" == *":$AMY_DIR/amyc/dist/amyc:"* ]]; then
    echo "amyc is already in PATH"
else
    echo "Adding compiler to PATH"
    echo "NOTE: this only persists for the current shell"
    export PATH="$AMY_DIR/amyc/dist/amyc:$PATH"
fi

# Build interpreter
echo "Building AmyAssembly Interpreter"
cd amyasmi
./build.sh
cd ..

# Add interpreter to path
# Currently this is temporary
if [[ ":$PATH:" == *":$AMY_DIR/amyasmi/dist/amyasmi:"* ]]; then 
    echo "amyasmi is already in PATH"
else 
    echo "Adding interpreter to PATH"
    echo "NOTE: this only persists for the current shell"
    export PATH="$AMY_DIR/amyasmi/dist/amyasmi:$PATH"
fi 
