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
        self.records = {}
        self.numParams = 0
        self.paramlabels = []

class Record:

    def __init__(self, start_index:int, function_name):
        self.start_index = start_index
        self.variables = {}
        self.records = {
            function_name : self
        }
        self.numParams = 0
        self.paramlabels = []
        self.returnedValue = 0
    
    def getInstance(self):
        ri = RecordInstance(self.start_index)
        ri.variables = dict(self.variables)
        ri.records = dict(self.records)
        ri.numParams = self.numParams
        ri.paramlabels = list(self.paramlabels)
        return ri 