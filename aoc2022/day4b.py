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
    # Statement
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(10)
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append(__field____main____Vector__char__1____capacity)
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
    # Int Literal
    stack.append(0)
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append(__field____main____Vector__char__1____size)
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
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__char__1____capacity)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __dim = stack.pop ()
    __res = [None] * __dim
    stack.append (__res)
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append(__field____main____Vector__char__1____data)
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
    # Precomputing all if/elif conditions and give unique names
    # bc we can't have code between if and elif
    # Condition
    # Greater Than or Equal to
    # LHS
    # Addition
    # LHS
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__char__1____size)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # RHS
    # Int Literal
    stack.append(1)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs + __rhs
    stack.append(__res)
    # RHS
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__char__1____capacity)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs >= __rhs
    stack.append (__res)
    __if__2__cond = stack.pop ()
    # get condition from stack
    if (__if__2__cond):
        # Body
        #-----------------------------------------------------------------
        # Code Block
        # Statement
        # Assignment - '='
        # RHS
        # Multiplication
        # LHS
        # Member Accessor
        # LHS
        stack.append(this)
        # RHS
        stack.append (__field____main____Vector__char__1____capacity)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # RHS
        # Int Literal
        stack.append(2)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs * __rhs
        stack.append(__res)
        # LHS
        # Member Accessor Assignment
        # LHS
        stack.append(this)
        # RHS
        stack.append(__field____main____Vector__char__1____capacity)
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
        # Member Accessor
        # LHS
        stack.append(this)
        # RHS
        stack.append (__field____main____Vector__char__1____capacity)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        __dim = stack.pop ()
        __res = [None] * __dim
        stack.append (__res)
        # LHS
        __main____Vector__char__1__pushBack__block__1__if__2__block__3__nData = 0
        __rhs = stack.pop()
        __main____Vector__char__1__pushBack__block__1__if__2__block__3__nData = __rhs
        stack.append (__main____Vector__char__1__pushBack__block__1__if__2__block__3__nData)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
        # For-Loop
        # Init
        # Assignment - '='
        # RHS
        # Int Literal
        stack.append(0)
        # LHS
        __main____Vector__char__1__pushBack__block__1__if__2__block__3__for__4__i = 0
        __rhs = stack.pop()
        __main____Vector__char__1__pushBack__block__1__if__2__block__3__for__4__i = __rhs
        stack.append (__main____Vector__char__1__pushBack__block__1__if__2__block__3__for__4__i)
        # Using an infinite loop so we can write a separate multi-line condition
        while (1):
            # Condition
            # Less Than
            # LHS
            stack.append(__main____Vector__char__1__pushBack__block__1__if__2__block__3__for__4__i)
            # RHS
            # Member Accessor
            # LHS
            stack.append(this)
            # RHS
            stack.append (__field____main____Vector__char__1____size)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs < __rhs
            stack.append (__res)
            __cond = stack.pop ()
            # break out of loop if condition is false
            if (__cond == 0): break
            # Body
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Assignment - '='
            # RHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(this)
            # RHS
            stack.append (__field____main____Vector__char__1____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main____Vector__char__1__pushBack__block__1__if__2__block__3__for__4__i)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # LHS
            # Subscript assignment
            # LHS
            stack.append(__main____Vector__char__1__pushBack__block__1__if__2__block__3__nData)
            # OFFSET
            stack.append(__main____Vector__char__1__pushBack__block__1__if__2__block__3__for__4__i)
            __offset = stack.pop()
            __pointer = stack.pop()
            __rhs = stack.pop()
            __pointer[__offset] = __rhs
            stack.append (__pointer[__offset])
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            #-------------------------------------------------------------
            # Update
            # Pre-Increment
            # RHS
            stack.append(__main____Vector__char__1__pushBack__block__1__if__2__block__3__for__4__i)
            __rhs = stack.pop ()
            __main____Vector__char__1__pushBack__block__1__if__2__block__3__for__4__i = __main____Vector__char__1__pushBack__block__1__if__2__block__3__for__4__i + 1
            __res = __main____Vector__char__1__pushBack__block__1__if__2__block__3__for__4__i
            stack.append (__res)
        #-----------------------------------------------------------------
        # Statement
        # Member Accessor
        # LHS
        stack.append(this)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        __arr = stack.pop ()
        free (__arr)
        stack.append (0)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main____Vector__char__1__pushBack__block__1__if__2__block__3__nData)
        # LHS
        # Member Accessor Assignment
        # LHS
        stack.append(this)
        # RHS
        stack.append(__field____main____Vector__char__1____data)
        __child = stack.pop()
        __parent = stack.pop()
        __rhs = stack.pop()
        __parent[__child] = __rhs
        stack.append (__parent[__child])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
    # End of if
    #---------------------------------------------------------------------
    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main____Vector__char__1__pushBack__val)
    # LHS
    # Subscript assignment
    # LHS
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__char__1____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__char__1____size)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __offset = stack.pop()
    __pointer = stack.pop()
    __rhs = stack.pop()
    __pointer[__offset] = __rhs
    stack.append (__pointer[__offset])
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Pre-Increment
    # RHS
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__char__1____size)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __rhs = stack.pop ()
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__char__1____size)
    __child = stack.pop ()
    __parent = stack.pop ()
    __parent[__child] = __parent[__child] + 1
    __res = __parent[__child]
    stack.append (__res)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

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
    # Return
    # Subscript
    # LHS
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__char__1____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    # Pre-Decrement
    # RHS
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__char__1____size)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __rhs = stack.pop ()
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__char__1____size)
    __child = stack.pop ()
    __parent = stack.pop ()
    __parent[__child] = __parent[__child] - 1
    __res = __parent[__child]
    stack.append (__res)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    __rVal = stack.pop ()
    return __rVal
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
    # Return
    # Subscript
    # LHS
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__char__1____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    stack.append(__main____Vector__char__1__get__index)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    __rVal = stack.pop ()
    return __rVal
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
    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main____Vector__char__1__set__value)
    # LHS
    # Subscript assignment
    # LHS
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__char__1____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    stack.append(__main____Vector__char__1__set__index)
    __offset = stack.pop()
    __pointer = stack.pop()
    __rhs = stack.pop()
    __pointer[__offset] = __rhs
    stack.append (__pointer[__offset])
    # Statement results can be ignored
    stack.pop ()
    # End Statement

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

# Statement
# Assignment - '='
# RHS
# Function Call - input() -> char[]
# Arguments
# *** input
__res = input ()
stack.append (__res) # function call result
# LHS
__main__line = 0
__rhs = stack.pop()
__main__line = __rhs
stack.append (__main__line)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Assignment - '='
# RHS
# Int Literal
stack.append(0)
# LHS
__main__total = 0
__rhs = stack.pop()
__main__total = __rhs
stack.append (__main__total)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Assignment - '='
# RHS
# Constructor Call - Vector<:char[]:>::Vector() -> Vector<:char[]:>
# Arguments
__retval = __ctor____main____Vector__char__1____Vector ()
stack.append (__retval)
# LHS
__main__lines = 0
__rhs = stack.pop()
__main__lines = __rhs
stack.append (__main__lines)
# Statement results can be ignored
stack.pop ()
# End Statement

#-------------------------------------------------------------------------
# While-Loop
# Using an infinite loop so we can write a separate multi-line condition
while (1):
    # Condition
    # Not Equal
    # LHS
    # Subscript
    # LHS
    stack.append(__main__line)
    # OFFSET
    # Int Literal
    stack.append(0)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    # RHS
    # Char Literal
    stack.append('$')
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs != __rhs
    stack.append (__res)
    __cond = stack.pop ()
    # break out of loop if condition is false
    if (__cond == 0): break
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Method Call - Vector<:char[]:>::pushBack(char[]) -> void
    # LHS
    stack.append(__main__lines)
    # RHS
    # Arguments
    stack.append(__main__line)
    __arg0 = stack.pop ()
    __obj = stack.pop ()
    __retval = __method____main____Vector__char__1____pushBack__char__1 (__obj, __arg0)
    stack.append (__retval)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Function Call - input() -> char[]
    # Arguments
    # *** input
    __res = input ()
    stack.append (__res) # function call result
    __rhs = stack.pop()
    __main__line = __rhs
    stack.append (__main__line)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
# End of While
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# For-Loop
# Init
# Assignment - '='
# RHS
# Int Literal
stack.append(0)
# LHS
__main__for__11__l = 0
__rhs = stack.pop()
__main__for__11__l = __rhs
stack.append (__main__for__11__l)
# Using an infinite loop so we can write a separate multi-line condition
while (1):
    # Condition
    # Less Than
    # LHS
    stack.append(__main__for__11__l)
    # RHS
    # Member Accessor
    # LHS
    stack.append(__main__lines)
    # RHS
    stack.append (__field____main____Vector__char__1____size)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
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
    # Assignment - '='
    # RHS
    # Subscript
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main__lines)
    # RHS
    stack.append (__field____main____Vector__char__1____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    stack.append(__main__for__11__l)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    # LHS
    __main__for__11__block__12__line = 0
    __rhs = stack.pop()
    __main__for__11__block__12__line = __rhs
    stack.append (__main__for__11__block__12__line)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(0)
    # LHS
    __main__for__11__block__12__indexcomma = 0
    __rhs = stack.pop()
    __main__for__11__block__12__indexcomma = __rhs
    stack.append (__main__for__11__block__12__indexcomma)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(0)
    # LHS
    __main__for__11__block__12__indexdash0 = 0
    __rhs = stack.pop()
    __main__for__11__block__12__indexdash0 = __rhs
    stack.append (__main__for__11__block__12__indexdash0)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(0)
    # LHS
    __main__for__11__block__12__indexdash1 = 0
    __rhs = stack.pop()
    __main__for__11__block__12__indexdash1 = __rhs
    stack.append (__main__for__11__block__12__indexdash1)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
    # For-Loop
    # Init
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(0)
    # LHS
    __main__for__11__block__12__for__13__i = 0
    __rhs = stack.pop()
    __main__for__11__block__12__for__13__i = __rhs
    stack.append (__main__for__11__block__12__for__13__i)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        stack.append(__main__for__11__block__12__for__13__i)
        # RHS
        stack.append(__main__for__11__block__12__line)
        __arr = stack.pop ()
        __res = len (__arr)
        stack.append (__res)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs < __rhs
        stack.append (__res)
        __cond = stack.pop ()
        # break out of loop if condition is false
        if (__cond == 0): break
        # Body
        #-----------------------------------------------------------------
        # Code Block
        #-----------------------------------------------------------------
        # If-Statement
        # Precomputing all if/elif conditions and give unique names
        # bc we can't have code between if and elif
        # Condition
        # AND
        # LHS
        # Equal
        # LHS
        # Subscript
        # LHS
        stack.append(__main__for__11__block__12__line)
        # OFFSET
        stack.append(__main__for__11__block__12__for__13__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        # Char Literal
        stack.append('-')
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs == __rhs
        stack.append (__res)
        # RHS
        # Equal
        # LHS
        stack.append(__main__for__11__block__12__indexcomma)
        # RHS
        # Int Literal
        stack.append(0)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs == __rhs
        stack.append (__res)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs and __rhs
        stack.append (__res)
        __if__15__cond = stack.pop ()
        # Condition for elif #0
        # Equal
        # LHS
        # Subscript
        # LHS
        stack.append(__main__for__11__block__12__line)
        # OFFSET
        stack.append(__main__for__11__block__12__for__13__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        # Char Literal
        stack.append('-')
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs == __rhs
        stack.append (__res)
        __elif__15x0__cond = stack.pop ()
        # get condition from stack
        if (__if__15__cond):
            # Body
            # Statement
            # Assignment - '='
            # RHS
            stack.append(__main__for__11__block__12__for__13__i)
            __rhs = stack.pop()
            __main__for__11__block__12__indexdash0 = __rhs
            stack.append (__main__for__11__block__12__indexdash0)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

        #-----------------------------------------------------------------
        # Elif-Statement
        # Condition
        elif (__elif__15x0__cond):
            # Body
            # Statement
            # Assignment - '='
            # RHS
            stack.append(__main__for__11__block__12__for__13__i)
            __rhs = stack.pop()
            __main__for__11__block__12__indexdash1 = __rhs
            stack.append (__main__for__11__block__12__indexdash1)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

        #-----------------------------------------------------------------
        # End of if
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # If-Statement
        # Precomputing all if/elif conditions and give unique names
        # bc we can't have code between if and elif
        # Condition
        # Equal
        # LHS
        # Subscript
        # LHS
        stack.append(__main__for__11__block__12__line)
        # OFFSET
        stack.append(__main__for__11__block__12__for__13__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        # Char Literal
        stack.append(',')
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs == __rhs
        stack.append (__res)
        __if__16__cond = stack.pop ()
        # get condition from stack
        if (__if__16__cond):
            # Body
            # Statement
            # Assignment - '='
            # RHS
            stack.append(__main__for__11__block__12__for__13__i)
            __rhs = stack.pop()
            __main__for__11__block__12__indexcomma = __rhs
            stack.append (__main__for__11__block__12__indexcomma)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

        # End of if
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # Update
        # Pre-Increment
        # RHS
        stack.append(__main__for__11__block__12__for__13__i)
        __rhs = stack.pop ()
        __main__for__11__block__12__for__13__i = __main__for__11__block__12__for__13__i + 1
        __res = __main__for__11__block__12__for__13__i
        stack.append (__res)
    #---------------------------------------------------------------------
    # Statement
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(0)
    # LHS
    __main__for__11__block__12__begin = 0
    __rhs = stack.pop()
    __main__for__11__block__12__begin = __rhs
    stack.append (__main__for__11__block__12__begin)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main__for__11__block__12__indexdash0)
    # LHS
    __main__for__11__block__12__end = 0
    __rhs = stack.pop()
    __main__for__11__block__12__end = __rhs
    stack.append (__main__for__11__block__12__end)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(0)
    # LHS
    __main__for__11__block__12__iter = 0
    __rhs = stack.pop()
    __main__for__11__block__12__iter = __rhs
    stack.append (__main__for__11__block__12__iter)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Subtraction
    # LHS
    stack.append(__main__for__11__block__12__end)
    # RHS
    stack.append(__main__for__11__block__12__begin)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs - __rhs
    stack.append(__res)
    __dim = stack.pop ()
    __res = [None] * __dim
    stack.append (__res)
    # LHS
    __main__for__11__block__12__a_ = 0
    __rhs = stack.pop()
    __main__for__11__block__12__a_ = __rhs
    stack.append (__main__for__11__block__12__a_)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
    # For-Loop
    # Init
    # Assignment - '='
    # RHS
    stack.append(__main__for__11__block__12__begin)
    # LHS
    __main__for__11__block__12__for__17__i = 0
    __rhs = stack.pop()
    __main__for__11__block__12__for__17__i = __rhs
    stack.append (__main__for__11__block__12__for__17__i)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        stack.append(__main__for__11__block__12__for__17__i)
        # RHS
        stack.append(__main__for__11__block__12__end)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs < __rhs
        stack.append (__res)
        __cond = stack.pop ()
        # break out of loop if condition is false
        if (__cond == 0): break
        # Body
        # Statement
        # Assignment - '='
        # RHS
        # Subscript
        # LHS
        stack.append(__main__for__11__block__12__line)
        # OFFSET
        stack.append(__main__for__11__block__12__for__17__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # LHS
        # Subscript assignment
        # LHS
        stack.append(__main__for__11__block__12__a_)
        # OFFSET
        # Post-Increment
        __res = __main__for__11__block__12__iter
        __main__for__11__block__12__iter = __main__for__11__block__12__iter + 1
        stack.append (__res)
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Update
        # Pre-Increment
        # RHS
        stack.append(__main__for__11__block__12__for__17__i)
        __rhs = stack.pop ()
        __main__for__11__block__12__for__17__i = __main__for__11__block__12__for__17__i + 1
        __res = __main__for__11__block__12__for__17__i
        stack.append (__res)
    #---------------------------------------------------------------------
    # Statement
    # Assignment - '='
    # RHS
    # Addition
    # LHS
    stack.append(__main__for__11__block__12__indexdash0)
    # RHS
    # Int Literal
    stack.append(1)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs + __rhs
    stack.append(__res)
    __rhs = stack.pop()
    __main__for__11__block__12__begin = __rhs
    stack.append (__main__for__11__block__12__begin)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main__for__11__block__12__indexcomma)
    __rhs = stack.pop()
    __main__for__11__block__12__end = __rhs
    stack.append (__main__for__11__block__12__end)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(0)
    __rhs = stack.pop()
    __main__for__11__block__12__iter = __rhs
    stack.append (__main__for__11__block__12__iter)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Subtraction
    # LHS
    stack.append(__main__for__11__block__12__end)
    # RHS
    stack.append(__main__for__11__block__12__begin)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs - __rhs
    stack.append(__res)
    __dim = stack.pop ()
    __res = [None] * __dim
    stack.append (__res)
    # LHS
    __main__for__11__block__12__b_ = 0
    __rhs = stack.pop()
    __main__for__11__block__12__b_ = __rhs
    stack.append (__main__for__11__block__12__b_)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
    # For-Loop
    # Init
    # Assignment - '='
    # RHS
    stack.append(__main__for__11__block__12__begin)
    # LHS
    __main__for__11__block__12__for__18__i = 0
    __rhs = stack.pop()
    __main__for__11__block__12__for__18__i = __rhs
    stack.append (__main__for__11__block__12__for__18__i)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        stack.append(__main__for__11__block__12__for__18__i)
        # RHS
        stack.append(__main__for__11__block__12__end)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs < __rhs
        stack.append (__res)
        __cond = stack.pop ()
        # break out of loop if condition is false
        if (__cond == 0): break
        # Body
        # Statement
        # Assignment - '='
        # RHS
        # Subscript
        # LHS
        stack.append(__main__for__11__block__12__line)
        # OFFSET
        stack.append(__main__for__11__block__12__for__18__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # LHS
        # Subscript assignment
        # LHS
        stack.append(__main__for__11__block__12__b_)
        # OFFSET
        # Post-Increment
        __res = __main__for__11__block__12__iter
        __main__for__11__block__12__iter = __main__for__11__block__12__iter + 1
        stack.append (__res)
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Update
        # Pre-Increment
        # RHS
        stack.append(__main__for__11__block__12__for__18__i)
        __rhs = stack.pop ()
        __main__for__11__block__12__for__18__i = __main__for__11__block__12__for__18__i + 1
        __res = __main__for__11__block__12__for__18__i
        stack.append (__res)
    #---------------------------------------------------------------------
    # Statement
    # Assignment - '='
    # RHS
    # Addition
    # LHS
    stack.append(__main__for__11__block__12__indexcomma)
    # RHS
    # Int Literal
    stack.append(1)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs + __rhs
    stack.append(__res)
    __rhs = stack.pop()
    __main__for__11__block__12__begin = __rhs
    stack.append (__main__for__11__block__12__begin)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main__for__11__block__12__indexdash1)
    __rhs = stack.pop()
    __main__for__11__block__12__end = __rhs
    stack.append (__main__for__11__block__12__end)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(0)
    __rhs = stack.pop()
    __main__for__11__block__12__iter = __rhs
    stack.append (__main__for__11__block__12__iter)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Subtraction
    # LHS
    stack.append(__main__for__11__block__12__end)
    # RHS
    stack.append(__main__for__11__block__12__begin)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs - __rhs
    stack.append(__res)
    __dim = stack.pop ()
    __res = [None] * __dim
    stack.append (__res)
    # LHS
    __main__for__11__block__12__c_ = 0
    __rhs = stack.pop()
    __main__for__11__block__12__c_ = __rhs
    stack.append (__main__for__11__block__12__c_)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
    # For-Loop
    # Init
    # Assignment - '='
    # RHS
    stack.append(__main__for__11__block__12__begin)
    # LHS
    __main__for__11__block__12__for__19__i = 0
    __rhs = stack.pop()
    __main__for__11__block__12__for__19__i = __rhs
    stack.append (__main__for__11__block__12__for__19__i)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        stack.append(__main__for__11__block__12__for__19__i)
        # RHS
        stack.append(__main__for__11__block__12__end)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs < __rhs
        stack.append (__res)
        __cond = stack.pop ()
        # break out of loop if condition is false
        if (__cond == 0): break
        # Body
        # Statement
        # Assignment - '='
        # RHS
        # Subscript
        # LHS
        stack.append(__main__for__11__block__12__line)
        # OFFSET
        stack.append(__main__for__11__block__12__for__19__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # LHS
        # Subscript assignment
        # LHS
        stack.append(__main__for__11__block__12__c_)
        # OFFSET
        # Post-Increment
        __res = __main__for__11__block__12__iter
        __main__for__11__block__12__iter = __main__for__11__block__12__iter + 1
        stack.append (__res)
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Update
        # Pre-Increment
        # RHS
        stack.append(__main__for__11__block__12__for__19__i)
        __rhs = stack.pop ()
        __main__for__11__block__12__for__19__i = __main__for__11__block__12__for__19__i + 1
        __res = __main__for__11__block__12__for__19__i
        stack.append (__res)
    #---------------------------------------------------------------------
    # Statement
    # Assignment - '='
    # RHS
    # Addition
    # LHS
    stack.append(__main__for__11__block__12__indexdash1)
    # RHS
    # Int Literal
    stack.append(1)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs + __rhs
    stack.append(__res)
    __rhs = stack.pop()
    __main__for__11__block__12__begin = __rhs
    stack.append (__main__for__11__block__12__begin)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Subtraction
    # LHS
    stack.append(__main__for__11__block__12__line)
    __arr = stack.pop ()
    __res = len (__arr)
    stack.append (__res)
    # RHS
    # Int Literal
    stack.append(1)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs - __rhs
    stack.append(__res)
    __rhs = stack.pop()
    __main__for__11__block__12__end = __rhs
    stack.append (__main__for__11__block__12__end)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(0)
    __rhs = stack.pop()
    __main__for__11__block__12__iter = __rhs
    stack.append (__main__for__11__block__12__iter)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Subtraction
    # LHS
    stack.append(__main__for__11__block__12__end)
    # RHS
    stack.append(__main__for__11__block__12__begin)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs - __rhs
    stack.append(__res)
    __dim = stack.pop ()
    __res = [None] * __dim
    stack.append (__res)
    # LHS
    __main__for__11__block__12__d_ = 0
    __rhs = stack.pop()
    __main__for__11__block__12__d_ = __rhs
    stack.append (__main__for__11__block__12__d_)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
    # For-Loop
    # Init
    # Assignment - '='
    # RHS
    stack.append(__main__for__11__block__12__begin)
    # LHS
    __main__for__11__block__12__for__20__i = 0
    __rhs = stack.pop()
    __main__for__11__block__12__for__20__i = __rhs
    stack.append (__main__for__11__block__12__for__20__i)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        stack.append(__main__for__11__block__12__for__20__i)
        # RHS
        stack.append(__main__for__11__block__12__end)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs < __rhs
        stack.append (__res)
        __cond = stack.pop ()
        # break out of loop if condition is false
        if (__cond == 0): break
        # Body
        # Statement
        # Assignment - '='
        # RHS
        # Subscript
        # LHS
        stack.append(__main__for__11__block__12__line)
        # OFFSET
        stack.append(__main__for__11__block__12__for__20__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # LHS
        # Subscript assignment
        # LHS
        stack.append(__main__for__11__block__12__d_)
        # OFFSET
        # Post-Increment
        __res = __main__for__11__block__12__iter
        __main__for__11__block__12__iter = __main__for__11__block__12__iter + 1
        stack.append (__res)
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Update
        # Pre-Increment
        # RHS
        stack.append(__main__for__11__block__12__for__20__i)
        __rhs = stack.pop ()
        __main__for__11__block__12__for__20__i = __main__for__11__block__12__for__20__i + 1
        __res = __main__for__11__block__12__for__20__i
        stack.append (__res)
    #---------------------------------------------------------------------
    # Statement
    # Assignment - '='
    # RHS
    # Function Call - stringToInt(char[]) -> int
    # Arguments
    stack.append(__main__for__11__block__12__a_)
    __arg0 = stack.pop ()
    # *** stringToInt
    __res = stringToInt__char__1 (__arg0)
    stack.append (__res) # function call result
    # LHS
    __main__for__11__block__12__begin0 = 0
    __rhs = stack.pop()
    __main__for__11__block__12__begin0 = __rhs
    stack.append (__main__for__11__block__12__begin0)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Function Call - stringToInt(char[]) -> int
    # Arguments
    stack.append(__main__for__11__block__12__b_)
    __arg0 = stack.pop ()
    # *** stringToInt
    __res = stringToInt__char__1 (__arg0)
    stack.append (__res) # function call result
    # LHS
    __main__for__11__block__12__end0 = 0
    __rhs = stack.pop()
    __main__for__11__block__12__end0 = __rhs
    stack.append (__main__for__11__block__12__end0)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Function Call - stringToInt(char[]) -> int
    # Arguments
    stack.append(__main__for__11__block__12__c_)
    __arg0 = stack.pop ()
    # *** stringToInt
    __res = stringToInt__char__1 (__arg0)
    stack.append (__res) # function call result
    # LHS
    __main__for__11__block__12__begin1 = 0
    __rhs = stack.pop()
    __main__for__11__block__12__begin1 = __rhs
    stack.append (__main__for__11__block__12__begin1)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Function Call - stringToInt(char[]) -> int
    # Arguments
    stack.append(__main__for__11__block__12__d_)
    __arg0 = stack.pop ()
    # *** stringToInt
    __res = stringToInt__char__1 (__arg0)
    stack.append (__res) # function call result
    # LHS
    __main__for__11__block__12__end1 = 0
    __rhs = stack.pop()
    __main__for__11__block__12__end1 = __rhs
    stack.append (__main__for__11__block__12__end1)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(0)
    # LHS
    __main__for__11__block__12__overlaps = 0
    __rhs = stack.pop()
    __main__for__11__block__12__overlaps = __rhs
    stack.append (__main__for__11__block__12__overlaps)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
    # If-Statement
    # Precomputing all if/elif conditions and give unique names
    # bc we can't have code between if and elif
    # Condition
    # AND
    # LHS
    # Greater Than or Equal to
    # LHS
    stack.append(__main__for__11__block__12__begin0)
    # RHS
    stack.append(__main__for__11__block__12__begin1)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs >= __rhs
    stack.append (__res)
    # RHS
    # Less Than or Equal to
    # LHS
    stack.append(__main__for__11__block__12__begin0)
    # RHS
    stack.append(__main__for__11__block__12__end1)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs <= __rhs
    stack.append (__res)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs and __rhs
    stack.append (__res)
    __if__21__cond = stack.pop ()
    # get condition from stack
    if (__if__21__cond):
        # Body
        # Statement
        # Assignment - '='
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __main__for__11__block__12__overlaps = __rhs
        stack.append (__main__for__11__block__12__overlaps)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

    # End of if
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    # If-Statement
    # Precomputing all if/elif conditions and give unique names
    # bc we can't have code between if and elif
    # Condition
    # AND
    # LHS
    # Greater Than or Equal to
    # LHS
    stack.append(__main__for__11__block__12__end0)
    # RHS
    stack.append(__main__for__11__block__12__begin1)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs >= __rhs
    stack.append (__res)
    # RHS
    # Less Than or Equal to
    # LHS
    stack.append(__main__for__11__block__12__end0)
    # RHS
    stack.append(__main__for__11__block__12__end1)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs <= __rhs
    stack.append (__res)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs and __rhs
    stack.append (__res)
    __if__22__cond = stack.pop ()
    # get condition from stack
    if (__if__22__cond):
        # Body
        # Statement
        # Assignment - '='
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __main__for__11__block__12__overlaps = __rhs
        stack.append (__main__for__11__block__12__overlaps)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

    # End of if
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    # If-Statement
    # Precomputing all if/elif conditions and give unique names
    # bc we can't have code between if and elif
    # Condition
    # AND
    # LHS
    # Greater Than or Equal to
    # LHS
    stack.append(__main__for__11__block__12__begin1)
    # RHS
    stack.append(__main__for__11__block__12__begin0)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs >= __rhs
    stack.append (__res)
    # RHS
    # Less Than or Equal to
    # LHS
    stack.append(__main__for__11__block__12__begin1)
    # RHS
    stack.append(__main__for__11__block__12__end0)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs <= __rhs
    stack.append (__res)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs and __rhs
    stack.append (__res)
    __if__23__cond = stack.pop ()
    # get condition from stack
    if (__if__23__cond):
        # Body
        # Statement
        # Assignment - '='
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __main__for__11__block__12__overlaps = __rhs
        stack.append (__main__for__11__block__12__overlaps)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

    # End of if
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    # If-Statement
    # Precomputing all if/elif conditions and give unique names
    # bc we can't have code between if and elif
    # Condition
    # AND
    # LHS
    # Greater Than or Equal to
    # LHS
    stack.append(__main__for__11__block__12__end1)
    # RHS
    stack.append(__main__for__11__block__12__begin0)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs >= __rhs
    stack.append (__res)
    # RHS
    # Less Than or Equal to
    # LHS
    stack.append(__main__for__11__block__12__end1)
    # RHS
    stack.append(__main__for__11__block__12__end0)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs <= __rhs
    stack.append (__res)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs and __rhs
    stack.append (__res)
    __if__24__cond = stack.pop ()
    # get condition from stack
    if (__if__24__cond):
        # Body
        # Statement
        # Assignment - '='
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __main__for__11__block__12__overlaps = __rhs
        stack.append (__main__for__11__block__12__overlaps)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

    # End of if
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    # If-Statement
    # Precomputing all if/elif conditions and give unique names
    # bc we can't have code between if and elif
    # Condition
    stack.append(__main__for__11__block__12__overlaps)
    __if__25__cond = stack.pop ()
    # get condition from stack
    if (__if__25__cond):
        # Body
        #-----------------------------------------------------------------
        # Code Block
        # Statement
        # Post-Increment
        __res = __main__total
        __main__total = __main__total + 1
        stack.append (__res)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
    # End of if
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    # Update
    # Pre-Increment
    # RHS
    stack.append(__main__for__11__l)
    __rhs = stack.pop ()
    __main__for__11__l = __main__for__11__l + 1
    __res = __main__for__11__l
    stack.append (__res)
#-------------------------------------------------------------------------
# Statement
# Function Call - println(int) -> void
# Arguments
stack.append(__main__total)
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

