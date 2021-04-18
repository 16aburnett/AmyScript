# The Amy Programming Language Stack
# By Amy Burnett
# November 5 2020
##########################################################################
# Imports


##########################################################################

class RecordInstance:

    def __init__(self, start_index:int):
        self.index = start_index
        self.variables = {}
        self.numParams = 0
        self.paramlabels = []

class Record:

    def __init__(self, start_index:int, function_name):
        self.start_index = start_index
        self.variables = {
            # save function name for recursion
            function_name : self 
        }
        self.numParams = 0
        self.paramlabels = []
        self.returnedValue = 0
    
    def getInstance(self):
        ri = RecordInstance(self.start_index)
        ri.variables = dict(self.variables)
        ri.numParams = self.numParams
        ri.paramlabels = list(self.paramlabels)
        return ri 

class Stack:

    def __init__(self):
        self.stack = [];

    def getIndex(self):
        return self.stack[-1].index
    
    def setIndex(self, index):
        self.stack[-1].index = index

    def incrementIndex(self):
        self.stack[-1].index += 1

    def getVariable(self, varname):
        return self.stack[-1].variables[varname]
    
    def hasVariable(self, varname):
        return varname in self.stack[-1].variables

    def setVariable(self, varname, value):
        self.stack[-1].variables[varname] = value

    def modifyVariable(self, varname, offset, value):
        self.stack[-1].variables[varname][offset] = value

    def pop(self):
        self.stack.pop()
    
    def push(self, recordInstance:RecordInstance):
        self.stack += [recordInstance]

    def setReturnedValue(self, rval):
        self.stack[-1].returnedValue = rval
    
    def getReturnedValue(self):
        return self.stack[-1].returnedValue