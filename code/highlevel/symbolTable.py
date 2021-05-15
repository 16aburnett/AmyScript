



class SymbolTable:

    def __init__(self):
        self.nestLevel = 0
        # list of dictionaries
        self.table = [{}]

    def enterScope (self):
        self.table.append ({})
        self.nestLevel += 1

    def exitScope (self):
        self.table.pop ()
        self.nestLevel -= 1

    def insert (self, decl):
        name = decl.id
        # ensure variable wasnt already declared
        if (name in self.table[-1]):
            return False
        # add declaration to table
        self.table[-1][name] = decl
        return True

    def lookup (self, name):
        for i in range(len(self.table)-1, -1, -1):
            # check scope for var 
            if (name in self.table[i]):
                return self.table[i][name]
        # reaches here if no matching variable declaration was found
        return None
