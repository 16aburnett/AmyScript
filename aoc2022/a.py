# Python compiled from AmyScript
#=========================================================================

#=========================================================================
#### LIBRARY CODE #######################################################
#=========================================================================

# # AmyScript Built-in library
# # Author: Amy Burnett
# # ========================================================================

# # ========================================================================

# # Exits the program with the given exit code 
# # void exit(int exit_code)
# # - exit_code : [rbp + 16]
# # - uses external exit function from libc
def exit__int (exit_code):
    exit (exit_code)

# # ========================================================================

# # Frees memory of the given pointer
# # void free()
# # - exit_code : [rbp + 16]
# # - uses external exit function from libc
def free (ptr):
    # do nothing, python has its own garbage collection
    pass

# # ========================================================================
# # Prints a given string to the screen
# # void print (char[] stringToPrint)#
# # stringToPrint : [rbp + 16]
def print__char__1 (s):
    print (s, end="")

# # ========================================================================

# # Prints an int to the screen
# # Utilizes printf "%d"
# # void print (int valueToPrint)#
# # valueToPrint : [rbp + 16]
def print__int (v):
    print (v, end="")

# # ========================================================================

# # Prints a char to the screen
# # Utilizes printf "%c"
# # void print (char valueToPrint)#
# # valueToPrint : [rbp + 16]
def print__char (v):
    print (v, end="")

# # ========================================================================

# # Prints a float to the screen
# # void print (float valueToPrint)
def print__float (v):
    print (v, end="")

# # //========================================================================
# # // Prints a given string to the screen with a newline at the end
# # // void println (char[] stringToPrint)#
# # stringToPrint : [rbp + 16]
def println__char__1 (v):
    print (v)

# # ========================================================================

# # Prints an int to the screen with a newline
# # Utilizes printf "%d"
# # void println (int valueToPrint)#
# # valueToPrint : [rbp + 16]
def println__int (v):
    print (v)

# # ========================================================================
# # // Prints a float to the screen with a newline
# # // void println (float floatToPrint)#
# # valueToPrint : [rbp + 16]
def println__float (v):
    print (v)

# # //========================================================================
# # // Prints a char to the screen with a newline
# # // void println (char charToPrint)#
def println__char (v):
    print (v)

# # //========================================================================
# # // Prints an enum's integer value with a newline
# # // void println (Enum e)#
def println__Enum (v):
    print (v)

# # //========================================================================
# # // Prints a newline to the console
# # // void println ()#
def println ():
    print ()

# # //========================================================================
# # // grabs input from the console 
# # this waits for a line if there isnt one
# # // char[] input ()#
def _input ():
    return input ()

# # //========================================================================
# # // returns default float value
# # // float float ()#
def float ():
    return 0.0

# # //========================================================================
# # // converts int to float
# # // float intToFloat (int value)#
# # value : [rbp + 16]
def intToFloat__int (v):
    return float (v)

# # //========================================================================
# # // parses a float from a given char[]
# # // float stringToFloat (char[])#
# # str : [rbp + 16]
def stringToFloat__char__1 (s):
    return float (s)

# # //========================================================================
# # // returns default int value
# # // int int ()#
def int ():
    return 0

# # //========================================================================
# # // returns default char value
# # // char char ()#
def char ():
 return '0'

# # //========================================================================
# # // converts float to int
# # // int floatToInt (float)#
def floatToInt__float (f):
    return int(f)

# # //========================================================================
# # // parses an int from a given char[]
# # // int stringToInt (char[] str)#
# # str : [rbp + 16]
def stringToInt__char__1 (s):
    return int(s)

# # //========================================================================
# # // parses an int from a given char
# # // int charToInt (char)#
def charToInt__char (c):
    return int(c)

# # //========================================================================
# # // converts int to string
# # // char[] string (int)#
def string__int (i):
    return str(i)

# # //========================================================================
# # // converts float to string
# # // char[] string (float)#
def string__float (f):
    return str(f)

# # //========================================================================

# # // returns default value for array and object (null)
# # // null null ()#
def null ():
    return None

# # //========================================================================
#=========================================================================
#### COMPILED CODE ######################################################
#=========================================================================

#=========================================================================
# Class Template - 
#=========================================================================
# Class Declaration - __main____Vector__char__1 inherits __main__Object
# Creating Dispatch Table (will be populated later)
__dtable____main____Vector__char__1 = []
#-------------------------------------------------------------------------
# Field - char[][] Vector<:char[]:>::data
__field____main____Vector__char__1____data = 1
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Field - int Vector<:char[]:>::size
__field____main____Vector__char__1____size = 2
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Field - int Vector<:char[]:>::capacity
__field____main____Vector__char__1____capacity = 3
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Constructor Declaration - Vector<:char[]:>::Vector() -> Vector<:char[]:>
def __ctor____main____Vector__char__1____Vector ():
    # Creating Class Instance
    this = [0] * 4
    # Add Dispatch Table
    this[0] = __dtable____main____Vector__char__1
    # Body
    #---------------------------------------------------------------------
    # Code Block
    this[__field____main____Vector__char__1____capacity] = 10
    this[__field____main____Vector__char__1____size] = 0
    this[__field____main____Vector__char__1____data] = [None] * this[__field____main____Vector__char__1____capacity]
    #---------------------------------------------------------------------
    # Return the constructed instance
    return this
# End Constructor Declaration - __ctor____main____Vector__char__1____Vector
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vector<:char[]:>::pushBack(char[]) -> void
def __method____main____Vector__char__1____pushBack__char__1 (this, __main____Vector__char__1__pushBack__val):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    #---------------------------------------------------------------------
    # If-Statement
    if (this[__field____main____Vector__char__1____size] + 1 >= this[__field____main____Vector__char__1____capacity]):
        # Body
        #-----------------------------------------------------------------
        # Code Block
        this[__field____main____Vector__char__1____capacity] = this[__field____main____Vector__char__1____capacity] * 2
        __main____Vector__char__1__pushBack__block__1__if__2__block__3__nData = [None] * this[__field____main____Vector__char__1____capacity]
        #-----------------------------------------------------------------
        # For-Loop
        # Init
        __main____Vector__char__1__pushBack__block__1__if__2__block__3__for__4__i = 0
        while (__main____Vector__char__1__pushBack__block__1__if__2__block__3__for__4__i < this[__field____main____Vector__char__1____size]):
            #-------------------------------------------------------------
            # Code Block
            __main____Vector__char__1__pushBack__block__1__if__2__block__3__nData[__main____Vector__char__1__pushBack__block__1__if__2__block__3__for__4__i] = this[__field____main____Vector__char__1____data][__main____Vector__char__1__pushBack__block__1__if__2__block__3__for__4__i]
            #-------------------------------------------------------------
            (__main____Vector__char__1__pushBack__block__1__if__2__block__3__for__4__i:=__main____Vector__char__1__pushBack__block__1__if__2__block__3__for__4__i+1)
        #-----------------------------------------------------------------
        free (this[__field____main____Vector__char__1____data])
        this[__field____main____Vector__char__1____data] = __main____Vector__char__1__pushBack__block__1__if__2__block__3__nData
        #-----------------------------------------------------------------
    #---------------------------------------------------------------------
    this[__field____main____Vector__char__1____data][this[__field____main____Vector__char__1____size]] = __main____Vector__char__1__pushBack__val
    (this[__field____main____Vector__char__1____size]:=this[__field____main____Vector__char__1____size]+1)
    #---------------------------------------------------------------------
    return 0
# End Method Declaration - __method____main____Vector__char__1____pushBack__char__1
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vector<:char[]:>::popBack() -> char[]
def __method____main____Vector__char__1____popBack (this):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    return this[__field____main____Vector__char__1____data][(this[__field____main____Vector__char__1____size]:=this[__field____main____Vector__char__1____size]-1)]
    #---------------------------------------------------------------------
    return 0
# End Method Declaration - __method____main____Vector__char__1____popBack
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vector<:char[]:>::get(int) -> char[]
def __method____main____Vector__char__1____get__int (this, __main____Vector__char__1__get__index):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    return this[__field____main____Vector__char__1____data][__main____Vector__char__1__get__index]
    #---------------------------------------------------------------------
    return 0
# End Method Declaration - __method____main____Vector__char__1____get__int
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vector<:char[]:>::set(int, char[]) -> void
def __method____main____Vector__char__1____set__int__char__1 (this, __main____Vector__char__1__set__index, __main____Vector__char__1__set__value):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    this[__field____main____Vector__char__1____data][__main____Vector__char__1__set__index] = __main____Vector__char__1__set__value
    #---------------------------------------------------------------------
    return 0
# End Method Declaration - __method____main____Vector__char__1____set__int__char__1
#-------------------------------------------------------------------------

# Populate Dispatch Table
__dtable____main____Vector__char__1 = [__method____main____Vector__char__1____pushBack__char__1, __method____main____Vector__char__1____popBack, __method____main____Vector__char__1____get__int, __method____main____Vector__char__1____set__int__char__1]
# End Class Declaration - __main____Vector__char__1
#=========================================================================

# End Class Template - 
#=========================================================================

__main__line = input ()
__main__total = 0
__main__lines = __ctor____main____Vector__char__1____Vector ()
#-------------------------------------------------------------------------
# While-Loop
while (__main__line[0] != '$'):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    __method____main____Vector__char__1____pushBack__char__1 (__main__lines, __main__line)
    __main__line = input ()
    #---------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# For-Loop
# Init
__main__for__11__l = 0
while (__main__for__11__l < __main__lines[__field____main____Vector__char__1____size]):
    #---------------------------------------------------------------------
    # Code Block
    __main__for__11__block__12__line = __main__lines[__field____main____Vector__char__1____data][__main__for__11__l]
    __main__for__11__block__12__indexcomma = 0
    __main__for__11__block__12__indexdash0 = 0
    __main__for__11__block__12__indexdash1 = 0
    #---------------------------------------------------------------------
    # For-Loop
    # Init
    __main__for__11__block__12__for__13__i = 0
    while (__main__for__11__block__12__for__13__i < len (__main__for__11__block__12__line)):
        #-----------------------------------------------------------------
        # Code Block
        #-----------------------------------------------------------------
        # If-Statement
        if (__main__for__11__block__12__line[__main__for__11__block__12__for__13__i] == '-' and __main__for__11__block__12__indexcomma == 0):
            # Body
            __main__for__11__block__12__indexdash0 = __main__for__11__block__12__for__13__i
        #-----------------------------------------------------------------
        # Elif-Statement
        elif (__main__for__11__block__12__line[__main__for__11__block__12__for__13__i] == '-'):
            # Body
            __main__for__11__block__12__indexdash1 = __main__for__11__block__12__for__13__i
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # If-Statement
        if (__main__for__11__block__12__line[__main__for__11__block__12__for__13__i] == ','):
            # Body
            __main__for__11__block__12__indexcomma = __main__for__11__block__12__for__13__i
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        (__main__for__11__block__12__for__13__i:=__main__for__11__block__12__for__13__i+1)
    #---------------------------------------------------------------------
    __main__for__11__block__12__begin = 0
    __main__for__11__block__12__end = __main__for__11__block__12__indexdash0
    __main__for__11__block__12__iter = 0
    __main__for__11__block__12__a_ = [None] * __main__for__11__block__12__end - __main__for__11__block__12__begin
    #---------------------------------------------------------------------
    # For-Loop
    # Init
    __main__for__11__block__12__for__17__i = __main__for__11__block__12__begin
    while (__main__for__11__block__12__for__17__i < __main__for__11__block__12__end):
        __main__for__11__block__12__a_[(__main__for__11__block__12__iter:=__main__for__11__block__12__iter+1)-1] = __main__for__11__block__12__line[__main__for__11__block__12__for__17__i]
        (__main__for__11__block__12__for__17__i:=__main__for__11__block__12__for__17__i+1)
    #---------------------------------------------------------------------
    __main__for__11__block__12__begin = __main__for__11__block__12__indexdash0 + 1
    __main__for__11__block__12__end = __main__for__11__block__12__indexcomma
    __main__for__11__block__12__iter = 0
    __main__for__11__block__12__b_ = [None] * __main__for__11__block__12__end - __main__for__11__block__12__begin
    #---------------------------------------------------------------------
    # For-Loop
    # Init
    __main__for__11__block__12__for__18__i = __main__for__11__block__12__begin
    while (__main__for__11__block__12__for__18__i < __main__for__11__block__12__end):
        __main__for__11__block__12__b_[(__main__for__11__block__12__iter:=__main__for__11__block__12__iter+1)-1] = __main__for__11__block__12__line[__main__for__11__block__12__for__18__i]
        (__main__for__11__block__12__for__18__i:=__main__for__11__block__12__for__18__i+1)
    #---------------------------------------------------------------------
    __main__for__11__block__12__begin = __main__for__11__block__12__indexcomma + 1
    __main__for__11__block__12__end = __main__for__11__block__12__indexdash1
    __main__for__11__block__12__iter = 0
    __main__for__11__block__12__c_ = [None] * __main__for__11__block__12__end - __main__for__11__block__12__begin
    #---------------------------------------------------------------------
    # For-Loop
    # Init
    __main__for__11__block__12__for__19__i = __main__for__11__block__12__begin
    while (__main__for__11__block__12__for__19__i < __main__for__11__block__12__end):
        __main__for__11__block__12__c_[(__main__for__11__block__12__iter:=__main__for__11__block__12__iter+1)-1] = __main__for__11__block__12__line[__main__for__11__block__12__for__19__i]
        (__main__for__11__block__12__for__19__i:=__main__for__11__block__12__for__19__i+1)
    #---------------------------------------------------------------------
    __main__for__11__block__12__begin = __main__for__11__block__12__indexdash1 + 1
    __main__for__11__block__12__end = len (__main__for__11__block__12__line) - 1
    __main__for__11__block__12__iter = 0
    __main__for__11__block__12__d_ = [None] * __main__for__11__block__12__end - __main__for__11__block__12__begin
    #---------------------------------------------------------------------
    # For-Loop
    # Init
    __main__for__11__block__12__for__20__i = __main__for__11__block__12__begin
    while (__main__for__11__block__12__for__20__i < __main__for__11__block__12__end):
        __main__for__11__block__12__d_[(__main__for__11__block__12__iter:=__main__for__11__block__12__iter+1)-1] = __main__for__11__block__12__line[__main__for__11__block__12__for__20__i]
        (__main__for__11__block__12__for__20__i:=__main__for__11__block__12__for__20__i+1)
    #---------------------------------------------------------------------
    __main__for__11__block__12__begin0 = stringToInt__char__1 (__main__for__11__block__12__a_)
    __main__for__11__block__12__end0 = stringToInt__char__1 (__main__for__11__block__12__b_) + 1
    __main__for__11__block__12__begin1 = stringToInt__char__1 (__main__for__11__block__12__c_)
    __main__for__11__block__12__end1 = stringToInt__char__1 (__main__for__11__block__12__d_) + 1
    __main__for__11__block__12__isAInB = 0
    __main__for__11__block__12__isBInA = 0
    #---------------------------------------------------------------------
    # If-Statement
    if (__main__for__11__block__12__begin0 >= __main__for__11__block__12__begin1 and __main__for__11__block__12__end0 <= __main__for__11__block__12__end1):
        # Body
        __main__for__11__block__12__isAInB = 1
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    # If-Statement
    if (__main__for__11__block__12__begin1 >= __main__for__11__block__12__begin0 and __main__for__11__block__12__end1 <= __main__for__11__block__12__end0):
        # Body
        __main__for__11__block__12__isBInA = 1
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    # If-Statement
    if (__main__for__11__block__12__isAInB or __main__for__11__block__12__isBInA):
        # Body
        #-----------------------------------------------------------------
        # Code Block
        (__main__total:=__main__total+1)-1
        #-----------------------------------------------------------------
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    (__main__for__11__l:=__main__for__11__l+1)
#-------------------------------------------------------------------------
println__int (__main__total)

#=========================================================================
#### END OF CODE ########################################################
#=========================================================================

