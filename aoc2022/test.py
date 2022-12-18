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
def __builtin__exit__int (exit_code):
    exit (exit_code)

# # ========================================================================

# # Frees memory of the given pointer
# # void free()
# # - exit_code : [rbp + 16]
# # - uses external exit function from libc
def __builtin__free (ptr):
    # do nothing, python has its own garbage collection
    pass

# # ========================================================================
# # Prints a given string to the screen
# # void print (char[] stringToPrint)#
# # stringToPrint : [rbp + 16]
def __builtin__print__char__1 (s):
    # collapse char[] to python string
    # -1 to ignore null terminator
    print (''.join(s[:-1]), end="")

# # ========================================================================

# # Prints an int to the screen
# # Utilizes printf "%d"
# # void print (int valueToPrint)#
# # valueToPrint : [rbp + 16]
def __builtin__print__int (v):
    print (v, end="")

# # ========================================================================

# # Prints a char to the screen
# # Utilizes printf "%c"
# # void print (char valueToPrint)#
# # valueToPrint : [rbp + 16]
def __builtin__print__char (v):
    print (v, end="")

# # ========================================================================

# # Prints a float to the screen
# # void print (float valueToPrint)
def __builtin__print__float (v):
    print (v, end="")

# # //========================================================================
# # // Prints a given string to the screen with a newline at the end
# # // void println (char[] stringToPrint)#
# # stringToPrint : [rbp + 16]
def __builtin__println__char__1 (v):
    # collapse char[] to python string
    # -1 to ignore null terminator
    print (''.join(v[:-1]))

# # ========================================================================

# # Prints an int to the screen with a newline
# # Utilizes printf "%d"
# # void println (int valueToPrint)#
# # valueToPrint : [rbp + 16]
def __builtin__println__int (v):
    print (v)

# # ========================================================================
# # // Prints a float to the screen with a newline
# # // void println (float floatToPrint)#
# # valueToPrint : [rbp + 16]
def __builtin__println__float (v):
    print (v)

# # //========================================================================
# # // Prints a char to the screen with a newline
# # // void println (char charToPrint)#
def __builtin__println__char (v):
    print (v)

# # //========================================================================
# # // Prints an enum's integer value with a newline
# # // void println (Enum e)#
def __builtin__println__Enum (v):
    print (v)

# # //========================================================================
# # // Prints a newline to the console
# # // void println ()#
def __builtin__println ():
    print ()

# # //========================================================================
# # // grabs input from the console 
# # this waits for a line if there isnt one
# # // char[] input ()#
def __builtin__input ():
    try:
        # amyscript expects the newline and null character
        line = input () + "\n" + '\0'
    except EOFError:
        # return null if eof is encountered
        line = None
    return line


# # //========================================================================
# # // returns default float value
# # // float float ()#
def __builtin__float ():
    return 0.0

# # //========================================================================
# # // converts int to float
# # // float intToFloat (int value)#
# # value : [rbp + 16]
def __builtin__intToFloat__int (v):
    return float (v)

# # //========================================================================
# # // parses a float from a given char[]
# # // float stringToFloat (char[])#
# # str : [rbp + 16]
def __builtin__stringToFloat__char__1 (s):
    return float (s)

# # //========================================================================
# # // returns default int value
# # // int int ()#
def __builtin__int ():
    return 0

# # //========================================================================
# # // returns default char value
# # // char char ()#
def __builtin__char ():
 return '0'

# # //========================================================================
# # // converts float to int
# # // int floatToInt (float)#
def __builtin__floatToInt__float (f):
    # -1 to ignore the null terminator
    if f[-1] == '\0':
        return int(''.join(f[:-1]))
    return int(''.join(f))

# # //========================================================================
# # // parses an int from a given char[]
# # // int stringToInt (char[] str)#
# # str : [rbp + 16]
def __builtin__stringToInt__char__1 (s):
    # print (s)
    # try:
    #     res = int(''.join(s))
    # except:
    #     res = 0
    # return res
    # -1 to ignore the null terminator
    # count till null terminator
    i = 0
    while s[i] != '\0':
        i += 1
    if s[-1] == '\0':
        return int(''.join(s[:-1]))
    return int(''.join(s[:i]))


# # //========================================================================
# # // parses an int from a given char
# # // int charToInt (char)#
def __builtin__charToInt__char (c):
    return int(c)

# # //========================================================================
# # // converts int to string
# # // char[] string (int)#
def __builtin__string__int (i):
    return str(i)

# # //========================================================================
# # // converts float to string
# # // char[] string (float)#
def __builtin__string__float (f):
    return str(f)

# # //========================================================================

# # // returns default value for array and object (null)
# # // null null ()#
def __builtin__null ():
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
# Class Declaration - __main____Vector__char__1 inherits __builtin____main__Object
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
# Constructor Declaration - Vector<:char[]:>::Vector(int) -> Vector<:char[]:>
def __ctor____main____Vector__char__1____Vector__int (__main____Vector__char__1__Vector__size):
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
    # Addition
    # LHS
    stack.append(__main____Vector__char__1__Vector__size)
    # RHS
    # Int Literal
    stack.append(10)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs + __rhs
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
    stack.append(__main____Vector__char__1__Vector__size)
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
# End Constructor Declaration - __ctor____main____Vector__char__1____Vector__int
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
    __if__3__cond = stack.pop ()
    # get condition from stack
    if (__if__3__cond):
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
        __main____Vector__char__1__pushBack__block__2__if__3__block__4__nData = 0
        __rhs = stack.pop()
        __main____Vector__char__1__pushBack__block__2__if__3__block__4__nData = __rhs
        stack.append (__main____Vector__char__1__pushBack__block__2__if__3__block__4__nData)
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
        __main____Vector__char__1__pushBack__block__2__if__3__block__4__for__5__i = 0
        __rhs = stack.pop()
        __main____Vector__char__1__pushBack__block__2__if__3__block__4__for__5__i = __rhs
        stack.append (__main____Vector__char__1__pushBack__block__2__if__3__block__4__for__5__i)
        # Using an infinite loop so we can write a separate multi-line condition
        while (1):
            # Condition
            # Less Than
            # LHS
            stack.append(__main____Vector__char__1__pushBack__block__2__if__3__block__4__for__5__i)
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
            stack.append(__main____Vector__char__1__pushBack__block__2__if__3__block__4__for__5__i)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # LHS
            # Subscript assignment
            # LHS
            stack.append(__main____Vector__char__1__pushBack__block__2__if__3__block__4__nData)
            # OFFSET
            stack.append(__main____Vector__char__1__pushBack__block__2__if__3__block__4__for__5__i)
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
            stack.append(__main____Vector__char__1__pushBack__block__2__if__3__block__4__for__5__i)
            __rhs = stack.pop ()
            __main____Vector__char__1__pushBack__block__2__if__3__block__4__for__5__i = __main____Vector__char__1__pushBack__block__2__if__3__block__4__for__5__i + 1
            __res = __main____Vector__char__1__pushBack__block__2__if__3__block__4__for__5__i
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
        __builtin__free (__arr)
        stack.append (0)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main____Vector__char__1__pushBack__block__2__if__3__block__4__nData)
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
# Method Declaration - Vector<:char[]:>::clear() -> void
def __method____main____Vector__char__1____clear (this):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    #---------------------------------------------------------------------
    # While-Loop
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Greater Than
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
        stack.append(0)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs > __rhs
        stack.append (__res)
        __cond = stack.pop ()
        # break out of loop if condition is false
        if (__cond == 0): break
        # Body
        # Statement
        # Method Call - Vector<:char[]:>::popBack() -> char[]
        # LHS
        stack.append(this)
        # RHS
        # Arguments
        __obj = stack.pop ()
        __retval = __method____main____Vector__char__1____popBack (__obj)
        stack.append (__retval)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

    # End of While
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    return 0
# End Method Declaration - __method____main____Vector__char__1____clear
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
__dtable____main____Vector__char__1 = [__method____main____Vector__char__1____pushBack__char__1, __method____main____Vector__char__1____popBack, __method____main____Vector__char__1____clear, __method____main____Vector__char__1____get__int, __method____main____Vector__char__1____set__int__char__1]
# End Class Declaration - __main____Vector__char__1
#=========================================================================

# End Class Template - 
#=========================================================================

#=========================================================================
# Function Template - 
# End Function Template - 
#=========================================================================

#=========================================================================
# Function Template - 
# End Function Template - 
#=========================================================================

#=========================================================================
# Function Declaration - strlen(char[]) -> int
def __main____strlen__char__1 (__main__strlen__str):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    #---------------------------------------------------------------------
    # If-Statement
    # Precomputing all if/elif conditions and give unique names
    # bc we can't have code between if and elif
    # Condition
    # Equal
    # LHS
    stack.append(__main__strlen__str)
    # RHS
    # Null Literal
    stack.append (None)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs == __rhs
    stack.append (__res)
    __if__13__cond = stack.pop ()
    # get condition from stack
    if (__if__13__cond):
        # Body
        # Return
        # Negative
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop ()
        __res = -__rhs
        stack.append (__res)
        __rVal = stack.pop ()
        return __rVal
    # End of if
    #---------------------------------------------------------------------
    # Statement
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(0)
    # LHS
    __main__strlen__block__12__size = 0
    __rhs = stack.pop()
    __main__strlen__block__12__size = __rhs
    stack.append (__main__strlen__block__12__size)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
    # While-Loop
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Not Equal
        # LHS
        # Subscript
        # LHS
        stack.append(__main__strlen__str)
        # OFFSET
        # Post-Increment
        __res = __main__strlen__block__12__size
        __main__strlen__block__12__size = __main__strlen__block__12__size + 1
        stack.append (__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        # Char Literal
        stack.append('\0')
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs != __rhs
        stack.append (__res)
        __cond = stack.pop ()
        # break out of loop if condition is false
        if (__cond == 0): break
        # Body
    # End of While
    #---------------------------------------------------------------------
    # Return
    # Subtraction
    # LHS
    stack.append(__main__strlen__block__12__size)
    # RHS
    # Int Literal
    stack.append(1)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs - __rhs
    stack.append(__res)
    __rVal = stack.pop ()
    return __rVal
    #---------------------------------------------------------------------
# End Function Declaration - __main____strlen__char__1
#=========================================================================

#=========================================================================
# Function Declaration - strcmp(char[], char[]) -> int
def __main____strcmp__char__1__char__1 (__main__strcmp__a, __main__strcmp__b):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Assignment - '='
    # RHS
    # Function Call - strlen(char[]) -> int
    # Arguments
    stack.append(__main__strcmp__a)
    __arg0 = stack.pop ()
    # *** strlen
    __res = __main____strlen__char__1 (__arg0)
    stack.append (__res) # function call result
    # LHS
    __main__strcmp__block__15__asize = 0
    __rhs = stack.pop()
    __main__strcmp__block__15__asize = __rhs
    stack.append (__main__strcmp__block__15__asize)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Function Call - strlen(char[]) -> int
    # Arguments
    stack.append(__main__strcmp__b)
    __arg0 = stack.pop ()
    # *** strlen
    __res = __main____strlen__char__1 (__arg0)
    stack.append (__res) # function call result
    # LHS
    __main__strcmp__block__15__bsize = 0
    __rhs = stack.pop()
    __main__strcmp__block__15__bsize = __rhs
    stack.append (__main__strcmp__block__15__bsize)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
    # If-Statement
    # Precomputing all if/elif conditions and give unique names
    # bc we can't have code between if and elif
    # Condition
    # Not Equal
    # LHS
    stack.append(__main__strcmp__block__15__asize)
    # RHS
    stack.append(__main__strcmp__block__15__bsize)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs != __rhs
    stack.append (__res)
    __if__16__cond = stack.pop ()
    # get condition from stack
    if (__if__16__cond):
        # Body
        # Return
        # Int Literal
        stack.append(0)
        __rVal = stack.pop ()
        return __rVal
    # End of if
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    # For-Loop
    # Init
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(0)
    # LHS
    __main__strcmp__block__15__for__17__i = 0
    __rhs = stack.pop()
    __main__strcmp__block__15__for__17__i = __rhs
    stack.append (__main__strcmp__block__15__for__17__i)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        stack.append(__main__strcmp__block__15__for__17__i)
        # RHS
        stack.append(__main__strcmp__block__15__asize)
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
        # Not Equal
        # LHS
        # Subscript
        # LHS
        stack.append(__main__strcmp__a)
        # OFFSET
        stack.append(__main__strcmp__block__15__for__17__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        # Subscript
        # LHS
        stack.append(__main__strcmp__b)
        # OFFSET
        stack.append(__main__strcmp__block__15__for__17__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs != __rhs
        stack.append (__res)
        __if__19__cond = stack.pop ()
        # get condition from stack
        if (__if__19__cond):
            # Body
            #-------------------------------------------------------------
            # Code Block
            # Return
            # Int Literal
            stack.append(0)
            __rVal = stack.pop ()
            return __rVal
            #-------------------------------------------------------------
        # End of if
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # Update
        # Pre-Increment
        # RHS
        stack.append(__main__strcmp__block__15__for__17__i)
        __rhs = stack.pop ()
        __main__strcmp__block__15__for__17__i = __main__strcmp__block__15__for__17__i + 1
        __res = __main__strcmp__block__15__for__17__i
        stack.append (__res)
    #---------------------------------------------------------------------
    # Return
    # Int Literal
    stack.append(1)
    __rVal = stack.pop ()
    return __rVal
    #---------------------------------------------------------------------
# End Function Declaration - __main____strcmp__char__1__char__1
#=========================================================================

#=========================================================================
# Function Declaration - substr(char[], int, int) -> char[]
def __main____substr__char__1__int__int (__main__substr__a, __main__substr__start, __main__substr__end):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Assignment - '='
    # RHS
    # Addition
    # LHS
    # Subtraction
    # LHS
    stack.append(__main__substr__end)
    # RHS
    stack.append(__main__substr__start)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs - __rhs
    stack.append(__res)
    # RHS
    # Int Literal
    stack.append(1)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs + __rhs
    stack.append(__res)
    __dim = stack.pop ()
    __res = [None] * __dim
    stack.append (__res)
    # LHS
    __main__substr__block__21__res = 0
    __rhs = stack.pop()
    __main__substr__block__21__res = __rhs
    stack.append (__main__substr__block__21__res)
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
    __main__substr__block__21__for__22__i = 0
    __rhs = stack.pop()
    __main__substr__block__21__for__22__i = __rhs
    stack.append (__main__substr__block__21__for__22__i)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        stack.append(__main__substr__block__21__for__22__i)
        # RHS
        # Subtraction
        # LHS
        stack.append(__main__substr__end)
        # RHS
        stack.append(__main__substr__start)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs - __rhs
        stack.append(__res)
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
        # Statement
        # Assignment - '='
        # RHS
        # Subscript
        # LHS
        stack.append(__main__substr__a)
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__substr__block__21__for__22__i)
        # RHS
        stack.append(__main__substr__start)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # LHS
        # Subscript assignment
        # LHS
        stack.append(__main__substr__block__21__res)
        # OFFSET
        stack.append(__main__substr__block__21__for__22__i)
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
        # Update
        # Pre-Increment
        # RHS
        stack.append(__main__substr__block__21__for__22__i)
        __rhs = stack.pop ()
        __main__substr__block__21__for__22__i = __main__substr__block__21__for__22__i + 1
        __res = __main__substr__block__21__for__22__i
        stack.append (__res)
    #---------------------------------------------------------------------
    # Statement
    # Assignment - '='
    # RHS
    # Char Literal
    stack.append('\0')
    # LHS
    # Subscript assignment
    # LHS
    stack.append(__main__substr__block__21__res)
    # OFFSET
    # Subtraction
    # LHS
    stack.append(__main__substr__end)
    # RHS
    stack.append(__main__substr__start)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs - __rhs
    stack.append(__res)
    __offset = stack.pop()
    __pointer = stack.pop()
    __rhs = stack.pop()
    __pointer[__offset] = __rhs
    stack.append (__pointer[__offset])
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Return
    stack.append(__main__substr__block__21__res)
    __rVal = stack.pop ()
    return __rVal
    #---------------------------------------------------------------------
# End Function Declaration - __main____substr__char__1__int__int
#=========================================================================

#=========================================================================
# Function Declaration - first_index_of(char[], char) -> int
def __main____first_index_of__char__1__char (__main__first_index_of__arr, __main__first_index_of__c):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Assignment - '='
    # RHS
    # Function Call - strlen(char[]) -> int
    # Arguments
    stack.append(__main__first_index_of__arr)
    __arg0 = stack.pop ()
    # *** strlen
    __res = __main____strlen__char__1 (__arg0)
    stack.append (__res) # function call result
    # LHS
    __main__first_index_of__block__24__size = 0
    __rhs = stack.pop()
    __main__first_index_of__block__24__size = __rhs
    stack.append (__main__first_index_of__block__24__size)
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
    __main__first_index_of__block__24__for__25__i = 0
    __rhs = stack.pop()
    __main__first_index_of__block__24__for__25__i = __rhs
    stack.append (__main__first_index_of__block__24__for__25__i)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        stack.append(__main__first_index_of__block__24__for__25__i)
        # RHS
        stack.append(__main__first_index_of__block__24__size)
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
        # Equal
        # LHS
        # Subscript
        # LHS
        stack.append(__main__first_index_of__arr)
        # OFFSET
        stack.append(__main__first_index_of__block__24__for__25__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        stack.append(__main__first_index_of__c)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs == __rhs
        stack.append (__res)
        __if__27__cond = stack.pop ()
        # get condition from stack
        if (__if__27__cond):
            # Body
            # Return
            stack.append(__main__first_index_of__block__24__for__25__i)
            __rVal = stack.pop ()
            return __rVal
        # End of if
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # Update
        # Pre-Increment
        # RHS
        stack.append(__main__first_index_of__block__24__for__25__i)
        __rhs = stack.pop ()
        __main__first_index_of__block__24__for__25__i = __main__first_index_of__block__24__for__25__i + 1
        __res = __main__first_index_of__block__24__for__25__i
        stack.append (__res)
    #---------------------------------------------------------------------
    # Return
    # Negative
    # RHS
    # Int Literal
    stack.append(1)
    __rhs = stack.pop ()
    __res = -__rhs
    stack.append (__res)
    __rVal = stack.pop ()
    return __rVal
    #---------------------------------------------------------------------
# End Function Declaration - __main____first_index_of__char__1__char
#=========================================================================

#=========================================================================
# Function Declaration - split(char[], char) -> Vector<:char[]:>
def __main____split__char__1__char (__main__split__str, __main__split__delim):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Assignment - '='
    # RHS
    # Constructor Call - Vector<:char[]:>::Vector() -> Vector<:char[]:>
    # Arguments
    __retval = __ctor____main____Vector__char__1____Vector ()
    stack.append (__retval)
    # LHS
    __main__split__block__28__tokens = 0
    __rhs = stack.pop()
    __main__split__block__28__tokens = __rhs
    stack.append (__main__split__block__28__tokens)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Function Call - strlen(char[]) -> int
    # Arguments
    stack.append(__main__split__str)
    __arg0 = stack.pop ()
    # *** strlen
    __res = __main____strlen__char__1 (__arg0)
    stack.append (__res) # function call result
    # LHS
    __main__split__block__28__size = 0
    __rhs = stack.pop()
    __main__split__block__28__size = __rhs
    stack.append (__main__split__block__28__size)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(0)
    # LHS
    __main__split__block__28__i = 0
    __rhs = stack.pop()
    __main__split__block__28__i = __rhs
    stack.append (__main__split__block__28__i)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(0)
    # LHS
    __main__split__block__28__j = 0
    __rhs = stack.pop()
    __main__split__block__28__j = __rhs
    stack.append (__main__split__block__28__j)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
    # While-Loop
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        stack.append(__main__split__block__28__i)
        # RHS
        stack.append(__main__split__block__28__size)
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
        # Not Equal
        # LHS
        # Subscript
        # LHS
        stack.append(__main__split__str)
        # OFFSET
        stack.append(__main__split__block__28__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        stack.append(__main__split__delim)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs != __rhs
        stack.append (__res)
        __if__31__cond = stack.pop ()
        # get condition from stack
        if (__if__31__cond):
            # Body
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Assignment - '='
            # RHS
            # Int Literal
            stack.append(0)
            # LHS
            __main__split__block__28__while__29__block__30__if__31__block__32__count = 0
            __rhs = stack.pop()
            __main__split__block__28__while__29__block__30__if__31__block__32__count = __rhs
            stack.append (__main__split__block__28__while__29__block__30__if__31__block__32__count)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            # Statement
            # Assignment - '='
            # RHS
            stack.append(__main__split__block__28__i)
            # LHS
            __main__split__block__28__while__29__block__30__if__31__block__32__k = 0
            __rhs = stack.pop()
            __main__split__block__28__while__29__block__30__if__31__block__32__k = __rhs
            stack.append (__main__split__block__28__while__29__block__30__if__31__block__32__k)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            #-------------------------------------------------------------
            # While-Loop
            # Using an infinite loop so we can write a separate multi-line condition
            while (1):
                # Condition
                # Less Than
                # LHS
                stack.append(__main__split__block__28__while__29__block__30__if__31__block__32__k)
                # RHS
                stack.append(__main__split__block__28__size)
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs < __rhs
                stack.append (__res)
                __cond = stack.pop ()
                # break out of loop if condition is false
                if (__cond == 0): break
                # Body
                #---------------------------------------------------------
                # If-Statement
                # Precomputing all if/elif conditions and give unique names
                # bc we can't have code between if and elif
                # Condition
                # Not Equal
                # LHS
                # Subscript
                # LHS
                stack.append(__main__split__str)
                # OFFSET
                # Post-Increment
                __res = __main__split__block__28__while__29__block__30__if__31__block__32__k
                __main__split__block__28__while__29__block__30__if__31__block__32__k = __main__split__block__28__while__29__block__30__if__31__block__32__k + 1
                stack.append (__res)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # RHS
                stack.append(__main__split__delim)
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs != __rhs
                stack.append (__res)
                __if__34__cond = stack.pop ()
                # get condition from stack
                if (__if__34__cond):
                    # Body
                    # Statement
                    # Pre-Increment
                    # RHS
                    stack.append(__main__split__block__28__while__29__block__30__if__31__block__32__count)
                    __rhs = stack.pop ()
                    __main__split__block__28__while__29__block__30__if__31__block__32__count = __main__split__block__28__while__29__block__30__if__31__block__32__count + 1
                    __res = __main__split__block__28__while__29__block__30__if__31__block__32__count
                    stack.append (__res)
                    # Statement results can be ignored
                    stack.pop ()
                    # End Statement

                #---------------------------------------------------------
                # Else-Statement
                else:
                    # Break out of __while__33
                    break
                #---------------------------------------------------------
                # End of if
                #---------------------------------------------------------
            # End of While
            #-------------------------------------------------------------
            # Statement
            # Method Call - Vector<:char[]:>::pushBack(char[]) -> void
            # LHS
            stack.append(__main__split__block__28__tokens)
            # RHS
            # Arguments
            # Addition
            # LHS
            stack.append(__main__split__block__28__while__29__block__30__if__31__block__32__count)
            # RHS
            # Int Literal
            stack.append(1)
            __rhs = stack.pop()
            __lhs = stack.pop()
            __res = __lhs + __rhs
            stack.append(__res)
            __dim = stack.pop ()
            __res = [None] * __dim
            stack.append (__res)
            __arg0 = stack.pop ()
            __obj = stack.pop ()
            __retval = __method____main____Vector__char__1____pushBack__char__1 (__obj, __arg0)
            stack.append (__retval)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            #-------------------------------------------------------------
            # For-Loop
            # Init
            # Assignment - '='
            # RHS
            # Int Literal
            stack.append(0)
            # LHS
            __main__split__block__28__while__29__block__30__if__31__block__32__for__35__k = 0
            __rhs = stack.pop()
            __main__split__block__28__while__29__block__30__if__31__block__32__for__35__k = __rhs
            stack.append (__main__split__block__28__while__29__block__30__if__31__block__32__for__35__k)
            # Using an infinite loop so we can write a separate multi-line condition
            while (1):
                # Condition
                # Less Than
                # LHS
                stack.append(__main__split__block__28__while__29__block__30__if__31__block__32__for__35__k)
                # RHS
                stack.append(__main__split__block__28__while__29__block__30__if__31__block__32__count)
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs < __rhs
                stack.append (__res)
                __cond = stack.pop ()
                # break out of loop if condition is false
                if (__cond == 0): break
                # Body
                #---------------------------------------------------------
                # Code Block
                # Statement
                # Assignment - '='
                # RHS
                # Subscript
                # LHS
                stack.append(__main__split__str)
                # OFFSET
                # Post-Increment
                __res = __main__split__block__28__i
                __main__split__block__28__i = __main__split__block__28__i + 1
                stack.append (__res)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # LHS
                # Subscript assignment
                # LHS
                # Subscript
                # LHS
                # Member Accessor
                # LHS
                stack.append(__main__split__block__28__tokens)
                # RHS
                stack.append (__field____main____Vector__char__1____data)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                # OFFSET
                stack.append(__main__split__block__28__j)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # OFFSET
                stack.append(__main__split__block__28__while__29__block__30__if__31__block__32__for__35__k)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                #---------------------------------------------------------
                # Update
                # Pre-Increment
                # RHS
                stack.append(__main__split__block__28__while__29__block__30__if__31__block__32__for__35__k)
                __rhs = stack.pop ()
                __main__split__block__28__while__29__block__30__if__31__block__32__for__35__k = __main__split__block__28__while__29__block__30__if__31__block__32__for__35__k + 1
                __res = __main__split__block__28__while__29__block__30__if__31__block__32__for__35__k
                stack.append (__res)
            #-------------------------------------------------------------
            # Statement
            # Assignment - '='
            # RHS
            # Char Literal
            stack.append('\0')
            # LHS
            # Subscript assignment
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__split__block__28__tokens)
            # RHS
            stack.append (__field____main____Vector__char__1____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main__split__block__28__j)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # OFFSET
            stack.append(__main__split__block__28__while__29__block__30__if__31__block__32__count)
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
            stack.append(__main__split__block__28__j)
            __rhs = stack.pop ()
            __main__split__block__28__j = __main__split__block__28__j + 1
            __res = __main__split__block__28__j
            stack.append (__res)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            #-------------------------------------------------------------
        # End of if
        #-----------------------------------------------------------------
        # Statement
        # Pre-Increment
        # RHS
        stack.append(__main__split__block__28__i)
        __rhs = stack.pop ()
        __main__split__block__28__i = __main__split__block__28__i + 1
        __res = __main__split__block__28__i
        stack.append (__res)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
    # End of While
    #---------------------------------------------------------------------
    # Return
    stack.append(__main__split__block__28__tokens)
    __rVal = stack.pop ()
    return __rVal
    #---------------------------------------------------------------------
# End Function Declaration - __main____split__char__1__char
#=========================================================================

#=========================================================================
# Function Declaration - max(int, int) -> int
def __main____max__int__int (__main__max__a, __main__max__b):
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
    stack.append(__main__max__a)
    # RHS
    stack.append(__main__max__b)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs >= __rhs
    stack.append (__res)
    __if__38__cond = stack.pop ()
    # get condition from stack
    if (__if__38__cond):
        # Body
        # Return
        stack.append(__main__max__a)
        __rVal = stack.pop ()
        return __rVal
    # End of if
    #---------------------------------------------------------------------
    # Return
    stack.append(__main__max__b)
    __rVal = stack.pop ()
    return __rVal
    #---------------------------------------------------------------------
# End Function Declaration - __main____max__int__int
#=========================================================================

#=========================================================================
# Function Declaration - max(float, float) -> float
def __main____max__float__float (__main__max__a, __main__max__b):
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
    stack.append(__main__max__a)
    # RHS
    stack.append(__main__max__b)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs >= __rhs
    stack.append (__res)
    __if__40__cond = stack.pop ()
    # get condition from stack
    if (__if__40__cond):
        # Body
        # Return
        stack.append(__main__max__a)
        __rVal = stack.pop ()
        return __rVal
    # End of if
    #---------------------------------------------------------------------
    # Return
    stack.append(__main__max__b)
    __rVal = stack.pop ()
    return __rVal
    #---------------------------------------------------------------------
# End Function Declaration - __main____max__float__float
#=========================================================================

#=========================================================================
# Function Declaration - min(int, int) -> int
def __main____min__int__int (__main__min__a, __main__min__b):
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
    stack.append(__main__min__a)
    # RHS
    stack.append(__main__min__b)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs <= __rhs
    stack.append (__res)
    __if__42__cond = stack.pop ()
    # get condition from stack
    if (__if__42__cond):
        # Body
        # Return
        stack.append(__main__min__a)
        __rVal = stack.pop ()
        return __rVal
    # End of if
    #---------------------------------------------------------------------
    # Return
    stack.append(__main__min__b)
    __rVal = stack.pop ()
    return __rVal
    #---------------------------------------------------------------------
# End Function Declaration - __main____min__int__int
#=========================================================================

#=========================================================================
# Function Declaration - min(float, float) -> float
def __main____min__float__float (__main__min__a, __main__min__b):
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
    stack.append(__main__min__a)
    # RHS
    stack.append(__main__min__b)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs <= __rhs
    stack.append (__res)
    __if__44__cond = stack.pop ()
    # get condition from stack
    if (__if__44__cond):
        # Body
        # Return
        stack.append(__main__min__a)
        __rVal = stack.pop ()
        return __rVal
    # End of if
    #---------------------------------------------------------------------
    # Return
    stack.append(__main__min__b)
    __rVal = stack.pop ()
    return __rVal
    #---------------------------------------------------------------------
# End Function Declaration - __main____min__float__float
#=========================================================================

#=========================================================================
# Function Declaration - abs(int) -> int
def __main____abs__int (__main__abs__v):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    #---------------------------------------------------------------------
    # If-Statement
    # Precomputing all if/elif conditions and give unique names
    # bc we can't have code between if and elif
    # Condition
    # Less Than
    # LHS
    stack.append(__main__abs__v)
    # RHS
    # Int Literal
    stack.append(0)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs < __rhs
    stack.append (__res)
    __if__46__cond = stack.pop ()
    # get condition from stack
    if (__if__46__cond):
        # Body
        # Return
        # Negative
        # RHS
        stack.append(__main__abs__v)
        __rhs = stack.pop ()
        __res = -__rhs
        stack.append (__res)
        __rVal = stack.pop ()
        return __rVal
    # End of if
    #---------------------------------------------------------------------
    # Return
    stack.append(__main__abs__v)
    __rVal = stack.pop ()
    return __rVal
    #---------------------------------------------------------------------
# End Function Declaration - __main____abs__int
#=========================================================================

#=========================================================================
# Function Declaration - abs(float) -> float
def __main____abs__float (__main__abs__v):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    #---------------------------------------------------------------------
    # If-Statement
    # Precomputing all if/elif conditions and give unique names
    # bc we can't have code between if and elif
    # Condition
    # Less Than
    # LHS
    stack.append(__main__abs__v)
    # RHS
    # Float Literal
    stack.append(0.0)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs < __rhs
    stack.append (__res)
    __if__48__cond = stack.pop ()
    # get condition from stack
    if (__if__48__cond):
        # Body
        # Return
        # Negative
        # RHS
        stack.append(__main__abs__v)
        __rhs = stack.pop ()
        __res = -__rhs
        stack.append (__res)
        __rVal = stack.pop ()
        return __rVal
    # End of if
    #---------------------------------------------------------------------
    # Return
    stack.append(__main__abs__v)
    __rVal = stack.pop ()
    return __rVal
    #---------------------------------------------------------------------
# End Function Declaration - __main____abs__float
#=========================================================================

#=========================================================================
# Class Template - 
# End Class Template - 
#=========================================================================

#=========================================================================
# Class Template - 
# End Class Template - 
#=========================================================================

#=========================================================================
# Function Template - 
# End Function Template - 
#=========================================================================

#=========================================================================
# Function Template - 
# End Function Template - 
#=========================================================================

# Statement
# Assignment - '='
# RHS
# Function Call - input() -> char[]
# Arguments
# *** input
__res = __builtin__input ()
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
    stack.append(__main__line)
    # RHS
    # Null Literal
    stack.append (None)
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
    __res = __builtin__input ()
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
# Statement
# Assignment - '='
# RHS
# Int Literal
stack.append(0)
# LHS
__main__x = 0
__rhs = stack.pop()
__main__x = __rhs
stack.append (__main__x)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Assignment - '='
# RHS
# Int Literal
stack.append(0)
# LHS
__main__y = 0
__rhs = stack.pop()
__main__y = __rhs
stack.append (__main__y)
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
__main__board = 0
__rhs = stack.pop()
__main__board = __rhs
stack.append (__main__board)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Method Call - Vector<:char[]:>::pushBack(char[]) -> void
# LHS
stack.append(__main__board)
# RHS
# Arguments
# String Literal
stack.append([*("+-------+"+'\0')])
__arg0 = stack.pop ()
__obj = stack.pop ()
__retval = __method____main____Vector__char__1____pushBack__char__1 (__obj, __arg0)
stack.append (__retval)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Method Call - Vector<:char[]:>::pushBack(char[]) -> void
# LHS
stack.append(__main__board)
# RHS
# Arguments
# String Literal
stack.append([*("|.......|"+'\0')])
__arg0 = stack.pop ()
__obj = stack.pop ()
__retval = __method____main____Vector__char__1____pushBack__char__1 (__obj, __arg0)
stack.append (__retval)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Method Call - Vector<:char[]:>::pushBack(char[]) -> void
# LHS
stack.append(__main__board)
# RHS
# Arguments
# String Literal
stack.append([*("|.......|"+'\0')])
__arg0 = stack.pop ()
__obj = stack.pop ()
__retval = __method____main____Vector__char__1____pushBack__char__1 (__obj, __arg0)
stack.append (__retval)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Method Call - Vector<:char[]:>::pushBack(char[]) -> void
# LHS
stack.append(__main__board)
# RHS
# Arguments
# String Literal
stack.append([*("|.......|"+'\0')])
__arg0 = stack.pop ()
__obj = stack.pop ()
__retval = __method____main____Vector__char__1____pushBack__char__1 (__obj, __arg0)
stack.append (__retval)
# Statement results can be ignored
stack.pop ()
# End Statement

#=========================================================================
# Function Declaration - printboard(Vector<:char[]:>) -> void
def __main____printboard__Vector__tparam0__char (__main__printboard__board):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Return
    return
    #---------------------------------------------------------------------
    # For-Loop
    # Init
    # Assignment - '='
    # RHS
    # Subtraction
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main__printboard__board)
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
    __res = __lhs - __rhs
    stack.append(__res)
    # LHS
    __main__printboard__block__51__for__52__i = 0
    __rhs = stack.pop()
    __main__printboard__block__51__for__52__i = __rhs
    stack.append (__main__printboard__block__51__for__52__i)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Greater Than or Equal to
        # LHS
        stack.append(__main__printboard__block__51__for__52__i)
        # RHS
        # Int Literal
        stack.append(0)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs >= __rhs
        stack.append (__res)
        __cond = stack.pop ()
        # break out of loop if condition is false
        if (__cond == 0): break
        # Body
        #-----------------------------------------------------------------
        # Code Block
        #-----------------------------------------------------------------
        # For-Loop
        # Init
        # Assignment - '='
        # RHS
        # Int Literal
        stack.append(0)
        # LHS
        __main__printboard__block__51__for__52__block__53__for__54__j = 0
        __rhs = stack.pop()
        __main__printboard__block__51__for__52__block__53__for__54__j = __rhs
        stack.append (__main__printboard__block__51__for__52__block__53__for__54__j)
        # Using an infinite loop so we can write a separate multi-line condition
        while (1):
            # Condition
            # Less Than
            # LHS
            stack.append(__main__printboard__block__51__for__52__block__53__for__54__j)
            # RHS
            # Int Literal
            stack.append(9)
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
            # Function Call - print(char) -> void
            # Arguments
            # Subscript
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__printboard__board)
            # RHS
            stack.append (__field____main____Vector__char__1____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main__printboard__block__51__for__52__i)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # OFFSET
            stack.append(__main__printboard__block__51__for__52__block__53__for__54__j)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            __arg0 = stack.pop ()
            # *** print
            __res = __builtin__print__char (__arg0)
            stack.append (__res) # function call result
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            #-------------------------------------------------------------
            # Update
            # Pre-Increment
            # RHS
            stack.append(__main__printboard__block__51__for__52__block__53__for__54__j)
            __rhs = stack.pop ()
            __main__printboard__block__51__for__52__block__53__for__54__j = __main__printboard__block__51__for__52__block__53__for__54__j + 1
            __res = __main__printboard__block__51__for__52__block__53__for__54__j
            stack.append (__res)
        #-----------------------------------------------------------------
        # Statement
        # Function Call - println() -> void
        # Arguments
        # *** println
        __res = __builtin__println ()
        stack.append (__res) # function call result
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
        # Update
        # Pre-Decrement
        # RHS
        stack.append(__main__printboard__block__51__for__52__i)
        __rhs = stack.pop ()
        __main__printboard__block__51__for__52__i = __main__printboard__block__51__for__52__i - 1
        __res = __main__printboard__block__51__for__52__i
        stack.append (__res)
    #---------------------------------------------------------------------
    # Statement
    # Function Call - println() -> void
    # Arguments
    # *** println
    __res = __builtin__println ()
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
# End Function Declaration - __main____printboard__Vector__tparam0__char
#=========================================================================

#=========================================================================
# Function Declaration - printboard2(Vector<:char[]:>) -> void
def __main____printboard2__Vector__tparam0__char (__main__printboard2__board):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    #---------------------------------------------------------------------
    # For-Loop
    # Init
    # Assignment - '='
    # RHS
    # Subtraction
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main__printboard2__board)
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
    __res = __lhs - __rhs
    stack.append(__res)
    # LHS
    __main__printboard2__block__56__for__57__i = 0
    __rhs = stack.pop()
    __main__printboard2__block__56__for__57__i = __rhs
    stack.append (__main__printboard2__block__56__for__57__i)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Greater Than or Equal to
        # LHS
        stack.append(__main__printboard2__block__56__for__57__i)
        # RHS
        # Int Literal
        stack.append(0)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs >= __rhs
        stack.append (__res)
        __cond = stack.pop ()
        # break out of loop if condition is false
        if (__cond == 0): break
        # Body
        #-----------------------------------------------------------------
        # Code Block
        #-----------------------------------------------------------------
        # For-Loop
        # Init
        # Assignment - '='
        # RHS
        # Int Literal
        stack.append(0)
        # LHS
        __main__printboard2__block__56__for__57__block__58__for__59__j = 0
        __rhs = stack.pop()
        __main__printboard2__block__56__for__57__block__58__for__59__j = __rhs
        stack.append (__main__printboard2__block__56__for__57__block__58__for__59__j)
        # Using an infinite loop so we can write a separate multi-line condition
        while (1):
            # Condition
            # Less Than
            # LHS
            stack.append(__main__printboard2__block__56__for__57__block__58__for__59__j)
            # RHS
            # Int Literal
            stack.append(9)
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
            # Function Call - print(char) -> void
            # Arguments
            # Subscript
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__printboard2__board)
            # RHS
            stack.append (__field____main____Vector__char__1____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main__printboard2__block__56__for__57__i)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # OFFSET
            stack.append(__main__printboard2__block__56__for__57__block__58__for__59__j)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            __arg0 = stack.pop ()
            # *** print
            __res = __builtin__print__char (__arg0)
            stack.append (__res) # function call result
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            #-------------------------------------------------------------
            # Update
            # Pre-Increment
            # RHS
            stack.append(__main__printboard2__block__56__for__57__block__58__for__59__j)
            __rhs = stack.pop ()
            __main__printboard2__block__56__for__57__block__58__for__59__j = __main__printboard2__block__56__for__57__block__58__for__59__j + 1
            __res = __main__printboard2__block__56__for__57__block__58__for__59__j
            stack.append (__res)
        #-----------------------------------------------------------------
        # Statement
        # Function Call - println(int) -> void
        # Arguments
        stack.append(__main__printboard2__block__56__for__57__i)
        __arg0 = stack.pop ()
        # *** println
        __res = __builtin__println__int (__arg0)
        stack.append (__res) # function call result
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
        # Update
        # Pre-Decrement
        # RHS
        stack.append(__main__printboard2__block__56__for__57__i)
        __rhs = stack.pop ()
        __main__printboard2__block__56__for__57__i = __main__printboard2__block__56__for__57__i - 1
        __res = __main__printboard2__block__56__for__57__i
        stack.append (__res)
    #---------------------------------------------------------------------
    # Statement
    # Function Call - println() -> void
    # Arguments
    # *** println
    __res = __builtin__println ()
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
# End Function Declaration - __main____printboard2__Vector__tparam0__char
#=========================================================================

# Statement
# Assignment - '='
# RHS
# Int Literal
stack.append(0)
# LHS
__main__shift_index = 0
__rhs = stack.pop()
__main__shift_index = __rhs
stack.append (__main__shift_index)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Assignment - '='
# RHS
# Subtraction
# LHS
# Function Call - strlen(char[]) -> int
# Arguments
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
# Int Literal
stack.append(0)
__offset = stack.pop ()
__pointer = stack.pop ()
stack.append (__pointer[__offset])
__arg0 = stack.pop ()
# *** strlen
__res = __main____strlen__char__1 (__arg0)
stack.append (__res) # function call result
# RHS
# Int Literal
stack.append(1)
__rhs = stack.pop()
__lhs = stack.pop()
__res = __lhs - __rhs
stack.append(__res)
# LHS
__main__shift_max = 0
__rhs = stack.pop()
__main__shift_max = __rhs
stack.append (__main__shift_max)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Assignment - '='
# RHS
# Int Literal
stack.append(0)
# LHS
__main__iter = 0
__rhs = stack.pop()
__main__iter = __rhs
stack.append (__main__iter)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Assignment - '='
# RHS
# Int Literal
stack.append(0)
# LHS
__main__num_rocks = 0
__rhs = stack.pop()
__main__num_rocks = __rhs
stack.append (__main__num_rocks)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Assignment - '='
# RHS
# Int Literal
stack.append(2022)
# LHS
__main__max_rocks = 0
__rhs = stack.pop()
__main__max_rocks = __rhs
stack.append (__main__max_rocks)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Assignment - '='
# RHS
# Int Literal
stack.append(0)
# LHS
__main__height = 0
__rhs = stack.pop()
__main__height = __rhs
stack.append (__main__height)
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
    # Code Block
    # Statement
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(0)
    # LHS
    __main__while__61__block__62__block__63__rock_height = 0
    __rhs = stack.pop()
    __main__while__61__block__62__block__63__rock_height = __rhs
    stack.append (__main__while__61__block__62__block__63__rock_height)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
    # For-Loop
    # Init
    # Assignment - '='
    # RHS
    # Subtraction
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main__board)
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
    __res = __lhs - __rhs
    stack.append(__res)
    # LHS
    __main__while__61__block__62__block__63__for__64__i = 0
    __rhs = stack.pop()
    __main__while__61__block__62__block__63__for__64__i = __rhs
    stack.append (__main__while__61__block__62__block__63__for__64__i)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Greater Than or Equal to
        # LHS
        stack.append(__main__while__61__block__62__block__63__for__64__i)
        # RHS
        # Int Literal
        stack.append(0)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs >= __rhs
        stack.append (__res)
        __cond = stack.pop ()
        # break out of loop if condition is false
        if (__cond == 0): break
        # Body
        #-----------------------------------------------------------------
        # Code Block
        #-----------------------------------------------------------------
        # For-Loop
        # Init
        # Assignment - '='
        # RHS
        # Int Literal
        stack.append(1)
        # LHS
        __main__while__61__block__62__block__63__for__64__block__65__for__66__j = 0
        __rhs = stack.pop()
        __main__while__61__block__62__block__63__for__64__block__65__for__66__j = __rhs
        stack.append (__main__while__61__block__62__block__63__for__64__block__65__for__66__j)
        # Using an infinite loop so we can write a separate multi-line condition
        while (1):
            # Condition
            # Less Than
            # LHS
            stack.append(__main__while__61__block__62__block__63__for__64__block__65__for__66__j)
            # RHS
            # Int Literal
            stack.append(8)
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
            #-------------------------------------------------------------
            # If-Statement
            # Precomputing all if/elif conditions and give unique names
            # bc we can't have code between if and elif
            # Condition
            # Not Equal
            # LHS
            # Subscript
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__board)
            # RHS
            stack.append (__field____main____Vector__char__1____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main__while__61__block__62__block__63__for__64__i)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # OFFSET
            stack.append(__main__while__61__block__62__block__63__for__64__block__65__for__66__j)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            # Char Literal
            stack.append('.')
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs != __rhs
            stack.append (__res)
            __if__68__cond = stack.pop ()
            # get condition from stack
            if (__if__68__cond):
                # Body
                #---------------------------------------------------------
                # Code Block
                # Statement
                # Assignment - '='
                # RHS
                stack.append(__main__while__61__block__62__block__63__for__64__i)
                __rhs = stack.pop()
                __main__while__61__block__62__block__63__rock_height = __rhs
                stack.append (__main__while__61__block__62__block__63__rock_height)
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Break out of __for__66
                break
                #---------------------------------------------------------
            # End of if
            #-------------------------------------------------------------
            #-------------------------------------------------------------
            # Update
            # Pre-Increment
            # RHS
            stack.append(__main__while__61__block__62__block__63__for__64__block__65__for__66__j)
            __rhs = stack.pop ()
            __main__while__61__block__62__block__63__for__64__block__65__for__66__j = __main__while__61__block__62__block__63__for__64__block__65__for__66__j + 1
            __res = __main__while__61__block__62__block__63__for__64__block__65__for__66__j
            stack.append (__res)
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # If-Statement
        # Precomputing all if/elif conditions and give unique names
        # bc we can't have code between if and elif
        # Condition
        # Not Equal
        # LHS
        stack.append(__main__while__61__block__62__block__63__rock_height)
        # RHS
        # Int Literal
        stack.append(0)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs != __rhs
        stack.append (__res)
        __if__70__cond = stack.pop ()
        # get condition from stack
        if (__if__70__cond):
            # Body
            # Break out of __for__64
            break
        # End of if
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # Update
        # Pre-Decrement
        # RHS
        stack.append(__main__while__61__block__62__block__63__for__64__i)
        __rhs = stack.pop ()
        __main__while__61__block__62__block__63__for__64__i = __main__while__61__block__62__block__63__for__64__i - 1
        __res = __main__while__61__block__62__block__63__for__64__i
        stack.append (__res)
    #---------------------------------------------------------------------
    # Statement
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(1)
    # LHS
    __main__while__61__block__62__block__63__shape_height = 0
    __rhs = stack.pop()
    __main__while__61__block__62__block__63__shape_height = __rhs
    stack.append (__main__while__61__block__62__block__63__shape_height)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Char Literal
    stack.append('0')
    # LHS
    __main__while__61__block__62__block__63__rock_char = 0
    __rhs = stack.pop()
    __main__while__61__block__62__block__63__rock_char = __rhs
    stack.append (__main__while__61__block__62__block__63__rock_char)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Addition
    # LHS
    # Addition
    # LHS
    stack.append(__main__while__61__block__62__block__63__rock_height)
    # RHS
    # Int Literal
    stack.append(3)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs + __rhs
    stack.append(__res)
    # RHS
    stack.append(__main__while__61__block__62__block__63__shape_height)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs + __rhs
    stack.append(__res)
    # LHS
    __main__while__61__block__62__block__63__desired_height = 0
    __rhs = stack.pop()
    __main__while__61__block__62__block__63__desired_height = __rhs
    stack.append (__main__while__61__block__62__block__63__desired_height)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
    # While-Loop
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        # Subtraction
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
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
        __res = __lhs - __rhs
        stack.append(__res)
        # RHS
        stack.append(__main__while__61__block__62__block__63__desired_height)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs < __rhs
        stack.append (__res)
        __cond = stack.pop ()
        # break out of loop if condition is false
        if (__cond == 0): break
        # Body
        # Statement
        # Method Call - Vector<:char[]:>::pushBack(char[]) -> void
        # LHS
        stack.append(__main__board)
        # RHS
        # Arguments
        # String Literal
        stack.append([*("|.......|"+'\0')])
        __arg0 = stack.pop ()
        __obj = stack.pop ()
        __retval = __method____main____Vector__char__1____pushBack__char__1 (__obj, __arg0)
        stack.append (__retval)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

    # End of While
    #---------------------------------------------------------------------
    # Statement
    # Function Call - printboard(Vector<:char[]:>) -> void
    # Arguments
    stack.append(__main__board)
    __arg0 = stack.pop ()
    # *** printboard
    __res = __main____printboard__Vector__tparam0__char (__arg0)
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Array Constructor
    # Elements
    # Int Literal
    stack.append(3)
    # Int Literal
    stack.append(4)
    # Int Literal
    stack.append(5)
    # Int Literal
    stack.append(6)
    __elem3 = stack.pop ()
    __elem2 = stack.pop ()
    __elem1 = stack.pop ()
    __elem0 = stack.pop ()
    __list = [0] * 4
    __list[0] = __elem0
    __list[1] = __elem1
    __list[2] = __elem2
    __list[3] = __elem3
    stack.append (__list)
    # LHS
    __main__while__61__block__62__block__63__posx0 = 0
    __rhs = stack.pop()
    __main__while__61__block__62__block__63__posx0 = __rhs
    stack.append (__main__while__61__block__62__block__63__posx0)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Addition
    # LHS
    # Addition
    # LHS
    stack.append(__main__while__61__block__62__block__63__rock_height)
    # RHS
    # Int Literal
    stack.append(3)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs + __rhs
    stack.append(__res)
    # RHS
    # Int Literal
    stack.append(1)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs + __rhs
    stack.append(__res)
    # LHS
    __main__while__61__block__62__block__63__posy = 0
    __rhs = stack.pop()
    __main__while__61__block__62__block__63__posy = __rhs
    stack.append (__main__while__61__block__62__block__63__posy)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main__while__61__block__62__block__63__rock_char)
    # LHS
    # Subscript assignment
    # LHS
    # Subscript
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main__board)
    # RHS
    stack.append (__field____main____Vector__char__1____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    stack.append(__main__while__61__block__62__block__63__posy)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    # OFFSET
    # Subscript
    # LHS
    stack.append(__main__while__61__block__62__block__63__posx0)
    # OFFSET
    # Int Literal
    stack.append(0)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    __offset = stack.pop()
    __pointer = stack.pop()
    __rhs = stack.pop()
    __pointer[__offset] = __rhs
    stack.append (__pointer[__offset])
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main__while__61__block__62__block__63__rock_char)
    # LHS
    # Subscript assignment
    # LHS
    # Subscript
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main__board)
    # RHS
    stack.append (__field____main____Vector__char__1____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    stack.append(__main__while__61__block__62__block__63__posy)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    # OFFSET
    # Subscript
    # LHS
    stack.append(__main__while__61__block__62__block__63__posx0)
    # OFFSET
    # Int Literal
    stack.append(1)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    __offset = stack.pop()
    __pointer = stack.pop()
    __rhs = stack.pop()
    __pointer[__offset] = __rhs
    stack.append (__pointer[__offset])
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main__while__61__block__62__block__63__rock_char)
    # LHS
    # Subscript assignment
    # LHS
    # Subscript
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main__board)
    # RHS
    stack.append (__field____main____Vector__char__1____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    stack.append(__main__while__61__block__62__block__63__posy)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    # OFFSET
    # Subscript
    # LHS
    stack.append(__main__while__61__block__62__block__63__posx0)
    # OFFSET
    # Int Literal
    stack.append(2)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    __offset = stack.pop()
    __pointer = stack.pop()
    __rhs = stack.pop()
    __pointer[__offset] = __rhs
    stack.append (__pointer[__offset])
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main__while__61__block__62__block__63__rock_char)
    # LHS
    # Subscript assignment
    # LHS
    # Subscript
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main__board)
    # RHS
    stack.append (__field____main____Vector__char__1____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    stack.append(__main__while__61__block__62__block__63__posy)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    # OFFSET
    # Subscript
    # LHS
    stack.append(__main__while__61__block__62__block__63__posx0)
    # OFFSET
    # Int Literal
    stack.append(3)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    __offset = stack.pop()
    __pointer = stack.pop()
    __rhs = stack.pop()
    __pointer[__offset] = __rhs
    stack.append (__pointer[__offset])
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Function Call - printboard(Vector<:char[]:>) -> void
    # Arguments
    stack.append(__main__board)
    __arg0 = stack.pop ()
    # *** printboard
    __res = __main____printboard__Vector__tparam0__char (__arg0)
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
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
        #-----------------------------------------------------------------
        # Code Block
        # Statement
        # Function Call - println(int) -> void
        # Arguments
        stack.append(__main__shift_index)
        __arg0 = stack.pop ()
        # *** println
        __res = __builtin__println__int (__arg0)
        stack.append (__res) # function call result
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Char Literal
        stack.append('.')
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__63__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__63__posx0)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Char Literal
        stack.append('.')
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__63__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__63__posx0)
        # OFFSET
        # Int Literal
        stack.append(1)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Char Literal
        stack.append('.')
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__63__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__63__posx0)
        # OFFSET
        # Int Literal
        stack.append(2)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Char Literal
        stack.append('.')
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__63__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__63__posx0)
        # OFFSET
        # Int Literal
        stack.append(3)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
        # If-Statement
        # Precomputing all if/elif conditions and give unique names
        # bc we can't have code between if and elif
        # Condition
        # Equal
        # LHS
        # Subscript
        # LHS
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
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        stack.append(__main__shift_index)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        # Char Literal
        stack.append('<')
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs == __rhs
        stack.append (__res)
        __if__74__cond = stack.pop ()
        # get condition from stack
        if (__if__74__cond):
            # Body
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Function Call - println(char[]) -> void
            # Arguments
            # String Literal
            stack.append([*("shift left"+'\0')])
            __arg0 = stack.pop ()
            # *** println
            __res = __builtin__println__char__1 (__arg0)
            stack.append (__res) # function call result
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            #-------------------------------------------------------------
            # If-Statement
            # Precomputing all if/elif conditions and give unique names
            # bc we can't have code between if and elif
            # Condition
            # Equal
            # LHS
            # Subscript
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__board)
            # RHS
            stack.append (__field____main____Vector__char__1____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main__while__61__block__62__block__63__posy)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # OFFSET
            # Subtraction
            # LHS
            # Subscript
            # LHS
            stack.append(__main__while__61__block__62__block__63__posx0)
            # OFFSET
            # Int Literal
            stack.append(0)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            # Int Literal
            stack.append(1)
            __rhs = stack.pop()
            __lhs = stack.pop()
            __res = __lhs - __rhs
            stack.append(__res)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            # Char Literal
            stack.append('.')
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs == __rhs
            stack.append (__res)
            __if__76__cond = stack.pop ()
            # get condition from stack
            if (__if__76__cond):
                # Body
                #---------------------------------------------------------
                # Code Block
                # Statement
                # Assignment - '-='
                # RHS
                # Int Literal
                stack.append(1)
                # LHS
                # Subscript assignment
                # LHS
                stack.append(__main__while__61__block__62__block__63__posx0)
                # OFFSET
                # Int Literal
                stack.append(0)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __pointer[__offset] - __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Statement
                # Assignment - '-='
                # RHS
                # Int Literal
                stack.append(1)
                # LHS
                # Subscript assignment
                # LHS
                stack.append(__main__while__61__block__62__block__63__posx0)
                # OFFSET
                # Int Literal
                stack.append(1)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __pointer[__offset] - __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Statement
                # Assignment - '-='
                # RHS
                # Int Literal
                stack.append(1)
                # LHS
                # Subscript assignment
                # LHS
                stack.append(__main__while__61__block__62__block__63__posx0)
                # OFFSET
                # Int Literal
                stack.append(2)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __pointer[__offset] - __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Statement
                # Assignment - '-='
                # RHS
                # Int Literal
                stack.append(1)
                # LHS
                # Subscript assignment
                # LHS
                stack.append(__main__while__61__block__62__block__63__posx0)
                # OFFSET
                # Int Literal
                stack.append(3)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __pointer[__offset] - __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                #---------------------------------------------------------
            # End of if
            #-------------------------------------------------------------
            #-------------------------------------------------------------
        #-----------------------------------------------------------------
        # Else-Statement
        else:
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Function Call - println(char[]) -> void
            # Arguments
            # String Literal
            stack.append([*("shift right"+'\0')])
            __arg0 = stack.pop ()
            # *** println
            __res = __builtin__println__char__1 (__arg0)
            stack.append (__res) # function call result
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            #-------------------------------------------------------------
            # If-Statement
            # Precomputing all if/elif conditions and give unique names
            # bc we can't have code between if and elif
            # Condition
            # Equal
            # LHS
            # Subscript
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__board)
            # RHS
            stack.append (__field____main____Vector__char__1____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main__while__61__block__62__block__63__posy)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # OFFSET
            # Addition
            # LHS
            # Subscript
            # LHS
            stack.append(__main__while__61__block__62__block__63__posx0)
            # OFFSET
            # Int Literal
            stack.append(3)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            # Int Literal
            stack.append(1)
            __rhs = stack.pop()
            __lhs = stack.pop()
            __res = __lhs + __rhs
            stack.append(__res)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            # Char Literal
            stack.append('.')
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs == __rhs
            stack.append (__res)
            __if__79__cond = stack.pop ()
            # get condition from stack
            if (__if__79__cond):
                # Body
                #---------------------------------------------------------
                # Code Block
                # Statement
                # Assignment - '+='
                # RHS
                # Int Literal
                stack.append(1)
                # LHS
                # Subscript assignment
                # LHS
                stack.append(__main__while__61__block__62__block__63__posx0)
                # OFFSET
                # Int Literal
                stack.append(0)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __pointer[__offset] + __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Statement
                # Assignment - '+='
                # RHS
                # Int Literal
                stack.append(1)
                # LHS
                # Subscript assignment
                # LHS
                stack.append(__main__while__61__block__62__block__63__posx0)
                # OFFSET
                # Int Literal
                stack.append(1)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __pointer[__offset] + __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Statement
                # Assignment - '+='
                # RHS
                # Int Literal
                stack.append(1)
                # LHS
                # Subscript assignment
                # LHS
                stack.append(__main__while__61__block__62__block__63__posx0)
                # OFFSET
                # Int Literal
                stack.append(2)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __pointer[__offset] + __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Statement
                # Assignment - '+='
                # RHS
                # Int Literal
                stack.append(1)
                # LHS
                # Subscript assignment
                # LHS
                stack.append(__main__while__61__block__62__block__63__posx0)
                # OFFSET
                # Int Literal
                stack.append(3)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __pointer[__offset] + __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                #---------------------------------------------------------
            # End of if
            #-------------------------------------------------------------
            #-------------------------------------------------------------
        #-----------------------------------------------------------------
        # End of if
        #-----------------------------------------------------------------
        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main__while__61__block__62__block__63__rock_char)
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__63__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__63__posx0)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main__while__61__block__62__block__63__rock_char)
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__63__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__63__posx0)
        # OFFSET
        # Int Literal
        stack.append(1)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main__while__61__block__62__block__63__rock_char)
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__63__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__63__posx0)
        # OFFSET
        # Int Literal
        stack.append(2)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main__while__61__block__62__block__63__rock_char)
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__63__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__63__posx0)
        # OFFSET
        # Int Literal
        stack.append(3)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Modulus
        # LHS
        # Addition
        # LHS
        stack.append(__main__shift_index)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        # RHS
        stack.append(__main__shift_max)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs % __rhs
        stack.append(__res)
        __rhs = stack.pop()
        __main__shift_index = __rhs
        stack.append (__main__shift_index)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Function Call - printboard(Vector<:char[]:>) -> void
        # Arguments
        stack.append(__main__board)
        __arg0 = stack.pop ()
        # *** printboard
        __res = __main____printboard__Vector__tparam0__char (__arg0)
        stack.append (__res) # function call result
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
        # If-Statement
        # Precomputing all if/elif conditions and give unique names
        # bc we can't have code between if and elif
        # Condition
        # OR
        # LHS
        # OR
        # LHS
        # OR
        # LHS
        # OR
        # LHS
        # Not Equal
        # LHS
        # Subscript
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Subtraction
        # LHS
        stack.append(__main__while__61__block__62__block__63__posy)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs - __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__63__posx0)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        # Char Literal
        stack.append('.')
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs != __rhs
        stack.append (__res)
        # RHS
        # Not Equal
        # LHS
        # Subscript
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Subtraction
        # LHS
        stack.append(__main__while__61__block__62__block__63__posy)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs - __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__63__posx0)
        # OFFSET
        # Int Literal
        stack.append(1)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        # Char Literal
        stack.append('.')
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs != __rhs
        stack.append (__res)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs or __rhs
        stack.append (__res)
        # RHS
        # Not Equal
        # LHS
        # Subscript
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Subtraction
        # LHS
        stack.append(__main__while__61__block__62__block__63__posy)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs - __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__63__posx0)
        # OFFSET
        # Int Literal
        stack.append(2)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        # Char Literal
        stack.append('.')
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs != __rhs
        stack.append (__res)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs or __rhs
        stack.append (__res)
        # RHS
        # Not Equal
        # LHS
        # Subscript
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Subtraction
        # LHS
        stack.append(__main__while__61__block__62__block__63__posy)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs - __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__63__posx0)
        # OFFSET
        # Int Literal
        stack.append(3)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        # Char Literal
        stack.append('.')
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs != __rhs
        stack.append (__res)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs or __rhs
        stack.append (__res)
        # RHS
        # Equal
        # LHS
        # Subtraction
        # LHS
        stack.append(__main__while__61__block__62__block__63__posy)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs - __rhs
        stack.append(__res)
        # RHS
        # Int Literal
        stack.append(0)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs == __rhs
        stack.append (__res)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs or __rhs
        stack.append (__res)
        __if__81__cond = stack.pop ()
        # get condition from stack
        if (__if__81__cond):
            # Body
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Function Call - println(char[]) -> void
            # Arguments
            # String Literal
            stack.append([*("rock at rest"+'\0')])
            __arg0 = stack.pop ()
            # *** println
            __res = __builtin__println__char__1 (__arg0)
            stack.append (__res) # function call result
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            # Break out of __while__72
            break
            #-------------------------------------------------------------
        # End of if
        #-----------------------------------------------------------------
        # Statement
        # Assignment - '='
        # RHS
        # Char Literal
        stack.append('.')
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__63__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__63__posx0)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Char Literal
        stack.append('.')
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__63__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__63__posx0)
        # OFFSET
        # Int Literal
        stack.append(1)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Char Literal
        stack.append('.')
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__63__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__63__posx0)
        # OFFSET
        # Int Literal
        stack.append(2)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Char Literal
        stack.append('.')
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__63__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__63__posx0)
        # OFFSET
        # Int Literal
        stack.append(3)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '-='
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __main__while__61__block__62__block__63__posy = __main__while__61__block__62__block__63__posy - __rhs
        stack.append (__main__while__61__block__62__block__63__posy)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main__while__61__block__62__block__63__rock_char)
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__63__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__63__posx0)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main__while__61__block__62__block__63__rock_char)
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__63__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__63__posx0)
        # OFFSET
        # Int Literal
        stack.append(1)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main__while__61__block__62__block__63__rock_char)
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__63__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__63__posx0)
        # OFFSET
        # Int Literal
        stack.append(2)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main__while__61__block__62__block__63__rock_char)
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__63__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__63__posx0)
        # OFFSET
        # Int Literal
        stack.append(3)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Function Call - printboard(Vector<:char[]:>) -> void
        # Arguments
        stack.append(__main__board)
        __arg0 = stack.pop ()
        # *** printboard
        __res = __main____printboard__Vector__tparam0__char (__arg0)
        stack.append (__res) # function call result
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
    # End of While
    #---------------------------------------------------------------------
    # Statement
    # Function Call - printboard(Vector<:char[]:>) -> void
    # Arguments
    stack.append(__main__board)
    __arg0 = stack.pop ()
    # *** printboard
    __res = __main____printboard__Vector__tparam0__char (__arg0)
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
    # Statement
    # Assignment - '+='
    # RHS
    # Int Literal
    stack.append(1)
    __rhs = stack.pop()
    __main__num_rocks = __main__num_rocks + __rhs
    stack.append (__main__num_rocks)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
    # If-Statement
    # Precomputing all if/elif conditions and give unique names
    # bc we can't have code between if and elif
    # Condition
    # Greater Than or Equal to
    # LHS
    stack.append(__main__num_rocks)
    # RHS
    stack.append(__main__max_rocks)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs >= __rhs
    stack.append (__res)
    __if__83__cond = stack.pop ()
    # get condition from stack
    if (__if__83__cond):
        # Body
        # Break out of __while__61
        break
    # End of if
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(0)
    # LHS
    __main__while__61__block__62__block__84__rock_height = 0
    __rhs = stack.pop()
    __main__while__61__block__62__block__84__rock_height = __rhs
    stack.append (__main__while__61__block__62__block__84__rock_height)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
    # For-Loop
    # Init
    # Assignment - '='
    # RHS
    # Subtraction
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main__board)
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
    __res = __lhs - __rhs
    stack.append(__res)
    # LHS
    __main__while__61__block__62__block__84__for__85__i = 0
    __rhs = stack.pop()
    __main__while__61__block__62__block__84__for__85__i = __rhs
    stack.append (__main__while__61__block__62__block__84__for__85__i)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Greater Than or Equal to
        # LHS
        stack.append(__main__while__61__block__62__block__84__for__85__i)
        # RHS
        # Int Literal
        stack.append(0)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs >= __rhs
        stack.append (__res)
        __cond = stack.pop ()
        # break out of loop if condition is false
        if (__cond == 0): break
        # Body
        #-----------------------------------------------------------------
        # Code Block
        #-----------------------------------------------------------------
        # For-Loop
        # Init
        # Assignment - '='
        # RHS
        # Int Literal
        stack.append(1)
        # LHS
        __main__while__61__block__62__block__84__for__85__block__86__for__87__j = 0
        __rhs = stack.pop()
        __main__while__61__block__62__block__84__for__85__block__86__for__87__j = __rhs
        stack.append (__main__while__61__block__62__block__84__for__85__block__86__for__87__j)
        # Using an infinite loop so we can write a separate multi-line condition
        while (1):
            # Condition
            # Less Than
            # LHS
            stack.append(__main__while__61__block__62__block__84__for__85__block__86__for__87__j)
            # RHS
            # Int Literal
            stack.append(8)
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
            #-------------------------------------------------------------
            # If-Statement
            # Precomputing all if/elif conditions and give unique names
            # bc we can't have code between if and elif
            # Condition
            # Not Equal
            # LHS
            # Subscript
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__board)
            # RHS
            stack.append (__field____main____Vector__char__1____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main__while__61__block__62__block__84__for__85__i)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # OFFSET
            stack.append(__main__while__61__block__62__block__84__for__85__block__86__for__87__j)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            # Char Literal
            stack.append('.')
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs != __rhs
            stack.append (__res)
            __if__89__cond = stack.pop ()
            # get condition from stack
            if (__if__89__cond):
                # Body
                #---------------------------------------------------------
                # Code Block
                # Statement
                # Assignment - '='
                # RHS
                stack.append(__main__while__61__block__62__block__84__for__85__i)
                __rhs = stack.pop()
                __main__while__61__block__62__block__84__rock_height = __rhs
                stack.append (__main__while__61__block__62__block__84__rock_height)
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Break out of __for__87
                break
                #---------------------------------------------------------
            # End of if
            #-------------------------------------------------------------
            #-------------------------------------------------------------
            # Update
            # Pre-Increment
            # RHS
            stack.append(__main__while__61__block__62__block__84__for__85__block__86__for__87__j)
            __rhs = stack.pop ()
            __main__while__61__block__62__block__84__for__85__block__86__for__87__j = __main__while__61__block__62__block__84__for__85__block__86__for__87__j + 1
            __res = __main__while__61__block__62__block__84__for__85__block__86__for__87__j
            stack.append (__res)
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # If-Statement
        # Precomputing all if/elif conditions and give unique names
        # bc we can't have code between if and elif
        # Condition
        # Not Equal
        # LHS
        stack.append(__main__while__61__block__62__block__84__rock_height)
        # RHS
        # Int Literal
        stack.append(0)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs != __rhs
        stack.append (__res)
        __if__91__cond = stack.pop ()
        # get condition from stack
        if (__if__91__cond):
            # Body
            # Break out of __for__85
            break
        # End of if
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # Update
        # Pre-Decrement
        # RHS
        stack.append(__main__while__61__block__62__block__84__for__85__i)
        __rhs = stack.pop ()
        __main__while__61__block__62__block__84__for__85__i = __main__while__61__block__62__block__84__for__85__i - 1
        __res = __main__while__61__block__62__block__84__for__85__i
        stack.append (__res)
    #---------------------------------------------------------------------
    # Statement
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(3)
    # LHS
    __main__while__61__block__62__block__84__shape_height = 0
    __rhs = stack.pop()
    __main__while__61__block__62__block__84__shape_height = __rhs
    stack.append (__main__while__61__block__62__block__84__shape_height)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Char Literal
    stack.append('1')
    # LHS
    __main__while__61__block__62__block__84__rock_char = 0
    __rhs = stack.pop()
    __main__while__61__block__62__block__84__rock_char = __rhs
    stack.append (__main__while__61__block__62__block__84__rock_char)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Addition
    # LHS
    # Addition
    # LHS
    stack.append(__main__while__61__block__62__block__84__rock_height)
    # RHS
    # Int Literal
    stack.append(3)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs + __rhs
    stack.append(__res)
    # RHS
    stack.append(__main__while__61__block__62__block__84__shape_height)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs + __rhs
    stack.append(__res)
    # LHS
    __main__while__61__block__62__block__84__desired_height = 0
    __rhs = stack.pop()
    __main__while__61__block__62__block__84__desired_height = __rhs
    stack.append (__main__while__61__block__62__block__84__desired_height)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
    # While-Loop
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        # Subtraction
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
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
        __res = __lhs - __rhs
        stack.append(__res)
        # RHS
        stack.append(__main__while__61__block__62__block__84__desired_height)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs < __rhs
        stack.append (__res)
        __cond = stack.pop ()
        # break out of loop if condition is false
        if (__cond == 0): break
        # Body
        # Statement
        # Method Call - Vector<:char[]:>::pushBack(char[]) -> void
        # LHS
        stack.append(__main__board)
        # RHS
        # Arguments
        # String Literal
        stack.append([*("|.......|"+'\0')])
        __arg0 = stack.pop ()
        __obj = stack.pop ()
        __retval = __method____main____Vector__char__1____pushBack__char__1 (__obj, __arg0)
        stack.append (__retval)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

    # End of While
    #---------------------------------------------------------------------
    # Statement
    # Function Call - printboard(Vector<:char[]:>) -> void
    # Arguments
    stack.append(__main__board)
    __arg0 = stack.pop ()
    # *** printboard
    __res = __main____printboard__Vector__tparam0__char (__arg0)
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Array Constructor
    # Elements
    # Int Literal
    stack.append(4)
    __elem0 = stack.pop ()
    __list = [0] * 1
    __list[0] = __elem0
    stack.append (__list)
    # LHS
    __main__while__61__block__62__block__84__posx0 = 0
    __rhs = stack.pop()
    __main__while__61__block__62__block__84__posx0 = __rhs
    stack.append (__main__while__61__block__62__block__84__posx0)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Array Constructor
    # Elements
    # Int Literal
    stack.append(3)
    # Int Literal
    stack.append(4)
    # Int Literal
    stack.append(5)
    __elem2 = stack.pop ()
    __elem1 = stack.pop ()
    __elem0 = stack.pop ()
    __list = [0] * 3
    __list[0] = __elem0
    __list[1] = __elem1
    __list[2] = __elem2
    stack.append (__list)
    # LHS
    __main__while__61__block__62__block__84__posx1 = 0
    __rhs = stack.pop()
    __main__while__61__block__62__block__84__posx1 = __rhs
    stack.append (__main__while__61__block__62__block__84__posx1)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Array Constructor
    # Elements
    # Int Literal
    stack.append(4)
    __elem0 = stack.pop ()
    __list = [0] * 1
    __list[0] = __elem0
    stack.append (__list)
    # LHS
    __main__while__61__block__62__block__84__posx2 = 0
    __rhs = stack.pop()
    __main__while__61__block__62__block__84__posx2 = __rhs
    stack.append (__main__while__61__block__62__block__84__posx2)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Addition
    # LHS
    # Addition
    # LHS
    stack.append(__main__while__61__block__62__block__84__rock_height)
    # RHS
    # Int Literal
    stack.append(3)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs + __rhs
    stack.append(__res)
    # RHS
    # Int Literal
    stack.append(1)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs + __rhs
    stack.append(__res)
    # LHS
    __main__while__61__block__62__block__84__posy = 0
    __rhs = stack.pop()
    __main__while__61__block__62__block__84__posy = __rhs
    stack.append (__main__while__61__block__62__block__84__posy)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main__while__61__block__62__block__84__rock_char)
    # LHS
    # Subscript assignment
    # LHS
    # Subscript
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main__board)
    # RHS
    stack.append (__field____main____Vector__char__1____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    stack.append(__main__while__61__block__62__block__84__posy)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    # OFFSET
    # Subscript
    # LHS
    stack.append(__main__while__61__block__62__block__84__posx0)
    # OFFSET
    # Int Literal
    stack.append(0)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    __offset = stack.pop()
    __pointer = stack.pop()
    __rhs = stack.pop()
    __pointer[__offset] = __rhs
    stack.append (__pointer[__offset])
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main__while__61__block__62__block__84__rock_char)
    # LHS
    # Subscript assignment
    # LHS
    # Subscript
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main__board)
    # RHS
    stack.append (__field____main____Vector__char__1____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    # Addition
    # LHS
    stack.append(__main__while__61__block__62__block__84__posy)
    # RHS
    # Int Literal
    stack.append(1)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs + __rhs
    stack.append(__res)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    # OFFSET
    # Subscript
    # LHS
    stack.append(__main__while__61__block__62__block__84__posx1)
    # OFFSET
    # Int Literal
    stack.append(0)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    __offset = stack.pop()
    __pointer = stack.pop()
    __rhs = stack.pop()
    __pointer[__offset] = __rhs
    stack.append (__pointer[__offset])
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main__while__61__block__62__block__84__rock_char)
    # LHS
    # Subscript assignment
    # LHS
    # Subscript
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main__board)
    # RHS
    stack.append (__field____main____Vector__char__1____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    # Addition
    # LHS
    stack.append(__main__while__61__block__62__block__84__posy)
    # RHS
    # Int Literal
    stack.append(1)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs + __rhs
    stack.append(__res)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    # OFFSET
    # Subscript
    # LHS
    stack.append(__main__while__61__block__62__block__84__posx1)
    # OFFSET
    # Int Literal
    stack.append(1)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    __offset = stack.pop()
    __pointer = stack.pop()
    __rhs = stack.pop()
    __pointer[__offset] = __rhs
    stack.append (__pointer[__offset])
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main__while__61__block__62__block__84__rock_char)
    # LHS
    # Subscript assignment
    # LHS
    # Subscript
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main__board)
    # RHS
    stack.append (__field____main____Vector__char__1____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    # Addition
    # LHS
    stack.append(__main__while__61__block__62__block__84__posy)
    # RHS
    # Int Literal
    stack.append(1)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs + __rhs
    stack.append(__res)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    # OFFSET
    # Subscript
    # LHS
    stack.append(__main__while__61__block__62__block__84__posx1)
    # OFFSET
    # Int Literal
    stack.append(2)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    __offset = stack.pop()
    __pointer = stack.pop()
    __rhs = stack.pop()
    __pointer[__offset] = __rhs
    stack.append (__pointer[__offset])
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main__while__61__block__62__block__84__rock_char)
    # LHS
    # Subscript assignment
    # LHS
    # Subscript
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main__board)
    # RHS
    stack.append (__field____main____Vector__char__1____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    # Addition
    # LHS
    stack.append(__main__while__61__block__62__block__84__posy)
    # RHS
    # Int Literal
    stack.append(2)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs + __rhs
    stack.append(__res)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    # OFFSET
    # Subscript
    # LHS
    stack.append(__main__while__61__block__62__block__84__posx2)
    # OFFSET
    # Int Literal
    stack.append(0)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    __offset = stack.pop()
    __pointer = stack.pop()
    __rhs = stack.pop()
    __pointer[__offset] = __rhs
    stack.append (__pointer[__offset])
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Function Call - printboard(Vector<:char[]:>) -> void
    # Arguments
    stack.append(__main__board)
    __arg0 = stack.pop ()
    # *** printboard
    __res = __main____printboard__Vector__tparam0__char (__arg0)
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
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
        #-----------------------------------------------------------------
        # Code Block
        # Statement
        # Function Call - println(int) -> void
        # Arguments
        stack.append(__main__shift_index)
        __arg0 = stack.pop ()
        # *** println
        __res = __builtin__println__int (__arg0)
        stack.append (__res) # function call result
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Char Literal
        stack.append('.')
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__84__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__84__posx0)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Char Literal
        stack.append('.')
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__while__61__block__62__block__84__posy)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__84__posx1)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Char Literal
        stack.append('.')
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__while__61__block__62__block__84__posy)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__84__posx1)
        # OFFSET
        # Int Literal
        stack.append(1)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Char Literal
        stack.append('.')
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__while__61__block__62__block__84__posy)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__84__posx1)
        # OFFSET
        # Int Literal
        stack.append(2)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Char Literal
        stack.append('.')
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__while__61__block__62__block__84__posy)
        # RHS
        # Int Literal
        stack.append(2)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__84__posx2)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
        # If-Statement
        # Precomputing all if/elif conditions and give unique names
        # bc we can't have code between if and elif
        # Condition
        # Equal
        # LHS
        # Subscript
        # LHS
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
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        stack.append(__main__shift_index)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        # Char Literal
        stack.append('<')
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs == __rhs
        stack.append (__res)
        __if__95__cond = stack.pop ()
        # get condition from stack
        if (__if__95__cond):
            # Body
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Function Call - println(char[]) -> void
            # Arguments
            # String Literal
            stack.append([*("shift left"+'\0')])
            __arg0 = stack.pop ()
            # *** println
            __res = __builtin__println__char__1 (__arg0)
            stack.append (__res) # function call result
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            #-------------------------------------------------------------
            # If-Statement
            # Precomputing all if/elif conditions and give unique names
            # bc we can't have code between if and elif
            # Condition
            # AND
            # LHS
            # AND
            # LHS
            # Equal
            # LHS
            # Subscript
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__board)
            # RHS
            stack.append (__field____main____Vector__char__1____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main__while__61__block__62__block__84__posy)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # OFFSET
            # Subtraction
            # LHS
            # Subscript
            # LHS
            stack.append(__main__while__61__block__62__block__84__posx0)
            # OFFSET
            # Int Literal
            stack.append(0)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            # Int Literal
            stack.append(1)
            __rhs = stack.pop()
            __lhs = stack.pop()
            __res = __lhs - __rhs
            stack.append(__res)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            # Char Literal
            stack.append('.')
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs == __rhs
            stack.append (__res)
            # Only check rhs if lhs was true
            __lhs = stack[-1]
            if (__lhs):
                # RHS
                # Equal
                # LHS
                # Subscript
                # LHS
                # Subscript
                # LHS
                # Member Accessor
                # LHS
                stack.append(__main__board)
                # RHS
                stack.append (__field____main____Vector__char__1____data)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                # OFFSET
                # Addition
                # LHS
                stack.append(__main__while__61__block__62__block__84__posy)
                # RHS
                # Int Literal
                stack.append(1)
                __rhs = stack.pop()
                __lhs = stack.pop()
                __res = __lhs + __rhs
                stack.append(__res)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # OFFSET
                # Subtraction
                # LHS
                # Subscript
                # LHS
                stack.append(__main__while__61__block__62__block__84__posx1)
                # OFFSET
                # Int Literal
                stack.append(0)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # RHS
                # Int Literal
                stack.append(1)
                __rhs = stack.pop()
                __lhs = stack.pop()
                __res = __lhs - __rhs
                stack.append(__res)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # RHS
                # Char Literal
                stack.append('.')
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs == __rhs
                stack.append (__res)
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs and __rhs
            else:
                __res = stack.pop ()
            stack.append (__res)
            # Only check rhs if lhs was true
            __lhs = stack[-1]
            if (__lhs):
                # RHS
                # Equal
                # LHS
                # Subscript
                # LHS
                # Subscript
                # LHS
                # Member Accessor
                # LHS
                stack.append(__main__board)
                # RHS
                stack.append (__field____main____Vector__char__1____data)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                # OFFSET
                # Addition
                # LHS
                stack.append(__main__while__61__block__62__block__84__posy)
                # RHS
                # Int Literal
                stack.append(2)
                __rhs = stack.pop()
                __lhs = stack.pop()
                __res = __lhs + __rhs
                stack.append(__res)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # OFFSET
                # Subtraction
                # LHS
                # Subscript
                # LHS
                stack.append(__main__while__61__block__62__block__84__posx2)
                # OFFSET
                # Int Literal
                stack.append(0)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # RHS
                # Int Literal
                stack.append(1)
                __rhs = stack.pop()
                __lhs = stack.pop()
                __res = __lhs - __rhs
                stack.append(__res)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # RHS
                # Char Literal
                stack.append('.')
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs == __rhs
                stack.append (__res)
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs and __rhs
            else:
                __res = stack.pop ()
            stack.append (__res)
            __if__97__cond = stack.pop ()
            # get condition from stack
            if (__if__97__cond):
                # Body
                #---------------------------------------------------------
                # Code Block
                # Statement
                # Assignment - '-='
                # RHS
                # Int Literal
                stack.append(1)
                # LHS
                # Subscript assignment
                # LHS
                stack.append(__main__while__61__block__62__block__84__posx0)
                # OFFSET
                # Int Literal
                stack.append(0)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __pointer[__offset] - __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Statement
                # Assignment - '-='
                # RHS
                # Int Literal
                stack.append(1)
                # LHS
                # Subscript assignment
                # LHS
                stack.append(__main__while__61__block__62__block__84__posx1)
                # OFFSET
                # Int Literal
                stack.append(0)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __pointer[__offset] - __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Statement
                # Assignment - '-='
                # RHS
                # Int Literal
                stack.append(1)
                # LHS
                # Subscript assignment
                # LHS
                stack.append(__main__while__61__block__62__block__84__posx1)
                # OFFSET
                # Int Literal
                stack.append(1)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __pointer[__offset] - __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Statement
                # Assignment - '-='
                # RHS
                # Int Literal
                stack.append(1)
                # LHS
                # Subscript assignment
                # LHS
                stack.append(__main__while__61__block__62__block__84__posx1)
                # OFFSET
                # Int Literal
                stack.append(2)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __pointer[__offset] - __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Statement
                # Assignment - '-='
                # RHS
                # Int Literal
                stack.append(1)
                # LHS
                # Subscript assignment
                # LHS
                stack.append(__main__while__61__block__62__block__84__posx2)
                # OFFSET
                # Int Literal
                stack.append(0)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __pointer[__offset] - __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                #---------------------------------------------------------
            # End of if
            #-------------------------------------------------------------
            #-------------------------------------------------------------
        #-----------------------------------------------------------------
        # Else-Statement
        else:
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Function Call - println(char[]) -> void
            # Arguments
            # String Literal
            stack.append([*("shift right"+'\0')])
            __arg0 = stack.pop ()
            # *** println
            __res = __builtin__println__char__1 (__arg0)
            stack.append (__res) # function call result
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            #-------------------------------------------------------------
            # If-Statement
            # Precomputing all if/elif conditions and give unique names
            # bc we can't have code between if and elif
            # Condition
            # AND
            # LHS
            # AND
            # LHS
            # Equal
            # LHS
            # Subscript
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__board)
            # RHS
            stack.append (__field____main____Vector__char__1____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main__while__61__block__62__block__84__posy)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # OFFSET
            # Addition
            # LHS
            # Subscript
            # LHS
            stack.append(__main__while__61__block__62__block__84__posx0)
            # OFFSET
            # Int Literal
            stack.append(0)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            # Int Literal
            stack.append(1)
            __rhs = stack.pop()
            __lhs = stack.pop()
            __res = __lhs + __rhs
            stack.append(__res)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            # Char Literal
            stack.append('.')
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs == __rhs
            stack.append (__res)
            # Only check rhs if lhs was true
            __lhs = stack[-1]
            if (__lhs):
                # RHS
                # Equal
                # LHS
                # Subscript
                # LHS
                # Subscript
                # LHS
                # Member Accessor
                # LHS
                stack.append(__main__board)
                # RHS
                stack.append (__field____main____Vector__char__1____data)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                # OFFSET
                # Addition
                # LHS
                stack.append(__main__while__61__block__62__block__84__posy)
                # RHS
                # Int Literal
                stack.append(1)
                __rhs = stack.pop()
                __lhs = stack.pop()
                __res = __lhs + __rhs
                stack.append(__res)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # OFFSET
                # Addition
                # LHS
                # Subscript
                # LHS
                stack.append(__main__while__61__block__62__block__84__posx1)
                # OFFSET
                # Int Literal
                stack.append(2)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # RHS
                # Int Literal
                stack.append(1)
                __rhs = stack.pop()
                __lhs = stack.pop()
                __res = __lhs + __rhs
                stack.append(__res)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # RHS
                # Char Literal
                stack.append('.')
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs == __rhs
                stack.append (__res)
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs and __rhs
            else:
                __res = stack.pop ()
            stack.append (__res)
            # Only check rhs if lhs was true
            __lhs = stack[-1]
            if (__lhs):
                # RHS
                # Equal
                # LHS
                # Subscript
                # LHS
                # Subscript
                # LHS
                # Member Accessor
                # LHS
                stack.append(__main__board)
                # RHS
                stack.append (__field____main____Vector__char__1____data)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                # OFFSET
                # Addition
                # LHS
                stack.append(__main__while__61__block__62__block__84__posy)
                # RHS
                # Int Literal
                stack.append(2)
                __rhs = stack.pop()
                __lhs = stack.pop()
                __res = __lhs + __rhs
                stack.append(__res)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # OFFSET
                # Addition
                # LHS
                # Subscript
                # LHS
                stack.append(__main__while__61__block__62__block__84__posx2)
                # OFFSET
                # Int Literal
                stack.append(0)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # RHS
                # Int Literal
                stack.append(1)
                __rhs = stack.pop()
                __lhs = stack.pop()
                __res = __lhs + __rhs
                stack.append(__res)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # RHS
                # Char Literal
                stack.append('.')
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs == __rhs
                stack.append (__res)
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs and __rhs
            else:
                __res = stack.pop ()
            stack.append (__res)
            __if__100__cond = stack.pop ()
            # get condition from stack
            if (__if__100__cond):
                # Body
                #---------------------------------------------------------
                # Code Block
                # Statement
                # Assignment - '+='
                # RHS
                # Int Literal
                stack.append(1)
                # LHS
                # Subscript assignment
                # LHS
                stack.append(__main__while__61__block__62__block__84__posx0)
                # OFFSET
                # Int Literal
                stack.append(0)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __pointer[__offset] + __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Statement
                # Assignment - '+='
                # RHS
                # Int Literal
                stack.append(1)
                # LHS
                # Subscript assignment
                # LHS
                stack.append(__main__while__61__block__62__block__84__posx1)
                # OFFSET
                # Int Literal
                stack.append(0)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __pointer[__offset] + __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Statement
                # Assignment - '+='
                # RHS
                # Int Literal
                stack.append(1)
                # LHS
                # Subscript assignment
                # LHS
                stack.append(__main__while__61__block__62__block__84__posx1)
                # OFFSET
                # Int Literal
                stack.append(1)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __pointer[__offset] + __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Statement
                # Assignment - '+='
                # RHS
                # Int Literal
                stack.append(1)
                # LHS
                # Subscript assignment
                # LHS
                stack.append(__main__while__61__block__62__block__84__posx1)
                # OFFSET
                # Int Literal
                stack.append(2)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __pointer[__offset] + __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Statement
                # Assignment - '+='
                # RHS
                # Int Literal
                stack.append(1)
                # LHS
                # Subscript assignment
                # LHS
                stack.append(__main__while__61__block__62__block__84__posx2)
                # OFFSET
                # Int Literal
                stack.append(0)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __pointer[__offset] + __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                #---------------------------------------------------------
            # End of if
            #-------------------------------------------------------------
            #-------------------------------------------------------------
        #-----------------------------------------------------------------
        # End of if
        #-----------------------------------------------------------------
        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main__while__61__block__62__block__84__rock_char)
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__84__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__84__posx0)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main__while__61__block__62__block__84__rock_char)
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__while__61__block__62__block__84__posy)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__84__posx1)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main__while__61__block__62__block__84__rock_char)
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__while__61__block__62__block__84__posy)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__84__posx1)
        # OFFSET
        # Int Literal
        stack.append(1)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main__while__61__block__62__block__84__rock_char)
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__while__61__block__62__block__84__posy)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__84__posx1)
        # OFFSET
        # Int Literal
        stack.append(2)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main__while__61__block__62__block__84__rock_char)
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__while__61__block__62__block__84__posy)
        # RHS
        # Int Literal
        stack.append(2)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__84__posx2)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Modulus
        # LHS
        # Addition
        # LHS
        stack.append(__main__shift_index)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        # RHS
        stack.append(__main__shift_max)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs % __rhs
        stack.append(__res)
        __rhs = stack.pop()
        __main__shift_index = __rhs
        stack.append (__main__shift_index)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Function Call - printboard(Vector<:char[]:>) -> void
        # Arguments
        stack.append(__main__board)
        __arg0 = stack.pop ()
        # *** printboard
        __res = __main____printboard__Vector__tparam0__char (__arg0)
        stack.append (__res) # function call result
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
        # If-Statement
        # Precomputing all if/elif conditions and give unique names
        # bc we can't have code between if and elif
        # Condition
        # OR
        # LHS
        # OR
        # LHS
        # OR
        # LHS
        # Not Equal
        # LHS
        # Subscript
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__84__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subtraction
        # LHS
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__84__posx0)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs - __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        # Char Literal
        stack.append('.')
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs != __rhs
        stack.append (__res)
        # RHS
        # Not Equal
        # LHS
        # Subscript
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Subtraction
        # LHS
        stack.append(__main__while__61__block__62__block__84__posy)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs - __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__84__posx0)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        # Char Literal
        stack.append('.')
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs != __rhs
        stack.append (__res)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs or __rhs
        stack.append (__res)
        # RHS
        # Not Equal
        # LHS
        # Subscript
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__84__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Addition
        # LHS
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__84__posx0)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        # Char Literal
        stack.append('.')
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs != __rhs
        stack.append (__res)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs or __rhs
        stack.append (__res)
        # RHS
        # Equal
        # LHS
        # Subtraction
        # LHS
        stack.append(__main__while__61__block__62__block__84__posy)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs - __rhs
        stack.append(__res)
        # RHS
        # Int Literal
        stack.append(0)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs == __rhs
        stack.append (__res)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs or __rhs
        stack.append (__res)
        __if__102__cond = stack.pop ()
        # get condition from stack
        if (__if__102__cond):
            # Body
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Function Call - println(char[]) -> void
            # Arguments
            # String Literal
            stack.append([*("rock at rest"+'\0')])
            __arg0 = stack.pop ()
            # *** println
            __res = __builtin__println__char__1 (__arg0)
            stack.append (__res) # function call result
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            # Break out of __while__93
            break
            #-------------------------------------------------------------
        # End of if
        #-----------------------------------------------------------------
        # Statement
        # Assignment - '='
        # RHS
        # Char Literal
        stack.append('.')
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__84__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__84__posx0)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Char Literal
        stack.append('.')
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__while__61__block__62__block__84__posy)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__84__posx1)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Char Literal
        stack.append('.')
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__while__61__block__62__block__84__posy)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__84__posx1)
        # OFFSET
        # Int Literal
        stack.append(1)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Char Literal
        stack.append('.')
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__while__61__block__62__block__84__posy)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__84__posx1)
        # OFFSET
        # Int Literal
        stack.append(2)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Char Literal
        stack.append('.')
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__while__61__block__62__block__84__posy)
        # RHS
        # Int Literal
        stack.append(2)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__84__posx2)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '-='
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __main__while__61__block__62__block__84__posy = __main__while__61__block__62__block__84__posy - __rhs
        stack.append (__main__while__61__block__62__block__84__posy)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main__while__61__block__62__block__84__rock_char)
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__84__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__84__posx0)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main__while__61__block__62__block__84__rock_char)
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__while__61__block__62__block__84__posy)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__84__posx1)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main__while__61__block__62__block__84__rock_char)
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__while__61__block__62__block__84__posy)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__84__posx1)
        # OFFSET
        # Int Literal
        stack.append(1)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main__while__61__block__62__block__84__rock_char)
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__while__61__block__62__block__84__posy)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__84__posx1)
        # OFFSET
        # Int Literal
        stack.append(2)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main__while__61__block__62__block__84__rock_char)
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__while__61__block__62__block__84__posy)
        # RHS
        # Int Literal
        stack.append(2)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__84__posx2)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Function Call - printboard(Vector<:char[]:>) -> void
        # Arguments
        stack.append(__main__board)
        __arg0 = stack.pop ()
        # *** printboard
        __res = __main____printboard__Vector__tparam0__char (__arg0)
        stack.append (__res) # function call result
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
    # End of While
    #---------------------------------------------------------------------
    # Statement
    # Function Call - printboard(Vector<:char[]:>) -> void
    # Arguments
    stack.append(__main__board)
    __arg0 = stack.pop ()
    # *** printboard
    __res = __main____printboard__Vector__tparam0__char (__arg0)
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
    # Statement
    # Assignment - '+='
    # RHS
    # Int Literal
    stack.append(1)
    __rhs = stack.pop()
    __main__num_rocks = __main__num_rocks + __rhs
    stack.append (__main__num_rocks)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
    # If-Statement
    # Precomputing all if/elif conditions and give unique names
    # bc we can't have code between if and elif
    # Condition
    # Greater Than or Equal to
    # LHS
    stack.append(__main__num_rocks)
    # RHS
    stack.append(__main__max_rocks)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs >= __rhs
    stack.append (__res)
    __if__104__cond = stack.pop ()
    # get condition from stack
    if (__if__104__cond):
        # Body
        # Break out of __while__61
        break
    # End of if
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(0)
    # LHS
    __main__while__61__block__62__block__105__rock_height = 0
    __rhs = stack.pop()
    __main__while__61__block__62__block__105__rock_height = __rhs
    stack.append (__main__while__61__block__62__block__105__rock_height)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
    # For-Loop
    # Init
    # Assignment - '='
    # RHS
    # Subtraction
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main__board)
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
    __res = __lhs - __rhs
    stack.append(__res)
    # LHS
    __main__while__61__block__62__block__105__for__106__i = 0
    __rhs = stack.pop()
    __main__while__61__block__62__block__105__for__106__i = __rhs
    stack.append (__main__while__61__block__62__block__105__for__106__i)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Greater Than or Equal to
        # LHS
        stack.append(__main__while__61__block__62__block__105__for__106__i)
        # RHS
        # Int Literal
        stack.append(0)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs >= __rhs
        stack.append (__res)
        __cond = stack.pop ()
        # break out of loop if condition is false
        if (__cond == 0): break
        # Body
        #-----------------------------------------------------------------
        # Code Block
        #-----------------------------------------------------------------
        # For-Loop
        # Init
        # Assignment - '='
        # RHS
        # Int Literal
        stack.append(1)
        # LHS
        __main__while__61__block__62__block__105__for__106__block__107__for__108__j = 0
        __rhs = stack.pop()
        __main__while__61__block__62__block__105__for__106__block__107__for__108__j = __rhs
        stack.append (__main__while__61__block__62__block__105__for__106__block__107__for__108__j)
        # Using an infinite loop so we can write a separate multi-line condition
        while (1):
            # Condition
            # Less Than
            # LHS
            stack.append(__main__while__61__block__62__block__105__for__106__block__107__for__108__j)
            # RHS
            # Int Literal
            stack.append(8)
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
            #-------------------------------------------------------------
            # If-Statement
            # Precomputing all if/elif conditions and give unique names
            # bc we can't have code between if and elif
            # Condition
            # Not Equal
            # LHS
            # Subscript
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__board)
            # RHS
            stack.append (__field____main____Vector__char__1____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main__while__61__block__62__block__105__for__106__i)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # OFFSET
            stack.append(__main__while__61__block__62__block__105__for__106__block__107__for__108__j)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            # Char Literal
            stack.append('.')
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs != __rhs
            stack.append (__res)
            __if__110__cond = stack.pop ()
            # get condition from stack
            if (__if__110__cond):
                # Body
                #---------------------------------------------------------
                # Code Block
                # Statement
                # Assignment - '='
                # RHS
                stack.append(__main__while__61__block__62__block__105__for__106__i)
                __rhs = stack.pop()
                __main__while__61__block__62__block__105__rock_height = __rhs
                stack.append (__main__while__61__block__62__block__105__rock_height)
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Break out of __for__108
                break
                #---------------------------------------------------------
            # End of if
            #-------------------------------------------------------------
            #-------------------------------------------------------------
            # Update
            # Pre-Increment
            # RHS
            stack.append(__main__while__61__block__62__block__105__for__106__block__107__for__108__j)
            __rhs = stack.pop ()
            __main__while__61__block__62__block__105__for__106__block__107__for__108__j = __main__while__61__block__62__block__105__for__106__block__107__for__108__j + 1
            __res = __main__while__61__block__62__block__105__for__106__block__107__for__108__j
            stack.append (__res)
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # If-Statement
        # Precomputing all if/elif conditions and give unique names
        # bc we can't have code between if and elif
        # Condition
        # Not Equal
        # LHS
        stack.append(__main__while__61__block__62__block__105__rock_height)
        # RHS
        # Int Literal
        stack.append(0)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs != __rhs
        stack.append (__res)
        __if__112__cond = stack.pop ()
        # get condition from stack
        if (__if__112__cond):
            # Body
            # Break out of __for__106
            break
        # End of if
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # Update
        # Pre-Decrement
        # RHS
        stack.append(__main__while__61__block__62__block__105__for__106__i)
        __rhs = stack.pop ()
        __main__while__61__block__62__block__105__for__106__i = __main__while__61__block__62__block__105__for__106__i - 1
        __res = __main__while__61__block__62__block__105__for__106__i
        stack.append (__res)
    #---------------------------------------------------------------------
    # Statement
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(3)
    # LHS
    __main__while__61__block__62__block__105__shape_height = 0
    __rhs = stack.pop()
    __main__while__61__block__62__block__105__shape_height = __rhs
    stack.append (__main__while__61__block__62__block__105__shape_height)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Char Literal
    stack.append('2')
    # LHS
    __main__while__61__block__62__block__105__rock_char = 0
    __rhs = stack.pop()
    __main__while__61__block__62__block__105__rock_char = __rhs
    stack.append (__main__while__61__block__62__block__105__rock_char)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Addition
    # LHS
    # Addition
    # LHS
    stack.append(__main__while__61__block__62__block__105__rock_height)
    # RHS
    # Int Literal
    stack.append(3)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs + __rhs
    stack.append(__res)
    # RHS
    stack.append(__main__while__61__block__62__block__105__shape_height)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs + __rhs
    stack.append(__res)
    # LHS
    __main__while__61__block__62__block__105__desired_height = 0
    __rhs = stack.pop()
    __main__while__61__block__62__block__105__desired_height = __rhs
    stack.append (__main__while__61__block__62__block__105__desired_height)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
    # While-Loop
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        # Subtraction
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
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
        __res = __lhs - __rhs
        stack.append(__res)
        # RHS
        stack.append(__main__while__61__block__62__block__105__desired_height)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs < __rhs
        stack.append (__res)
        __cond = stack.pop ()
        # break out of loop if condition is false
        if (__cond == 0): break
        # Body
        # Statement
        # Method Call - Vector<:char[]:>::pushBack(char[]) -> void
        # LHS
        stack.append(__main__board)
        # RHS
        # Arguments
        # String Literal
        stack.append([*("|.......|"+'\0')])
        __arg0 = stack.pop ()
        __obj = stack.pop ()
        __retval = __method____main____Vector__char__1____pushBack__char__1 (__obj, __arg0)
        stack.append (__retval)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

    # End of While
    #---------------------------------------------------------------------
    # Statement
    # Function Call - printboard(Vector<:char[]:>) -> void
    # Arguments
    stack.append(__main__board)
    __arg0 = stack.pop ()
    # *** printboard
    __res = __main____printboard__Vector__tparam0__char (__arg0)
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Array Constructor
    # Elements
    # Int Literal
    stack.append(3)
    # Int Literal
    stack.append(4)
    # Int Literal
    stack.append(5)
    __elem2 = stack.pop ()
    __elem1 = stack.pop ()
    __elem0 = stack.pop ()
    __list = [0] * 3
    __list[0] = __elem0
    __list[1] = __elem1
    __list[2] = __elem2
    stack.append (__list)
    # LHS
    __main__while__61__block__62__block__105__posx0 = 0
    __rhs = stack.pop()
    __main__while__61__block__62__block__105__posx0 = __rhs
    stack.append (__main__while__61__block__62__block__105__posx0)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Array Constructor
    # Elements
    # Int Literal
    stack.append(5)
    __elem0 = stack.pop ()
    __list = [0] * 1
    __list[0] = __elem0
    stack.append (__list)
    # LHS
    __main__while__61__block__62__block__105__posx1 = 0
    __rhs = stack.pop()
    __main__while__61__block__62__block__105__posx1 = __rhs
    stack.append (__main__while__61__block__62__block__105__posx1)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Array Constructor
    # Elements
    # Int Literal
    stack.append(5)
    __elem0 = stack.pop ()
    __list = [0] * 1
    __list[0] = __elem0
    stack.append (__list)
    # LHS
    __main__while__61__block__62__block__105__posx2 = 0
    __rhs = stack.pop()
    __main__while__61__block__62__block__105__posx2 = __rhs
    stack.append (__main__while__61__block__62__block__105__posx2)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Addition
    # LHS
    # Addition
    # LHS
    stack.append(__main__while__61__block__62__block__105__rock_height)
    # RHS
    # Int Literal
    stack.append(3)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs + __rhs
    stack.append(__res)
    # RHS
    # Int Literal
    stack.append(1)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs + __rhs
    stack.append(__res)
    # LHS
    __main__while__61__block__62__block__105__posy = 0
    __rhs = stack.pop()
    __main__while__61__block__62__block__105__posy = __rhs
    stack.append (__main__while__61__block__62__block__105__posy)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main__while__61__block__62__block__105__rock_char)
    # LHS
    # Subscript assignment
    # LHS
    # Subscript
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main__board)
    # RHS
    stack.append (__field____main____Vector__char__1____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    stack.append(__main__while__61__block__62__block__105__posy)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    # OFFSET
    # Subscript
    # LHS
    stack.append(__main__while__61__block__62__block__105__posx0)
    # OFFSET
    # Int Literal
    stack.append(0)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    __offset = stack.pop()
    __pointer = stack.pop()
    __rhs = stack.pop()
    __pointer[__offset] = __rhs
    stack.append (__pointer[__offset])
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main__while__61__block__62__block__105__rock_char)
    # LHS
    # Subscript assignment
    # LHS
    # Subscript
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main__board)
    # RHS
    stack.append (__field____main____Vector__char__1____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    stack.append(__main__while__61__block__62__block__105__posy)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    # OFFSET
    # Subscript
    # LHS
    stack.append(__main__while__61__block__62__block__105__posx0)
    # OFFSET
    # Int Literal
    stack.append(1)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    __offset = stack.pop()
    __pointer = stack.pop()
    __rhs = stack.pop()
    __pointer[__offset] = __rhs
    stack.append (__pointer[__offset])
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main__while__61__block__62__block__105__rock_char)
    # LHS
    # Subscript assignment
    # LHS
    # Subscript
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main__board)
    # RHS
    stack.append (__field____main____Vector__char__1____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    stack.append(__main__while__61__block__62__block__105__posy)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    # OFFSET
    # Subscript
    # LHS
    stack.append(__main__while__61__block__62__block__105__posx0)
    # OFFSET
    # Int Literal
    stack.append(2)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    __offset = stack.pop()
    __pointer = stack.pop()
    __rhs = stack.pop()
    __pointer[__offset] = __rhs
    stack.append (__pointer[__offset])
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main__while__61__block__62__block__105__rock_char)
    # LHS
    # Subscript assignment
    # LHS
    # Subscript
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main__board)
    # RHS
    stack.append (__field____main____Vector__char__1____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    # Addition
    # LHS
    stack.append(__main__while__61__block__62__block__105__posy)
    # RHS
    # Int Literal
    stack.append(1)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs + __rhs
    stack.append(__res)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    # OFFSET
    # Subscript
    # LHS
    stack.append(__main__while__61__block__62__block__105__posx1)
    # OFFSET
    # Int Literal
    stack.append(0)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    __offset = stack.pop()
    __pointer = stack.pop()
    __rhs = stack.pop()
    __pointer[__offset] = __rhs
    stack.append (__pointer[__offset])
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main__while__61__block__62__block__105__rock_char)
    # LHS
    # Subscript assignment
    # LHS
    # Subscript
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main__board)
    # RHS
    stack.append (__field____main____Vector__char__1____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    # Addition
    # LHS
    stack.append(__main__while__61__block__62__block__105__posy)
    # RHS
    # Int Literal
    stack.append(2)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs + __rhs
    stack.append(__res)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    # OFFSET
    # Subscript
    # LHS
    stack.append(__main__while__61__block__62__block__105__posx2)
    # OFFSET
    # Int Literal
    stack.append(0)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    __offset = stack.pop()
    __pointer = stack.pop()
    __rhs = stack.pop()
    __pointer[__offset] = __rhs
    stack.append (__pointer[__offset])
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Function Call - printboard(Vector<:char[]:>) -> void
    # Arguments
    stack.append(__main__board)
    __arg0 = stack.pop ()
    # *** printboard
    __res = __main____printboard__Vector__tparam0__char (__arg0)
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
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
        #-----------------------------------------------------------------
        # Code Block
        # Statement
        # Function Call - println(int) -> void
        # Arguments
        stack.append(__main__shift_index)
        __arg0 = stack.pop ()
        # *** println
        __res = __builtin__println__int (__arg0)
        stack.append (__res) # function call result
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Char Literal
        stack.append('.')
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__105__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__105__posx0)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Char Literal
        stack.append('.')
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__105__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__105__posx0)
        # OFFSET
        # Int Literal
        stack.append(1)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Char Literal
        stack.append('.')
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__105__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__105__posx0)
        # OFFSET
        # Int Literal
        stack.append(2)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Char Literal
        stack.append('.')
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__while__61__block__62__block__105__posy)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__105__posx1)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Char Literal
        stack.append('.')
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__while__61__block__62__block__105__posy)
        # RHS
        # Int Literal
        stack.append(2)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__105__posx2)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
        # If-Statement
        # Precomputing all if/elif conditions and give unique names
        # bc we can't have code between if and elif
        # Condition
        # Equal
        # LHS
        # Subscript
        # LHS
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
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        stack.append(__main__shift_index)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        # Char Literal
        stack.append('<')
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs == __rhs
        stack.append (__res)
        __if__116__cond = stack.pop ()
        # get condition from stack
        if (__if__116__cond):
            # Body
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Function Call - println(char[]) -> void
            # Arguments
            # String Literal
            stack.append([*("shift left"+'\0')])
            __arg0 = stack.pop ()
            # *** println
            __res = __builtin__println__char__1 (__arg0)
            stack.append (__res) # function call result
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            #-------------------------------------------------------------
            # If-Statement
            # Precomputing all if/elif conditions and give unique names
            # bc we can't have code between if and elif
            # Condition
            # AND
            # LHS
            # AND
            # LHS
            # Equal
            # LHS
            # Subscript
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__board)
            # RHS
            stack.append (__field____main____Vector__char__1____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main__while__61__block__62__block__105__posy)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # OFFSET
            # Subtraction
            # LHS
            # Subscript
            # LHS
            stack.append(__main__while__61__block__62__block__105__posx0)
            # OFFSET
            # Int Literal
            stack.append(0)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            # Int Literal
            stack.append(1)
            __rhs = stack.pop()
            __lhs = stack.pop()
            __res = __lhs - __rhs
            stack.append(__res)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            # Char Literal
            stack.append('.')
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs == __rhs
            stack.append (__res)
            # Only check rhs if lhs was true
            __lhs = stack[-1]
            if (__lhs):
                # RHS
                # Equal
                # LHS
                # Subscript
                # LHS
                # Subscript
                # LHS
                # Member Accessor
                # LHS
                stack.append(__main__board)
                # RHS
                stack.append (__field____main____Vector__char__1____data)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                # OFFSET
                # Addition
                # LHS
                stack.append(__main__while__61__block__62__block__105__posy)
                # RHS
                # Int Literal
                stack.append(1)
                __rhs = stack.pop()
                __lhs = stack.pop()
                __res = __lhs + __rhs
                stack.append(__res)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # OFFSET
                # Subtraction
                # LHS
                # Subscript
                # LHS
                stack.append(__main__while__61__block__62__block__105__posx1)
                # OFFSET
                # Int Literal
                stack.append(0)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # RHS
                # Int Literal
                stack.append(1)
                __rhs = stack.pop()
                __lhs = stack.pop()
                __res = __lhs - __rhs
                stack.append(__res)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # RHS
                # Char Literal
                stack.append('.')
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs == __rhs
                stack.append (__res)
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs and __rhs
            else:
                __res = stack.pop ()
            stack.append (__res)
            # Only check rhs if lhs was true
            __lhs = stack[-1]
            if (__lhs):
                # RHS
                # Equal
                # LHS
                # Subscript
                # LHS
                # Subscript
                # LHS
                # Member Accessor
                # LHS
                stack.append(__main__board)
                # RHS
                stack.append (__field____main____Vector__char__1____data)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                # OFFSET
                # Addition
                # LHS
                stack.append(__main__while__61__block__62__block__105__posy)
                # RHS
                # Int Literal
                stack.append(2)
                __rhs = stack.pop()
                __lhs = stack.pop()
                __res = __lhs + __rhs
                stack.append(__res)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # OFFSET
                # Subtraction
                # LHS
                # Subscript
                # LHS
                stack.append(__main__while__61__block__62__block__105__posx2)
                # OFFSET
                # Int Literal
                stack.append(0)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # RHS
                # Int Literal
                stack.append(1)
                __rhs = stack.pop()
                __lhs = stack.pop()
                __res = __lhs - __rhs
                stack.append(__res)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # RHS
                # Char Literal
                stack.append('.')
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs == __rhs
                stack.append (__res)
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs and __rhs
            else:
                __res = stack.pop ()
            stack.append (__res)
            __if__118__cond = stack.pop ()
            # get condition from stack
            if (__if__118__cond):
                # Body
                #---------------------------------------------------------
                # Code Block
                # Statement
                # Assignment - '-='
                # RHS
                # Int Literal
                stack.append(1)
                # LHS
                # Subscript assignment
                # LHS
                stack.append(__main__while__61__block__62__block__105__posx0)
                # OFFSET
                # Int Literal
                stack.append(0)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __pointer[__offset] - __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Statement
                # Assignment - '-='
                # RHS
                # Int Literal
                stack.append(1)
                # LHS
                # Subscript assignment
                # LHS
                stack.append(__main__while__61__block__62__block__105__posx0)
                # OFFSET
                # Int Literal
                stack.append(1)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __pointer[__offset] - __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Statement
                # Assignment - '-='
                # RHS
                # Int Literal
                stack.append(1)
                # LHS
                # Subscript assignment
                # LHS
                stack.append(__main__while__61__block__62__block__105__posx0)
                # OFFSET
                # Int Literal
                stack.append(2)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __pointer[__offset] - __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Statement
                # Assignment - '-='
                # RHS
                # Int Literal
                stack.append(1)
                # LHS
                # Subscript assignment
                # LHS
                stack.append(__main__while__61__block__62__block__105__posx1)
                # OFFSET
                # Int Literal
                stack.append(0)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __pointer[__offset] - __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Statement
                # Assignment - '-='
                # RHS
                # Int Literal
                stack.append(1)
                # LHS
                # Subscript assignment
                # LHS
                stack.append(__main__while__61__block__62__block__105__posx2)
                # OFFSET
                # Int Literal
                stack.append(0)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __pointer[__offset] - __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                #---------------------------------------------------------
            # End of if
            #-------------------------------------------------------------
            #-------------------------------------------------------------
        #-----------------------------------------------------------------
        # Else-Statement
        else:
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Function Call - println(char[]) -> void
            # Arguments
            # String Literal
            stack.append([*("shift right"+'\0')])
            __arg0 = stack.pop ()
            # *** println
            __res = __builtin__println__char__1 (__arg0)
            stack.append (__res) # function call result
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            #-------------------------------------------------------------
            # If-Statement
            # Precomputing all if/elif conditions and give unique names
            # bc we can't have code between if and elif
            # Condition
            # AND
            # LHS
            # AND
            # LHS
            # Equal
            # LHS
            # Subscript
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__board)
            # RHS
            stack.append (__field____main____Vector__char__1____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main__while__61__block__62__block__105__posy)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # OFFSET
            # Addition
            # LHS
            # Subscript
            # LHS
            stack.append(__main__while__61__block__62__block__105__posx0)
            # OFFSET
            # Int Literal
            stack.append(2)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            # Int Literal
            stack.append(1)
            __rhs = stack.pop()
            __lhs = stack.pop()
            __res = __lhs + __rhs
            stack.append(__res)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            # Char Literal
            stack.append('.')
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs == __rhs
            stack.append (__res)
            # Only check rhs if lhs was true
            __lhs = stack[-1]
            if (__lhs):
                # RHS
                # Equal
                # LHS
                # Subscript
                # LHS
                # Subscript
                # LHS
                # Member Accessor
                # LHS
                stack.append(__main__board)
                # RHS
                stack.append (__field____main____Vector__char__1____data)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                # OFFSET
                # Addition
                # LHS
                stack.append(__main__while__61__block__62__block__105__posy)
                # RHS
                # Int Literal
                stack.append(1)
                __rhs = stack.pop()
                __lhs = stack.pop()
                __res = __lhs + __rhs
                stack.append(__res)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # OFFSET
                # Addition
                # LHS
                # Subscript
                # LHS
                stack.append(__main__while__61__block__62__block__105__posx1)
                # OFFSET
                # Int Literal
                stack.append(0)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # RHS
                # Int Literal
                stack.append(1)
                __rhs = stack.pop()
                __lhs = stack.pop()
                __res = __lhs + __rhs
                stack.append(__res)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # RHS
                # Char Literal
                stack.append('.')
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs == __rhs
                stack.append (__res)
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs and __rhs
            else:
                __res = stack.pop ()
            stack.append (__res)
            # Only check rhs if lhs was true
            __lhs = stack[-1]
            if (__lhs):
                # RHS
                # Equal
                # LHS
                # Subscript
                # LHS
                # Subscript
                # LHS
                # Member Accessor
                # LHS
                stack.append(__main__board)
                # RHS
                stack.append (__field____main____Vector__char__1____data)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                # OFFSET
                # Addition
                # LHS
                stack.append(__main__while__61__block__62__block__105__posy)
                # RHS
                # Int Literal
                stack.append(2)
                __rhs = stack.pop()
                __lhs = stack.pop()
                __res = __lhs + __rhs
                stack.append(__res)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # OFFSET
                # Addition
                # LHS
                # Subscript
                # LHS
                stack.append(__main__while__61__block__62__block__105__posx2)
                # OFFSET
                # Int Literal
                stack.append(0)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # RHS
                # Int Literal
                stack.append(1)
                __rhs = stack.pop()
                __lhs = stack.pop()
                __res = __lhs + __rhs
                stack.append(__res)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # RHS
                # Char Literal
                stack.append('.')
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs == __rhs
                stack.append (__res)
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs and __rhs
            else:
                __res = stack.pop ()
            stack.append (__res)
            __if__121__cond = stack.pop ()
            # get condition from stack
            if (__if__121__cond):
                # Body
                #---------------------------------------------------------
                # Code Block
                # Statement
                # Assignment - '+='
                # RHS
                # Int Literal
                stack.append(1)
                # LHS
                # Subscript assignment
                # LHS
                stack.append(__main__while__61__block__62__block__105__posx0)
                # OFFSET
                # Int Literal
                stack.append(0)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __pointer[__offset] + __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Statement
                # Assignment - '+='
                # RHS
                # Int Literal
                stack.append(1)
                # LHS
                # Subscript assignment
                # LHS
                stack.append(__main__while__61__block__62__block__105__posx0)
                # OFFSET
                # Int Literal
                stack.append(1)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __pointer[__offset] + __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Statement
                # Assignment - '+='
                # RHS
                # Int Literal
                stack.append(1)
                # LHS
                # Subscript assignment
                # LHS
                stack.append(__main__while__61__block__62__block__105__posx0)
                # OFFSET
                # Int Literal
                stack.append(2)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __pointer[__offset] + __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Statement
                # Assignment - '+='
                # RHS
                # Int Literal
                stack.append(1)
                # LHS
                # Subscript assignment
                # LHS
                stack.append(__main__while__61__block__62__block__105__posx1)
                # OFFSET
                # Int Literal
                stack.append(0)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __pointer[__offset] + __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Statement
                # Assignment - '+='
                # RHS
                # Int Literal
                stack.append(1)
                # LHS
                # Subscript assignment
                # LHS
                stack.append(__main__while__61__block__62__block__105__posx2)
                # OFFSET
                # Int Literal
                stack.append(0)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __pointer[__offset] + __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                #---------------------------------------------------------
            # End of if
            #-------------------------------------------------------------
            #-------------------------------------------------------------
        #-----------------------------------------------------------------
        # End of if
        #-----------------------------------------------------------------
        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main__while__61__block__62__block__105__rock_char)
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__105__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__105__posx0)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main__while__61__block__62__block__105__rock_char)
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__105__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__105__posx0)
        # OFFSET
        # Int Literal
        stack.append(1)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main__while__61__block__62__block__105__rock_char)
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__105__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__105__posx0)
        # OFFSET
        # Int Literal
        stack.append(2)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main__while__61__block__62__block__105__rock_char)
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__while__61__block__62__block__105__posy)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__105__posx1)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main__while__61__block__62__block__105__rock_char)
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__while__61__block__62__block__105__posy)
        # RHS
        # Int Literal
        stack.append(2)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__105__posx2)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Modulus
        # LHS
        # Addition
        # LHS
        stack.append(__main__shift_index)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        # RHS
        stack.append(__main__shift_max)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs % __rhs
        stack.append(__res)
        __rhs = stack.pop()
        __main__shift_index = __rhs
        stack.append (__main__shift_index)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Function Call - printboard(Vector<:char[]:>) -> void
        # Arguments
        stack.append(__main__board)
        __arg0 = stack.pop ()
        # *** printboard
        __res = __main____printboard__Vector__tparam0__char (__arg0)
        stack.append (__res) # function call result
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
        # If-Statement
        # Precomputing all if/elif conditions and give unique names
        # bc we can't have code between if and elif
        # Condition
        # OR
        # LHS
        # OR
        # LHS
        # OR
        # LHS
        # Not Equal
        # LHS
        # Subscript
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Subtraction
        # LHS
        stack.append(__main__while__61__block__62__block__105__posy)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs - __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__105__posx0)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        # Char Literal
        stack.append('.')
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs != __rhs
        stack.append (__res)
        # RHS
        # Not Equal
        # LHS
        # Subscript
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Subtraction
        # LHS
        stack.append(__main__while__61__block__62__block__105__posy)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs - __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__105__posx0)
        # OFFSET
        # Int Literal
        stack.append(1)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        # Char Literal
        stack.append('.')
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs != __rhs
        stack.append (__res)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs or __rhs
        stack.append (__res)
        # RHS
        # Not Equal
        # LHS
        # Subscript
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Subtraction
        # LHS
        stack.append(__main__while__61__block__62__block__105__posy)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs - __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__105__posx0)
        # OFFSET
        # Int Literal
        stack.append(2)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        # Char Literal
        stack.append('.')
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs != __rhs
        stack.append (__res)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs or __rhs
        stack.append (__res)
        # RHS
        # Equal
        # LHS
        # Subtraction
        # LHS
        stack.append(__main__while__61__block__62__block__105__posy)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs - __rhs
        stack.append(__res)
        # RHS
        # Int Literal
        stack.append(0)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs == __rhs
        stack.append (__res)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs or __rhs
        stack.append (__res)
        __if__123__cond = stack.pop ()
        # get condition from stack
        if (__if__123__cond):
            # Body
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Function Call - println(char[]) -> void
            # Arguments
            # String Literal
            stack.append([*("rock at rest"+'\0')])
            __arg0 = stack.pop ()
            # *** println
            __res = __builtin__println__char__1 (__arg0)
            stack.append (__res) # function call result
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            # Break out of __while__114
            break
            #-------------------------------------------------------------
        # End of if
        #-----------------------------------------------------------------
        # Statement
        # Assignment - '='
        # RHS
        # Char Literal
        stack.append('.')
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__105__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__105__posx0)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Char Literal
        stack.append('.')
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__105__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__105__posx0)
        # OFFSET
        # Int Literal
        stack.append(1)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Char Literal
        stack.append('.')
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__105__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__105__posx0)
        # OFFSET
        # Int Literal
        stack.append(2)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Char Literal
        stack.append('.')
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__while__61__block__62__block__105__posy)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__105__posx1)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Char Literal
        stack.append('.')
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__while__61__block__62__block__105__posy)
        # RHS
        # Int Literal
        stack.append(2)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__105__posx2)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '-='
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __main__while__61__block__62__block__105__posy = __main__while__61__block__62__block__105__posy - __rhs
        stack.append (__main__while__61__block__62__block__105__posy)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main__while__61__block__62__block__105__rock_char)
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__105__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__105__posx0)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main__while__61__block__62__block__105__rock_char)
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__105__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__105__posx0)
        # OFFSET
        # Int Literal
        stack.append(1)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main__while__61__block__62__block__105__rock_char)
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__105__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__105__posx0)
        # OFFSET
        # Int Literal
        stack.append(2)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main__while__61__block__62__block__105__rock_char)
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__while__61__block__62__block__105__posy)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__105__posx1)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main__while__61__block__62__block__105__rock_char)
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__while__61__block__62__block__105__posy)
        # RHS
        # Int Literal
        stack.append(2)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__105__posx2)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Function Call - printboard(Vector<:char[]:>) -> void
        # Arguments
        stack.append(__main__board)
        __arg0 = stack.pop ()
        # *** printboard
        __res = __main____printboard__Vector__tparam0__char (__arg0)
        stack.append (__res) # function call result
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
    # End of While
    #---------------------------------------------------------------------
    # Statement
    # Function Call - printboard(Vector<:char[]:>) -> void
    # Arguments
    stack.append(__main__board)
    __arg0 = stack.pop ()
    # *** printboard
    __res = __main____printboard__Vector__tparam0__char (__arg0)
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
    # Statement
    # Assignment - '+='
    # RHS
    # Int Literal
    stack.append(1)
    __rhs = stack.pop()
    __main__num_rocks = __main__num_rocks + __rhs
    stack.append (__main__num_rocks)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
    # If-Statement
    # Precomputing all if/elif conditions and give unique names
    # bc we can't have code between if and elif
    # Condition
    # Greater Than or Equal to
    # LHS
    stack.append(__main__num_rocks)
    # RHS
    stack.append(__main__max_rocks)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs >= __rhs
    stack.append (__res)
    __if__125__cond = stack.pop ()
    # get condition from stack
    if (__if__125__cond):
        # Body
        # Break out of __while__61
        break
    # End of if
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(0)
    # LHS
    __main__while__61__block__62__block__126__rock_height = 0
    __rhs = stack.pop()
    __main__while__61__block__62__block__126__rock_height = __rhs
    stack.append (__main__while__61__block__62__block__126__rock_height)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
    # For-Loop
    # Init
    # Assignment - '='
    # RHS
    # Subtraction
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main__board)
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
    __res = __lhs - __rhs
    stack.append(__res)
    # LHS
    __main__while__61__block__62__block__126__for__127__i = 0
    __rhs = stack.pop()
    __main__while__61__block__62__block__126__for__127__i = __rhs
    stack.append (__main__while__61__block__62__block__126__for__127__i)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Greater Than or Equal to
        # LHS
        stack.append(__main__while__61__block__62__block__126__for__127__i)
        # RHS
        # Int Literal
        stack.append(0)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs >= __rhs
        stack.append (__res)
        __cond = stack.pop ()
        # break out of loop if condition is false
        if (__cond == 0): break
        # Body
        #-----------------------------------------------------------------
        # Code Block
        #-----------------------------------------------------------------
        # For-Loop
        # Init
        # Assignment - '='
        # RHS
        # Int Literal
        stack.append(1)
        # LHS
        __main__while__61__block__62__block__126__for__127__block__128__for__129__j = 0
        __rhs = stack.pop()
        __main__while__61__block__62__block__126__for__127__block__128__for__129__j = __rhs
        stack.append (__main__while__61__block__62__block__126__for__127__block__128__for__129__j)
        # Using an infinite loop so we can write a separate multi-line condition
        while (1):
            # Condition
            # Less Than
            # LHS
            stack.append(__main__while__61__block__62__block__126__for__127__block__128__for__129__j)
            # RHS
            # Int Literal
            stack.append(8)
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
            #-------------------------------------------------------------
            # If-Statement
            # Precomputing all if/elif conditions and give unique names
            # bc we can't have code between if and elif
            # Condition
            # Not Equal
            # LHS
            # Subscript
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__board)
            # RHS
            stack.append (__field____main____Vector__char__1____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main__while__61__block__62__block__126__for__127__i)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # OFFSET
            stack.append(__main__while__61__block__62__block__126__for__127__block__128__for__129__j)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            # Char Literal
            stack.append('.')
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs != __rhs
            stack.append (__res)
            __if__131__cond = stack.pop ()
            # get condition from stack
            if (__if__131__cond):
                # Body
                #---------------------------------------------------------
                # Code Block
                # Statement
                # Assignment - '='
                # RHS
                stack.append(__main__while__61__block__62__block__126__for__127__i)
                __rhs = stack.pop()
                __main__while__61__block__62__block__126__rock_height = __rhs
                stack.append (__main__while__61__block__62__block__126__rock_height)
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Break out of __for__129
                break
                #---------------------------------------------------------
            # End of if
            #-------------------------------------------------------------
            #-------------------------------------------------------------
            # Update
            # Pre-Increment
            # RHS
            stack.append(__main__while__61__block__62__block__126__for__127__block__128__for__129__j)
            __rhs = stack.pop ()
            __main__while__61__block__62__block__126__for__127__block__128__for__129__j = __main__while__61__block__62__block__126__for__127__block__128__for__129__j + 1
            __res = __main__while__61__block__62__block__126__for__127__block__128__for__129__j
            stack.append (__res)
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # If-Statement
        # Precomputing all if/elif conditions and give unique names
        # bc we can't have code between if and elif
        # Condition
        # Not Equal
        # LHS
        stack.append(__main__while__61__block__62__block__126__rock_height)
        # RHS
        # Int Literal
        stack.append(0)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs != __rhs
        stack.append (__res)
        __if__133__cond = stack.pop ()
        # get condition from stack
        if (__if__133__cond):
            # Body
            # Break out of __for__127
            break
        # End of if
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # Update
        # Pre-Decrement
        # RHS
        stack.append(__main__while__61__block__62__block__126__for__127__i)
        __rhs = stack.pop ()
        __main__while__61__block__62__block__126__for__127__i = __main__while__61__block__62__block__126__for__127__i - 1
        __res = __main__while__61__block__62__block__126__for__127__i
        stack.append (__res)
    #---------------------------------------------------------------------
    # Statement
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(4)
    # LHS
    __main__while__61__block__62__block__126__shape_height = 0
    __rhs = stack.pop()
    __main__while__61__block__62__block__126__shape_height = __rhs
    stack.append (__main__while__61__block__62__block__126__shape_height)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Char Literal
    stack.append('3')
    # LHS
    __main__while__61__block__62__block__126__rock_char = 0
    __rhs = stack.pop()
    __main__while__61__block__62__block__126__rock_char = __rhs
    stack.append (__main__while__61__block__62__block__126__rock_char)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Addition
    # LHS
    # Addition
    # LHS
    stack.append(__main__while__61__block__62__block__126__rock_height)
    # RHS
    # Int Literal
    stack.append(3)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs + __rhs
    stack.append(__res)
    # RHS
    stack.append(__main__while__61__block__62__block__126__shape_height)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs + __rhs
    stack.append(__res)
    # LHS
    __main__while__61__block__62__block__126__desired_height = 0
    __rhs = stack.pop()
    __main__while__61__block__62__block__126__desired_height = __rhs
    stack.append (__main__while__61__block__62__block__126__desired_height)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
    # While-Loop
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        # Subtraction
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
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
        __res = __lhs - __rhs
        stack.append(__res)
        # RHS
        stack.append(__main__while__61__block__62__block__126__desired_height)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs < __rhs
        stack.append (__res)
        __cond = stack.pop ()
        # break out of loop if condition is false
        if (__cond == 0): break
        # Body
        # Statement
        # Method Call - Vector<:char[]:>::pushBack(char[]) -> void
        # LHS
        stack.append(__main__board)
        # RHS
        # Arguments
        # String Literal
        stack.append([*("|.......|"+'\0')])
        __arg0 = stack.pop ()
        __obj = stack.pop ()
        __retval = __method____main____Vector__char__1____pushBack__char__1 (__obj, __arg0)
        stack.append (__retval)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

    # End of While
    #---------------------------------------------------------------------
    # Statement
    # Function Call - printboard(Vector<:char[]:>) -> void
    # Arguments
    stack.append(__main__board)
    __arg0 = stack.pop ()
    # *** printboard
    __res = __main____printboard__Vector__tparam0__char (__arg0)
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Array Constructor
    # Elements
    # Int Literal
    stack.append(3)
    __elem0 = stack.pop ()
    __list = [0] * 1
    __list[0] = __elem0
    stack.append (__list)
    # LHS
    __main__while__61__block__62__block__126__posx0 = 0
    __rhs = stack.pop()
    __main__while__61__block__62__block__126__posx0 = __rhs
    stack.append (__main__while__61__block__62__block__126__posx0)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Array Constructor
    # Elements
    # Int Literal
    stack.append(3)
    __elem0 = stack.pop ()
    __list = [0] * 1
    __list[0] = __elem0
    stack.append (__list)
    # LHS
    __main__while__61__block__62__block__126__posx1 = 0
    __rhs = stack.pop()
    __main__while__61__block__62__block__126__posx1 = __rhs
    stack.append (__main__while__61__block__62__block__126__posx1)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Array Constructor
    # Elements
    # Int Literal
    stack.append(3)
    __elem0 = stack.pop ()
    __list = [0] * 1
    __list[0] = __elem0
    stack.append (__list)
    # LHS
    __main__while__61__block__62__block__126__posx2 = 0
    __rhs = stack.pop()
    __main__while__61__block__62__block__126__posx2 = __rhs
    stack.append (__main__while__61__block__62__block__126__posx2)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Array Constructor
    # Elements
    # Int Literal
    stack.append(3)
    __elem0 = stack.pop ()
    __list = [0] * 1
    __list[0] = __elem0
    stack.append (__list)
    # LHS
    __main__while__61__block__62__block__126__posx3 = 0
    __rhs = stack.pop()
    __main__while__61__block__62__block__126__posx3 = __rhs
    stack.append (__main__while__61__block__62__block__126__posx3)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Addition
    # LHS
    # Addition
    # LHS
    stack.append(__main__while__61__block__62__block__126__rock_height)
    # RHS
    # Int Literal
    stack.append(3)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs + __rhs
    stack.append(__res)
    # RHS
    # Int Literal
    stack.append(1)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs + __rhs
    stack.append(__res)
    # LHS
    __main__while__61__block__62__block__126__posy = 0
    __rhs = stack.pop()
    __main__while__61__block__62__block__126__posy = __rhs
    stack.append (__main__while__61__block__62__block__126__posy)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main__while__61__block__62__block__126__rock_char)
    # LHS
    # Subscript assignment
    # LHS
    # Subscript
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main__board)
    # RHS
    stack.append (__field____main____Vector__char__1____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    stack.append(__main__while__61__block__62__block__126__posy)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    # OFFSET
    # Subscript
    # LHS
    stack.append(__main__while__61__block__62__block__126__posx0)
    # OFFSET
    # Int Literal
    stack.append(0)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    __offset = stack.pop()
    __pointer = stack.pop()
    __rhs = stack.pop()
    __pointer[__offset] = __rhs
    stack.append (__pointer[__offset])
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main__while__61__block__62__block__126__rock_char)
    # LHS
    # Subscript assignment
    # LHS
    # Subscript
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main__board)
    # RHS
    stack.append (__field____main____Vector__char__1____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    # Addition
    # LHS
    stack.append(__main__while__61__block__62__block__126__posy)
    # RHS
    # Int Literal
    stack.append(1)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs + __rhs
    stack.append(__res)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    # OFFSET
    # Subscript
    # LHS
    stack.append(__main__while__61__block__62__block__126__posx1)
    # OFFSET
    # Int Literal
    stack.append(0)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    __offset = stack.pop()
    __pointer = stack.pop()
    __rhs = stack.pop()
    __pointer[__offset] = __rhs
    stack.append (__pointer[__offset])
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main__while__61__block__62__block__126__rock_char)
    # LHS
    # Subscript assignment
    # LHS
    # Subscript
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main__board)
    # RHS
    stack.append (__field____main____Vector__char__1____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    # Addition
    # LHS
    stack.append(__main__while__61__block__62__block__126__posy)
    # RHS
    # Int Literal
    stack.append(2)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs + __rhs
    stack.append(__res)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    # OFFSET
    # Subscript
    # LHS
    stack.append(__main__while__61__block__62__block__126__posx2)
    # OFFSET
    # Int Literal
    stack.append(0)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    __offset = stack.pop()
    __pointer = stack.pop()
    __rhs = stack.pop()
    __pointer[__offset] = __rhs
    stack.append (__pointer[__offset])
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main__while__61__block__62__block__126__rock_char)
    # LHS
    # Subscript assignment
    # LHS
    # Subscript
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main__board)
    # RHS
    stack.append (__field____main____Vector__char__1____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    # Addition
    # LHS
    stack.append(__main__while__61__block__62__block__126__posy)
    # RHS
    # Int Literal
    stack.append(3)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs + __rhs
    stack.append(__res)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    # OFFSET
    # Subscript
    # LHS
    stack.append(__main__while__61__block__62__block__126__posx3)
    # OFFSET
    # Int Literal
    stack.append(0)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    __offset = stack.pop()
    __pointer = stack.pop()
    __rhs = stack.pop()
    __pointer[__offset] = __rhs
    stack.append (__pointer[__offset])
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Function Call - printboard(Vector<:char[]:>) -> void
    # Arguments
    stack.append(__main__board)
    __arg0 = stack.pop ()
    # *** printboard
    __res = __main____printboard__Vector__tparam0__char (__arg0)
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
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
        #-----------------------------------------------------------------
        # Code Block
        # Statement
        # Function Call - println(int) -> void
        # Arguments
        stack.append(__main__shift_index)
        __arg0 = stack.pop ()
        # *** println
        __res = __builtin__println__int (__arg0)
        stack.append (__res) # function call result
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Char Literal
        stack.append('.')
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__126__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__126__posx0)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Char Literal
        stack.append('.')
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__while__61__block__62__block__126__posy)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__126__posx1)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Char Literal
        stack.append('.')
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__while__61__block__62__block__126__posy)
        # RHS
        # Int Literal
        stack.append(2)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__126__posx2)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Char Literal
        stack.append('.')
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__while__61__block__62__block__126__posy)
        # RHS
        # Int Literal
        stack.append(3)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__126__posx3)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
        # If-Statement
        # Precomputing all if/elif conditions and give unique names
        # bc we can't have code between if and elif
        # Condition
        # Equal
        # LHS
        # Subscript
        # LHS
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
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        stack.append(__main__shift_index)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        # Char Literal
        stack.append('<')
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs == __rhs
        stack.append (__res)
        __if__137__cond = stack.pop ()
        # get condition from stack
        if (__if__137__cond):
            # Body
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Function Call - println(char[]) -> void
            # Arguments
            # String Literal
            stack.append([*("shift left"+'\0')])
            __arg0 = stack.pop ()
            # *** println
            __res = __builtin__println__char__1 (__arg0)
            stack.append (__res) # function call result
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            #-------------------------------------------------------------
            # If-Statement
            # Precomputing all if/elif conditions and give unique names
            # bc we can't have code between if and elif
            # Condition
            # AND
            # LHS
            # AND
            # LHS
            # AND
            # LHS
            # Equal
            # LHS
            # Subscript
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__board)
            # RHS
            stack.append (__field____main____Vector__char__1____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main__while__61__block__62__block__126__posy)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # OFFSET
            # Subtraction
            # LHS
            # Subscript
            # LHS
            stack.append(__main__while__61__block__62__block__126__posx0)
            # OFFSET
            # Int Literal
            stack.append(0)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            # Int Literal
            stack.append(1)
            __rhs = stack.pop()
            __lhs = stack.pop()
            __res = __lhs - __rhs
            stack.append(__res)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            # Char Literal
            stack.append('.')
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs == __rhs
            stack.append (__res)
            # Only check rhs if lhs was true
            __lhs = stack[-1]
            if (__lhs):
                # RHS
                # Equal
                # LHS
                # Subscript
                # LHS
                # Subscript
                # LHS
                # Member Accessor
                # LHS
                stack.append(__main__board)
                # RHS
                stack.append (__field____main____Vector__char__1____data)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                # OFFSET
                # Addition
                # LHS
                stack.append(__main__while__61__block__62__block__126__posy)
                # RHS
                # Int Literal
                stack.append(1)
                __rhs = stack.pop()
                __lhs = stack.pop()
                __res = __lhs + __rhs
                stack.append(__res)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # OFFSET
                # Subtraction
                # LHS
                # Subscript
                # LHS
                stack.append(__main__while__61__block__62__block__126__posx1)
                # OFFSET
                # Int Literal
                stack.append(0)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # RHS
                # Int Literal
                stack.append(1)
                __rhs = stack.pop()
                __lhs = stack.pop()
                __res = __lhs - __rhs
                stack.append(__res)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # RHS
                # Char Literal
                stack.append('.')
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs == __rhs
                stack.append (__res)
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs and __rhs
            else:
                __res = stack.pop ()
            stack.append (__res)
            # Only check rhs if lhs was true
            __lhs = stack[-1]
            if (__lhs):
                # RHS
                # Equal
                # LHS
                # Subscript
                # LHS
                # Subscript
                # LHS
                # Member Accessor
                # LHS
                stack.append(__main__board)
                # RHS
                stack.append (__field____main____Vector__char__1____data)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                # OFFSET
                # Addition
                # LHS
                stack.append(__main__while__61__block__62__block__126__posy)
                # RHS
                # Int Literal
                stack.append(2)
                __rhs = stack.pop()
                __lhs = stack.pop()
                __res = __lhs + __rhs
                stack.append(__res)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # OFFSET
                # Subtraction
                # LHS
                # Subscript
                # LHS
                stack.append(__main__while__61__block__62__block__126__posx2)
                # OFFSET
                # Int Literal
                stack.append(0)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # RHS
                # Int Literal
                stack.append(1)
                __rhs = stack.pop()
                __lhs = stack.pop()
                __res = __lhs - __rhs
                stack.append(__res)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # RHS
                # Char Literal
                stack.append('.')
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs == __rhs
                stack.append (__res)
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs and __rhs
            else:
                __res = stack.pop ()
            stack.append (__res)
            # Only check rhs if lhs was true
            __lhs = stack[-1]
            if (__lhs):
                # RHS
                # Equal
                # LHS
                # Subscript
                # LHS
                # Subscript
                # LHS
                # Member Accessor
                # LHS
                stack.append(__main__board)
                # RHS
                stack.append (__field____main____Vector__char__1____data)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                # OFFSET
                # Addition
                # LHS
                stack.append(__main__while__61__block__62__block__126__posy)
                # RHS
                # Int Literal
                stack.append(3)
                __rhs = stack.pop()
                __lhs = stack.pop()
                __res = __lhs + __rhs
                stack.append(__res)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # OFFSET
                # Subtraction
                # LHS
                # Subscript
                # LHS
                stack.append(__main__while__61__block__62__block__126__posx3)
                # OFFSET
                # Int Literal
                stack.append(0)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # RHS
                # Int Literal
                stack.append(1)
                __rhs = stack.pop()
                __lhs = stack.pop()
                __res = __lhs - __rhs
                stack.append(__res)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # RHS
                # Char Literal
                stack.append('.')
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs == __rhs
                stack.append (__res)
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs and __rhs
            else:
                __res = stack.pop ()
            stack.append (__res)
            __if__139__cond = stack.pop ()
            # get condition from stack
            if (__if__139__cond):
                # Body
                #---------------------------------------------------------
                # Code Block
                # Statement
                # Assignment - '-='
                # RHS
                # Int Literal
                stack.append(1)
                # LHS
                # Subscript assignment
                # LHS
                stack.append(__main__while__61__block__62__block__126__posx0)
                # OFFSET
                # Int Literal
                stack.append(0)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __pointer[__offset] - __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Statement
                # Assignment - '-='
                # RHS
                # Int Literal
                stack.append(1)
                # LHS
                # Subscript assignment
                # LHS
                stack.append(__main__while__61__block__62__block__126__posx1)
                # OFFSET
                # Int Literal
                stack.append(0)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __pointer[__offset] - __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Statement
                # Assignment - '-='
                # RHS
                # Int Literal
                stack.append(1)
                # LHS
                # Subscript assignment
                # LHS
                stack.append(__main__while__61__block__62__block__126__posx2)
                # OFFSET
                # Int Literal
                stack.append(0)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __pointer[__offset] - __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Statement
                # Assignment - '-='
                # RHS
                # Int Literal
                stack.append(1)
                # LHS
                # Subscript assignment
                # LHS
                stack.append(__main__while__61__block__62__block__126__posx3)
                # OFFSET
                # Int Literal
                stack.append(0)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __pointer[__offset] - __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                #---------------------------------------------------------
            # End of if
            #-------------------------------------------------------------
            #-------------------------------------------------------------
        #-----------------------------------------------------------------
        # Else-Statement
        else:
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Function Call - println(char[]) -> void
            # Arguments
            # String Literal
            stack.append([*("shift right"+'\0')])
            __arg0 = stack.pop ()
            # *** println
            __res = __builtin__println__char__1 (__arg0)
            stack.append (__res) # function call result
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            #-------------------------------------------------------------
            # If-Statement
            # Precomputing all if/elif conditions and give unique names
            # bc we can't have code between if and elif
            # Condition
            # AND
            # LHS
            # AND
            # LHS
            # AND
            # LHS
            # Equal
            # LHS
            # Subscript
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__board)
            # RHS
            stack.append (__field____main____Vector__char__1____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main__while__61__block__62__block__126__posy)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # OFFSET
            # Addition
            # LHS
            # Subscript
            # LHS
            stack.append(__main__while__61__block__62__block__126__posx0)
            # OFFSET
            # Int Literal
            stack.append(0)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            # Int Literal
            stack.append(1)
            __rhs = stack.pop()
            __lhs = stack.pop()
            __res = __lhs + __rhs
            stack.append(__res)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            # Char Literal
            stack.append('.')
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs == __rhs
            stack.append (__res)
            # Only check rhs if lhs was true
            __lhs = stack[-1]
            if (__lhs):
                # RHS
                # Equal
                # LHS
                # Subscript
                # LHS
                # Subscript
                # LHS
                # Member Accessor
                # LHS
                stack.append(__main__board)
                # RHS
                stack.append (__field____main____Vector__char__1____data)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                # OFFSET
                # Addition
                # LHS
                stack.append(__main__while__61__block__62__block__126__posy)
                # RHS
                # Int Literal
                stack.append(1)
                __rhs = stack.pop()
                __lhs = stack.pop()
                __res = __lhs + __rhs
                stack.append(__res)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # OFFSET
                # Addition
                # LHS
                # Subscript
                # LHS
                stack.append(__main__while__61__block__62__block__126__posx1)
                # OFFSET
                # Int Literal
                stack.append(0)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # RHS
                # Int Literal
                stack.append(1)
                __rhs = stack.pop()
                __lhs = stack.pop()
                __res = __lhs + __rhs
                stack.append(__res)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # RHS
                # Char Literal
                stack.append('.')
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs == __rhs
                stack.append (__res)
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs and __rhs
            else:
                __res = stack.pop ()
            stack.append (__res)
            # Only check rhs if lhs was true
            __lhs = stack[-1]
            if (__lhs):
                # RHS
                # Equal
                # LHS
                # Subscript
                # LHS
                # Subscript
                # LHS
                # Member Accessor
                # LHS
                stack.append(__main__board)
                # RHS
                stack.append (__field____main____Vector__char__1____data)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                # OFFSET
                # Addition
                # LHS
                stack.append(__main__while__61__block__62__block__126__posy)
                # RHS
                # Int Literal
                stack.append(2)
                __rhs = stack.pop()
                __lhs = stack.pop()
                __res = __lhs + __rhs
                stack.append(__res)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # OFFSET
                # Addition
                # LHS
                # Subscript
                # LHS
                stack.append(__main__while__61__block__62__block__126__posx2)
                # OFFSET
                # Int Literal
                stack.append(0)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # RHS
                # Int Literal
                stack.append(1)
                __rhs = stack.pop()
                __lhs = stack.pop()
                __res = __lhs + __rhs
                stack.append(__res)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # RHS
                # Char Literal
                stack.append('.')
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs == __rhs
                stack.append (__res)
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs and __rhs
            else:
                __res = stack.pop ()
            stack.append (__res)
            # Only check rhs if lhs was true
            __lhs = stack[-1]
            if (__lhs):
                # RHS
                # Equal
                # LHS
                # Subscript
                # LHS
                # Subscript
                # LHS
                # Member Accessor
                # LHS
                stack.append(__main__board)
                # RHS
                stack.append (__field____main____Vector__char__1____data)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                # OFFSET
                # Addition
                # LHS
                stack.append(__main__while__61__block__62__block__126__posy)
                # RHS
                # Int Literal
                stack.append(3)
                __rhs = stack.pop()
                __lhs = stack.pop()
                __res = __lhs + __rhs
                stack.append(__res)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # OFFSET
                # Addition
                # LHS
                # Subscript
                # LHS
                stack.append(__main__while__61__block__62__block__126__posx3)
                # OFFSET
                # Int Literal
                stack.append(0)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # RHS
                # Int Literal
                stack.append(1)
                __rhs = stack.pop()
                __lhs = stack.pop()
                __res = __lhs + __rhs
                stack.append(__res)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # RHS
                # Char Literal
                stack.append('.')
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs == __rhs
                stack.append (__res)
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs and __rhs
            else:
                __res = stack.pop ()
            stack.append (__res)
            __if__142__cond = stack.pop ()
            # get condition from stack
            if (__if__142__cond):
                # Body
                #---------------------------------------------------------
                # Code Block
                # Statement
                # Assignment - '+='
                # RHS
                # Int Literal
                stack.append(1)
                # LHS
                # Subscript assignment
                # LHS
                stack.append(__main__while__61__block__62__block__126__posx0)
                # OFFSET
                # Int Literal
                stack.append(0)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __pointer[__offset] + __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Statement
                # Assignment - '+='
                # RHS
                # Int Literal
                stack.append(1)
                # LHS
                # Subscript assignment
                # LHS
                stack.append(__main__while__61__block__62__block__126__posx1)
                # OFFSET
                # Int Literal
                stack.append(0)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __pointer[__offset] + __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Statement
                # Assignment - '+='
                # RHS
                # Int Literal
                stack.append(1)
                # LHS
                # Subscript assignment
                # LHS
                stack.append(__main__while__61__block__62__block__126__posx2)
                # OFFSET
                # Int Literal
                stack.append(0)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __pointer[__offset] + __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Statement
                # Assignment - '+='
                # RHS
                # Int Literal
                stack.append(1)
                # LHS
                # Subscript assignment
                # LHS
                stack.append(__main__while__61__block__62__block__126__posx3)
                # OFFSET
                # Int Literal
                stack.append(0)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __pointer[__offset] + __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                #---------------------------------------------------------
            # End of if
            #-------------------------------------------------------------
            #-------------------------------------------------------------
        #-----------------------------------------------------------------
        # End of if
        #-----------------------------------------------------------------
        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main__while__61__block__62__block__126__rock_char)
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__126__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__126__posx0)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main__while__61__block__62__block__126__rock_char)
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__while__61__block__62__block__126__posy)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__126__posx1)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main__while__61__block__62__block__126__rock_char)
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__while__61__block__62__block__126__posy)
        # RHS
        # Int Literal
        stack.append(2)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__126__posx2)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main__while__61__block__62__block__126__rock_char)
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__while__61__block__62__block__126__posy)
        # RHS
        # Int Literal
        stack.append(3)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__126__posx3)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Modulus
        # LHS
        # Addition
        # LHS
        stack.append(__main__shift_index)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        # RHS
        stack.append(__main__shift_max)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs % __rhs
        stack.append(__res)
        __rhs = stack.pop()
        __main__shift_index = __rhs
        stack.append (__main__shift_index)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Function Call - printboard(Vector<:char[]:>) -> void
        # Arguments
        stack.append(__main__board)
        __arg0 = stack.pop ()
        # *** printboard
        __res = __main____printboard__Vector__tparam0__char (__arg0)
        stack.append (__res) # function call result
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
        # If-Statement
        # Precomputing all if/elif conditions and give unique names
        # bc we can't have code between if and elif
        # Condition
        # OR
        # LHS
        # Not Equal
        # LHS
        # Subscript
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Subtraction
        # LHS
        stack.append(__main__while__61__block__62__block__126__posy)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs - __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__126__posx0)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        # Char Literal
        stack.append('.')
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs != __rhs
        stack.append (__res)
        # RHS
        # Equal
        # LHS
        # Subtraction
        # LHS
        stack.append(__main__while__61__block__62__block__126__posy)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs - __rhs
        stack.append(__res)
        # RHS
        # Int Literal
        stack.append(0)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs == __rhs
        stack.append (__res)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs or __rhs
        stack.append (__res)
        __if__144__cond = stack.pop ()
        # get condition from stack
        if (__if__144__cond):
            # Body
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Function Call - println(char[]) -> void
            # Arguments
            # String Literal
            stack.append([*("rock at rest"+'\0')])
            __arg0 = stack.pop ()
            # *** println
            __res = __builtin__println__char__1 (__arg0)
            stack.append (__res) # function call result
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            # Break out of __while__135
            break
            #-------------------------------------------------------------
        # End of if
        #-----------------------------------------------------------------
        # Statement
        # Assignment - '='
        # RHS
        # Char Literal
        stack.append('.')
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__126__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__126__posx0)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Char Literal
        stack.append('.')
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__while__61__block__62__block__126__posy)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__126__posx1)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Char Literal
        stack.append('.')
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__while__61__block__62__block__126__posy)
        # RHS
        # Int Literal
        stack.append(2)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__126__posx2)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Char Literal
        stack.append('.')
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__while__61__block__62__block__126__posy)
        # RHS
        # Int Literal
        stack.append(3)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__126__posx3)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '-='
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __main__while__61__block__62__block__126__posy = __main__while__61__block__62__block__126__posy - __rhs
        stack.append (__main__while__61__block__62__block__126__posy)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main__while__61__block__62__block__126__rock_char)
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__126__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__126__posx0)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main__while__61__block__62__block__126__rock_char)
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__while__61__block__62__block__126__posy)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__126__posx1)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main__while__61__block__62__block__126__rock_char)
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__while__61__block__62__block__126__posy)
        # RHS
        # Int Literal
        stack.append(2)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__126__posx2)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main__while__61__block__62__block__126__rock_char)
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__while__61__block__62__block__126__posy)
        # RHS
        # Int Literal
        stack.append(3)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__126__posx3)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Function Call - printboard(Vector<:char[]:>) -> void
        # Arguments
        stack.append(__main__board)
        __arg0 = stack.pop ()
        # *** printboard
        __res = __main____printboard__Vector__tparam0__char (__arg0)
        stack.append (__res) # function call result
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
    # End of While
    #---------------------------------------------------------------------
    # Statement
    # Function Call - printboard(Vector<:char[]:>) -> void
    # Arguments
    stack.append(__main__board)
    __arg0 = stack.pop ()
    # *** printboard
    __res = __main____printboard__Vector__tparam0__char (__arg0)
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
    # Statement
    # Assignment - '+='
    # RHS
    # Int Literal
    stack.append(1)
    __rhs = stack.pop()
    __main__num_rocks = __main__num_rocks + __rhs
    stack.append (__main__num_rocks)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
    # If-Statement
    # Precomputing all if/elif conditions and give unique names
    # bc we can't have code between if and elif
    # Condition
    # Greater Than or Equal to
    # LHS
    stack.append(__main__num_rocks)
    # RHS
    stack.append(__main__max_rocks)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs >= __rhs
    stack.append (__res)
    __if__146__cond = stack.pop ()
    # get condition from stack
    if (__if__146__cond):
        # Body
        # Break out of __while__61
        break
    # End of if
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(0)
    # LHS
    __main__while__61__block__62__block__147__rock_height = 0
    __rhs = stack.pop()
    __main__while__61__block__62__block__147__rock_height = __rhs
    stack.append (__main__while__61__block__62__block__147__rock_height)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
    # For-Loop
    # Init
    # Assignment - '='
    # RHS
    # Subtraction
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main__board)
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
    __res = __lhs - __rhs
    stack.append(__res)
    # LHS
    __main__while__61__block__62__block__147__for__148__i = 0
    __rhs = stack.pop()
    __main__while__61__block__62__block__147__for__148__i = __rhs
    stack.append (__main__while__61__block__62__block__147__for__148__i)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Greater Than or Equal to
        # LHS
        stack.append(__main__while__61__block__62__block__147__for__148__i)
        # RHS
        # Int Literal
        stack.append(0)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs >= __rhs
        stack.append (__res)
        __cond = stack.pop ()
        # break out of loop if condition is false
        if (__cond == 0): break
        # Body
        #-----------------------------------------------------------------
        # Code Block
        #-----------------------------------------------------------------
        # For-Loop
        # Init
        # Assignment - '='
        # RHS
        # Int Literal
        stack.append(1)
        # LHS
        __main__while__61__block__62__block__147__for__148__block__149__for__150__j = 0
        __rhs = stack.pop()
        __main__while__61__block__62__block__147__for__148__block__149__for__150__j = __rhs
        stack.append (__main__while__61__block__62__block__147__for__148__block__149__for__150__j)
        # Using an infinite loop so we can write a separate multi-line condition
        while (1):
            # Condition
            # Less Than
            # LHS
            stack.append(__main__while__61__block__62__block__147__for__148__block__149__for__150__j)
            # RHS
            # Int Literal
            stack.append(8)
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
            #-------------------------------------------------------------
            # If-Statement
            # Precomputing all if/elif conditions and give unique names
            # bc we can't have code between if and elif
            # Condition
            # Not Equal
            # LHS
            # Subscript
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__board)
            # RHS
            stack.append (__field____main____Vector__char__1____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main__while__61__block__62__block__147__for__148__i)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # OFFSET
            stack.append(__main__while__61__block__62__block__147__for__148__block__149__for__150__j)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            # Char Literal
            stack.append('.')
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs != __rhs
            stack.append (__res)
            __if__152__cond = stack.pop ()
            # get condition from stack
            if (__if__152__cond):
                # Body
                #---------------------------------------------------------
                # Code Block
                # Statement
                # Assignment - '='
                # RHS
                stack.append(__main__while__61__block__62__block__147__for__148__i)
                __rhs = stack.pop()
                __main__while__61__block__62__block__147__rock_height = __rhs
                stack.append (__main__while__61__block__62__block__147__rock_height)
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Break out of __for__150
                break
                #---------------------------------------------------------
            # End of if
            #-------------------------------------------------------------
            #-------------------------------------------------------------
            # Update
            # Pre-Increment
            # RHS
            stack.append(__main__while__61__block__62__block__147__for__148__block__149__for__150__j)
            __rhs = stack.pop ()
            __main__while__61__block__62__block__147__for__148__block__149__for__150__j = __main__while__61__block__62__block__147__for__148__block__149__for__150__j + 1
            __res = __main__while__61__block__62__block__147__for__148__block__149__for__150__j
            stack.append (__res)
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # If-Statement
        # Precomputing all if/elif conditions and give unique names
        # bc we can't have code between if and elif
        # Condition
        # Not Equal
        # LHS
        stack.append(__main__while__61__block__62__block__147__rock_height)
        # RHS
        # Int Literal
        stack.append(0)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs != __rhs
        stack.append (__res)
        __if__154__cond = stack.pop ()
        # get condition from stack
        if (__if__154__cond):
            # Body
            # Break out of __for__148
            break
        # End of if
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # Update
        # Pre-Decrement
        # RHS
        stack.append(__main__while__61__block__62__block__147__for__148__i)
        __rhs = stack.pop ()
        __main__while__61__block__62__block__147__for__148__i = __main__while__61__block__62__block__147__for__148__i - 1
        __res = __main__while__61__block__62__block__147__for__148__i
        stack.append (__res)
    #---------------------------------------------------------------------
    # Statement
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(2)
    # LHS
    __main__while__61__block__62__block__147__shape_height = 0
    __rhs = stack.pop()
    __main__while__61__block__62__block__147__shape_height = __rhs
    stack.append (__main__while__61__block__62__block__147__shape_height)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Char Literal
    stack.append('4')
    # LHS
    __main__while__61__block__62__block__147__rock_char = 0
    __rhs = stack.pop()
    __main__while__61__block__62__block__147__rock_char = __rhs
    stack.append (__main__while__61__block__62__block__147__rock_char)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Addition
    # LHS
    # Addition
    # LHS
    stack.append(__main__while__61__block__62__block__147__rock_height)
    # RHS
    # Int Literal
    stack.append(3)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs + __rhs
    stack.append(__res)
    # RHS
    stack.append(__main__while__61__block__62__block__147__shape_height)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs + __rhs
    stack.append(__res)
    # LHS
    __main__while__61__block__62__block__147__desired_height = 0
    __rhs = stack.pop()
    __main__while__61__block__62__block__147__desired_height = __rhs
    stack.append (__main__while__61__block__62__block__147__desired_height)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
    # While-Loop
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        # Subtraction
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
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
        __res = __lhs - __rhs
        stack.append(__res)
        # RHS
        stack.append(__main__while__61__block__62__block__147__desired_height)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs < __rhs
        stack.append (__res)
        __cond = stack.pop ()
        # break out of loop if condition is false
        if (__cond == 0): break
        # Body
        # Statement
        # Method Call - Vector<:char[]:>::pushBack(char[]) -> void
        # LHS
        stack.append(__main__board)
        # RHS
        # Arguments
        # String Literal
        stack.append([*("|.......|"+'\0')])
        __arg0 = stack.pop ()
        __obj = stack.pop ()
        __retval = __method____main____Vector__char__1____pushBack__char__1 (__obj, __arg0)
        stack.append (__retval)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

    # End of While
    #---------------------------------------------------------------------
    # Statement
    # Function Call - printboard(Vector<:char[]:>) -> void
    # Arguments
    stack.append(__main__board)
    __arg0 = stack.pop ()
    # *** printboard
    __res = __main____printboard__Vector__tparam0__char (__arg0)
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Array Constructor
    # Elements
    # Int Literal
    stack.append(3)
    # Int Literal
    stack.append(4)
    __elem1 = stack.pop ()
    __elem0 = stack.pop ()
    __list = [0] * 2
    __list[0] = __elem0
    __list[1] = __elem1
    stack.append (__list)
    # LHS
    __main__while__61__block__62__block__147__posx0 = 0
    __rhs = stack.pop()
    __main__while__61__block__62__block__147__posx0 = __rhs
    stack.append (__main__while__61__block__62__block__147__posx0)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Array Constructor
    # Elements
    # Int Literal
    stack.append(3)
    # Int Literal
    stack.append(4)
    __elem1 = stack.pop ()
    __elem0 = stack.pop ()
    __list = [0] * 2
    __list[0] = __elem0
    __list[1] = __elem1
    stack.append (__list)
    # LHS
    __main__while__61__block__62__block__147__posx1 = 0
    __rhs = stack.pop()
    __main__while__61__block__62__block__147__posx1 = __rhs
    stack.append (__main__while__61__block__62__block__147__posx1)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Addition
    # LHS
    # Addition
    # LHS
    stack.append(__main__while__61__block__62__block__147__rock_height)
    # RHS
    # Int Literal
    stack.append(3)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs + __rhs
    stack.append(__res)
    # RHS
    # Int Literal
    stack.append(1)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs + __rhs
    stack.append(__res)
    # LHS
    __main__while__61__block__62__block__147__posy = 0
    __rhs = stack.pop()
    __main__while__61__block__62__block__147__posy = __rhs
    stack.append (__main__while__61__block__62__block__147__posy)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main__while__61__block__62__block__147__rock_char)
    # LHS
    # Subscript assignment
    # LHS
    # Subscript
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main__board)
    # RHS
    stack.append (__field____main____Vector__char__1____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    stack.append(__main__while__61__block__62__block__147__posy)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    # OFFSET
    # Subscript
    # LHS
    stack.append(__main__while__61__block__62__block__147__posx0)
    # OFFSET
    # Int Literal
    stack.append(0)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    __offset = stack.pop()
    __pointer = stack.pop()
    __rhs = stack.pop()
    __pointer[__offset] = __rhs
    stack.append (__pointer[__offset])
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main__while__61__block__62__block__147__rock_char)
    # LHS
    # Subscript assignment
    # LHS
    # Subscript
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main__board)
    # RHS
    stack.append (__field____main____Vector__char__1____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    stack.append(__main__while__61__block__62__block__147__posy)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    # OFFSET
    # Subscript
    # LHS
    stack.append(__main__while__61__block__62__block__147__posx0)
    # OFFSET
    # Int Literal
    stack.append(1)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    __offset = stack.pop()
    __pointer = stack.pop()
    __rhs = stack.pop()
    __pointer[__offset] = __rhs
    stack.append (__pointer[__offset])
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main__while__61__block__62__block__147__rock_char)
    # LHS
    # Subscript assignment
    # LHS
    # Subscript
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main__board)
    # RHS
    stack.append (__field____main____Vector__char__1____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    # Addition
    # LHS
    stack.append(__main__while__61__block__62__block__147__posy)
    # RHS
    # Int Literal
    stack.append(1)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs + __rhs
    stack.append(__res)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    # OFFSET
    # Subscript
    # LHS
    stack.append(__main__while__61__block__62__block__147__posx1)
    # OFFSET
    # Int Literal
    stack.append(0)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    __offset = stack.pop()
    __pointer = stack.pop()
    __rhs = stack.pop()
    __pointer[__offset] = __rhs
    stack.append (__pointer[__offset])
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main__while__61__block__62__block__147__rock_char)
    # LHS
    # Subscript assignment
    # LHS
    # Subscript
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main__board)
    # RHS
    stack.append (__field____main____Vector__char__1____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    # Addition
    # LHS
    stack.append(__main__while__61__block__62__block__147__posy)
    # RHS
    # Int Literal
    stack.append(1)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs + __rhs
    stack.append(__res)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    # OFFSET
    # Subscript
    # LHS
    stack.append(__main__while__61__block__62__block__147__posx1)
    # OFFSET
    # Int Literal
    stack.append(1)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    __offset = stack.pop()
    __pointer = stack.pop()
    __rhs = stack.pop()
    __pointer[__offset] = __rhs
    stack.append (__pointer[__offset])
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Function Call - printboard(Vector<:char[]:>) -> void
    # Arguments
    stack.append(__main__board)
    __arg0 = stack.pop ()
    # *** printboard
    __res = __main____printboard__Vector__tparam0__char (__arg0)
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
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
        #-----------------------------------------------------------------
        # Code Block
        # Statement
        # Function Call - println(int) -> void
        # Arguments
        stack.append(__main__shift_index)
        __arg0 = stack.pop ()
        # *** println
        __res = __builtin__println__int (__arg0)
        stack.append (__res) # function call result
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Char Literal
        stack.append('.')
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__147__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__147__posx0)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Char Literal
        stack.append('.')
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__147__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__147__posx0)
        # OFFSET
        # Int Literal
        stack.append(1)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Char Literal
        stack.append('.')
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__while__61__block__62__block__147__posy)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__147__posx1)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Char Literal
        stack.append('.')
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__while__61__block__62__block__147__posy)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__147__posx1)
        # OFFSET
        # Int Literal
        stack.append(1)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
        # If-Statement
        # Precomputing all if/elif conditions and give unique names
        # bc we can't have code between if and elif
        # Condition
        # Equal
        # LHS
        # Subscript
        # LHS
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
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        stack.append(__main__shift_index)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        # Char Literal
        stack.append('<')
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs == __rhs
        stack.append (__res)
        __if__158__cond = stack.pop ()
        # get condition from stack
        if (__if__158__cond):
            # Body
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Function Call - println(char[]) -> void
            # Arguments
            # String Literal
            stack.append([*("shift left"+'\0')])
            __arg0 = stack.pop ()
            # *** println
            __res = __builtin__println__char__1 (__arg0)
            stack.append (__res) # function call result
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            #-------------------------------------------------------------
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
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__board)
            # RHS
            stack.append (__field____main____Vector__char__1____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main__while__61__block__62__block__147__posy)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # OFFSET
            # Subtraction
            # LHS
            # Subscript
            # LHS
            stack.append(__main__while__61__block__62__block__147__posx0)
            # OFFSET
            # Int Literal
            stack.append(0)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            # Int Literal
            stack.append(1)
            __rhs = stack.pop()
            __lhs = stack.pop()
            __res = __lhs - __rhs
            stack.append(__res)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            # Char Literal
            stack.append('.')
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs == __rhs
            stack.append (__res)
            # Only check rhs if lhs was true
            __lhs = stack[-1]
            if (__lhs):
                # RHS
                # Equal
                # LHS
                # Subscript
                # LHS
                # Subscript
                # LHS
                # Member Accessor
                # LHS
                stack.append(__main__board)
                # RHS
                stack.append (__field____main____Vector__char__1____data)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                # OFFSET
                # Addition
                # LHS
                stack.append(__main__while__61__block__62__block__147__posy)
                # RHS
                # Int Literal
                stack.append(1)
                __rhs = stack.pop()
                __lhs = stack.pop()
                __res = __lhs + __rhs
                stack.append(__res)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # OFFSET
                # Subtraction
                # LHS
                # Subscript
                # LHS
                stack.append(__main__while__61__block__62__block__147__posx1)
                # OFFSET
                # Int Literal
                stack.append(0)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # RHS
                # Int Literal
                stack.append(1)
                __rhs = stack.pop()
                __lhs = stack.pop()
                __res = __lhs - __rhs
                stack.append(__res)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # RHS
                # Char Literal
                stack.append('.')
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs == __rhs
                stack.append (__res)
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs and __rhs
            else:
                __res = stack.pop ()
            stack.append (__res)
            __if__160__cond = stack.pop ()
            # get condition from stack
            if (__if__160__cond):
                # Body
                #---------------------------------------------------------
                # Code Block
                # Statement
                # Assignment - '-='
                # RHS
                # Int Literal
                stack.append(1)
                # LHS
                # Subscript assignment
                # LHS
                stack.append(__main__while__61__block__62__block__147__posx0)
                # OFFSET
                # Int Literal
                stack.append(0)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __pointer[__offset] - __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Statement
                # Assignment - '-='
                # RHS
                # Int Literal
                stack.append(1)
                # LHS
                # Subscript assignment
                # LHS
                stack.append(__main__while__61__block__62__block__147__posx0)
                # OFFSET
                # Int Literal
                stack.append(1)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __pointer[__offset] - __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Statement
                # Assignment - '-='
                # RHS
                # Int Literal
                stack.append(1)
                # LHS
                # Subscript assignment
                # LHS
                stack.append(__main__while__61__block__62__block__147__posx1)
                # OFFSET
                # Int Literal
                stack.append(0)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __pointer[__offset] - __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Statement
                # Assignment - '-='
                # RHS
                # Int Literal
                stack.append(1)
                # LHS
                # Subscript assignment
                # LHS
                stack.append(__main__while__61__block__62__block__147__posx1)
                # OFFSET
                # Int Literal
                stack.append(1)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __pointer[__offset] - __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                #---------------------------------------------------------
            # End of if
            #-------------------------------------------------------------
            #-------------------------------------------------------------
        #-----------------------------------------------------------------
        # Else-Statement
        else:
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Function Call - println(char[]) -> void
            # Arguments
            # String Literal
            stack.append([*("shift right"+'\0')])
            __arg0 = stack.pop ()
            # *** println
            __res = __builtin__println__char__1 (__arg0)
            stack.append (__res) # function call result
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            #-------------------------------------------------------------
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
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__board)
            # RHS
            stack.append (__field____main____Vector__char__1____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main__while__61__block__62__block__147__posy)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # OFFSET
            # Addition
            # LHS
            # Subscript
            # LHS
            stack.append(__main__while__61__block__62__block__147__posx0)
            # OFFSET
            # Int Literal
            stack.append(1)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            # Int Literal
            stack.append(1)
            __rhs = stack.pop()
            __lhs = stack.pop()
            __res = __lhs + __rhs
            stack.append(__res)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            # Char Literal
            stack.append('.')
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs == __rhs
            stack.append (__res)
            # Only check rhs if lhs was true
            __lhs = stack[-1]
            if (__lhs):
                # RHS
                # Equal
                # LHS
                # Subscript
                # LHS
                # Subscript
                # LHS
                # Member Accessor
                # LHS
                stack.append(__main__board)
                # RHS
                stack.append (__field____main____Vector__char__1____data)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                # OFFSET
                # Addition
                # LHS
                stack.append(__main__while__61__block__62__block__147__posy)
                # RHS
                # Int Literal
                stack.append(1)
                __rhs = stack.pop()
                __lhs = stack.pop()
                __res = __lhs + __rhs
                stack.append(__res)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # OFFSET
                # Addition
                # LHS
                # Subscript
                # LHS
                stack.append(__main__while__61__block__62__block__147__posx1)
                # OFFSET
                # Int Literal
                stack.append(1)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # RHS
                # Int Literal
                stack.append(1)
                __rhs = stack.pop()
                __lhs = stack.pop()
                __res = __lhs + __rhs
                stack.append(__res)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # RHS
                # Char Literal
                stack.append('.')
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs == __rhs
                stack.append (__res)
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs and __rhs
            else:
                __res = stack.pop ()
            stack.append (__res)
            __if__163__cond = stack.pop ()
            # get condition from stack
            if (__if__163__cond):
                # Body
                #---------------------------------------------------------
                # Code Block
                # Statement
                # Assignment - '+='
                # RHS
                # Int Literal
                stack.append(1)
                # LHS
                # Subscript assignment
                # LHS
                stack.append(__main__while__61__block__62__block__147__posx0)
                # OFFSET
                # Int Literal
                stack.append(0)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __pointer[__offset] + __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Statement
                # Assignment - '+='
                # RHS
                # Int Literal
                stack.append(1)
                # LHS
                # Subscript assignment
                # LHS
                stack.append(__main__while__61__block__62__block__147__posx0)
                # OFFSET
                # Int Literal
                stack.append(1)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __pointer[__offset] + __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Statement
                # Assignment - '+='
                # RHS
                # Int Literal
                stack.append(1)
                # LHS
                # Subscript assignment
                # LHS
                stack.append(__main__while__61__block__62__block__147__posx1)
                # OFFSET
                # Int Literal
                stack.append(0)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __pointer[__offset] + __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Statement
                # Assignment - '+='
                # RHS
                # Int Literal
                stack.append(1)
                # LHS
                # Subscript assignment
                # LHS
                stack.append(__main__while__61__block__62__block__147__posx1)
                # OFFSET
                # Int Literal
                stack.append(1)
                __offset = stack.pop()
                __pointer = stack.pop()
                __rhs = stack.pop()
                __pointer[__offset] = __pointer[__offset] + __rhs
                stack.append (__pointer[__offset])
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                #---------------------------------------------------------
            # End of if
            #-------------------------------------------------------------
            #-------------------------------------------------------------
        #-----------------------------------------------------------------
        # End of if
        #-----------------------------------------------------------------
        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main__while__61__block__62__block__147__rock_char)
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__147__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__147__posx0)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main__while__61__block__62__block__147__rock_char)
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__147__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__147__posx0)
        # OFFSET
        # Int Literal
        stack.append(1)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main__while__61__block__62__block__147__rock_char)
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__while__61__block__62__block__147__posy)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__147__posx1)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main__while__61__block__62__block__147__rock_char)
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__while__61__block__62__block__147__posy)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__147__posx1)
        # OFFSET
        # Int Literal
        stack.append(1)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Modulus
        # LHS
        # Addition
        # LHS
        stack.append(__main__shift_index)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        # RHS
        stack.append(__main__shift_max)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs % __rhs
        stack.append(__res)
        __rhs = stack.pop()
        __main__shift_index = __rhs
        stack.append (__main__shift_index)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Function Call - printboard(Vector<:char[]:>) -> void
        # Arguments
        stack.append(__main__board)
        __arg0 = stack.pop ()
        # *** printboard
        __res = __main____printboard__Vector__tparam0__char (__arg0)
        stack.append (__res) # function call result
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
        # If-Statement
        # Precomputing all if/elif conditions and give unique names
        # bc we can't have code between if and elif
        # Condition
        # OR
        # LHS
        # OR
        # LHS
        # Not Equal
        # LHS
        # Subscript
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Subtraction
        # LHS
        stack.append(__main__while__61__block__62__block__147__posy)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs - __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__147__posx0)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        # Char Literal
        stack.append('.')
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs != __rhs
        stack.append (__res)
        # RHS
        # Not Equal
        # LHS
        # Subscript
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Subtraction
        # LHS
        stack.append(__main__while__61__block__62__block__147__posy)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs - __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__147__posx0)
        # OFFSET
        # Int Literal
        stack.append(1)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        # Char Literal
        stack.append('.')
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs != __rhs
        stack.append (__res)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs or __rhs
        stack.append (__res)
        # RHS
        # Equal
        # LHS
        # Subtraction
        # LHS
        stack.append(__main__while__61__block__62__block__147__posy)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs - __rhs
        stack.append(__res)
        # RHS
        # Int Literal
        stack.append(0)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs == __rhs
        stack.append (__res)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs or __rhs
        stack.append (__res)
        __if__165__cond = stack.pop ()
        # get condition from stack
        if (__if__165__cond):
            # Body
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Function Call - println(char[]) -> void
            # Arguments
            # String Literal
            stack.append([*("rock at rest"+'\0')])
            __arg0 = stack.pop ()
            # *** println
            __res = __builtin__println__char__1 (__arg0)
            stack.append (__res) # function call result
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            # Break out of __while__156
            break
            #-------------------------------------------------------------
        # End of if
        #-----------------------------------------------------------------
        # Statement
        # Assignment - '='
        # RHS
        # Char Literal
        stack.append('.')
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__147__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__147__posx0)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Char Literal
        stack.append('.')
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__147__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__147__posx0)
        # OFFSET
        # Int Literal
        stack.append(1)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Char Literal
        stack.append('.')
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__while__61__block__62__block__147__posy)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__147__posx1)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Char Literal
        stack.append('.')
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__while__61__block__62__block__147__posy)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__147__posx1)
        # OFFSET
        # Int Literal
        stack.append(1)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '-='
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __main__while__61__block__62__block__147__posy = __main__while__61__block__62__block__147__posy - __rhs
        stack.append (__main__while__61__block__62__block__147__posy)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main__while__61__block__62__block__147__rock_char)
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__147__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__147__posx0)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main__while__61__block__62__block__147__rock_char)
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__while__61__block__62__block__147__posy)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__147__posx0)
        # OFFSET
        # Int Literal
        stack.append(1)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main__while__61__block__62__block__147__rock_char)
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__while__61__block__62__block__147__posy)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__147__posx1)
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        stack.append(__main__while__61__block__62__block__147__rock_char)
        # LHS
        # Subscript assignment
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Addition
        # LHS
        stack.append(__main__while__61__block__62__block__147__posy)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        # Subscript
        # LHS
        stack.append(__main__while__61__block__62__block__147__posx1)
        # OFFSET
        # Int Literal
        stack.append(1)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __offset = stack.pop()
        __pointer = stack.pop()
        __rhs = stack.pop()
        __pointer[__offset] = __rhs
        stack.append (__pointer[__offset])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Function Call - printboard(Vector<:char[]:>) -> void
        # Arguments
        stack.append(__main__board)
        __arg0 = stack.pop ()
        # *** printboard
        __res = __main____printboard__Vector__tparam0__char (__arg0)
        stack.append (__res) # function call result
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
    # End of While
    #---------------------------------------------------------------------
    # Statement
    # Function Call - printboard(Vector<:char[]:>) -> void
    # Arguments
    stack.append(__main__board)
    __arg0 = stack.pop ()
    # *** printboard
    __res = __main____printboard__Vector__tparam0__char (__arg0)
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
    # Statement
    # Assignment - '+='
    # RHS
    # Int Literal
    stack.append(1)
    __rhs = stack.pop()
    __main__num_rocks = __main__num_rocks + __rhs
    stack.append (__main__num_rocks)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
    # If-Statement
    # Precomputing all if/elif conditions and give unique names
    # bc we can't have code between if and elif
    # Condition
    # Greater Than or Equal to
    # LHS
    stack.append(__main__num_rocks)
    # RHS
    stack.append(__main__max_rocks)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs >= __rhs
    stack.append (__res)
    __if__167__cond = stack.pop ()
    # get condition from stack
    if (__if__167__cond):
        # Body
        # Break out of __while__61
        break
    # End of if
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
# End of While
#-------------------------------------------------------------------------
# Statement
# Assignment - '='
# RHS
# Int Literal
stack.append(0)
# LHS
__main__rock_height = 0
__rhs = stack.pop()
__main__rock_height = __rhs
stack.append (__main__rock_height)
# Statement results can be ignored
stack.pop ()
# End Statement

#-------------------------------------------------------------------------
# For-Loop
# Init
# Assignment - '='
# RHS
# Subtraction
# LHS
# Member Accessor
# LHS
stack.append(__main__board)
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
__res = __lhs - __rhs
stack.append(__res)
# LHS
__main__for__168__i = 0
__rhs = stack.pop()
__main__for__168__i = __rhs
stack.append (__main__for__168__i)
# Using an infinite loop so we can write a separate multi-line condition
while (1):
    # Condition
    # Greater Than or Equal to
    # LHS
    stack.append(__main__for__168__i)
    # RHS
    # Int Literal
    stack.append(0)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs >= __rhs
    stack.append (__res)
    __cond = stack.pop ()
    # break out of loop if condition is false
    if (__cond == 0): break
    # Body
    #---------------------------------------------------------------------
    # Code Block
    #---------------------------------------------------------------------
    # For-Loop
    # Init
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(1)
    # LHS
    __main__for__168__block__169__for__170__j = 0
    __rhs = stack.pop()
    __main__for__168__block__169__for__170__j = __rhs
    stack.append (__main__for__168__block__169__for__170__j)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        stack.append(__main__for__168__block__169__for__170__j)
        # RHS
        # Int Literal
        stack.append(8)
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
        # Not Equal
        # LHS
        # Subscript
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__board)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__for__168__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        stack.append(__main__for__168__block__169__for__170__j)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        # Char Literal
        stack.append('.')
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs != __rhs
        stack.append (__res)
        __if__172__cond = stack.pop ()
        # get condition from stack
        if (__if__172__cond):
            # Body
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Assignment - '='
            # RHS
            stack.append(__main__for__168__i)
            __rhs = stack.pop()
            __main__rock_height = __rhs
            stack.append (__main__rock_height)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            # Break out of __for__170
            break
            #-------------------------------------------------------------
        # End of if
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # Update
        # Pre-Increment
        # RHS
        stack.append(__main__for__168__block__169__for__170__j)
        __rhs = stack.pop ()
        __main__for__168__block__169__for__170__j = __main__for__168__block__169__for__170__j + 1
        __res = __main__for__168__block__169__for__170__j
        stack.append (__res)
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    # If-Statement
    # Precomputing all if/elif conditions and give unique names
    # bc we can't have code between if and elif
    # Condition
    # Not Equal
    # LHS
    stack.append(__main__rock_height)
    # RHS
    # Int Literal
    stack.append(0)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs != __rhs
    stack.append (__res)
    __if__174__cond = stack.pop ()
    # get condition from stack
    if (__if__174__cond):
        # Body
        # Break out of __for__168
        break
    # End of if
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    # Update
    # Pre-Decrement
    # RHS
    stack.append(__main__for__168__i)
    __rhs = stack.pop ()
    __main__for__168__i = __main__for__168__i - 1
    __res = __main__for__168__i
    stack.append (__res)
#-------------------------------------------------------------------------
# Statement
# Function Call - printboard2(Vector<:char[]:>) -> void
# Arguments
stack.append(__main__board)
__arg0 = stack.pop ()
# *** printboard2
__res = __main____printboard2__Vector__tparam0__char (__arg0)
stack.append (__res) # function call result
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Function Call - println(int) -> void
# Arguments
stack.append(__main__rock_height)
__arg0 = stack.pop ()
# *** println
__res = __builtin__println__int (__arg0)
stack.append (__res) # function call result
# Statement results can be ignored
stack.pop ()
# End Statement


#=========================================================================
#### END OF CODE ########################################################
#=========================================================================

