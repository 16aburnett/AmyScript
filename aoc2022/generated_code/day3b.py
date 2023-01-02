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
    print (''.join(s), end="")

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
    print (''.join(v))

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

# Statement
# Assignment - '='
# RHS
# String Literal
stack.append(" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"+'\0')
# LHS
__main__letters = 0
__rhs = stack.pop()
__main__letters = __rhs
stack.append (__main__letters)
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
# Int Literal
stack.append(26)
# RHS
# Int Literal
stack.append(26)
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
__main__letters_size = 0
__rhs = stack.pop()
__main__letters_size = __rhs
stack.append (__main__letters_size)
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
#-------------------------------------------------------------------------
# For-Loop
# Init
# Assignment - '='
# RHS
# Int Literal
stack.append(0)
# LHS
__main__for__14__l = 0
__rhs = stack.pop()
__main__for__14__l = __rhs
stack.append (__main__for__14__l)
# Using an infinite loop so we can write a separate multi-line condition
while (1):
    # Condition
    # Less Than
    # LHS
    stack.append(__main__for__14__l)
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
    # Addition
    # LHS
    stack.append(__main__for__14__l)
    # RHS
    # Int Literal
    stack.append(0)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs + __rhs
    stack.append(__res)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    # LHS
    __main__for__14__block__15__line0 = 0
    __rhs = stack.pop()
    __main__for__14__block__15__line0 = __rhs
    stack.append (__main__for__14__block__15__line0)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(0)
    # LHS
    __main__for__14__block__15__line0_size = 0
    __rhs = stack.pop()
    __main__for__14__block__15__line0_size = __rhs
    stack.append (__main__for__14__block__15__line0_size)
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
        stack.append(__main__for__14__block__15__line0)
        # OFFSET
        # Post-Increment
        __res = __main__for__14__block__15__line0_size
        __main__for__14__block__15__line0_size = __main__for__14__block__15__line0_size + 1
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
    # Statement
    # Pre-Decrement
    # RHS
    stack.append(__main__for__14__block__15__line0_size)
    __rhs = stack.pop ()
    __main__for__14__block__15__line0_size = __main__for__14__block__15__line0_size - 1
    __res = __main__for__14__block__15__line0_size
    stack.append (__res)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

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
    # Addition
    # LHS
    stack.append(__main__for__14__l)
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
    # LHS
    __main__for__14__block__15__line1 = 0
    __rhs = stack.pop()
    __main__for__14__block__15__line1 = __rhs
    stack.append (__main__for__14__block__15__line1)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(0)
    # LHS
    __main__for__14__block__15__line1_size = 0
    __rhs = stack.pop()
    __main__for__14__block__15__line1_size = __rhs
    stack.append (__main__for__14__block__15__line1_size)
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
        stack.append(__main__for__14__block__15__line1)
        # OFFSET
        # Post-Increment
        __res = __main__for__14__block__15__line1_size
        __main__for__14__block__15__line1_size = __main__for__14__block__15__line1_size + 1
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
    # Statement
    # Pre-Decrement
    # RHS
    stack.append(__main__for__14__block__15__line1_size)
    __rhs = stack.pop ()
    __main__for__14__block__15__line1_size = __main__for__14__block__15__line1_size - 1
    __res = __main__for__14__block__15__line1_size
    stack.append (__res)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

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
    # Addition
    # LHS
    stack.append(__main__for__14__l)
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
    # LHS
    __main__for__14__block__15__line2 = 0
    __rhs = stack.pop()
    __main__for__14__block__15__line2 = __rhs
    stack.append (__main__for__14__block__15__line2)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(0)
    # LHS
    __main__for__14__block__15__line2_size = 0
    __rhs = stack.pop()
    __main__for__14__block__15__line2_size = __rhs
    stack.append (__main__for__14__block__15__line2_size)
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
        stack.append(__main__for__14__block__15__line2)
        # OFFSET
        # Post-Increment
        __res = __main__for__14__block__15__line2_size
        __main__for__14__block__15__line2_size = __main__for__14__block__15__line2_size + 1
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
    # Statement
    # Pre-Decrement
    # RHS
    stack.append(__main__for__14__block__15__line2_size)
    __rhs = stack.pop ()
    __main__for__14__block__15__line2_size = __main__for__14__block__15__line2_size - 1
    __res = __main__for__14__block__15__line2_size
    stack.append (__res)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Char Literal
    stack.append('0')
    # LHS
    __main__for__14__block__15__common = 0
    __rhs = stack.pop()
    __main__for__14__block__15__common = __rhs
    stack.append (__main__for__14__block__15__common)
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
    __main__for__14__block__15__for__19__i = 0
    __rhs = stack.pop()
    __main__for__14__block__15__for__19__i = __rhs
    stack.append (__main__for__14__block__15__for__19__i)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        stack.append(__main__for__14__block__15__for__19__i)
        # RHS
        # Subtraction
        # LHS
        stack.append(__main__for__14__block__15__line0_size)
        # RHS
        # Int Literal
        stack.append(1)
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
        #-----------------------------------------------------------------
        # For-Loop
        # Init
        # Assignment - '='
        # RHS
        # Int Literal
        stack.append(0)
        # LHS
        __main__for__14__block__15__for__19__block__20__for__21__j = 0
        __rhs = stack.pop()
        __main__for__14__block__15__for__19__block__20__for__21__j = __rhs
        stack.append (__main__for__14__block__15__for__19__block__20__for__21__j)
        # Using an infinite loop so we can write a separate multi-line condition
        while (1):
            # Condition
            # Less Than
            # LHS
            stack.append(__main__for__14__block__15__for__19__block__20__for__21__j)
            # RHS
            # Subtraction
            # LHS
            stack.append(__main__for__14__block__15__line1_size)
            # RHS
            # Int Literal
            stack.append(1)
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
            #-------------------------------------------------------------
            # Code Block
            #-------------------------------------------------------------
            # If-Statement
            # Precomputing all if/elif conditions and give unique names
            # bc we can't have code between if and elif
            # Condition
            # Equal
            # LHS
            # Subscript
            # LHS
            stack.append(__main__for__14__block__15__line0)
            # OFFSET
            stack.append(__main__for__14__block__15__for__19__i)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            # Subscript
            # LHS
            stack.append(__main__for__14__block__15__line1)
            # OFFSET
            stack.append(__main__for__14__block__15__for__19__block__20__for__21__j)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs == __rhs
            stack.append (__res)
            __if__23__cond = stack.pop ()
            # get condition from stack
            if (__if__23__cond):
                # Body
                #---------------------------------------------------------
                # Code Block
                #---------------------------------------------------------
                # For-Loop
                # Init
                # Assignment - '='
                # RHS
                # Int Literal
                stack.append(0)
                # LHS
                __main__for__14__block__15__for__19__block__20__for__21__block__22__if__23__block__24__for__25__k = 0
                __rhs = stack.pop()
                __main__for__14__block__15__for__19__block__20__for__21__block__22__if__23__block__24__for__25__k = __rhs
                stack.append (__main__for__14__block__15__for__19__block__20__for__21__block__22__if__23__block__24__for__25__k)
                # Using an infinite loop so we can write a separate multi-line condition
                while (1):
                    # Condition
                    # Less Than
                    # LHS
                    stack.append(__main__for__14__block__15__for__19__block__20__for__21__block__22__if__23__block__24__for__25__k)
                    # RHS
                    # Subtraction
                    # LHS
                    stack.append(__main__for__14__block__15__line2_size)
                    # RHS
                    # Int Literal
                    stack.append(1)
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
                    #-----------------------------------------------------
                    # Code Block
                    #-----------------------------------------------------
                    # If-Statement
                    # Precomputing all if/elif conditions and give unique names
                    # bc we can't have code between if and elif
                    # Condition
                    # Equal
                    # LHS
                    # Subscript
                    # LHS
                    stack.append(__main__for__14__block__15__line0)
                    # OFFSET
                    stack.append(__main__for__14__block__15__for__19__i)
                    __offset = stack.pop ()
                    __pointer = stack.pop ()
                    stack.append (__pointer[__offset])
                    # RHS
                    # Subscript
                    # LHS
                    stack.append(__main__for__14__block__15__line2)
                    # OFFSET
                    stack.append(__main__for__14__block__15__for__19__block__20__for__21__block__22__if__23__block__24__for__25__k)
                    __offset = stack.pop ()
                    __pointer = stack.pop ()
                    stack.append (__pointer[__offset])
                    __rhs = stack.pop ()
                    __lhs = stack.pop ()
                    __res = __lhs == __rhs
                    stack.append (__res)
                    __if__27__cond = stack.pop ()
                    # get condition from stack
                    if (__if__27__cond):
                        # Body
                        #-------------------------------------------------
                        # Code Block
                        # Statement
                        # Assignment - '='
                        # RHS
                        # Subscript
                        # LHS
                        stack.append(__main__for__14__block__15__line0)
                        # OFFSET
                        stack.append(__main__for__14__block__15__for__19__i)
                        __offset = stack.pop ()
                        __pointer = stack.pop ()
                        stack.append (__pointer[__offset])
                        __rhs = stack.pop()
                        __main__for__14__block__15__common = __rhs
                        stack.append (__main__for__14__block__15__common)
                        # Statement results can be ignored
                        stack.pop ()
                        # End Statement

                        #-------------------------------------------------
                    # End of if
                    #-----------------------------------------------------
                    #-----------------------------------------------------
                    # Update
                    # Pre-Increment
                    # RHS
                    stack.append(__main__for__14__block__15__for__19__block__20__for__21__block__22__if__23__block__24__for__25__k)
                    __rhs = stack.pop ()
                    __main__for__14__block__15__for__19__block__20__for__21__block__22__if__23__block__24__for__25__k = __main__for__14__block__15__for__19__block__20__for__21__block__22__if__23__block__24__for__25__k + 1
                    __res = __main__for__14__block__15__for__19__block__20__for__21__block__22__if__23__block__24__for__25__k
                    stack.append (__res)
                #---------------------------------------------------------
                #---------------------------------------------------------
            # End of if
            #-------------------------------------------------------------
            #-------------------------------------------------------------
            # Update
            # Pre-Increment
            # RHS
            stack.append(__main__for__14__block__15__for__19__block__20__for__21__j)
            __rhs = stack.pop ()
            __main__for__14__block__15__for__19__block__20__for__21__j = __main__for__14__block__15__for__19__block__20__for__21__j + 1
            __res = __main__for__14__block__15__for__19__block__20__for__21__j
            stack.append (__res)
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # Update
        # Pre-Increment
        # RHS
        stack.append(__main__for__14__block__15__for__19__i)
        __rhs = stack.pop ()
        __main__for__14__block__15__for__19__i = __main__for__14__block__15__for__19__i + 1
        __res = __main__for__14__block__15__for__19__i
        stack.append (__res)
    #---------------------------------------------------------------------
    # Statement
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(0)
    # LHS
    __main__for__14__block__15__score = 0
    __rhs = stack.pop()
    __main__for__14__block__15__score = __rhs
    stack.append (__main__for__14__block__15__score)
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
    __main__for__14__block__15__for__29__i = 0
    __rhs = stack.pop()
    __main__for__14__block__15__for__29__i = __rhs
    stack.append (__main__for__14__block__15__for__29__i)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        stack.append(__main__for__14__block__15__for__29__i)
        # RHS
        stack.append(__main__letters_size)
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
        stack.append(__main__letters)
        # OFFSET
        stack.append(__main__for__14__block__15__for__29__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        stack.append(__main__for__14__block__15__common)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs == __rhs
        stack.append (__res)
        __if__31__cond = stack.pop ()
        # get condition from stack
        if (__if__31__cond):
            # Body
            # Statement
            # Assignment - '='
            # RHS
            stack.append(__main__for__14__block__15__for__29__i)
            __rhs = stack.pop()
            __main__for__14__block__15__score = __rhs
            stack.append (__main__for__14__block__15__score)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

        # End of if
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # Update
        # Pre-Increment
        # RHS
        stack.append(__main__for__14__block__15__for__29__i)
        __rhs = stack.pop ()
        __main__for__14__block__15__for__29__i = __main__for__14__block__15__for__29__i + 1
        __res = __main__for__14__block__15__for__29__i
        stack.append (__res)
    #---------------------------------------------------------------------
    # Statement
    # Assignment - '+='
    # RHS
    stack.append(__main__for__14__block__15__score)
    __rhs = stack.pop()
    __main__total = __main__total + __rhs
    stack.append (__main__total)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
    # Update
    # Assignment - '+='
    # RHS
    # Int Literal
    stack.append(3)
    __rhs = stack.pop()
    __main__for__14__l = __main__for__14__l + __rhs
    stack.append (__main__for__14__l)
#-------------------------------------------------------------------------
# Statement
# Function Call - println(int) -> void
# Arguments
stack.append(__main__total)
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

