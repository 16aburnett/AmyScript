#! /bin/bash

# Build script for AmyScript Compiler 
# Author: Amy Burnett

# build 
echo "Building AmyScript Compiler"
pyinstaller amyScriptCompiler.py --noconfirm -n amyc --clean
echo "Finished Build"

# add AmyScript library
echo "Adding AmyScript builtin libraries to dist"
cp AmyScriptBuiltinLib.amy.assembly dist/amyc/
cp AmyScriptBuiltinLib_x86.asm dist/amyc/
cp AmyScriptBuiltinLib_python.py dist/amyc/
cp AmyScriptBuiltinLib_cpp.cpp dist/amyc/