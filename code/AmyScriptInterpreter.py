# AmyScript Interpreter 
# Author: Amy Burnett
#=========================================================================

import sys
from amyScriptCompiler.amyScriptCompiler import AmyScriptCompiler
from amyAssemblyInterpreter.amyAssemblyInterpreter import AmyAssemblyInterpreter

#=========================================================================

# determine what file to read from
file = sys.stdin
srcFilename = ""
destFilename = ""
if (len(sys.argv) == 2):
    srcFilename = sys.argv[1]
    destFilename = srcFilename + ".assembly"
    file = open(srcFilename)

srcCode = "".join (file.readlines())

# COMPILE AmyScript -> AmyAssembly

compiler = AmyScriptCompiler ()
assemblyCode = compiler.compile (srcCode)

# Write out AmyAssembly 

with open(destFilename, "w") as file:
    file.write (assemblyCode)

# EXECUTE AmyAssembly

interpreter = AmyAssemblyInterpreter (destFilename)
interpreter.debug = False
interpreter.execute (assemblyCode)

#=========================================================================
