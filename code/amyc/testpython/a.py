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
# Class Declaration - __main____IntArray inherits __main__Object
# Creating Dispatch Table (will be populated later)
__dtable____main____IntArray = []
#-------------------------------------------------------------------------
# Field - int[] IntArray::data
__field____main____IntArray____data = 1
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Field - int IntArray::size
__field____main____IntArray____size = 2
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Field - int IntArray::capacity
__field____main____IntArray____capacity = 3
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Constructor Declaration - IntArray::IntArray() -> IntArray
def __ctor____main____IntArray____IntArray ():
    # Creating Class Instance
    this = [0] * 4
    # Add Dispatch Table
    this[0] = __dtable____main____IntArray
    # Body
    #---------------------------------------------------------------------
    # Code Block
    this[__field____main____IntArray____capacity] = 10
    this[__field____main____IntArray____size] = 0
    this[__field____main____IntArray____data] = [None] * this[__field____main____IntArray____capacity]
    #---------------------------------------------------------------------
    # Return the constructed instance
    return this
# End Constructor Declaration - __ctor____main____IntArray____IntArray
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - IntArray::pushBack(int) -> void
def __method____main____IntArray____pushBack__int (this, __main____IntArray__pushBack__val):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    #---------------------------------------------------------------------
    # If-Statement
    if (this[__field____main____IntArray____size] + 1 >= this[__field____main____IntArray____capacity]):
        # Body
        #-----------------------------------------------------------------
        # Code Block
        this[__field____main____IntArray____capacity] = this[__field____main____IntArray____capacity] * 2
        __main____IntArray__pushBack__block__1__if__2__block__3__nData = [None] * this[__field____main____IntArray____capacity]
        #-----------------------------------------------------------------
        # For-Loop
        # Init
        __main____IntArray__pushBack__block__1__if__2__block__3__for__4__i = 0
        while (__main____IntArray__pushBack__block__1__if__2__block__3__for__4__i < this[__field____main____IntArray____size]):
            #-------------------------------------------------------------
            # Code Block
            __main____IntArray__pushBack__block__1__if__2__block__3__nData[__main____IntArray__pushBack__block__1__if__2__block__3__for__4__i] = this[__field____main____IntArray____data][__main____IntArray__pushBack__block__1__if__2__block__3__for__4__i]
            #-------------------------------------------------------------
            __main____IntArray__pushBack__block__1__if__2__block__3__for__4__i += 1
        #-----------------------------------------------------------------
        free (this[__field____main____IntArray____data])
        this[__field____main____IntArray____data] = __main____IntArray__pushBack__block__1__if__2__block__3__nData
        #-----------------------------------------------------------------
    #---------------------------------------------------------------------
    this[__field____main____IntArray____data][this[__field____main____IntArray____size]] = __main____IntArray__pushBack__val
    this[__field____main____IntArray____size] += 1
    #---------------------------------------------------------------------
    return 0
# End Method Declaration - __method____main____IntArray____pushBack__int
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - IntArray::popBack() -> int
def __method____main____IntArray____popBack (this):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    this[__field____main____IntArray____size] -= 1
    return this[__field____main____IntArray____data][this[__field____main____IntArray____size] + 1]
    #---------------------------------------------------------------------
    return 0
# End Method Declaration - __method____main____IntArray____popBack
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - IntArray::get(int) -> int
def __method____main____IntArray____get__int (this, __main____IntArray__get__index):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    return this[__field____main____IntArray____data][__main____IntArray__get__index]
    #---------------------------------------------------------------------
    return 0
# End Method Declaration - __method____main____IntArray____get__int
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - IntArray::set(int, int) -> void
def __method____main____IntArray____set__int__int (this, __main____IntArray__set__index, __main____IntArray__set__value):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    this[__field____main____IntArray____data][__main____IntArray__set__index] = __main____IntArray__set__value
    #---------------------------------------------------------------------
    return 0
# End Method Declaration - __method____main____IntArray____set__int__int
#-------------------------------------------------------------------------

# Populate Dispatch Table
__dtable____main____IntArray = [__method____main____IntArray____pushBack__int, __method____main____IntArray____popBack, __method____main____IntArray____get__int, __method____main____IntArray____set__int__int]
# End Class Declaration - __main____IntArray
#=========================================================================

#=========================================================================
# Function Declaration - print(IntArray) -> void
def __main____print__IntArray (__main__print__arr):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    print__char ('[')
    #---------------------------------------------------------------------
    # If-Statement
    if (__main__print__arr[__field____main____IntArray____size] != 0):
        # Body
        #-----------------------------------------------------------------
        # Code Block
        print__int (__main__print__arr[__field____main____IntArray____data][0])
        #-----------------------------------------------------------------
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    # For-Loop
    # Init
    __main__print__block__9__for__12__i = 1
    while (__main__print__block__9__for__12__i < __main__print__arr[__field____main____IntArray____size]):
        #-----------------------------------------------------------------
        # Code Block
        print__char (',')
        print__char (' ')
        print__int (__main__print__arr[__field____main____IntArray____data][__main__print__block__9__for__12__i])
        #-----------------------------------------------------------------
        __main__print__block__9__for__12__i += 1
    #---------------------------------------------------------------------
    print__char (']')
    #---------------------------------------------------------------------
# End Function Declaration - __main____print__IntArray
#=========================================================================

#=========================================================================
# Function Declaration - println(IntArray) -> void
def __main____println__IntArray (__main__println__arr):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    __main____print__IntArray (__main__println__arr)
    println ()
    #---------------------------------------------------------------------
# End Function Declaration - __main____println__IntArray
#=========================================================================

__main__arr = __ctor____main____IntArray____IntArray ()
__main____println__IntArray (__main__arr)
__method____main____IntArray____pushBack__int (__main__arr, 10)
__main____println__IntArray (__main__arr)
#-------------------------------------------------------------------------
# For-Loop
# Init
__main__for__15__i = 0
while (__main__for__15__i < 5):
    __method____main____IntArray____pushBack__int (__main__arr, __main__for__15__i * 2)
    __main__for__15__i += 1
#-------------------------------------------------------------------------
__main____println__IntArray (__main__arr)
__method____main____IntArray____popBack (__main__arr)
__main____println__IntArray (__main__arr)

#=========================================================================
#### END OF CODE ########################################################
#=========================================================================

