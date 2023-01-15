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

# install
export INSTALL_DIR="$HOME/bin"
echo "Installing into $INSTALL_DIR"
mkdir -p $INSTALL_DIR
# delete previous
rm -f $INSTALL_DIR/amyc
ln -s `pwd`/dist/amyc/amyc "$INSTALL_DIR/amyc"

# ensure it is in the path
if [[ ":$PATH:" != *":$HOME/bin:"* ]]; then
    echo "Warning: You need to add $HOME/bin to your path"
    echo "   you can do this by adding the following line to your ~/.bashrc"
    echo 'export PATH="$HOME/bin:$PATH"'
fi

echo "Install finished"
