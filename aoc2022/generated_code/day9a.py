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

#=========================================================================
# Class Declaration - __main____Vector__Point inherits __builtin____main__Object
# Creating Dispatch Table (will be populated later)
__dtable____main____Vector__Point = []
#-------------------------------------------------------------------------
# Field - Point[] Vector<:Point:>::data
__field____main____Vector__Point____data = 1
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Field - int Vector<:Point:>::size
__field____main____Vector__Point____size = 2
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Field - int Vector<:Point:>::capacity
__field____main____Vector__Point____capacity = 3
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Constructor Declaration - Vector<:Point:>::Vector() -> Vector<:Point:>
def __ctor____main____Vector__Point____Vector ():
    # Creating Class Instance
    this = [0] * 4
    # Add Dispatch Table
    this[0] = __dtable____main____Vector__Point
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
    stack.append(__field____main____Vector__Point____capacity)
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
    stack.append(__field____main____Vector__Point____size)
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
    stack.append (__field____main____Vector__Point____capacity)
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
    stack.append(__field____main____Vector__Point____data)
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
# End Constructor Declaration - __ctor____main____Vector__Point____Vector
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Constructor Declaration - Vector<:Point:>::Vector(int) -> Vector<:Point:>
def __ctor____main____Vector__Point____Vector__int (__main____Vector__Point__Vector__size):
    # Creating Class Instance
    this = [0] * 4
    # Add Dispatch Table
    this[0] = __dtable____main____Vector__Point
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Assignment - '='
    # RHS
    # Addition
    # LHS
    stack.append(__main____Vector__Point__Vector__size)
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
    stack.append(__field____main____Vector__Point____capacity)
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
    stack.append(__main____Vector__Point__Vector__size)
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append(__field____main____Vector__Point____size)
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
    stack.append (__field____main____Vector__Point____capacity)
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
    stack.append(__field____main____Vector__Point____data)
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
# End Constructor Declaration - __ctor____main____Vector__Point____Vector__int
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vector<:Point:>::pushBack(Point) -> void
def __method____main____Vector__Point____pushBack__Point (this, __main____Vector__Point__pushBack__val):
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
    stack.append (__field____main____Vector__Point____size)
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
    stack.append (__field____main____Vector__Point____capacity)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs >= __rhs
    stack.append (__res)
    __if__15__cond = stack.pop ()
    # get condition from stack
    if (__if__15__cond):
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
        stack.append (__field____main____Vector__Point____capacity)
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
        stack.append(__field____main____Vector__Point____capacity)
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
        stack.append (__field____main____Vector__Point____capacity)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        __dim = stack.pop ()
        __res = [None] * __dim
        stack.append (__res)
        # LHS
        __main____Vector__Point__pushBack__block__14__if__15__block__16__nData = 0
        __rhs = stack.pop()
        __main____Vector__Point__pushBack__block__14__if__15__block__16__nData = __rhs
        stack.append (__main____Vector__Point__pushBack__block__14__if__15__block__16__nData)
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
        __main____Vector__Point__pushBack__block__14__if__15__block__16__for__17__i = 0
        __rhs = stack.pop()
        __main____Vector__Point__pushBack__block__14__if__15__block__16__for__17__i = __rhs
        stack.append (__main____Vector__Point__pushBack__block__14__if__15__block__16__for__17__i)
        # Using an infinite loop so we can write a separate multi-line condition
        while (1):
            # Condition
            # Less Than
            # LHS
            stack.append(__main____Vector__Point__pushBack__block__14__if__15__block__16__for__17__i)
            # RHS
            # Member Accessor
            # LHS
            stack.append(this)
            # RHS
            stack.append (__field____main____Vector__Point____size)
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
            stack.append (__field____main____Vector__Point____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main____Vector__Point__pushBack__block__14__if__15__block__16__for__17__i)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # LHS
            # Subscript assignment
            # LHS
            stack.append(__main____Vector__Point__pushBack__block__14__if__15__block__16__nData)
            # OFFSET
            stack.append(__main____Vector__Point__pushBack__block__14__if__15__block__16__for__17__i)
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
            stack.append(__main____Vector__Point__pushBack__block__14__if__15__block__16__for__17__i)
            __rhs = stack.pop ()
            __main____Vector__Point__pushBack__block__14__if__15__block__16__for__17__i = __main____Vector__Point__pushBack__block__14__if__15__block__16__for__17__i + 1
            __res = __main____Vector__Point__pushBack__block__14__if__15__block__16__for__17__i
            stack.append (__res)
        #-----------------------------------------------------------------
        # Statement
        # Member Accessor
        # LHS
        stack.append(this)
        # RHS
        stack.append (__field____main____Vector__Point____data)
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
        stack.append(__main____Vector__Point__pushBack__block__14__if__15__block__16__nData)
        # LHS
        # Member Accessor Assignment
        # LHS
        stack.append(this)
        # RHS
        stack.append(__field____main____Vector__Point____data)
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
    stack.append(__main____Vector__Point__pushBack__val)
    # LHS
    # Subscript assignment
    # LHS
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__Point____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__Point____size)
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
    stack.append (__field____main____Vector__Point____size)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __rhs = stack.pop ()
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__Point____size)
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
# End Method Declaration - __method____main____Vector__Point____pushBack__Point
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vector<:Point:>::popBack() -> Point
def __method____main____Vector__Point____popBack (this):
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
    stack.append (__field____main____Vector__Point____data)
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
    stack.append (__field____main____Vector__Point____size)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __rhs = stack.pop ()
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__Point____size)
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
# End Method Declaration - __method____main____Vector__Point____popBack
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vector<:Point:>::clear() -> void
def __method____main____Vector__Point____clear (this):
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
        stack.append (__field____main____Vector__Point____size)
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
        # Method Call - Vector<:Point:>::popBack() -> Point
        # LHS
        stack.append(this)
        # RHS
        # Arguments
        __obj = stack.pop ()
        __retval = __method____main____Vector__Point____popBack (__obj)
        stack.append (__retval)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

    # End of While
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    return 0
# End Method Declaration - __method____main____Vector__Point____clear
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vector<:Point:>::get(int) -> Point
def __method____main____Vector__Point____get__int (this, __main____Vector__Point__get__index):
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
    stack.append (__field____main____Vector__Point____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    stack.append(__main____Vector__Point__get__index)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    __rVal = stack.pop ()
    return __rVal
    #---------------------------------------------------------------------
    return 0
# End Method Declaration - __method____main____Vector__Point____get__int
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vector<:Point:>::set(int, Point) -> void
def __method____main____Vector__Point____set__int__Point (this, __main____Vector__Point__set__index, __main____Vector__Point__set__value):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main____Vector__Point__set__value)
    # LHS
    # Subscript assignment
    # LHS
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__Point____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    stack.append(__main____Vector__Point__set__index)
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
# End Method Declaration - __method____main____Vector__Point____set__int__Point
#-------------------------------------------------------------------------

# Populate Dispatch Table
__dtable____main____Vector__Point = [__method____main____Vector__Point____pushBack__Point, __method____main____Vector__Point____popBack, __method____main____Vector__Point____clear, __method____main____Vector__Point____get__int, __method____main____Vector__Point____set__int__Point]
# End Class Declaration - __main____Vector__Point
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
    __if__25__cond = stack.pop ()
    # get condition from stack
    if (__if__25__cond):
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
    __main__strlen__block__24__size = 0
    __rhs = stack.pop()
    __main__strlen__block__24__size = __rhs
    stack.append (__main__strlen__block__24__size)
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
        __res = __main__strlen__block__24__size
        __main__strlen__block__24__size = __main__strlen__block__24__size + 1
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
    stack.append(__main__strlen__block__24__size)
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
    __main__strcmp__block__27__asize = 0
    __rhs = stack.pop()
    __main__strcmp__block__27__asize = __rhs
    stack.append (__main__strcmp__block__27__asize)
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
    __main__strcmp__block__27__bsize = 0
    __rhs = stack.pop()
    __main__strcmp__block__27__bsize = __rhs
    stack.append (__main__strcmp__block__27__bsize)
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
    stack.append(__main__strcmp__block__27__asize)
    # RHS
    stack.append(__main__strcmp__block__27__bsize)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs != __rhs
    stack.append (__res)
    __if__28__cond = stack.pop ()
    # get condition from stack
    if (__if__28__cond):
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
    __main__strcmp__block__27__for__29__i = 0
    __rhs = stack.pop()
    __main__strcmp__block__27__for__29__i = __rhs
    stack.append (__main__strcmp__block__27__for__29__i)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        stack.append(__main__strcmp__block__27__for__29__i)
        # RHS
        stack.append(__main__strcmp__block__27__asize)
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
        stack.append(__main__strcmp__block__27__for__29__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        # Subscript
        # LHS
        stack.append(__main__strcmp__b)
        # OFFSET
        stack.append(__main__strcmp__block__27__for__29__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
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
        stack.append(__main__strcmp__block__27__for__29__i)
        __rhs = stack.pop ()
        __main__strcmp__block__27__for__29__i = __main__strcmp__block__27__for__29__i + 1
        __res = __main__strcmp__block__27__for__29__i
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
    __main__substr__block__33__res = 0
    __rhs = stack.pop()
    __main__substr__block__33__res = __rhs
    stack.append (__main__substr__block__33__res)
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
    __main__substr__block__33__for__34__i = 0
    __rhs = stack.pop()
    __main__substr__block__33__for__34__i = __rhs
    stack.append (__main__substr__block__33__for__34__i)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        stack.append(__main__substr__block__33__for__34__i)
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
        stack.append(__main__substr__block__33__for__34__i)
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
        stack.append(__main__substr__block__33__res)
        # OFFSET
        stack.append(__main__substr__block__33__for__34__i)
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
        stack.append(__main__substr__block__33__for__34__i)
        __rhs = stack.pop ()
        __main__substr__block__33__for__34__i = __main__substr__block__33__for__34__i + 1
        __res = __main__substr__block__33__for__34__i
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
    stack.append(__main__substr__block__33__res)
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
    stack.append(__main__substr__block__33__res)
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
    __main__first_index_of__block__36__size = 0
    __rhs = stack.pop()
    __main__first_index_of__block__36__size = __rhs
    stack.append (__main__first_index_of__block__36__size)
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
    __main__first_index_of__block__36__for__37__i = 0
    __rhs = stack.pop()
    __main__first_index_of__block__36__for__37__i = __rhs
    stack.append (__main__first_index_of__block__36__for__37__i)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        stack.append(__main__first_index_of__block__36__for__37__i)
        # RHS
        stack.append(__main__first_index_of__block__36__size)
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
        stack.append(__main__first_index_of__block__36__for__37__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        stack.append(__main__first_index_of__c)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs == __rhs
        stack.append (__res)
        __if__39__cond = stack.pop ()
        # get condition from stack
        if (__if__39__cond):
            # Body
            # Return
            stack.append(__main__first_index_of__block__36__for__37__i)
            __rVal = stack.pop ()
            return __rVal
        # End of if
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # Update
        # Pre-Increment
        # RHS
        stack.append(__main__first_index_of__block__36__for__37__i)
        __rhs = stack.pop ()
        __main__first_index_of__block__36__for__37__i = __main__first_index_of__block__36__for__37__i + 1
        __res = __main__first_index_of__block__36__for__37__i
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
    __main__split__block__40__tokens = 0
    __rhs = stack.pop()
    __main__split__block__40__tokens = __rhs
    stack.append (__main__split__block__40__tokens)
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
    __main__split__block__40__size = 0
    __rhs = stack.pop()
    __main__split__block__40__size = __rhs
    stack.append (__main__split__block__40__size)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(0)
    # LHS
    __main__split__block__40__i = 0
    __rhs = stack.pop()
    __main__split__block__40__i = __rhs
    stack.append (__main__split__block__40__i)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(0)
    # LHS
    __main__split__block__40__j = 0
    __rhs = stack.pop()
    __main__split__block__40__j = __rhs
    stack.append (__main__split__block__40__j)
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
        stack.append(__main__split__block__40__i)
        # RHS
        stack.append(__main__split__block__40__size)
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
        stack.append(__main__split__block__40__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        stack.append(__main__split__delim)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs != __rhs
        stack.append (__res)
        __if__43__cond = stack.pop ()
        # get condition from stack
        if (__if__43__cond):
            # Body
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Assignment - '='
            # RHS
            # Int Literal
            stack.append(0)
            # LHS
            __main__split__block__40__while__41__block__42__if__43__block__44__count = 0
            __rhs = stack.pop()
            __main__split__block__40__while__41__block__42__if__43__block__44__count = __rhs
            stack.append (__main__split__block__40__while__41__block__42__if__43__block__44__count)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            # Statement
            # Assignment - '='
            # RHS
            stack.append(__main__split__block__40__i)
            # LHS
            __main__split__block__40__while__41__block__42__if__43__block__44__k = 0
            __rhs = stack.pop()
            __main__split__block__40__while__41__block__42__if__43__block__44__k = __rhs
            stack.append (__main__split__block__40__while__41__block__42__if__43__block__44__k)
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
                stack.append(__main__split__block__40__while__41__block__42__if__43__block__44__k)
                # RHS
                stack.append(__main__split__block__40__size)
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
                __res = __main__split__block__40__while__41__block__42__if__43__block__44__k
                __main__split__block__40__while__41__block__42__if__43__block__44__k = __main__split__block__40__while__41__block__42__if__43__block__44__k + 1
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
                __if__46__cond = stack.pop ()
                # get condition from stack
                if (__if__46__cond):
                    # Body
                    # Statement
                    # Pre-Increment
                    # RHS
                    stack.append(__main__split__block__40__while__41__block__42__if__43__block__44__count)
                    __rhs = stack.pop ()
                    __main__split__block__40__while__41__block__42__if__43__block__44__count = __main__split__block__40__while__41__block__42__if__43__block__44__count + 1
                    __res = __main__split__block__40__while__41__block__42__if__43__block__44__count
                    stack.append (__res)
                    # Statement results can be ignored
                    stack.pop ()
                    # End Statement

                #---------------------------------------------------------
                # Else-Statement
                else:
                    # Break out of __while__45
                    break
                #---------------------------------------------------------
                # End of if
                #---------------------------------------------------------
            # End of While
            #-------------------------------------------------------------
            # Statement
            # Method Call - Vector<:char[]:>::pushBack(char[]) -> void
            # LHS
            stack.append(__main__split__block__40__tokens)
            # RHS
            # Arguments
            # Addition
            # LHS
            stack.append(__main__split__block__40__while__41__block__42__if__43__block__44__count)
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
            __main__split__block__40__while__41__block__42__if__43__block__44__for__47__k = 0
            __rhs = stack.pop()
            __main__split__block__40__while__41__block__42__if__43__block__44__for__47__k = __rhs
            stack.append (__main__split__block__40__while__41__block__42__if__43__block__44__for__47__k)
            # Using an infinite loop so we can write a separate multi-line condition
            while (1):
                # Condition
                # Less Than
                # LHS
                stack.append(__main__split__block__40__while__41__block__42__if__43__block__44__for__47__k)
                # RHS
                stack.append(__main__split__block__40__while__41__block__42__if__43__block__44__count)
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
                __res = __main__split__block__40__i
                __main__split__block__40__i = __main__split__block__40__i + 1
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
                stack.append(__main__split__block__40__tokens)
                # RHS
                stack.append (__field____main____Vector__char__1____data)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                # OFFSET
                stack.append(__main__split__block__40__j)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # OFFSET
                stack.append(__main__split__block__40__while__41__block__42__if__43__block__44__for__47__k)
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
                stack.append(__main__split__block__40__while__41__block__42__if__43__block__44__for__47__k)
                __rhs = stack.pop ()
                __main__split__block__40__while__41__block__42__if__43__block__44__for__47__k = __main__split__block__40__while__41__block__42__if__43__block__44__for__47__k + 1
                __res = __main__split__block__40__while__41__block__42__if__43__block__44__for__47__k
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
            stack.append(__main__split__block__40__tokens)
            # RHS
            stack.append (__field____main____Vector__char__1____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main__split__block__40__j)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # OFFSET
            stack.append(__main__split__block__40__while__41__block__42__if__43__block__44__count)
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
            stack.append(__main__split__block__40__j)
            __rhs = stack.pop ()
            __main__split__block__40__j = __main__split__block__40__j + 1
            __res = __main__split__block__40__j
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
        stack.append(__main__split__block__40__i)
        __rhs = stack.pop ()
        __main__split__block__40__i = __main__split__block__40__i + 1
        __res = __main__split__block__40__i
        stack.append (__res)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
    # End of While
    #---------------------------------------------------------------------
    # Return
    stack.append(__main__split__block__40__tokens)
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
    __if__50__cond = stack.pop ()
    # get condition from stack
    if (__if__50__cond):
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
    __if__52__cond = stack.pop ()
    # get condition from stack
    if (__if__52__cond):
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
    __if__54__cond = stack.pop ()
    # get condition from stack
    if (__if__54__cond):
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
    __if__56__cond = stack.pop ()
    # get condition from stack
    if (__if__56__cond):
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
    __if__58__cond = stack.pop ()
    # get condition from stack
    if (__if__58__cond):
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
    __if__60__cond = stack.pop ()
    # get condition from stack
    if (__if__60__cond):
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
#=========================================================================
# Function Declaration - manhattan(int, int, int, int) -> int
def __main____manhattan__int__int__int__int (__main__manhattan__ax, __main__manhattan__ay, __main__manhattan__bx, __main__manhattan__by):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Return
    # Addition
    # LHS
    # Function Call - abs(int) -> int
    # Arguments
    # Subtraction
    # LHS
    stack.append(__main__manhattan__ax)
    # RHS
    stack.append(__main__manhattan__bx)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs - __rhs
    stack.append(__res)
    __arg0 = stack.pop ()
    # *** abs
    __res = __main____abs__int (__arg0)
    stack.append (__res) # function call result
    # RHS
    # Function Call - abs(int) -> int
    # Arguments
    # Subtraction
    # LHS
    stack.append(__main__manhattan__ay)
    # RHS
    stack.append(__main__manhattan__by)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs - __rhs
    stack.append(__res)
    __arg0 = stack.pop ()
    # *** abs
    __res = __main____abs__int (__arg0)
    stack.append (__res) # function call result
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs + __rhs
    stack.append(__res)
    __rVal = stack.pop ()
    return __rVal
    #---------------------------------------------------------------------
# End Function Declaration - __main____manhattan__int__int__int__int
#=========================================================================

#=========================================================================
# Class Declaration - __main____Point inherits __builtin____main__Object
# Creating Dispatch Table (will be populated later)
__dtable____main____Point = []
#-------------------------------------------------------------------------
# Field - int Point::x
__field____main____Point____x = 1
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Field - int Point::y
__field____main____Point____y = 2
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Constructor Declaration - Point::Point(int, int) -> Point
def __ctor____main____Point____Point__int__int (__main____Point__Point__x, __main____Point__Point__y):
    # Creating Class Instance
    this = [0] * 3
    # Add Dispatch Table
    this[0] = __dtable____main____Point
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main____Point__Point__x)
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append(__field____main____Point____x)
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
    stack.append(__main____Point__Point__y)
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append(__field____main____Point____y)
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
# End Constructor Declaration - __ctor____main____Point____Point__int__int
#-------------------------------------------------------------------------

# Populate Dispatch Table
__dtable____main____Point = []
# End Class Declaration - __main____Point
#=========================================================================

#=========================================================================
# Function Declaration - print(Point) -> void
def __main____print__Point (__main__print__p):
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
    __res = __builtin__print__char (__arg0)
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Function Call - print(int) -> void
    # Arguments
    # Member Accessor
    # LHS
    stack.append(__main__print__p)
    # RHS
    stack.append (__field____main____Point____x)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __arg0 = stack.pop ()
    # *** print
    __res = __builtin__print__int (__arg0)
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
    __res = __builtin__print__char (__arg0)
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
    __res = __builtin__print__char (__arg0)
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Function Call - print(int) -> void
    # Arguments
    # Member Accessor
    # LHS
    stack.append(__main__print__p)
    # RHS
    stack.append (__field____main____Point____y)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __arg0 = stack.pop ()
    # *** print
    __res = __builtin__print__int (__arg0)
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
    __res = __builtin__print__char (__arg0)
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
# End Function Declaration - __main____print__Point
#=========================================================================

# Statement
# Assignment - '='
# RHS
# Constructor Call - Vector<:Point:>::Vector() -> Vector<:Point:>
# Arguments
__retval = __ctor____main____Vector__Point____Vector ()
stack.append (__retval)
# LHS
__main__tail_positions = 0
__rhs = stack.pop()
__main__tail_positions = __rhs
stack.append (__main__tail_positions)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Assignment - '='
# RHS
# Int Literal
stack.append(0)
# LHS
__main__hx = 0
__rhs = stack.pop()
__main__hx = __rhs
stack.append (__main__hx)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Assignment - '='
# RHS
# Int Literal
stack.append(0)
# LHS
__main__hy = 0
__rhs = stack.pop()
__main__hy = __rhs
stack.append (__main__hy)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Assignment - '='
# RHS
# Int Literal
stack.append(0)
# LHS
__main__tx = 0
__rhs = stack.pop()
__main__tx = __rhs
stack.append (__main__tx)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Assignment - '='
# RHS
# Int Literal
stack.append(0)
# LHS
__main__ty = 0
__rhs = stack.pop()
__main__ty = __rhs
stack.append (__main__ty)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Assignment - '='
# RHS
# Int Literal
stack.append(0)
# LHS
__main__xmin = 0
__rhs = stack.pop()
__main__xmin = __rhs
stack.append (__main__xmin)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Assignment - '='
# RHS
# Int Literal
stack.append(0)
# LHS
__main__xmax = 0
__rhs = stack.pop()
__main__xmax = __rhs
stack.append (__main__xmax)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Assignment - '='
# RHS
# Int Literal
stack.append(0)
# LHS
__main__ymin = 0
__rhs = stack.pop()
__main__ymin = __rhs
stack.append (__main__ymin)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Assignment - '='
# RHS
# Int Literal
stack.append(0)
# LHS
__main__ymax = 0
__rhs = stack.pop()
__main__ymax = __rhs
stack.append (__main__ymax)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Method Call - Vector<:Point:>::pushBack(Point) -> void
# LHS
stack.append(__main__tail_positions)
# RHS
# Arguments
# Constructor Call - Point::Point(int, int) -> Point
# Arguments
# Int Literal
stack.append(0)
# Int Literal
stack.append(0)
__arg1 = stack.pop ()
__arg0 = stack.pop ()
__retval = __ctor____main____Point____Point__int__int (__arg0, __arg1)
stack.append (__retval)
__arg0 = stack.pop ()
__obj = stack.pop ()
__retval = __method____main____Vector__Point____pushBack__Point (__obj, __arg0)
stack.append (__retval)
# Statement results can be ignored
stack.pop ()
# End Statement

#-------------------------------------------------------------------------
# For-Loop
# Init
# Assignment - '='
# RHS
# Int Literal
stack.append(0)
# LHS
__main__for__66__i = 0
__rhs = stack.pop()
__main__for__66__i = __rhs
stack.append (__main__for__66__i)
# Using an infinite loop so we can write a separate multi-line condition
while (1):
    # Condition
    # Less Than
    # LHS
    stack.append(__main__for__66__i)
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
    stack.append(__main__for__66__i)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    # LHS
    __main__for__66__block__67__line = 0
    __rhs = stack.pop()
    __main__for__66__block__67__line = __rhs
    stack.append (__main__for__66__block__67__line)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Function Call - split(char[], char) -> Vector<:char[]:>
    # Arguments
    stack.append(__main__for__66__block__67__line)
    # Char Literal
    stack.append(' ')
    __arg1 = stack.pop ()
    __arg0 = stack.pop ()
    # *** split
    __res = __main____split__char__1__char (__arg0, __arg1)
    stack.append (__res) # function call result
    # LHS
    __main__for__66__block__67__tokens = 0
    __rhs = stack.pop()
    __main__for__66__block__67__tokens = __rhs
    stack.append (__main__for__66__block__67__tokens)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Function Call - stringToInt(char[]) -> int
    # Arguments
    # Subscript
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main__for__66__block__67__tokens)
    # RHS
    stack.append (__field____main____Vector__char__1____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    # Int Literal
    stack.append(1)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    __arg0 = stack.pop ()
    # *** stringToInt
    __res = __builtin__stringToInt__char__1 (__arg0)
    stack.append (__res) # function call result
    # LHS
    __main__for__66__block__67__amt = 0
    __rhs = stack.pop()
    __main__for__66__block__67__amt = __rhs
    stack.append (__main__for__66__block__67__amt)
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
    __main__for__66__block__67__for__68__j = 0
    __rhs = stack.pop()
    __main__for__66__block__67__for__68__j = __rhs
    stack.append (__main__for__66__block__67__for__68__j)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        stack.append(__main__for__66__block__67__for__68__j)
        # RHS
        stack.append(__main__for__66__block__67__amt)
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
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__for__66__block__67__tokens)
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
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        # Char Literal
        stack.append('U')
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs == __rhs
        stack.append (__res)
        __if__70__cond = stack.pop ()
        # Condition for elif #0
        # Equal
        # LHS
        # Subscript
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__for__66__block__67__tokens)
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
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        # Char Literal
        stack.append('R')
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs == __rhs
        stack.append (__res)
        __elif__70x0__cond = stack.pop ()
        # Condition for elif #1
        # Equal
        # LHS
        # Subscript
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__for__66__block__67__tokens)
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
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        # Char Literal
        stack.append('D')
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs == __rhs
        stack.append (__res)
        __elif__70x1__cond = stack.pop ()
        # Condition for elif #2
        # Equal
        # LHS
        # Subscript
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__for__66__block__67__tokens)
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
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        # Char Literal
        stack.append('L')
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs == __rhs
        stack.append (__res)
        __elif__70x2__cond = stack.pop ()
        # get condition from stack
        if (__if__70__cond):
            # Body
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Pre-Increment
            # RHS
            stack.append(__main__hy)
            __rhs = stack.pop ()
            __main__hy = __main__hy + 1
            __res = __main__hy
            stack.append (__res)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            #-------------------------------------------------------------
        #-----------------------------------------------------------------
        # Elif-Statement
        # Condition
        elif (__elif__70x0__cond):
            # Body
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Pre-Increment
            # RHS
            stack.append(__main__hx)
            __rhs = stack.pop ()
            __main__hx = __main__hx + 1
            __res = __main__hx
            stack.append (__res)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            #-------------------------------------------------------------
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # Elif-Statement
        # Condition
        elif (__elif__70x1__cond):
            # Body
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Pre-Decrement
            # RHS
            stack.append(__main__hy)
            __rhs = stack.pop ()
            __main__hy = __main__hy - 1
            __res = __main__hy
            stack.append (__res)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            #-------------------------------------------------------------
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # Elif-Statement
        # Condition
        elif (__elif__70x2__cond):
            # Body
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Pre-Decrement
            # RHS
            stack.append(__main__hx)
            __rhs = stack.pop ()
            __main__hx = __main__hx - 1
            __res = __main__hx
            stack.append (__res)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            #-------------------------------------------------------------
        #-----------------------------------------------------------------
        # End of if
        #-----------------------------------------------------------------
        # Statement
        # Assignment - '='
        # RHS
        # Int Literal
        stack.append(0)
        # LHS
        __main__for__66__block__67__for__68__block__69__tail_moved = 0
        __rhs = stack.pop()
        __main__for__66__block__67__for__68__block__69__tail_moved = __rhs
        stack.append (__main__for__66__block__67__for__68__block__69__tail_moved)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Function Call - abs(int) -> int
        # Arguments
        # Subtraction
        # LHS
        stack.append(__main__hx)
        # RHS
        stack.append(__main__tx)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs - __rhs
        stack.append(__res)
        __arg0 = stack.pop ()
        # *** abs
        __res = __main____abs__int (__arg0)
        stack.append (__res) # function call result
        # LHS
        __main__for__66__block__67__for__68__block__69__deltax = 0
        __rhs = stack.pop()
        __main__for__66__block__67__for__68__block__69__deltax = __rhs
        stack.append (__main__for__66__block__67__for__68__block__69__deltax)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Function Call - abs(int) -> int
        # Arguments
        # Subtraction
        # LHS
        stack.append(__main__hy)
        # RHS
        stack.append(__main__ty)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs - __rhs
        stack.append(__res)
        __arg0 = stack.pop ()
        # *** abs
        __res = __main____abs__int (__arg0)
        stack.append (__res) # function call result
        # LHS
        __main__for__66__block__67__for__68__block__69__deltay = 0
        __rhs = stack.pop()
        __main__for__66__block__67__for__68__block__69__deltay = __rhs
        stack.append (__main__for__66__block__67__for__68__block__69__deltay)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
        # If-Statement
        # Precomputing all if/elif conditions and give unique names
        # bc we can't have code between if and elif
        # Condition
        # AND
        # LHS
        # Equal
        # LHS
        stack.append(__main__hx)
        # RHS
        stack.append(__main__tx)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs == __rhs
        stack.append (__res)
        # RHS
        # Greater Than or Equal to
        # LHS
        stack.append(__main__for__66__block__67__for__68__block__69__deltay)
        # RHS
        # Int Literal
        stack.append(2)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs >= __rhs
        stack.append (__res)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs and __rhs
        stack.append (__res)
        __if__75__cond = stack.pop ()
        # Condition for elif #0
        # AND
        # LHS
        # Equal
        # LHS
        stack.append(__main__hy)
        # RHS
        stack.append(__main__ty)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs == __rhs
        stack.append (__res)
        # RHS
        # Greater Than or Equal to
        # LHS
        stack.append(__main__for__66__block__67__for__68__block__69__deltax)
        # RHS
        # Int Literal
        stack.append(2)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs >= __rhs
        stack.append (__res)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs and __rhs
        stack.append (__res)
        __elif__75x0__cond = stack.pop ()
        # Condition for elif #1
        # AND
        # LHS
        # AND
        # LHS
        # Not Equal
        # LHS
        stack.append(__main__hx)
        # RHS
        stack.append(__main__tx)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs != __rhs
        stack.append (__res)
        # RHS
        # Not Equal
        # LHS
        stack.append(__main__hy)
        # RHS
        stack.append(__main__ty)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs != __rhs
        stack.append (__res)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs and __rhs
        stack.append (__res)
        # RHS
        # Greater Than
        # LHS
        # Function Call - manhattan(int, int, int, int) -> int
        # Arguments
        stack.append(__main__hx)
        stack.append(__main__hy)
        stack.append(__main__tx)
        stack.append(__main__ty)
        __arg3 = stack.pop ()
        __arg2 = stack.pop ()
        __arg1 = stack.pop ()
        __arg0 = stack.pop ()
        # *** manhattan
        __res = __main____manhattan__int__int__int__int (__arg0, __arg1, __arg2, __arg3)
        stack.append (__res) # function call result
        # RHS
        # Int Literal
        stack.append(2)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs > __rhs
        stack.append (__res)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs and __rhs
        stack.append (__res)
        __elif__75x1__cond = stack.pop ()
        # get condition from stack
        if (__if__75__cond):
            # Body
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Assignment - '='
            # RHS
            # Greater Than
            # LHS
            stack.append(__main__hy)
            # RHS
            stack.append(__main__ty)
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs > __rhs
            stack.append (__res)
            # LHS
            __main__for__66__block__67__for__68__block__69__if__75__block__76__isup = 0
            __rhs = stack.pop()
            __main__for__66__block__67__for__68__block__69__if__75__block__76__isup = __rhs
            stack.append (__main__for__66__block__67__for__68__block__69__if__75__block__76__isup)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            #-------------------------------------------------------------
            # If-Statement
            # Precomputing all if/elif conditions and give unique names
            # bc we can't have code between if and elif
            # Condition
            stack.append(__main__for__66__block__67__for__68__block__69__if__75__block__76__isup)
            __if__77__cond = stack.pop ()
            # get condition from stack
            if (__if__77__cond):
                # Body
                #---------------------------------------------------------
                # Code Block
                # Statement
                # Assignment - '+='
                # RHS
                # Int Literal
                stack.append(1)
                __rhs = stack.pop()
                __main__ty = __main__ty + __rhs
                stack.append (__main__ty)
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                #---------------------------------------------------------
            #-------------------------------------------------------------
            # Else-Statement
            else:
                #---------------------------------------------------------
                # Code Block
                # Statement
                # Assignment - '-='
                # RHS
                # Int Literal
                stack.append(1)
                __rhs = stack.pop()
                __main__ty = __main__ty - __rhs
                stack.append (__main__ty)
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                #---------------------------------------------------------
            #-------------------------------------------------------------
            # End of if
            #-------------------------------------------------------------
            # Statement
            # Assignment - '='
            # RHS
            # Int Literal
            stack.append(1)
            __rhs = stack.pop()
            __main__for__66__block__67__for__68__block__69__tail_moved = __rhs
            stack.append (__main__for__66__block__67__for__68__block__69__tail_moved)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            #-------------------------------------------------------------
        #-----------------------------------------------------------------
        # Elif-Statement
        # Condition
        elif (__elif__75x0__cond):
            # Body
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Assignment - '='
            # RHS
            # Greater Than
            # LHS
            stack.append(__main__hx)
            # RHS
            stack.append(__main__tx)
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs > __rhs
            stack.append (__res)
            # LHS
            __main__for__66__block__67__for__68__block__69__elif__75x0__block__80__isright = 0
            __rhs = stack.pop()
            __main__for__66__block__67__for__68__block__69__elif__75x0__block__80__isright = __rhs
            stack.append (__main__for__66__block__67__for__68__block__69__elif__75x0__block__80__isright)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            #-------------------------------------------------------------
            # If-Statement
            # Precomputing all if/elif conditions and give unique names
            # bc we can't have code between if and elif
            # Condition
            stack.append(__main__for__66__block__67__for__68__block__69__elif__75x0__block__80__isright)
            __if__81__cond = stack.pop ()
            # get condition from stack
            if (__if__81__cond):
                # Body
                #---------------------------------------------------------
                # Code Block
                # Statement
                # Assignment - '+='
                # RHS
                # Int Literal
                stack.append(1)
                __rhs = stack.pop()
                __main__tx = __main__tx + __rhs
                stack.append (__main__tx)
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                #---------------------------------------------------------
            #-------------------------------------------------------------
            # Else-Statement
            else:
                #---------------------------------------------------------
                # Code Block
                # Statement
                # Assignment - '-='
                # RHS
                # Int Literal
                stack.append(1)
                __rhs = stack.pop()
                __main__tx = __main__tx - __rhs
                stack.append (__main__tx)
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                #---------------------------------------------------------
            #-------------------------------------------------------------
            # End of if
            #-------------------------------------------------------------
            # Statement
            # Assignment - '='
            # RHS
            # Int Literal
            stack.append(1)
            __rhs = stack.pop()
            __main__for__66__block__67__for__68__block__69__tail_moved = __rhs
            stack.append (__main__for__66__block__67__for__68__block__69__tail_moved)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            #-------------------------------------------------------------
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # Elif-Statement
        # Condition
        elif (__elif__75x1__cond):
            # Body
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Assignment - '='
            # RHS
            # Greater Than
            # LHS
            stack.append(__main__hy)
            # RHS
            stack.append(__main__ty)
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs > __rhs
            stack.append (__res)
            # LHS
            __main__for__66__block__67__for__68__block__69__elif__75x1__block__84__isup = 0
            __rhs = stack.pop()
            __main__for__66__block__67__for__68__block__69__elif__75x1__block__84__isup = __rhs
            stack.append (__main__for__66__block__67__for__68__block__69__elif__75x1__block__84__isup)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            # Statement
            # Assignment - '='
            # RHS
            # Greater Than
            # LHS
            stack.append(__main__hx)
            # RHS
            stack.append(__main__tx)
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs > __rhs
            stack.append (__res)
            # LHS
            __main__for__66__block__67__for__68__block__69__elif__75x1__block__84__isright = 0
            __rhs = stack.pop()
            __main__for__66__block__67__for__68__block__69__elif__75x1__block__84__isright = __rhs
            stack.append (__main__for__66__block__67__for__68__block__69__elif__75x1__block__84__isright)
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
            stack.append(__main__for__66__block__67__for__68__block__69__elif__75x1__block__84__isup)
            # RHS
            stack.append(__main__for__66__block__67__for__68__block__69__elif__75x1__block__84__isright)
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs and __rhs
            stack.append (__res)
            __if__85__cond = stack.pop ()
            # Condition for elif #0
            # AND
            # LHS
            # Negate
            # RHS
            stack.append(__main__for__66__block__67__for__68__block__69__elif__75x1__block__84__isup)
            __rhs = stack.pop ()
            __res = not __rhs
            stack.append (__res)
            # RHS
            stack.append(__main__for__66__block__67__for__68__block__69__elif__75x1__block__84__isright)
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs and __rhs
            stack.append (__res)
            __elif__85x0__cond = stack.pop ()
            # Condition for elif #1
            # AND
            # LHS
            # Negate
            # RHS
            stack.append(__main__for__66__block__67__for__68__block__69__elif__75x1__block__84__isup)
            __rhs = stack.pop ()
            __res = not __rhs
            stack.append (__res)
            # RHS
            # Negate
            # RHS
            stack.append(__main__for__66__block__67__for__68__block__69__elif__75x1__block__84__isright)
            __rhs = stack.pop ()
            __res = not __rhs
            stack.append (__res)
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs and __rhs
            stack.append (__res)
            __elif__85x1__cond = stack.pop ()
            # Condition for elif #2
            # AND
            # LHS
            stack.append(__main__for__66__block__67__for__68__block__69__elif__75x1__block__84__isup)
            # RHS
            # Negate
            # RHS
            stack.append(__main__for__66__block__67__for__68__block__69__elif__75x1__block__84__isright)
            __rhs = stack.pop ()
            __res = not __rhs
            stack.append (__res)
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs and __rhs
            stack.append (__res)
            __elif__85x2__cond = stack.pop ()
            # get condition from stack
            if (__if__85__cond):
                # Body
                #---------------------------------------------------------
                # Code Block
                # Statement
                # Pre-Increment
                # RHS
                stack.append(__main__ty)
                __rhs = stack.pop ()
                __main__ty = __main__ty + 1
                __res = __main__ty
                stack.append (__res)
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Statement
                # Pre-Increment
                # RHS
                stack.append(__main__tx)
                __rhs = stack.pop ()
                __main__tx = __main__tx + 1
                __res = __main__tx
                stack.append (__res)
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                #---------------------------------------------------------
            #-------------------------------------------------------------
            # Elif-Statement
            # Condition
            elif (__elif__85x0__cond):
                # Body
                #---------------------------------------------------------
                # Code Block
                # Statement
                # Pre-Decrement
                # RHS
                stack.append(__main__ty)
                __rhs = stack.pop ()
                __main__ty = __main__ty - 1
                __res = __main__ty
                stack.append (__res)
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Statement
                # Pre-Increment
                # RHS
                stack.append(__main__tx)
                __rhs = stack.pop ()
                __main__tx = __main__tx + 1
                __res = __main__tx
                stack.append (__res)
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                #---------------------------------------------------------
            #-------------------------------------------------------------
            #-------------------------------------------------------------
            # Elif-Statement
            # Condition
            elif (__elif__85x1__cond):
                # Body
                #---------------------------------------------------------
                # Code Block
                # Statement
                # Pre-Decrement
                # RHS
                stack.append(__main__ty)
                __rhs = stack.pop ()
                __main__ty = __main__ty - 1
                __res = __main__ty
                stack.append (__res)
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Statement
                # Pre-Decrement
                # RHS
                stack.append(__main__tx)
                __rhs = stack.pop ()
                __main__tx = __main__tx - 1
                __res = __main__tx
                stack.append (__res)
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                #---------------------------------------------------------
            #-------------------------------------------------------------
            #-------------------------------------------------------------
            # Elif-Statement
            # Condition
            elif (__elif__85x2__cond):
                # Body
                #---------------------------------------------------------
                # Code Block
                # Statement
                # Pre-Increment
                # RHS
                stack.append(__main__ty)
                __rhs = stack.pop ()
                __main__ty = __main__ty + 1
                __res = __main__ty
                stack.append (__res)
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Statement
                # Pre-Decrement
                # RHS
                stack.append(__main__tx)
                __rhs = stack.pop ()
                __main__tx = __main__tx - 1
                __res = __main__tx
                stack.append (__res)
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                #---------------------------------------------------------
            #-------------------------------------------------------------
            # End of if
            #-------------------------------------------------------------
            # Statement
            # Assignment - '='
            # RHS
            # Int Literal
            stack.append(1)
            __rhs = stack.pop()
            __main__for__66__block__67__for__68__block__69__tail_moved = __rhs
            stack.append (__main__for__66__block__67__for__68__block__69__tail_moved)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            #-------------------------------------------------------------
        #-----------------------------------------------------------------
        # End of if
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # If-Statement
        # Precomputing all if/elif conditions and give unique names
        # bc we can't have code between if and elif
        # Condition
        stack.append(__main__for__66__block__67__for__68__block__69__tail_moved)
        __if__90__cond = stack.pop ()
        # get condition from stack
        if (__if__90__cond):
            # Body
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Assignment - '='
            # RHS
            # Int Literal
            stack.append(0)
            # LHS
            __main__for__66__block__67__for__68__block__69__if__90__block__91__exists = 0
            __rhs = stack.pop()
            __main__for__66__block__67__for__68__block__69__if__90__block__91__exists = __rhs
            stack.append (__main__for__66__block__67__for__68__block__69__if__90__block__91__exists)
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
            __main__for__66__block__67__for__68__block__69__if__90__block__91__for__92__k = 0
            __rhs = stack.pop()
            __main__for__66__block__67__for__68__block__69__if__90__block__91__for__92__k = __rhs
            stack.append (__main__for__66__block__67__for__68__block__69__if__90__block__91__for__92__k)
            # Using an infinite loop so we can write a separate multi-line condition
            while (1):
                # Condition
                # Less Than
                # LHS
                stack.append(__main__for__66__block__67__for__68__block__69__if__90__block__91__for__92__k)
                # RHS
                # Member Accessor
                # LHS
                stack.append(__main__tail_positions)
                # RHS
                stack.append (__field____main____Vector__Point____size)
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
                #---------------------------------------------------------
                # Code Block
                # Statement
                # Assignment - '='
                # RHS
                # Subscript
                # LHS
                # Member Accessor
                # LHS
                stack.append(__main__tail_positions)
                # RHS
                stack.append (__field____main____Vector__Point____data)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                # OFFSET
                stack.append(__main__for__66__block__67__for__68__block__69__if__90__block__91__for__92__k)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # LHS
                __main__for__66__block__67__for__68__block__69__if__90__block__91__for__92__block__93__tail_pos = 0
                __rhs = stack.pop()
                __main__for__66__block__67__for__68__block__69__if__90__block__91__for__92__block__93__tail_pos = __rhs
                stack.append (__main__for__66__block__67__for__68__block__69__if__90__block__91__for__92__block__93__tail_pos)
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                #---------------------------------------------------------
                # If-Statement
                # Precomputing all if/elif conditions and give unique names
                # bc we can't have code between if and elif
                # Condition
                # AND
                # LHS
                # Equal
                # LHS
                # Member Accessor
                # LHS
                stack.append(__main__for__66__block__67__for__68__block__69__if__90__block__91__for__92__block__93__tail_pos)
                # RHS
                stack.append (__field____main____Point____x)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                # RHS
                stack.append(__main__tx)
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs == __rhs
                stack.append (__res)
                # RHS
                # Equal
                # LHS
                # Member Accessor
                # LHS
                stack.append(__main__for__66__block__67__for__68__block__69__if__90__block__91__for__92__block__93__tail_pos)
                # RHS
                stack.append (__field____main____Point____y)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                # RHS
                stack.append(__main__ty)
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs == __rhs
                stack.append (__res)
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs and __rhs
                stack.append (__res)
                __if__94__cond = stack.pop ()
                # get condition from stack
                if (__if__94__cond):
                    # Body
                    #-----------------------------------------------------
                    # Code Block
                    # Statement
                    # Assignment - '='
                    # RHS
                    # Int Literal
                    stack.append(1)
                    __rhs = stack.pop()
                    __main__for__66__block__67__for__68__block__69__if__90__block__91__exists = __rhs
                    stack.append (__main__for__66__block__67__for__68__block__69__if__90__block__91__exists)
                    # Statement results can be ignored
                    stack.pop ()
                    # End Statement

                    # Break out of __for__92
                    break
                    #-----------------------------------------------------
                # End of if
                #---------------------------------------------------------
                #---------------------------------------------------------
                # Update
                # Pre-Increment
                # RHS
                stack.append(__main__for__66__block__67__for__68__block__69__if__90__block__91__for__92__k)
                __rhs = stack.pop ()
                __main__for__66__block__67__for__68__block__69__if__90__block__91__for__92__k = __main__for__66__block__67__for__68__block__69__if__90__block__91__for__92__k + 1
                __res = __main__for__66__block__67__for__68__block__69__if__90__block__91__for__92__k
                stack.append (__res)
            #-------------------------------------------------------------
            #-------------------------------------------------------------
            # If-Statement
            # Precomputing all if/elif conditions and give unique names
            # bc we can't have code between if and elif
            # Condition
            # Negate
            # RHS
            stack.append(__main__for__66__block__67__for__68__block__69__if__90__block__91__exists)
            __rhs = stack.pop ()
            __res = not __rhs
            stack.append (__res)
            __if__96__cond = stack.pop ()
            # get condition from stack
            if (__if__96__cond):
                # Body
                # Statement
                # Method Call - Vector<:Point:>::pushBack(Point) -> void
                # LHS
                stack.append(__main__tail_positions)
                # RHS
                # Arguments
                # Constructor Call - Point::Point(int, int) -> Point
                # Arguments
                stack.append(__main__tx)
                stack.append(__main__ty)
                __arg1 = stack.pop ()
                __arg0 = stack.pop ()
                __retval = __ctor____main____Point____Point__int__int (__arg0, __arg1)
                stack.append (__retval)
                __arg0 = stack.pop ()
                __obj = stack.pop ()
                __retval = __method____main____Vector__Point____pushBack__Point (__obj, __arg0)
                stack.append (__retval)
                # Statement results can be ignored
                stack.pop ()
                # End Statement

            # End of if
            #-------------------------------------------------------------
            #-------------------------------------------------------------
        # End of if
        #-----------------------------------------------------------------
        # Statement
        # Assignment - '='
        # RHS
        # Function Call - min(int, int) -> int
        # Arguments
        stack.append(__main__hx)
        stack.append(__main__xmin)
        __arg1 = stack.pop ()
        __arg0 = stack.pop ()
        # *** min
        __res = __main____min__int__int (__arg0, __arg1)
        stack.append (__res) # function call result
        __rhs = stack.pop()
        __main__xmin = __rhs
        stack.append (__main__xmin)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Function Call - max(int, int) -> int
        # Arguments
        stack.append(__main__hx)
        stack.append(__main__xmax)
        __arg1 = stack.pop ()
        __arg0 = stack.pop ()
        # *** max
        __res = __main____max__int__int (__arg0, __arg1)
        stack.append (__res) # function call result
        __rhs = stack.pop()
        __main__xmax = __rhs
        stack.append (__main__xmax)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Function Call - min(int, int) -> int
        # Arguments
        stack.append(__main__hy)
        stack.append(__main__ymin)
        __arg1 = stack.pop ()
        __arg0 = stack.pop ()
        # *** min
        __res = __main____min__int__int (__arg0, __arg1)
        stack.append (__res) # function call result
        __rhs = stack.pop()
        __main__ymin = __rhs
        stack.append (__main__ymin)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Function Call - max(int, int) -> int
        # Arguments
        stack.append(__main__hy)
        stack.append(__main__ymax)
        __arg1 = stack.pop ()
        __arg0 = stack.pop ()
        # *** max
        __res = __main____max__int__int (__arg0, __arg1)
        stack.append (__res) # function call result
        __rhs = stack.pop()
        __main__ymax = __rhs
        stack.append (__main__ymax)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
        # Update
        # Pre-Increment
        # RHS
        stack.append(__main__for__66__block__67__for__68__j)
        __rhs = stack.pop ()
        __main__for__66__block__67__for__68__j = __main__for__66__block__67__for__68__j + 1
        __res = __main__for__66__block__67__for__68__j
        stack.append (__res)
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    # Update
    # Pre-Increment
    # RHS
    stack.append(__main__for__66__i)
    __rhs = stack.pop ()
    __main__for__66__i = __main__for__66__i + 1
    __res = __main__for__66__i
    stack.append (__res)
#-------------------------------------------------------------------------
# Statement
# Function Call - println(int) -> void
# Arguments
# Member Accessor
# LHS
stack.append(__main__tail_positions)
# RHS
stack.append (__field____main____Vector__Point____size)
__child = stack.pop ()
__parent = stack.pop ()
stack.append (__parent[__child])
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

