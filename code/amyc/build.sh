#! /bin/bash

# Build script for AmyScript Compiler 
# Author: Amy Burnett

# build 
echo "Building AmyScript Compiler"
pyinstaller amyScriptCompiler.py --noconfirm -n amyc --clean
echo "Finished Build"

# add AmyScript library
echo "Adding AmyScript builtin library to dist"
cp AmyScriptBuiltinLib.amy.assembly dist/amyc/