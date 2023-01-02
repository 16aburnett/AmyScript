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
#### SETUP EXPRESSION RESULT STACK ######################################
#=========================================================================

# This stack is used to store results of expressions
stack = []

#=========================================================================
#### COMPILED CODE ######################################################
#=========================================================================

# Statement
# Assignment - '='
# RHS
# Int Literal
stack.append(3)
# LHS
__main__x = 0
__rhs = stack.pop()
__main__x = __rhs
stack.append (__main__x)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Function Call - println(int) -> void
# Arguments
# Addition
# LHS
stack.append(__main__x)
# RHS
# Int Literal
stack.append(5)
__rhs = stack.pop()
__lhs = stack.pop()
__res = __lhs + __rhs
stack.append(__res)
__arg0 = stack.pop ()
# *** println
__res = println__int (__arg0)
stack.append (__res) # function call result
# Statement results can be ignored
stack.pop ()
# End Statement

#-------------------------------------------------------------------------
# If-Statement
# Precomputing all if/elif conditions and give unique names
# bc we can't have code between if and elif
# Condition
# Greater Than
# LHS
stack.append(__main__x)
# RHS
# Int Literal
stack.append(0)
__rhs = stack.pop ()
__lhs = stack.pop ()
__res = __lhs > __rhs
stack.append (__res)
__if__0__cond = stack.pop ()
# get condition from stack
if (__if__0__cond):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Function Call - println(int) -> void
    # Arguments
    # Pre-Increment
    # RHS
    stack.append(__main__x)
    __rhs = stack.pop ()
    __main__x = __main__x + 1
    __res = __main__x
    stack.append (__res)
    __arg0 = stack.pop ()
    # *** println
    __res = println__int (__arg0)
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
# End of if
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# For-Loop
# Init
# Assignment - '='
# RHS
# Int Literal
stack.append(0)
# LHS
__main__for__2__i = 0
__rhs = stack.pop()
__main__for__2__i = __rhs
stack.append (__main__for__2__i)
# Using an infinite loop so we can write a separate multi-line condition
while (1):
    # Condition
    # Less Than
    # LHS
    stack.append(__main__for__2__i)
    # RHS
    # Int Literal
    stack.append(10)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs < __rhs
    stack.append (__res)
    __cond = stack.pop ()
    # break out of loop if condition is false
    if (__cond == 0): break
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Function Call - print(int) -> void
    # Arguments
    # Multiplication
    # LHS
    stack.append(__main__for__2__i)
    # RHS
    # Int Literal
    stack.append(2)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs * __rhs
    stack.append(__res)
    __arg0 = stack.pop ()
    # *** print
    __res = print__int (__arg0)
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Function Call - print(char) -> void
    # Arguments
    # Char Literal
    stack.append(' ')
    __arg0 = stack.pop ()
    # *** print
    __res = print__char (__arg0)
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
    # Update
    # Pre-Increment
    # RHS
    stack.append(__main__for__2__i)
    __rhs = stack.pop ()
    __main__for__2__i = __main__for__2__i + 1
    __res = __main__for__2__i
    stack.append (__res)
#-------------------------------------------------------------------------
# Statement
# Function Call - print(char[]) -> void
# Arguments
stack.append("\n")
__arg0 = stack.pop ()
# *** print
__res = print__char__1 (__arg0)
stack.append (__res) # function call result
# Statement results can be ignored
stack.pop ()
# End Statement

#-------------------------------------------------------------------------
# While-Loop
# Using an infinite loop so we can write a separate multi-line condition
while (1):
    # Condition
    # Int Literal
    stack.append(1)
    __cond = stack.pop ()
    # break out of loop if condition is false
    if (__cond == 0): break
    # Body
    #---------------------------------------------------------------------
    # Code Block
    #---------------------------------------------------------------------
    # If-Statement
    # Precomputing all if/elif conditions and give unique names
    # bc we can't have code between if and elif
    # Condition
    # Less Than or Equal to
    # LHS
    stack.append(__main__x)
    # RHS
    # Int Literal
    stack.append(0)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs <= __rhs
    stack.append (__res)
    __if__6__cond = stack.pop ()
    # get condition from stack
    if (__if__6__cond):
        # Body
        # Break out of __while__4
        break
    # End of if
    #---------------------------------------------------------------------
    # Statement
    # Function Call - println(int) -> void
    # Arguments
    # Post-Decrement
    __res = __main__x
    __main__x = __main__x - 1
    stack.append (__res)
    __arg0 = stack.pop ()
    # *** println
    __res = println__int (__arg0)
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
# End of While
#-------------------------------------------------------------------------
#=========================================================================
# Function Declaration - sum(int, int) -> int
def __main____sum__int__int (__main__sum__a, __main__sum__b):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Return
    # Addition
    # LHS
    stack.append(__main__sum__a)
    # RHS
    stack.append(__main__sum__b)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs + __rhs
    stack.append(__res)
    __rVal = stack.pop ()
    return __rVal
    #---------------------------------------------------------------------
# End Function Declaration - __main____sum__int__int
#=========================================================================

# Statement
# Function Call - println(int) -> void
# Arguments
# Function Call - sum(int, int) -> int
# Arguments
# Int Literal
stack.append(7)
# Int Literal
stack.append(42)
__arg1 = stack.pop ()
__arg0 = stack.pop ()
# *** sum
__res = __main____sum__int__int (__arg0, __arg1)
stack.append (__res) # function call result
__arg0 = stack.pop ()
# *** println
__res = println__int (__arg0)
stack.append (__res) # function call result
# Statement results can be ignored
stack.pop ()
# End Statement

#=========================================================================
# Class Declaration - __main____Vec2 inherits __main__Object
# Creating Dispatch Table (will be populated later)
__dtable____main____Vec2 = []
#-------------------------------------------------------------------------
# Field - float Vec2::x
__field____main____Vec2____x = 1
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Field - float Vec2::y
__field____main____Vec2____y = 2
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Constructor Declaration - Vec2::Vec2(float, float) -> Vec2
def __ctor____main____Vec2____Vec2__float__float (__main____Vec2__Vec2__x, __main____Vec2__Vec2__y):
    # Creating Class Instance
    this = [0] * 3
    # Add Dispatch Table
    this[0] = __dtable____main____Vec2
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main____Vec2__Vec2__x)
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append(__field____main____Vec2____x)
    __child = stack.pop()
    __parent = stack.pop()
    __rhs = stack.pop()
    __parent[__child] = __rhs
    stack.append (__parent[__child])
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main____Vec2__Vec2__y)
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append(__field____main____Vec2____y)
    __child = stack.pop()
    __parent = stack.pop()
    __rhs = stack.pop()
    __parent[__child] = __rhs
    stack.append (__parent[__child])
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
    # Return the constructed instance
    return this
# End Constructor Declaration - __ctor____main____Vec2____Vec2__float__float
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vec2::add(Vec2) -> void
def __method____main____Vec2____add__Vec2 (this, __main____Vec2__add__other):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Assignment - '+='
    # RHS
    # Member Accessor
    # LHS
    stack.append(__main____Vec2__add__other)
    # RHS
    stack.append (__field____main____Vec2____x)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append(__field____main____Vec2____x)
    __child = stack.pop()
    __parent = stack.pop()
    __rhs = stack.pop()
    __parent[__child] = __parent[__child] + __rhs
    stack.append (__parent[__child])
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '+='
    # RHS
    # Member Accessor
    # LHS
    stack.append(__main____Vec2__add__other)
    # RHS
    stack.append (__field____main____Vec2____y)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append(__field____main____Vec2____y)
    __child = stack.pop()
    __parent = stack.pop()
    __rhs = stack.pop()
    __parent[__child] = __parent[__child] + __rhs
    stack.append (__parent[__child])
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
    return 0
# End Method Declaration - __method____main____Vec2____add__Vec2
#-------------------------------------------------------------------------

# Populate Dispatch Table
__dtable____main____Vec2 = [__method____main____Vec2____add__Vec2]
# End Class Declaration - __main____Vec2
#=========================================================================

#=========================================================================
# Function Declaration - print(Vec2) -> void
def __main____print__Vec2 (__main__print__v):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Function Call - print(char) -> void
    # Arguments
    # Char Literal
    stack.append('(')
    __arg0 = stack.pop ()
    # *** print
    __res = print__char (__arg0)
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Function Call - print(float) -> void
    # Arguments
    # Member Accessor
    # LHS
    stack.append(__main__print__v)
    # RHS
    stack.append (__field____main____Vec2____x)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __arg0 = stack.pop ()
    # *** print
    __res = print__float (__arg0)
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Function Call - print(char) -> void
    # Arguments
    # Char Literal
    stack.append(',')
    __arg0 = stack.pop ()
    # *** print
    __res = print__char (__arg0)
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Function Call - print(char) -> void
    # Arguments
    # Char Literal
    stack.append(' ')
    __arg0 = stack.pop ()
    # *** print
    __res = print__char (__arg0)
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Function Call - print(float) -> void
    # Arguments
    # Member Accessor
    # LHS
    stack.append(__main__print__v)
    # RHS
    stack.append (__field____main____Vec2____y)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __arg0 = stack.pop ()
    # *** print
    __res = print__float (__arg0)
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Function Call - print(char) -> void
    # Arguments
    # Char Literal
    stack.append(')')
    __arg0 = stack.pop ()
    # *** print
    __res = print__char (__arg0)
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
# End Function Declaration - __main____print__Vec2
#=========================================================================

#=========================================================================
# Function Declaration - println(Vec2) -> void
def __main____println__Vec2 (__main__println__v):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Function Call - print(Vec2) -> void
    # Arguments
    stack.append(__main__println__v)
    __arg0 = stack.pop ()
    # *** print
    __res = __main____print__Vec2 (__arg0)
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Function Call - println() -> void
    # Arguments
    # *** println
    __res = println ()
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
# End Function Declaration - __main____println__Vec2
#=========================================================================

# Statement
# Assignment - '='
# RHS
# Constructor Call - Vec2::Vec2(float, float) -> Vec2
# Arguments
# Float Literal
stack.append(1.0)
# Float Literal
stack.append(2.0)
__arg1 = stack.pop ()
__arg0 = stack.pop ()
__retval = __ctor____main____Vec2____Vec2__float__float (__arg0, __arg1)
stack.append (__retval)
# LHS
__main__v = 0
__rhs = stack.pop()
__main__v = __rhs
stack.append (__main__v)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Function Call - println(Vec2) -> void
# Arguments
stack.append(__main__v)
__arg0 = stack.pop ()
# *** println
__res = __main____println__Vec2 (__arg0)
stack.append (__res) # function call result
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Assignment - '='
# RHS
# Constructor Call - Vec2::Vec2(float, float) -> Vec2
# Arguments
# Float Literal
stack.append(3.14)
# Float Literal
stack.append(0.05)
__arg1 = stack.pop ()
__arg0 = stack.pop ()
__retval = __ctor____main____Vec2____Vec2__float__float (__arg0, __arg1)
stack.append (__retval)
# LHS
__main__v1 = 0
__rhs = stack.pop()
__main__v1 = __rhs
stack.append (__main__v1)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Method Call - Vec2::add(Vec2) -> void
# LHS
stack.append(__main__v)
# RHS
# Arguments
stack.append(__main__v1)
__arg0 = stack.pop ()
__obj = stack.pop ()
__retval = __method____main____Vec2____add__Vec2 (__obj, __arg0)
stack.append (__retval)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Function Call - println(Vec2) -> void
# Arguments
stack.append(__main__v)
__arg0 = stack.pop ()
# *** println
__res = __main____println__Vec2 (__arg0)
stack.append (__res) # function call result
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Function Call - println(Vec2) -> void
# Arguments
stack.append(__main__v1)
__arg0 = stack.pop ()
# *** println
__res = __main____println__Vec2 (__arg0)
stack.append (__res) # function call result
# Statement results can be ignored
stack.pop ()
# End Statement

#=========================================================================
# Class Declaration - __main____Vec3 inherits __main____Vec2
# Creating Dispatch Table (will be populated later)
__dtable____main____Vec3 = []
#-------------------------------------------------------------------------
# Field - float Vec3::x
# Inherited from Vec2
__field____main____Vec3____x = 1
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Field - float Vec3::y
# Inherited from Vec2
__field____main____Vec3____y = 2
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Field - float Vec3::z
__field____main____Vec3____z = 3
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Constructor Declaration - Vec3::Vec3(float, float, float) -> Vec3
def __ctor____main____Vec3____Vec3__float__float__float (__main____Vec3__Vec3__x, __main____Vec3__Vec3__y, __main____Vec3__Vec3__z):
    # Creating Class Instance
    this = [0] * 4
    # Add Dispatch Table
    this[0] = __dtable____main____Vec3
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main____Vec3__Vec3__x)
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append(__field____main____Vec3____x)
    __child = stack.pop()
    __parent = stack.pop()
    __rhs = stack.pop()
    __parent[__child] = __rhs
    stack.append (__parent[__child])
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main____Vec3__Vec3__y)
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append(__field____main____Vec3____y)
    __child = stack.pop()
    __parent = stack.pop()
    __rhs = stack.pop()
    __parent[__child] = __rhs
    stack.append (__parent[__child])
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main____Vec3__Vec3__z)
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append(__field____main____Vec3____z)
    __child = stack.pop()
    __parent = stack.pop()
    __rhs = stack.pop()
    __parent[__child] = __rhs
    stack.append (__parent[__child])
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
    # Return the constructed instance
    return this
# End Constructor Declaration - __ctor____main____Vec3____Vec3__float__float__float
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vec3::add(Vec2) -> void
# Inherited from Vec2
def __method____main____Vec3____add__Vec2 (this, __main____Vec3__add__other):
    # Jump to Vec2's version
    __retval = __method____main____Vec2____add__Vec2 (this, __main____Vec3__add__other)
    return __retval
# End Method Declaration - __method____main____Vec3____add__Vec2
#-------------------------------------------------------------------------

# Populate Dispatch Table
__dtable____main____Vec3 = [__method____main____Vec2____add__Vec2]
# End Class Declaration - __main____Vec3
#=========================================================================

# Statement
# Assignment - '='
# RHS
# Constructor Call - Vec3::Vec3(float, float, float) -> Vec3
# Arguments
# Float Literal
stack.append(1.2)
# Float Literal
stack.append(2.3)
# Float Literal
stack.append(3.4)
__arg2 = stack.pop ()
__arg1 = stack.pop ()
__arg0 = stack.pop ()
__retval = __ctor____main____Vec3____Vec3__float__float__float (__arg0, __arg1, __arg2)
stack.append (__retval)
# LHS
__main__v2 = 0
__rhs = stack.pop()
__main__v2 = __rhs
stack.append (__main__v2)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Function Call - println(Vec2) -> void
# Arguments
stack.append(__main__v2)
__arg0 = stack.pop ()
# *** println
__res = __main____println__Vec2 (__arg0)
stack.append (__res) # function call result
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Method Call - Vec3::add(Vec2) -> void
# LHS
stack.append(__main__v2)
# RHS
# Arguments
stack.append(__main__v1)
__arg0 = stack.pop ()
__obj = stack.pop ()
__retval = __method____main____Vec3____add__Vec2 (__obj, __arg0)
stack.append (__retval)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Function Call - println(Vec2) -> void
# Arguments
stack.append(__main__v2)
__arg0 = stack.pop ()
# *** println
__res = __main____println__Vec2 (__arg0)
stack.append (__res) # function call result
# Statement results can be ignored
stack.pop ()
# End Statement

#=========================================================================
# Function Declaration - print(Vec3) -> void
def __main____print__Vec3 (__main__print__v):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Function Call - print(char) -> void
    # Arguments
    # Char Literal
    stack.append('(')
    __arg0 = stack.pop ()
    # *** print
    __res = print__char (__arg0)
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Function Call - print(float) -> void
    # Arguments
    # Member Accessor
    # LHS
    stack.append(__main__print__v)
    # RHS
    stack.append (__field____main____Vec3____x)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __arg0 = stack.pop ()
    # *** print
    __res = print__float (__arg0)
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Function Call - print(char) -> void
    # Arguments
    # Char Literal
    stack.append(',')
    __arg0 = stack.pop ()
    # *** print
    __res = print__char (__arg0)
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Function Call - print(char) -> void
    # Arguments
    # Char Literal
    stack.append(' ')
    __arg0 = stack.pop ()
    # *** print
    __res = print__char (__arg0)
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Function Call - print(float) -> void
    # Arguments
    # Member Accessor
    # LHS
    stack.append(__main__print__v)
    # RHS
    stack.append (__field____main____Vec3____y)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __arg0 = stack.pop ()
    # *** print
    __res = print__float (__arg0)
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Function Call - print(char) -> void
    # Arguments
    # Char Literal
    stack.append(',')
    __arg0 = stack.pop ()
    # *** print
    __res = print__char (__arg0)
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Function Call - print(char) -> void
    # Arguments
    # Char Literal
    stack.append(' ')
    __arg0 = stack.pop ()
    # *** print
    __res = print__char (__arg0)
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Function Call - print(float) -> void
    # Arguments
    # Member Accessor
    # LHS
    stack.append(__main__print__v)
    # RHS
    stack.append (__field____main____Vec3____z)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __arg0 = stack.pop ()
    # *** print
    __res = print__float (__arg0)
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Function Call - print(char) -> void
    # Arguments
    # Char Literal
    stack.append(')')
    __arg0 = stack.pop ()
    # *** print
    __res = print__char (__arg0)
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
# End Function Declaration - __main____print__Vec3
#=========================================================================

#=========================================================================
# Function Declaration - println(Vec3) -> void
def __main____println__Vec3 (__main__println__v):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Function Call - print(Vec3) -> void
    # Arguments
    stack.append(__main__println__v)
    __arg0 = stack.pop ()
    # *** print
    __res = __main____print__Vec3 (__arg0)
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Function Call - println() -> void
    # Arguments
    # *** println
    __res = println ()
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
# End Function Declaration - __main____println__Vec3
#=========================================================================

# Statement
# Function Call - println(Vec3) -> void
# Arguments
stack.append(__main__v2)
__arg0 = stack.pop ()
# *** println
__res = __main____println__Vec3 (__arg0)
stack.append (__res) # function call result
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Function Call - println(int) -> void
# Arguments
# Subtraction
# LHS
# Int Literal
stack.append(21)
# RHS
# Int Literal
stack.append(23)
__rhs = stack.pop()
__lhs = stack.pop()
__res = __lhs - __rhs
stack.append(__res)
__arg0 = stack.pop ()
# *** println
__res = println__int (__arg0)
stack.append (__res) # function call result
# Statement results can be ignored
stack.pop ()
# End Statement


#=========================================================================
#### END OF CODE ########################################################
#=========================================================================

