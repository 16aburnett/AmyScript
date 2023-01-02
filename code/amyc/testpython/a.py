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
# Class Declaration - __main____Vector__int inherits __main__Object
# Creating Dispatch Table (will be populated later)
__dtable____main____Vector__int = []
#-------------------------------------------------------------------------
# Field - int[] Vector<:int:>::data
__field____main____Vector__int____data = 1
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Field - int Vector<:int:>::size
__field____main____Vector__int____size = 2
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Field - int Vector<:int:>::capacity
__field____main____Vector__int____capacity = 3
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Constructor Declaration - Vector<:int:>::Vector() -> Vector<:int:>
def __ctor____main____Vector__int____Vector ():
    # Creating Class Instance
    this = [0] * 4
    # Add Dispatch Table
    this[0] = __dtable____main____Vector__int
    # Body
    #---------------------------------------------------------------------
    # Code Block
    this[__field____main____Vector__int____capacity] = 10
    this[__field____main____Vector__int____size] = 0
    this[__field____main____Vector__int____data] = [None] * this[__field____main____Vector__int____capacity]
    #---------------------------------------------------------------------
    # Return the constructed instance
    return this
# End Constructor Declaration - __ctor____main____Vector__int____Vector
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vector<:int:>::pushBack(int) -> void
def __method____main____Vector__int____pushBack__int (this, __main____Vector__int__pushBack__val):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    #---------------------------------------------------------------------
    # If-Statement
    if (this[__field____main____Vector__int____size] + 1 >= this[__field____main____Vector__int____capacity]):
        # Body
        #-----------------------------------------------------------------
        # Code Block
        this[__field____main____Vector__int____capacity] = this[__field____main____Vector__int____capacity] * 2
        __main____Vector__int__pushBack__block__1__if__2__block__3__nData = [None] * this[__field____main____Vector__int____capacity]
        #-----------------------------------------------------------------
        # For-Loop
        # Init
        __main____Vector__int__pushBack__block__1__if__2__block__3__for__4__i = 0
        while (__main____Vector__int__pushBack__block__1__if__2__block__3__for__4__i < this[__field____main____Vector__int____size]):
            #-------------------------------------------------------------
            # Code Block
            __main____Vector__int__pushBack__block__1__if__2__block__3__nData[__main____Vector__int__pushBack__block__1__if__2__block__3__for__4__i] = this[__field____main____Vector__int____data][__main____Vector__int__pushBack__block__1__if__2__block__3__for__4__i]
            #-------------------------------------------------------------
            __main____Vector__int__pushBack__block__1__if__2__block__3__for__4__i += 1
        #-----------------------------------------------------------------
        free (this[__field____main____Vector__int____data])
        this[__field____main____Vector__int____data] = __main____Vector__int__pushBack__block__1__if__2__block__3__nData
        #-----------------------------------------------------------------
    #---------------------------------------------------------------------
    this[__field____main____Vector__int____data][this[__field____main____Vector__int____size]] = __main____Vector__int__pushBack__val
    this[__field____main____Vector__int____size] += 1
    #---------------------------------------------------------------------
    return 0
# End Method Declaration - __method____main____Vector__int____pushBack__int
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vector<:int:>::popBack() -> int
def __method____main____Vector__int____popBack (this):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    this[__field____main____Vector__int____size] -= 1
    return this[__field____main____Vector__int____data][this[__field____main____Vector__int____size]]
    #---------------------------------------------------------------------
    return 0
# End Method Declaration - __method____main____Vector__int____popBack
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vector<:int:>::get(int) -> int
def __method____main____Vector__int____get__int (this, __main____Vector__int__get__index):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    return this[__field____main____Vector__int____data][__main____Vector__int__get__index]
    #---------------------------------------------------------------------
    return 0
# End Method Declaration - __method____main____Vector__int____get__int
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vector<:int:>::set(int, int) -> void
def __method____main____Vector__int____set__int__int (this, __main____Vector__int__set__index, __main____Vector__int__set__value):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    this[__field____main____Vector__int____data][__main____Vector__int__set__index] = __main____Vector__int__set__value
    #---------------------------------------------------------------------
    return 0
# End Method Declaration - __method____main____Vector__int____set__int__int
#-------------------------------------------------------------------------

# Populate Dispatch Table
__dtable____main____Vector__int = [__method____main____Vector__int____pushBack__int, __method____main____Vector__int____popBack, __method____main____Vector__int____get__int, __method____main____Vector__int____set__int__int]
# End Class Declaration - __main____Vector__int
#=========================================================================

#=========================================================================
# Class Declaration - __main____Vector__float inherits __main__Object
# Creating Dispatch Table (will be populated later)
__dtable____main____Vector__float = []
#-------------------------------------------------------------------------
# Field - float[] Vector<:float:>::data
__field____main____Vector__float____data = 1
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Field - int Vector<:float:>::size
__field____main____Vector__float____size = 2
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Field - int Vector<:float:>::capacity
__field____main____Vector__float____capacity = 3
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Constructor Declaration - Vector<:float:>::Vector() -> Vector<:float:>
def __ctor____main____Vector__float____Vector ():
    # Creating Class Instance
    this = [0] * 4
    # Add Dispatch Table
    this[0] = __dtable____main____Vector__float
    # Body
    #---------------------------------------------------------------------
    # Code Block
    this[__field____main____Vector__float____capacity] = 10
    this[__field____main____Vector__float____size] = 0
    this[__field____main____Vector__float____data] = [None] * this[__field____main____Vector__float____capacity]
    #---------------------------------------------------------------------
    # Return the constructed instance
    return this
# End Constructor Declaration - __ctor____main____Vector__float____Vector
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vector<:float:>::pushBack(float) -> void
def __method____main____Vector__float____pushBack__float (this, __main____Vector__float__pushBack__val):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    #---------------------------------------------------------------------
    # If-Statement
    if (this[__field____main____Vector__float____size] + 1 >= this[__field____main____Vector__float____capacity]):
        # Body
        #-----------------------------------------------------------------
        # Code Block
        this[__field____main____Vector__float____capacity] = this[__field____main____Vector__float____capacity] * 2
        __main____Vector__float__pushBack__block__10__if__11__block__12__nData = [None] * this[__field____main____Vector__float____capacity]
        #-----------------------------------------------------------------
        # For-Loop
        # Init
        __main____Vector__float__pushBack__block__10__if__11__block__12__for__13__i = 0
        while (__main____Vector__float__pushBack__block__10__if__11__block__12__for__13__i < this[__field____main____Vector__float____size]):
            #-------------------------------------------------------------
            # Code Block
            __main____Vector__float__pushBack__block__10__if__11__block__12__nData[__main____Vector__float__pushBack__block__10__if__11__block__12__for__13__i] = this[__field____main____Vector__float____data][__main____Vector__float__pushBack__block__10__if__11__block__12__for__13__i]
            #-------------------------------------------------------------
            __main____Vector__float__pushBack__block__10__if__11__block__12__for__13__i += 1
        #-----------------------------------------------------------------
        free (this[__field____main____Vector__float____data])
        this[__field____main____Vector__float____data] = __main____Vector__float__pushBack__block__10__if__11__block__12__nData
        #-----------------------------------------------------------------
    #---------------------------------------------------------------------
    this[__field____main____Vector__float____data][this[__field____main____Vector__float____size]] = __main____Vector__float__pushBack__val
    this[__field____main____Vector__float____size] += 1
    #---------------------------------------------------------------------
    return 0
# End Method Declaration - __method____main____Vector__float____pushBack__float
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vector<:float:>::popBack() -> float
def __method____main____Vector__float____popBack (this):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    this[__field____main____Vector__float____size] -= 1
    return this[__field____main____Vector__float____data][this[__field____main____Vector__float____size]]
    #---------------------------------------------------------------------
    return 0
# End Method Declaration - __method____main____Vector__float____popBack
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vector<:float:>::get(int) -> float
def __method____main____Vector__float____get__int (this, __main____Vector__float__get__index):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    return this[__field____main____Vector__float____data][__main____Vector__float__get__index]
    #---------------------------------------------------------------------
    return 0
# End Method Declaration - __method____main____Vector__float____get__int
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vector<:float:>::set(int, float) -> void
def __method____main____Vector__float____set__int__float (this, __main____Vector__float__set__index, __main____Vector__float__set__value):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    this[__field____main____Vector__float____data][__main____Vector__float__set__index] = __main____Vector__float__set__value
    #---------------------------------------------------------------------
    return 0
# End Method Declaration - __method____main____Vector__float____set__int__float
#-------------------------------------------------------------------------

# Populate Dispatch Table
__dtable____main____Vector__float = [__method____main____Vector__float____pushBack__float, __method____main____Vector__float____popBack, __method____main____Vector__float____get__int, __method____main____Vector__float____set__int__float]
# End Class Declaration - __main____Vector__float
#=========================================================================

# End Class Template - 
#=========================================================================

#=========================================================================
# Function Template - 
#=========================================================================
# Function Declaration - print<:int:>(Vector<:int:>) -> void
def __main____print__int____Vector__tparam0__int (__main__print__v):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    print__char ('[')
    #---------------------------------------------------------------------
    # If-Statement
    if (__main__print__v[__field____main____Vector__int____size] != 0):
        # Body
        print__int (__main__print__v[__field____main____Vector__int____data][0])
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    # For-Loop
    # Init
    __main__print__block__18__for__20__i = 1
    while (__main__print__block__18__for__20__i < __main__print__v[__field____main____Vector__int____size]):
        #-----------------------------------------------------------------
        # Code Block
        print__char (',')
        print__char (' ')
        print__int (__main__print__v[__field____main____Vector__int____data][__main__print__block__18__for__20__i])
        #-----------------------------------------------------------------
        __main__print__block__18__for__20__i += 1
    #---------------------------------------------------------------------
    print__char (']')
    #---------------------------------------------------------------------
# End Function Declaration - __main____print__int____Vector__tparam0__int
#=========================================================================

#=========================================================================
# Function Declaration - print<:float:>(Vector<:float:>) -> void
def __main____print__float____Vector__tparam0__float (__main__print__v):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    print__char ('[')
    #---------------------------------------------------------------------
    # If-Statement
    if (__main__print__v[__field____main____Vector__float____size] != 0):
        # Body
        print__float (__main__print__v[__field____main____Vector__float____data][0])
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    # For-Loop
    # Init
    __main__print__block__22__for__24__i = 1
    while (__main__print__block__22__for__24__i < __main__print__v[__field____main____Vector__float____size]):
        #-----------------------------------------------------------------
        # Code Block
        print__char (',')
        print__char (' ')
        print__float (__main__print__v[__field____main____Vector__float____data][__main__print__block__22__for__24__i])
        #-----------------------------------------------------------------
        __main__print__block__22__for__24__i += 1
    #---------------------------------------------------------------------
    print__char (']')
    #---------------------------------------------------------------------
# End Function Declaration - __main____print__float____Vector__tparam0__float
#=========================================================================

# End Function Template - 
#=========================================================================

#=========================================================================
# Function Template - 
#=========================================================================
# Function Declaration - println<:int:>(Vector<:int:>) -> void
def __main____println__int____Vector__tparam0__int (__main__println__v):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    __main____print__int____Vector__tparam0__int (__main__println__v)
    println ()
    #---------------------------------------------------------------------
# End Function Declaration - __main____println__int____Vector__tparam0__int
#=========================================================================

#=========================================================================
# Function Declaration - println<:float:>(Vector<:float:>) -> void
def __main____println__float____Vector__tparam0__float (__main__println__v):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    __main____print__float____Vector__tparam0__float (__main__println__v)
    println ()
    #---------------------------------------------------------------------
# End Function Declaration - __main____println__float____Vector__tparam0__float
#=========================================================================

# End Function Template - 
#=========================================================================

__main__nums = __ctor____main____Vector__int____Vector ()
__main____println__int____Vector__tparam0__int (__main__nums)
__method____main____Vector__int____pushBack__int (__main__nums, 4)
__main____println__int____Vector__tparam0__int (__main__nums)
__method____main____Vector__int____pushBack__int (__main__nums, 24)
__main____println__int____Vector__tparam0__int (__main__nums)
println__int (__method____main____Vector__int____popBack (__main__nums))
__main____println__int____Vector__tparam0__int (__main__nums)
__method____main____Vector__int____pushBack__int (__main__nums, 42)
__main____println__int____Vector__tparam0__int (__main__nums)
#-------------------------------------------------------------------------
# For-Loop
# Init
__main__for__28__i = 0
while (__main__for__28__i < 10):
    #---------------------------------------------------------------------
    # Code Block
    __method____main____Vector__int____pushBack__int (__main__nums, __main__for__28__i * 2)
    #---------------------------------------------------------------------
    __main__for__28__i += 1
#-------------------------------------------------------------------------
__main____println__int____Vector__tparam0__int (__main__nums)
__main__v = __ctor____main____Vector__float____Vector ()
__main____println__float____Vector__tparam0__float (__main__v)
__method____main____Vector__float____pushBack__float (__main__v, 3.14)
__main____println__float____Vector__tparam0__float (__main__v)
__method____main____Vector__float____pushBack__float (__main__v, 21.0)
__main____println__float____Vector__tparam0__float (__main__v)
__method____main____Vector__float____pushBack__float (__main__v, 1.4123423423477723)
__main____println__float____Vector__tparam0__float (__main__v)
println__float (__method____main____Vector__float____popBack (__main__v))
__main____println__float____Vector__tparam0__float (__main__v)
__method____main____Vector__float____pushBack__float (__main__v, 0.0001)
__main____println__float____Vector__tparam0__float (__main__v)

#=========================================================================
#### END OF CODE ########################################################
#=========================================================================

