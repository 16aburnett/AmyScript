# Amy Script Preprocessor 
#    AmyScript's preprocessor that handles the preprocessor directives 
#    and any other pre-compile changes. 
# By Amy Burnett
# November 17 2021
# ========================================================================

import sys 
from sys import exit 
import os 

# ========================================================================

IDENTIFIER = 0
STRING = 1
OTHER = 2

class DirectiveToken:

    def __init__(self, type, value):
        self.type = type
        self.value = value 
    def __str__(self):
        return f"Token({self.type}, {self.value})"
    def __repr__(self):
        return self.__str__()

# ========================================================================

class AmyScriptPreprocessor:

    def __init__(self, mainFilename, otherFilenames=[], emitPreprocessed=False):
        self.mainFilename = mainFilename
        self.otherFilenames = otherFilenames
        self.outputProcessed = emitPreprocessed 
        self.outputFilename = mainFilename + ".preprocessed"
        self.outputDebug = False 
        self.debugOutputFilename = mainFilename + ".debug"
        self.files = {}

    def process (self):

        rootDir = os.path.abspath("")

        # print (rootDir.split(os.sep))

        # ensure main file exists
        if (not os.path.exists(os.path.abspath(self.mainFilename))):
            print (f"Preprocessor Error: '{self.mainFilename}' does not exist")
            print (f"   Current Dir: {os.getcwd()}")
            print (f"   Absolute Path: {os.path.abspath(self.mainFilename)}")
            exit (1)

        # Read in files 
        # print ("file:", self.mainFilename)
        self.files[os.path.abspath(self.mainFilename)] = open (os.path.abspath(self.mainFilename), "r").readlines ()
        # ensure last line ends in newline
        if len(self.files[os.path.abspath(self.mainFilename)]) > 0:
            if not self.files[os.path.abspath(self.mainFilename)][-1].endswith ("\n"):
                self.files[os.path.abspath(self.mainFilename)][-1] = self.files[os.path.abspath(self.mainFilename)][-1] + "\n"
        for i in range(len(self.otherFilenames)):
            # print ("file:", os.path.abspath(self.otherFilenames[i]))
            # ensure file exists
            if (not os.path.exists(os.path.abspath(self.otherFilenames[i]))):
                print (f"Preprocessor Error: '{self.otherFilenames[i]}' does not exist")
                print (f"   Current Dir: {os.getcwd()}")
                print (f"   Absolute Path: {os.path.abspath(self.otherFilenames[i])}")
                exit (1)
            # add file to included files 
            self.files[os.path.abspath(self.otherFilenames[i])] = open (os.path.abspath(self.otherFilenames[i]), "r").readlines ()
            # ensure last line ends in newline
            if len(self.files[os.path.abspath(self.otherFilenames[i])]) > 0:
                if not self.files[os.path.abspath(self.otherFilenames[i])][-1].endswith ("\n"):
                    self.files[os.path.abspath(self.otherFilenames[i])][-1] = self.files[os.path.abspath(self.otherFilenames[i])][-1] + "\n"
        # start by prcoessing the main file 
        # outputLines stores the lines that make it into the output file
        # it also stores each line's original file and line number 
        # not yet: along with the chain of includes to that line
        # which can be used for debugging. 
        self.outputLines = []
        fileToProcessStack = [[os.path.abspath(self.mainFilename), 0]]
        variables = {"COMPILER":sys.argv[0]}
        # stores the location and the success/fail of the containing if directive
        # this is used to include/exclude lines within a conditional directive block 
        containingIf = []
        # process all files
        while len(fileToProcessStack) > 0:
            # step through current file 
            currentDirectory = os.path.split(fileToProcessStack[-1][0])[0]
            currentFilename = fileToProcessStack[-1][0]
            currentLineNum = fileToProcessStack[-1][1]
            while currentLineNum < len(self.files[currentFilename]):
                
                line = self.files[currentFilename][currentLineNum]

                # attempt to parse a directive 
                wasSuccesful, cmd, args = self.parseLine(line)

                # ensure directive was parsed 
                if wasSuccesful:
                    # process directive - remember to save current state
                    # print (cmd, args)

                    # INCLUDE 
                    # include "<filename>"
                    if cmd == "include":
                        # ignore if containing if was false
                        if len(containingIf) > 0 and containingIf[-1][1] == False:
                            currentLineNum += 1
                            continue

                        # ensure string was provided 
                        if len(args) == 0 or args[0].type != STRING:
                            print (f"Preprocessor Error: {cmd} directive needs a string")
                            print (f"   in file {currentFilename}")
                            for i in range(len(fileToProcessStack)-2, -1, -1):
                                print (f"      included from {fileToProcessStack[i][0]}:{fileToProcessStack[i][1]}")
                            print (f"   on line {currentLineNum+1}")
                            print (line)
                            exit(1)
                        # abspath will simplify any '..' 
                        nextFilepath = os.path.abspath(os.path.join(currentDirectory, args[0].value))
                        # print ("including", nextFilepath)
                        # ensure file was provided to include
                        if nextFilepath not in self.files:
                            print (f"Preprocessor Error: Unknown file in relative include \"{args[0].value}\"")
                            print (f"   in file {currentFilename}")
                            for i in range(len(fileToProcessStack)-2, -1, -1):
                                print (f"      included from {fileToProcessStack[i][0]}:{fileToProcessStack[i][1]}")
                            print (f"   on line {currentLineNum+1}")
                            print (line)
                            print (f"   attempted lookup {nextFilepath}")
                            print (f"   *Make sure you provide all the necessary files to the compiler")
                            exit(1)
                        # save current file index
                        currentLineNum += 1
                        fileToProcessStack[-1][1] = currentLineNum
                        # switch to other file
                        fileToProcessStack += [[nextFilepath, 0]]
                        currentDirectory = os.path.split (fileToProcessStack[-1][0])[0]
                        currentFilename = fileToProcessStack[-1][0]
                        currentLineNum = fileToProcessStack[-1][1]
                        # process file
                        continue
                    # DEFINE 
                    # define <identifier> 
                    elif cmd == "define":
                        # ignore if containing if was false
                        if len(containingIf) > 0 and containingIf[-1][1] == False:
                            currentLineNum += 1
                            continue
                        
                        # ensure identifier was provided 
                        if len(args) == 0 or args[0].type != IDENTIFIER:
                            print (f"Preprocessor Error: {cmd} directive needs an identifier")
                            print (f"   in file {currentFilename}")
                            for i in range(len(fileToProcessStack)-2, -1, -1):
                                print (f"      included from {fileToProcessStack[i][0]}:{fileToProcessStack[i][1]}")
                            print (f"   on line {currentLineNum+1}")
                            print (line)
                            exit(1)
                        # define the identifier
                        variables[args[0].value] = 0
                    # IFDEF
                    # ifdef <identifier>
                    elif cmd == "ifdef":
                        # ensure identifier was provided 
                        if len(args) == 0 or args[0].type != IDENTIFIER:
                            print (f"Preprocessor Error: {cmd} directive needs an identifier")
                            print (f"   in file {currentFilename}")
                            for i in range(len(fileToProcessStack)-2, -1, -1):
                                print (f"      included from {fileToProcessStack[i][0]}:{fileToProcessStack[i][1]}")
                            print (f"   on line {currentLineNum+1}")
                            print (line)
                            exit(1)
                        fileToProcessStack[-1][1] = currentLineNum
                        currentLocation = [fileToProcessStack[-1][0], fileToProcessStack[-1][1]+1, [], line]
                        for i in range(len(fileToProcessStack)-2, -1, -1):
                            currentLocation[2] += [[fileToProcessStack[i][0], fileToProcessStack[i][1]]]
                        if args[0].value in variables:
                            # print ("exists")
                            # mark as false if containing if was false
                            if len(containingIf) > 0 and containingIf[-1][1] == False:
                                containingIf += [[currentLocation, False]]
                            else:
                                containingIf += [[currentLocation, True]]
                        else:
                            # print ("DNE")
                            # mark as false if containing if was false
                            if len(containingIf) > 0 and containingIf[-1][1] == False:
                                containingIf += [[currentLocation, False]]
                            else:
                                containingIf += [[currentLocation, False]]
                    # IFNDEF
                    # ifndef <identifier>
                    elif cmd == "ifndef":
                        # ensure identifier was provided 
                        if len(args) == 0 or args[0].type != IDENTIFIER:
                            print (f"Preprocessor Error: {cmd} directive needs an identifier")
                            print (f"   in file {currentFilename}")
                            for i in range(len(fileToProcessStack)-2, -1, -1):
                                print (f"      included from {fileToProcessStack[i][0]}:{fileToProcessStack[i][1]}")
                            print (f"   on line {currentLineNum+1}")
                            print (line)
                            exit(1)
                        fileToProcessStack[-1][1] = currentLineNum
                        currentLocation = [fileToProcessStack[-1][0], fileToProcessStack[-1][1]+1, [], line]
                        for i in range(len(fileToProcessStack)-2, -1, -1):
                            currentLocation[2] += [[fileToProcessStack[i][0], fileToProcessStack[i][1]]]
                        if args[0].value not in variables:
                            # print ("DNE")
                            # mark as false if containing if was false
                            if len(containingIf) > 0 and containingIf[-1][1] == False:
                                containingIf += [[currentLocation, False]]
                            else:
                                containingIf += [[currentLocation, True]]
                        else:
                            # print ("exists")
                            # mark as false if containing if was false
                            if len(containingIf) > 0 and containingIf[-1][1] == False:
                                containingIf += [[currentLocation, False]]
                            else:
                                containingIf += [[currentLocation, False]]
                    # ELSE
                    # else
                    elif cmd == "else":
                        # ensure there was a previous if  
                        if len(containingIf) == 0:
                            print (f"Preprocessor Error: else without a matching if")
                            print (f"   in file {currentFilename}")
                            for i in range(len(fileToProcessStack)-2, -1, -1):
                                print (f"      included from {fileToProcessStack[i][0]}:{fileToProcessStack[i][1]}")
                            print (f"   on line {currentLineNum+1}")
                            print (line)
                            exit(1)
                        # this is true only if the if that contains it is not false and the prev if was true 
                        # this else overwrites the prev containing if 
                        fileToProcessStack[-1][1] = currentLineNum
                        currentLocation = [fileToProcessStack[-1][0], fileToProcessStack[-1][1]+1, [], line]
                        for i in range(len(fileToProcessStack)-2, -1, -1):
                            currentLocation[2] += [[fileToProcessStack[i][0], fileToProcessStack[i][1]]]
                        if len(containingIf) > 1 and containingIf[-2][1] == False:
                            containingIf[-1] = [currentLocation, False]
                        else:
                            containingIf[-1] = [currentLocation, not containingIf[-1][1]]
                        
                    # ENDIF
                    # endif
                    elif cmd == "endif":
                        # ensure there was an if to end
                        if len(containingIf) == 0:
                            print (f"Preprocessor Error: unmatched {cmd}")
                            print (f"   in file {currentFilename}")
                            for i in range(len(fileToProcessStack)-2, -1, -1):
                                print (f"      included from {fileToProcessStack[i][0]}:{fileToProcessStack[i][1]}")
                            print (f"   on line {currentLineNum+1}")
                            print (line)
                            exit(1)
                        # exit prev 
                        containingIf.pop()

                    # move on to next line
                    currentLineNum += 1
                    continue 

                # no directive - just include line 
                if len(containingIf) == 0 or containingIf[-1][1] == True:
                    # determine include chain for error reporting 
                    includeChain = []
                    for j in range(len(fileToProcessStack)-2, -1, -1):
                        includeChain += [[fileToProcessStack[j][0], fileToProcessStack[j][1]]]
                    self.outputLines += [[currentFilename, currentLineNum+1, line, includeChain]]
                currentLineNum += 1
            
            # finished processing current file
            # return to previous file or end if this was the main file
            fileToProcessStack.pop ()

        # Ensure all ifs were closed 
        if len(containingIf) != 0:
            print (f"Preprocessor Error: Unclosed conditional directives")
            for i in range(len(containingIf)):
                print (f"   Unclosed if:")
                print (f"      in file {containingIf[i][0][0]}")
                for j in range(len(containingIf[i][0][2])):
                    print (f"         included from {containingIf[i][0][2][j][0]}:{containingIf[i][0][2][j][1]}")
                print (f"      on line {containingIf[i][0][1]}")
                print (f"      {containingIf[i][0][3]}")
                print (f"      condition result: {containingIf[i][1]}")
                print ()
            exit (1)

        # output new code
        debugOutputStr = []
        outputStr = []
        for line in self.outputLines:
            # print (f"[{line[0]}]:{line[1]} {line[2].rstrip()}")
            # print (f"   {line[3]}")
            debugOutputStr += [f"[{line[0]}]:{line[1]} {line[2].rstrip()}"]
            outputStr += [line[2]]
        debugOutputStr = "\n".join(debugOutputStr)
        outputStr = "".join(outputStr)

        if self.outputDebug:
            f = open(self.debugOutputFilename, "w")
            f.write (debugOutputStr)

        if self.outputProcessed:
            print (f"Writing preprocessed code to \"{self.outputFilename}\"")
            f = open(self.outputFilename, "w")
            f.write (outputStr)      

        # return preprocessed code 
        return outputStr  

    def parseLine (self, line):

        currentIndex = 0
        DELIMITERS = " \t\n\r\v\f"

        # skip over whitespace
        while currentIndex < len(line) and line[currentIndex] in DELIMITERS:
            currentIndex += 1
        
        # ensure next is #
        if currentIndex >= len(line) or line[currentIndex] != "#":
            return False, None, []

        # we should have a preprocessor directive here 
        # consume #
        currentIndex += 1 
        
        # skip over whitespace
        while currentIndex < len(line) and line[currentIndex] in DELIMITERS:
            currentIndex += 1

        # read in command name
        command = []
        while currentIndex < len(line) and line[currentIndex].isalnum():
            command += [line[currentIndex]]
            currentIndex += 1
        commandName = "".join(command)

        # skip over whitespace
        while currentIndex < len(line) and line[currentIndex] in DELIMITERS:
            currentIndex += 1

        # read in arguments 
        arguments = [] 
        while currentIndex < len(line):

            # skip over whitespace
            if line[currentIndex] in DELIMITERS:
                currentIndex += 1
                continue
                
            # read string
            if line[currentIndex] == "\"":
                # skip over "
                currentIndex += 1
                arg = []
                # read chars until " is seen again or end of line
                while currentIndex < len(line) and line[currentIndex] != "\"":
                    arg += [line[currentIndex]]
                    currentIndex += 1
                # ensure string was closed 
                if currentIndex >= len(line) or line[currentIndex] != "\"":
                    print ("Preprocessor Error: string not closed")
                    exit(1)
                # add string to args 
                arguments += [DirectiveToken(STRING, "".join(arg))]
                # skip over "
                currentIndex += 1
                continue
            
            # read identifier 
            if line[currentIndex].isalpha() or line[currentIndex] == '_':
                arg = [line[currentIndex]]
                currentIndex += 1
                # read rest of identifier
                while currentIndex < len(line) and (line[currentIndex].isalnum() or line[currentIndex] == '_'):
                    arg += [line[currentIndex]]
                    currentIndex += 1
                # add arg 
                arguments += [DirectiveToken(IDENTIFIER, "".join(arg))]
                continue
            
            # other 
            arguments += [DirectiveToken(OTHER, line[currentIndex])]
            currentIndex += 1
        
        return True, commandName, arguments


# ========================================================================

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage:", sys.argv[0], "<file-name> {<extra-filenames>}")
        exit(1)
    
    # get all filenames 
    # first file is main file 
    mainFilename = sys.argv[1]
    # get rest of files if they are provided 
    otherFilenames = []
    for i in range(2, len(sys.argv)):
        otherFilenames += [sys.argv[i]]
    
    preprocessor = AmyScriptPreprocessor(mainFilename, otherFilenames)

    preprocessedCode = preprocessor.process()

    