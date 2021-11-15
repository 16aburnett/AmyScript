#! /bin/sh

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
echo "Adding compiler to path"
echo "NOTE: this only persists for the current shell"
export PATH="$AMY_DIR/amyc/dist/amyc:$PATH"

# Build interpreter
echo "Building AmyAssembly Interpreter"
cd amyasmi
./build.sh
cd ..

# Add interpreter to path
# Currently this is temporary
echo "Adding interpreter to path"
echo "NOTE: this only persists for the current shell"
export PATH="$AMY_DIR/amyasmi/dist/amyasmi:$PATH"

