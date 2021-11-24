#! /bin/bash

# Build script for AmyAssembly Interpreter 
# Author: Amy Burnett

# build 
pyinstaller amyAssemblyInterpreter.py --noconfirm -n amyasmi --clean
echo "Finished Building AmyAssembly Interpreter"
