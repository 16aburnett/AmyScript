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
    if s[-1] == '\0':
        return int(''.join(s[:-1]))
    return int(''.join(s))


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

#=========================================================================
# Class Declaration - __main____Vector__int inherits __builtin____main__Object
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
    stack.append(__field____main____Vector__int____capacity)
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
    stack.append(__field____main____Vector__int____size)
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
    stack.append (__field____main____Vector__int____capacity)
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
    stack.append(__field____main____Vector__int____data)
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
# End Constructor Declaration - __ctor____main____Vector__int____Vector
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Constructor Declaration - Vector<:int:>::Vector(int) -> Vector<:int:>
def __ctor____main____Vector__int____Vector__int (__main____Vector__int__Vector__size):
    # Creating Class Instance
    this = [0] * 4
    # Add Dispatch Table
    this[0] = __dtable____main____Vector__int
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Assignment - '='
    # RHS
    # Addition
    # LHS
    stack.append(__main____Vector__int__Vector__size)
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
    stack.append(__field____main____Vector__int____capacity)
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
    stack.append(__main____Vector__int__Vector__size)
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append(__field____main____Vector__int____size)
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
    stack.append (__field____main____Vector__int____capacity)
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
    stack.append(__field____main____Vector__int____data)
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
# End Constructor Declaration - __ctor____main____Vector__int____Vector__int
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vector<:int:>::pushBack(int) -> void
def __method____main____Vector__int____pushBack__int (this, __main____Vector__int__pushBack__val):
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
    stack.append (__field____main____Vector__int____size)
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
    stack.append (__field____main____Vector__int____capacity)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs >= __rhs
    stack.append (__res)
    __if__13__cond = stack.pop ()
    # get condition from stack
    if (__if__13__cond):
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
        stack.append (__field____main____Vector__int____capacity)
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
        stack.append(__field____main____Vector__int____capacity)
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
        stack.append (__field____main____Vector__int____capacity)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        __dim = stack.pop ()
        __res = [None] * __dim
        stack.append (__res)
        # LHS
        __main____Vector__int__pushBack__block__12__if__13__block__14__nData = 0
        __rhs = stack.pop()
        __main____Vector__int__pushBack__block__12__if__13__block__14__nData = __rhs
        stack.append (__main____Vector__int__pushBack__block__12__if__13__block__14__nData)
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
        __main____Vector__int__pushBack__block__12__if__13__block__14__for__15__i = 0
        __rhs = stack.pop()
        __main____Vector__int__pushBack__block__12__if__13__block__14__for__15__i = __rhs
        stack.append (__main____Vector__int__pushBack__block__12__if__13__block__14__for__15__i)
        # Using an infinite loop so we can write a separate multi-line condition
        while (1):
            # Condition
            # Less Than
            # LHS
            stack.append(__main____Vector__int__pushBack__block__12__if__13__block__14__for__15__i)
            # RHS
            # Member Accessor
            # LHS
            stack.append(this)
            # RHS
            stack.append (__field____main____Vector__int____size)
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
            stack.append (__field____main____Vector__int____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main____Vector__int__pushBack__block__12__if__13__block__14__for__15__i)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # LHS
            # Subscript assignment
            # LHS
            stack.append(__main____Vector__int__pushBack__block__12__if__13__block__14__nData)
            # OFFSET
            stack.append(__main____Vector__int__pushBack__block__12__if__13__block__14__for__15__i)
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
            stack.append(__main____Vector__int__pushBack__block__12__if__13__block__14__for__15__i)
            __rhs = stack.pop ()
            __main____Vector__int__pushBack__block__12__if__13__block__14__for__15__i = __main____Vector__int__pushBack__block__12__if__13__block__14__for__15__i + 1
            __res = __main____Vector__int__pushBack__block__12__if__13__block__14__for__15__i
            stack.append (__res)
        #-----------------------------------------------------------------
        # Statement
        # Member Accessor
        # LHS
        stack.append(this)
        # RHS
        stack.append (__field____main____Vector__int____data)
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
        stack.append(__main____Vector__int__pushBack__block__12__if__13__block__14__nData)
        # LHS
        # Member Accessor Assignment
        # LHS
        stack.append(this)
        # RHS
        stack.append(__field____main____Vector__int____data)
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
    stack.append(__main____Vector__int__pushBack__val)
    # LHS
    # Subscript assignment
    # LHS
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__int____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__int____size)
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
    stack.append (__field____main____Vector__int____size)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __rhs = stack.pop ()
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__int____size)
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
# End Method Declaration - __method____main____Vector__int____pushBack__int
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vector<:int:>::popBack() -> int
def __method____main____Vector__int____popBack (this):
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
    stack.append (__field____main____Vector__int____data)
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
    stack.append (__field____main____Vector__int____size)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __rhs = stack.pop ()
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__int____size)
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
# End Method Declaration - __method____main____Vector__int____popBack
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vector<:int:>::get(int) -> int
def __method____main____Vector__int____get__int (this, __main____Vector__int__get__index):
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
    stack.append (__field____main____Vector__int____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    stack.append(__main____Vector__int__get__index)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    __rVal = stack.pop ()
    return __rVal
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
    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main____Vector__int__set__value)
    # LHS
    # Subscript assignment
    # LHS
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__int____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    stack.append(__main____Vector__int__set__index)
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
# End Method Declaration - __method____main____Vector__int____set__int__int
#-------------------------------------------------------------------------

# Populate Dispatch Table
__dtable____main____Vector__int = [__method____main____Vector__int____pushBack__int, __method____main____Vector__int____popBack, __method____main____Vector__int____get__int, __method____main____Vector__int____set__int__int]
# End Class Declaration - __main____Vector__int
#=========================================================================

#=========================================================================
# Class Declaration - __main____Vector__Vector inherits __builtin____main__Object
# Creating Dispatch Table (will be populated later)
__dtable____main____Vector__Vector = []
#-------------------------------------------------------------------------
# Field - Vector<:char:>[] Vector<:Vector<:char:>:>::data
__field____main____Vector__Vector____data = 1
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Field - int Vector<:Vector<:char:>:>::size
__field____main____Vector__Vector____size = 2
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Field - int Vector<:Vector<:char:>:>::capacity
__field____main____Vector__Vector____capacity = 3
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Constructor Declaration - Vector<:Vector<:char:>:>::Vector() -> Vector<:Vector<:char:>:>
def __ctor____main____Vector__Vector____Vector ():
    # Creating Class Instance
    this = [0] * 4
    # Add Dispatch Table
    this[0] = __dtable____main____Vector__Vector
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
    stack.append(__field____main____Vector__Vector____capacity)
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
    stack.append(__field____main____Vector__Vector____size)
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
    stack.append (__field____main____Vector__Vector____capacity)
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
    stack.append(__field____main____Vector__Vector____data)
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
# End Constructor Declaration - __ctor____main____Vector__Vector____Vector
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Constructor Declaration - Vector<:Vector<:char:>:>::Vector(int) -> Vector<:Vector<:char:>:>
def __ctor____main____Vector__Vector____Vector__int (__main____Vector__Vector__Vector__size):
    # Creating Class Instance
    this = [0] * 4
    # Add Dispatch Table
    this[0] = __dtable____main____Vector__Vector
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Assignment - '='
    # RHS
    # Addition
    # LHS
    stack.append(__main____Vector__Vector__Vector__size)
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
    stack.append(__field____main____Vector__Vector____capacity)
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
    stack.append(__main____Vector__Vector__Vector__size)
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append(__field____main____Vector__Vector____size)
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
    stack.append (__field____main____Vector__Vector____capacity)
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
    stack.append(__field____main____Vector__Vector____data)
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
# End Constructor Declaration - __ctor____main____Vector__Vector____Vector__int
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vector<:Vector<:char:>:>::pushBack(Vector<:char:>) -> void
def __method____main____Vector__Vector____pushBack__Vector (this, __main____Vector__Vector__pushBack__val):
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
    stack.append (__field____main____Vector__Vector____size)
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
    stack.append (__field____main____Vector__Vector____capacity)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs >= __rhs
    stack.append (__res)
    __if__23__cond = stack.pop ()
    # get condition from stack
    if (__if__23__cond):
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
        stack.append (__field____main____Vector__Vector____capacity)
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
        stack.append(__field____main____Vector__Vector____capacity)
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
        stack.append (__field____main____Vector__Vector____capacity)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        __dim = stack.pop ()
        __res = [None] * __dim
        stack.append (__res)
        # LHS
        __main____Vector__Vector__pushBack__block__22__if__23__block__24__nData = 0
        __rhs = stack.pop()
        __main____Vector__Vector__pushBack__block__22__if__23__block__24__nData = __rhs
        stack.append (__main____Vector__Vector__pushBack__block__22__if__23__block__24__nData)
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
        __main____Vector__Vector__pushBack__block__22__if__23__block__24__for__25__i = 0
        __rhs = stack.pop()
        __main____Vector__Vector__pushBack__block__22__if__23__block__24__for__25__i = __rhs
        stack.append (__main____Vector__Vector__pushBack__block__22__if__23__block__24__for__25__i)
        # Using an infinite loop so we can write a separate multi-line condition
        while (1):
            # Condition
            # Less Than
            # LHS
            stack.append(__main____Vector__Vector__pushBack__block__22__if__23__block__24__for__25__i)
            # RHS
            # Member Accessor
            # LHS
            stack.append(this)
            # RHS
            stack.append (__field____main____Vector__Vector____size)
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
            stack.append (__field____main____Vector__Vector____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main____Vector__Vector__pushBack__block__22__if__23__block__24__for__25__i)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # LHS
            # Subscript assignment
            # LHS
            stack.append(__main____Vector__Vector__pushBack__block__22__if__23__block__24__nData)
            # OFFSET
            stack.append(__main____Vector__Vector__pushBack__block__22__if__23__block__24__for__25__i)
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
            stack.append(__main____Vector__Vector__pushBack__block__22__if__23__block__24__for__25__i)
            __rhs = stack.pop ()
            __main____Vector__Vector__pushBack__block__22__if__23__block__24__for__25__i = __main____Vector__Vector__pushBack__block__22__if__23__block__24__for__25__i + 1
            __res = __main____Vector__Vector__pushBack__block__22__if__23__block__24__for__25__i
            stack.append (__res)
        #-----------------------------------------------------------------
        # Statement
        # Member Accessor
        # LHS
        stack.append(this)
        # RHS
        stack.append (__field____main____Vector__Vector____data)
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
        stack.append(__main____Vector__Vector__pushBack__block__22__if__23__block__24__nData)
        # LHS
        # Member Accessor Assignment
        # LHS
        stack.append(this)
        # RHS
        stack.append(__field____main____Vector__Vector____data)
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
    stack.append(__main____Vector__Vector__pushBack__val)
    # LHS
    # Subscript assignment
    # LHS
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__Vector____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__Vector____size)
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
    stack.append (__field____main____Vector__Vector____size)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __rhs = stack.pop ()
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__Vector____size)
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
# End Method Declaration - __method____main____Vector__Vector____pushBack__Vector
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vector<:Vector<:char:>:>::popBack() -> Vector<:char:>
def __method____main____Vector__Vector____popBack (this):
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
    stack.append (__field____main____Vector__Vector____data)
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
    stack.append (__field____main____Vector__Vector____size)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __rhs = stack.pop ()
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__Vector____size)
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
# End Method Declaration - __method____main____Vector__Vector____popBack
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vector<:Vector<:char:>:>::get(int) -> Vector<:char:>
def __method____main____Vector__Vector____get__int (this, __main____Vector__Vector__get__index):
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
    stack.append (__field____main____Vector__Vector____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    stack.append(__main____Vector__Vector__get__index)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    __rVal = stack.pop ()
    return __rVal
    #---------------------------------------------------------------------
    return 0
# End Method Declaration - __method____main____Vector__Vector____get__int
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vector<:Vector<:char:>:>::set(int, Vector<:char:>) -> void
def __method____main____Vector__Vector____set__int__Vector (this, __main____Vector__Vector__set__index, __main____Vector__Vector__set__value):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main____Vector__Vector__set__value)
    # LHS
    # Subscript assignment
    # LHS
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__Vector____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    stack.append(__main____Vector__Vector__set__index)
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
# End Method Declaration - __method____main____Vector__Vector____set__int__Vector
#-------------------------------------------------------------------------

# Populate Dispatch Table
__dtable____main____Vector__Vector = [__method____main____Vector__Vector____pushBack__Vector, __method____main____Vector__Vector____popBack, __method____main____Vector__Vector____get__int, __method____main____Vector__Vector____set__int__Vector]
# End Class Declaration - __main____Vector__Vector
#=========================================================================

#=========================================================================
# Class Declaration - __main____Vector__char inherits __builtin____main__Object
# Creating Dispatch Table (will be populated later)
__dtable____main____Vector__char = []
#-------------------------------------------------------------------------
# Field - char[] Vector<:char:>::data
__field____main____Vector__char____data = 1
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Field - int Vector<:char:>::size
__field____main____Vector__char____size = 2
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Field - int Vector<:char:>::capacity
__field____main____Vector__char____capacity = 3
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Constructor Declaration - Vector<:char:>::Vector() -> Vector<:char:>
def __ctor____main____Vector__char____Vector ():
    # Creating Class Instance
    this = [0] * 4
    # Add Dispatch Table
    this[0] = __dtable____main____Vector__char
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
    stack.append(__field____main____Vector__char____capacity)
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
    stack.append(__field____main____Vector__char____size)
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
    stack.append (__field____main____Vector__char____capacity)
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
    stack.append(__field____main____Vector__char____data)
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
# End Constructor Declaration - __ctor____main____Vector__char____Vector
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Constructor Declaration - Vector<:char:>::Vector(int) -> Vector<:char:>
def __ctor____main____Vector__char____Vector__int (__main____Vector__char__Vector__size):
    # Creating Class Instance
    this = [0] * 4
    # Add Dispatch Table
    this[0] = __dtable____main____Vector__char
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Assignment - '='
    # RHS
    # Addition
    # LHS
    stack.append(__main____Vector__char__Vector__size)
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
    stack.append(__field____main____Vector__char____capacity)
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
    stack.append(__main____Vector__char__Vector__size)
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append(__field____main____Vector__char____size)
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
    stack.append (__field____main____Vector__char____capacity)
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
    stack.append(__field____main____Vector__char____data)
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
# End Constructor Declaration - __ctor____main____Vector__char____Vector__int
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vector<:char:>::pushBack(char) -> void
def __method____main____Vector__char____pushBack__char (this, __main____Vector__char__pushBack__val):
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
    stack.append (__field____main____Vector__char____size)
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
    stack.append (__field____main____Vector__char____capacity)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs >= __rhs
    stack.append (__res)
    __if__33__cond = stack.pop ()
    # get condition from stack
    if (__if__33__cond):
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
        stack.append (__field____main____Vector__char____capacity)
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
        stack.append(__field____main____Vector__char____capacity)
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
        stack.append (__field____main____Vector__char____capacity)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        __dim = stack.pop ()
        __res = [None] * __dim
        stack.append (__res)
        # LHS
        __main____Vector__char__pushBack__block__32__if__33__block__34__nData = 0
        __rhs = stack.pop()
        __main____Vector__char__pushBack__block__32__if__33__block__34__nData = __rhs
        stack.append (__main____Vector__char__pushBack__block__32__if__33__block__34__nData)
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
        __main____Vector__char__pushBack__block__32__if__33__block__34__for__35__i = 0
        __rhs = stack.pop()
        __main____Vector__char__pushBack__block__32__if__33__block__34__for__35__i = __rhs
        stack.append (__main____Vector__char__pushBack__block__32__if__33__block__34__for__35__i)
        # Using an infinite loop so we can write a separate multi-line condition
        while (1):
            # Condition
            # Less Than
            # LHS
            stack.append(__main____Vector__char__pushBack__block__32__if__33__block__34__for__35__i)
            # RHS
            # Member Accessor
            # LHS
            stack.append(this)
            # RHS
            stack.append (__field____main____Vector__char____size)
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
            stack.append (__field____main____Vector__char____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main____Vector__char__pushBack__block__32__if__33__block__34__for__35__i)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # LHS
            # Subscript assignment
            # LHS
            stack.append(__main____Vector__char__pushBack__block__32__if__33__block__34__nData)
            # OFFSET
            stack.append(__main____Vector__char__pushBack__block__32__if__33__block__34__for__35__i)
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
            stack.append(__main____Vector__char__pushBack__block__32__if__33__block__34__for__35__i)
            __rhs = stack.pop ()
            __main____Vector__char__pushBack__block__32__if__33__block__34__for__35__i = __main____Vector__char__pushBack__block__32__if__33__block__34__for__35__i + 1
            __res = __main____Vector__char__pushBack__block__32__if__33__block__34__for__35__i
            stack.append (__res)
        #-----------------------------------------------------------------
        # Statement
        # Member Accessor
        # LHS
        stack.append(this)
        # RHS
        stack.append (__field____main____Vector__char____data)
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
        stack.append(__main____Vector__char__pushBack__block__32__if__33__block__34__nData)
        # LHS
        # Member Accessor Assignment
        # LHS
        stack.append(this)
        # RHS
        stack.append(__field____main____Vector__char____data)
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
    stack.append(__main____Vector__char__pushBack__val)
    # LHS
    # Subscript assignment
    # LHS
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__char____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__char____size)
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
    stack.append (__field____main____Vector__char____size)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __rhs = stack.pop ()
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__char____size)
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
# End Method Declaration - __method____main____Vector__char____pushBack__char
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vector<:char:>::popBack() -> char
def __method____main____Vector__char____popBack (this):
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
    stack.append (__field____main____Vector__char____data)
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
    stack.append (__field____main____Vector__char____size)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __rhs = stack.pop ()
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__char____size)
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
# End Method Declaration - __method____main____Vector__char____popBack
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vector<:char:>::get(int) -> char
def __method____main____Vector__char____get__int (this, __main____Vector__char__get__index):
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
    stack.append (__field____main____Vector__char____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    stack.append(__main____Vector__char__get__index)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    __rVal = stack.pop ()
    return __rVal
    #---------------------------------------------------------------------
    return 0
# End Method Declaration - __method____main____Vector__char____get__int
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vector<:char:>::set(int, char) -> void
def __method____main____Vector__char____set__int__char (this, __main____Vector__char__set__index, __main____Vector__char__set__value):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main____Vector__char__set__value)
    # LHS
    # Subscript assignment
    # LHS
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__char____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    stack.append(__main____Vector__char__set__index)
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
# End Method Declaration - __method____main____Vector__char____set__int__char
#-------------------------------------------------------------------------

# Populate Dispatch Table
__dtable____main____Vector__char = [__method____main____Vector__char____pushBack__char, __method____main____Vector__char____popBack, __method____main____Vector__char____get__int, __method____main____Vector__char____set__int__char]
# End Class Declaration - __main____Vector__char
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
    __if__41__cond = stack.pop ()
    # get condition from stack
    if (__if__41__cond):
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
    __main__strlen__block__40__size = 0
    __rhs = stack.pop()
    __main__strlen__block__40__size = __rhs
    stack.append (__main__strlen__block__40__size)
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
        __res = __main__strlen__block__40__size
        __main__strlen__block__40__size = __main__strlen__block__40__size + 1
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
    stack.append(__main__strlen__block__40__size)
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
    __main__strcmp__block__43__asize = 0
    __rhs = stack.pop()
    __main__strcmp__block__43__asize = __rhs
    stack.append (__main__strcmp__block__43__asize)
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
    __main__strcmp__block__43__bsize = 0
    __rhs = stack.pop()
    __main__strcmp__block__43__bsize = __rhs
    stack.append (__main__strcmp__block__43__bsize)
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
    stack.append(__main__strcmp__block__43__asize)
    # RHS
    stack.append(__main__strcmp__block__43__bsize)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs != __rhs
    stack.append (__res)
    __if__44__cond = stack.pop ()
    # get condition from stack
    if (__if__44__cond):
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
    __main__strcmp__block__43__for__45__i = 0
    __rhs = stack.pop()
    __main__strcmp__block__43__for__45__i = __rhs
    stack.append (__main__strcmp__block__43__for__45__i)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        stack.append(__main__strcmp__block__43__for__45__i)
        # RHS
        stack.append(__main__strcmp__block__43__asize)
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
        stack.append(__main__strcmp__block__43__for__45__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        # Subscript
        # LHS
        stack.append(__main__strcmp__b)
        # OFFSET
        stack.append(__main__strcmp__block__43__for__45__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs != __rhs
        stack.append (__res)
        __if__47__cond = stack.pop ()
        # get condition from stack
        if (__if__47__cond):
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
        stack.append(__main__strcmp__block__43__for__45__i)
        __rhs = stack.pop ()
        __main__strcmp__block__43__for__45__i = __main__strcmp__block__43__for__45__i + 1
        __res = __main__strcmp__block__43__for__45__i
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
    __main__first_index_of__block__49__size = 0
    __rhs = stack.pop()
    __main__first_index_of__block__49__size = __rhs
    stack.append (__main__first_index_of__block__49__size)
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
    __main__first_index_of__block__49__for__50__i = 0
    __rhs = stack.pop()
    __main__first_index_of__block__49__for__50__i = __rhs
    stack.append (__main__first_index_of__block__49__for__50__i)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        stack.append(__main__first_index_of__block__49__for__50__i)
        # RHS
        stack.append(__main__first_index_of__block__49__size)
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
        stack.append(__main__first_index_of__block__49__for__50__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        stack.append(__main__first_index_of__c)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs == __rhs
        stack.append (__res)
        __if__52__cond = stack.pop ()
        # get condition from stack
        if (__if__52__cond):
            # Body
            # Return
            stack.append(__main__first_index_of__block__49__for__50__i)
            __rVal = stack.pop ()
            return __rVal
        # End of if
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # Update
        # Pre-Increment
        # RHS
        stack.append(__main__first_index_of__block__49__for__50__i)
        __rhs = stack.pop ()
        __main__first_index_of__block__49__for__50__i = __main__first_index_of__block__49__for__50__i + 1
        __res = __main__first_index_of__block__49__for__50__i
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
    __main__split__block__53__tokens = 0
    __rhs = stack.pop()
    __main__split__block__53__tokens = __rhs
    stack.append (__main__split__block__53__tokens)
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
    __main__split__block__53__size = 0
    __rhs = stack.pop()
    __main__split__block__53__size = __rhs
    stack.append (__main__split__block__53__size)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(0)
    # LHS
    __main__split__block__53__i = 0
    __rhs = stack.pop()
    __main__split__block__53__i = __rhs
    stack.append (__main__split__block__53__i)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(0)
    # LHS
    __main__split__block__53__j = 0
    __rhs = stack.pop()
    __main__split__block__53__j = __rhs
    stack.append (__main__split__block__53__j)
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
        stack.append(__main__split__block__53__i)
        # RHS
        stack.append(__main__split__block__53__size)
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
        stack.append(__main__split__block__53__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        stack.append(__main__split__delim)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs != __rhs
        stack.append (__res)
        __if__56__cond = stack.pop ()
        # get condition from stack
        if (__if__56__cond):
            # Body
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Assignment - '='
            # RHS
            # Int Literal
            stack.append(0)
            # LHS
            __main__split__block__53__while__54__block__55__if__56__block__57__count = 0
            __rhs = stack.pop()
            __main__split__block__53__while__54__block__55__if__56__block__57__count = __rhs
            stack.append (__main__split__block__53__while__54__block__55__if__56__block__57__count)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            # Statement
            # Assignment - '='
            # RHS
            stack.append(__main__split__block__53__i)
            # LHS
            __main__split__block__53__while__54__block__55__if__56__block__57__k = 0
            __rhs = stack.pop()
            __main__split__block__53__while__54__block__55__if__56__block__57__k = __rhs
            stack.append (__main__split__block__53__while__54__block__55__if__56__block__57__k)
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
                stack.append(__main__split__block__53__while__54__block__55__if__56__block__57__k)
                # RHS
                stack.append(__main__split__block__53__size)
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
                __res = __main__split__block__53__while__54__block__55__if__56__block__57__k
                __main__split__block__53__while__54__block__55__if__56__block__57__k = __main__split__block__53__while__54__block__55__if__56__block__57__k + 1
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
                __if__59__cond = stack.pop ()
                # get condition from stack
                if (__if__59__cond):
                    # Body
                    # Statement
                    # Pre-Increment
                    # RHS
                    stack.append(__main__split__block__53__while__54__block__55__if__56__block__57__count)
                    __rhs = stack.pop ()
                    __main__split__block__53__while__54__block__55__if__56__block__57__count = __main__split__block__53__while__54__block__55__if__56__block__57__count + 1
                    __res = __main__split__block__53__while__54__block__55__if__56__block__57__count
                    stack.append (__res)
                    # Statement results can be ignored
                    stack.pop ()
                    # End Statement

                #---------------------------------------------------------
                # Else-Statement
                else:
                    # Break out of __while__58
                    break
                #---------------------------------------------------------
                # End of if
                #---------------------------------------------------------
            # End of While
            #-------------------------------------------------------------
            # Statement
            # Method Call - Vector<:char[]:>::pushBack(char[]) -> void
            # LHS
            stack.append(__main__split__block__53__tokens)
            # RHS
            # Arguments
            # Addition
            # LHS
            stack.append(__main__split__block__53__while__54__block__55__if__56__block__57__count)
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
            __main__split__block__53__while__54__block__55__if__56__block__57__for__60__k = 0
            __rhs = stack.pop()
            __main__split__block__53__while__54__block__55__if__56__block__57__for__60__k = __rhs
            stack.append (__main__split__block__53__while__54__block__55__if__56__block__57__for__60__k)
            # Using an infinite loop so we can write a separate multi-line condition
            while (1):
                # Condition
                # Less Than
                # LHS
                stack.append(__main__split__block__53__while__54__block__55__if__56__block__57__for__60__k)
                # RHS
                stack.append(__main__split__block__53__while__54__block__55__if__56__block__57__count)
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
                __res = __main__split__block__53__i
                __main__split__block__53__i = __main__split__block__53__i + 1
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
                stack.append(__main__split__block__53__tokens)
                # RHS
                stack.append (__field____main____Vector__char__1____data)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                # OFFSET
                stack.append(__main__split__block__53__j)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # OFFSET
                stack.append(__main__split__block__53__while__54__block__55__if__56__block__57__for__60__k)
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
                stack.append(__main__split__block__53__while__54__block__55__if__56__block__57__for__60__k)
                __rhs = stack.pop ()
                __main__split__block__53__while__54__block__55__if__56__block__57__for__60__k = __main__split__block__53__while__54__block__55__if__56__block__57__for__60__k + 1
                __res = __main__split__block__53__while__54__block__55__if__56__block__57__for__60__k
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
            stack.append(__main__split__block__53__tokens)
            # RHS
            stack.append (__field____main____Vector__char__1____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main__split__block__53__j)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # OFFSET
            stack.append(__main__split__block__53__while__54__block__55__if__56__block__57__count)
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
            stack.append(__main__split__block__53__j)
            __rhs = stack.pop ()
            __main__split__block__53__j = __main__split__block__53__j + 1
            __res = __main__split__block__53__j
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
        stack.append(__main__split__block__53__i)
        __rhs = stack.pop ()
        __main__split__block__53__i = __main__split__block__53__i + 1
        __res = __main__split__block__53__i
        stack.append (__res)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
    # End of While
    #---------------------------------------------------------------------
    # Return
    stack.append(__main__split__block__53__tokens)
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
    __if__63__cond = stack.pop ()
    # get condition from stack
    if (__if__63__cond):
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
    __if__65__cond = stack.pop ()
    # get condition from stack
    if (__if__65__cond):
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
    __if__67__cond = stack.pop ()
    # get condition from stack
    if (__if__67__cond):
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
    __if__69__cond = stack.pop ()
    # get condition from stack
    if (__if__69__cond):
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
    __if__71__cond = stack.pop ()
    # get condition from stack
    if (__if__71__cond):
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
    __if__73__cond = stack.pop ()
    # get condition from stack
    if (__if__73__cond):
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
# Statement
# Assignment - '='
# RHS
# Int Literal
stack.append(0)
# LHS
__main__cycle = 0
__rhs = stack.pop()
__main__cycle = __rhs
stack.append (__main__cycle)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Assignment - '='
# RHS
# Int Literal
stack.append(0)
# LHS
__main__column = 0
__rhs = stack.pop()
__main__column = __rhs
stack.append (__main__column)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Assignment - '='
# RHS
# Int Literal
stack.append(1)
# LHS
__main__registerx = 0
__rhs = stack.pop()
__main__registerx = __rhs
stack.append (__main__registerx)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Assignment - '='
# RHS
# Constructor Call - Vector<:int:>::Vector() -> Vector<:int:>
# Arguments
__retval = __ctor____main____Vector__int____Vector ()
stack.append (__retval)
# LHS
__main__x_prev = 0
__rhs = stack.pop()
__main__x_prev = __rhs
stack.append (__main__x_prev)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Method Call - Vector<:int:>::pushBack(int) -> void
# LHS
stack.append(__main__x_prev)
# RHS
# Arguments
stack.append(__main__registerx)
__arg0 = stack.pop ()
__obj = stack.pop ()
__retval = __method____main____Vector__int____pushBack__int (__obj, __arg0)
stack.append (__retval)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Assignment - '='
# RHS
# Constructor Call - Vector<:Vector<:char:>:>::Vector() -> Vector<:Vector<:char:>:>
# Arguments
__retval = __ctor____main____Vector__Vector____Vector ()
stack.append (__retval)
# LHS
__main__output = 0
__rhs = stack.pop()
__main__output = __rhs
stack.append (__main__output)
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
__main__for__76__l = 0
__rhs = stack.pop()
__main__for__76__l = __rhs
stack.append (__main__for__76__l)
# Using an infinite loop so we can write a separate multi-line condition
while (1):
    # Condition
    # Less Than
    # LHS
    stack.append(__main__for__76__l)
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
    # Function Call - split(char[], char) -> Vector<:char[]:>
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
    stack.append(__main__for__76__l)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    # Char Literal
    stack.append(' ')
    __arg1 = stack.pop ()
    __arg0 = stack.pop ()
    # *** split
    __res = __main____split__char__1__char (__arg0, __arg1)
    stack.append (__res) # function call result
    # LHS
    __main__for__76__block__77__tokens = 0
    __rhs = stack.pop()
    __main__for__76__block__77__tokens = __rhs
    stack.append (__main__for__76__block__77__tokens)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
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
    stack.append(__main__for__76__block__77__tokens)
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
    stack.append('n')
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs == __rhs
    stack.append (__res)
    __if__78__cond = stack.pop ()
    # Condition for elif #0
    # Equal
    # LHS
    # Subscript
    # LHS
    # Subscript
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main__for__76__block__77__tokens)
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
    stack.append('a')
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs == __rhs
    stack.append (__res)
    __elif__78x0__cond = stack.pop ()
    # get condition from stack
    if (__if__78__cond):
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
        stack.append(__main__column)
        # RHS
        # Int Literal
        stack.append(0)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs == __rhs
        stack.append (__res)
        __if__80__cond = stack.pop ()
        # get condition from stack
        if (__if__80__cond):
            # Body
            # Statement
            # Method Call - Vector<:Vector<:char:>:>::pushBack(Vector<:char:>) -> void
            # LHS
            stack.append(__main__output)
            # RHS
            # Arguments
            # Constructor Call - Vector<:char:>::Vector() -> Vector<:char:>
            # Arguments
            __retval = __ctor____main____Vector__char____Vector ()
            stack.append (__retval)
            __arg0 = stack.pop ()
            __obj = stack.pop ()
            __retval = __method____main____Vector__Vector____pushBack__Vector (__obj, __arg0)
            stack.append (__retval)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

        # End of if
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # If-Statement
        # Precomputing all if/elif conditions and give unique names
        # bc we can't have code between if and elif
        # Condition
        # AND
        # LHS
        # Less Than or Equal to
        # LHS
        # Subtraction
        # LHS
        stack.append(__main__registerx)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs - __rhs
        stack.append(__res)
        # RHS
        stack.append(__main__column)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs <= __rhs
        stack.append (__res)
        # RHS
        # Less Than or Equal to
        # LHS
        stack.append(__main__column)
        # RHS
        # Addition
        # LHS
        stack.append(__main__registerx)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs <= __rhs
        stack.append (__res)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs and __rhs
        stack.append (__res)
        __if__81__cond = stack.pop ()
        # get condition from stack
        if (__if__81__cond):
            # Body
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Method Call - Vector<:char:>::pushBack(char) -> void
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__output)
            # RHS
            stack.append (__field____main____Vector__Vector____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            # Subtraction
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__output)
            # RHS
            stack.append (__field____main____Vector__Vector____size)
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
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            # Arguments
            # Char Literal
            stack.append('#')
            __arg0 = stack.pop ()
            __obj = stack.pop ()
            __retval = __method____main____Vector__char____pushBack__char (__obj, __arg0)
            stack.append (__retval)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            #-------------------------------------------------------------
        #-----------------------------------------------------------------
        # Else-Statement
        else:
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Method Call - Vector<:char:>::pushBack(char) -> void
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__output)
            # RHS
            stack.append (__field____main____Vector__Vector____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            # Subtraction
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__output)
            # RHS
            stack.append (__field____main____Vector__Vector____size)
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
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            # Arguments
            # Char Literal
            stack.append('.')
            __arg0 = stack.pop ()
            __obj = stack.pop ()
            __retval = __method____main____Vector__char____pushBack__char (__obj, __arg0)
            stack.append (__retval)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            #-------------------------------------------------------------
        #-----------------------------------------------------------------
        # End of if
        #-----------------------------------------------------------------
        # Statement
        # Assignment - '+='
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __main__cycle = __main__cycle + __rhs
        stack.append (__main__cycle)
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
        stack.append(__main__column)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        # RHS
        # Int Literal
        stack.append(40)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs % __rhs
        stack.append(__res)
        __rhs = stack.pop()
        __main__column = __rhs
        stack.append (__main__column)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Method Call - Vector<:int:>::pushBack(int) -> void
        # LHS
        stack.append(__main__x_prev)
        # RHS
        # Arguments
        stack.append(__main__registerx)
        __arg0 = stack.pop ()
        __obj = stack.pop ()
        __retval = __method____main____Vector__int____pushBack__int (__obj, __arg0)
        stack.append (__retval)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
    #---------------------------------------------------------------------
    # Elif-Statement
    # Condition
    elif (__elif__78x0__cond):
        # Body
        #-----------------------------------------------------------------
        # Code Block
        # Statement
        # Assignment - '='
        # RHS
        # Function Call - stringToInt(char[]) -> int
        # Arguments
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__for__76__block__77__tokens)
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
        __main__for__76__block__77__elif__78x0__block__84__value = 0
        __rhs = stack.pop()
        __main__for__76__block__77__elif__78x0__block__84__value = __rhs
        stack.append (__main__for__76__block__77__elif__78x0__block__84__value)
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
        stack.append(__main__column)
        # RHS
        # Int Literal
        stack.append(0)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs == __rhs
        stack.append (__res)
        __if__85__cond = stack.pop ()
        # get condition from stack
        if (__if__85__cond):
            # Body
            # Statement
            # Method Call - Vector<:Vector<:char:>:>::pushBack(Vector<:char:>) -> void
            # LHS
            stack.append(__main__output)
            # RHS
            # Arguments
            # Constructor Call - Vector<:char:>::Vector() -> Vector<:char:>
            # Arguments
            __retval = __ctor____main____Vector__char____Vector ()
            stack.append (__retval)
            __arg0 = stack.pop ()
            __obj = stack.pop ()
            __retval = __method____main____Vector__Vector____pushBack__Vector (__obj, __arg0)
            stack.append (__retval)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

        # End of if
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # If-Statement
        # Precomputing all if/elif conditions and give unique names
        # bc we can't have code between if and elif
        # Condition
        # AND
        # LHS
        # Less Than or Equal to
        # LHS
        # Subtraction
        # LHS
        stack.append(__main__registerx)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs - __rhs
        stack.append(__res)
        # RHS
        stack.append(__main__column)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs <= __rhs
        stack.append (__res)
        # RHS
        # Less Than or Equal to
        # LHS
        stack.append(__main__column)
        # RHS
        # Addition
        # LHS
        stack.append(__main__registerx)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs <= __rhs
        stack.append (__res)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs and __rhs
        stack.append (__res)
        __if__86__cond = stack.pop ()
        # get condition from stack
        if (__if__86__cond):
            # Body
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Method Call - Vector<:char:>::pushBack(char) -> void
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__output)
            # RHS
            stack.append (__field____main____Vector__Vector____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            # Subtraction
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__output)
            # RHS
            stack.append (__field____main____Vector__Vector____size)
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
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            # Arguments
            # Char Literal
            stack.append('#')
            __arg0 = stack.pop ()
            __obj = stack.pop ()
            __retval = __method____main____Vector__char____pushBack__char (__obj, __arg0)
            stack.append (__retval)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            #-------------------------------------------------------------
        #-----------------------------------------------------------------
        # Else-Statement
        else:
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Method Call - Vector<:char:>::pushBack(char) -> void
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__output)
            # RHS
            stack.append (__field____main____Vector__Vector____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            # Subtraction
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__output)
            # RHS
            stack.append (__field____main____Vector__Vector____size)
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
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            # Arguments
            # Char Literal
            stack.append('.')
            __arg0 = stack.pop ()
            __obj = stack.pop ()
            __retval = __method____main____Vector__char____pushBack__char (__obj, __arg0)
            stack.append (__retval)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            #-------------------------------------------------------------
        #-----------------------------------------------------------------
        # End of if
        #-----------------------------------------------------------------
        # Statement
        # Assignment - '+='
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __main__cycle = __main__cycle + __rhs
        stack.append (__main__cycle)
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
        stack.append(__main__column)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        # RHS
        # Int Literal
        stack.append(40)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs % __rhs
        stack.append(__res)
        __rhs = stack.pop()
        __main__column = __rhs
        stack.append (__main__column)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Method Call - Vector<:int:>::pushBack(int) -> void
        # LHS
        stack.append(__main__x_prev)
        # RHS
        # Arguments
        stack.append(__main__registerx)
        __arg0 = stack.pop ()
        __obj = stack.pop ()
        __retval = __method____main____Vector__int____pushBack__int (__obj, __arg0)
        stack.append (__retval)
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
        stack.append(__main__column)
        # RHS
        # Int Literal
        stack.append(0)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs == __rhs
        stack.append (__res)
        __if__89__cond = stack.pop ()
        # get condition from stack
        if (__if__89__cond):
            # Body
            # Statement
            # Method Call - Vector<:Vector<:char:>:>::pushBack(Vector<:char:>) -> void
            # LHS
            stack.append(__main__output)
            # RHS
            # Arguments
            # Constructor Call - Vector<:char:>::Vector() -> Vector<:char:>
            # Arguments
            __retval = __ctor____main____Vector__char____Vector ()
            stack.append (__retval)
            __arg0 = stack.pop ()
            __obj = stack.pop ()
            __retval = __method____main____Vector__Vector____pushBack__Vector (__obj, __arg0)
            stack.append (__retval)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

        # End of if
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # If-Statement
        # Precomputing all if/elif conditions and give unique names
        # bc we can't have code between if and elif
        # Condition
        # AND
        # LHS
        # Less Than or Equal to
        # LHS
        # Subtraction
        # LHS
        stack.append(__main__registerx)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs - __rhs
        stack.append(__res)
        # RHS
        stack.append(__main__column)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs <= __rhs
        stack.append (__res)
        # RHS
        # Less Than or Equal to
        # LHS
        stack.append(__main__column)
        # RHS
        # Addition
        # LHS
        stack.append(__main__registerx)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs <= __rhs
        stack.append (__res)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs and __rhs
        stack.append (__res)
        __if__90__cond = stack.pop ()
        # get condition from stack
        if (__if__90__cond):
            # Body
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Method Call - Vector<:char:>::pushBack(char) -> void
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__output)
            # RHS
            stack.append (__field____main____Vector__Vector____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            # Subtraction
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__output)
            # RHS
            stack.append (__field____main____Vector__Vector____size)
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
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            # Arguments
            # Char Literal
            stack.append('#')
            __arg0 = stack.pop ()
            __obj = stack.pop ()
            __retval = __method____main____Vector__char____pushBack__char (__obj, __arg0)
            stack.append (__retval)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            #-------------------------------------------------------------
        #-----------------------------------------------------------------
        # Else-Statement
        else:
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Method Call - Vector<:char:>::pushBack(char) -> void
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__output)
            # RHS
            stack.append (__field____main____Vector__Vector____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            # Subtraction
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__output)
            # RHS
            stack.append (__field____main____Vector__Vector____size)
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
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            # Arguments
            # Char Literal
            stack.append('.')
            __arg0 = stack.pop ()
            __obj = stack.pop ()
            __retval = __method____main____Vector__char____pushBack__char (__obj, __arg0)
            stack.append (__retval)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            #-------------------------------------------------------------
        #-----------------------------------------------------------------
        # End of if
        #-----------------------------------------------------------------
        # Statement
        # Assignment - '+='
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __main__cycle = __main__cycle + __rhs
        stack.append (__main__cycle)
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
        stack.append(__main__column)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        # RHS
        # Int Literal
        stack.append(40)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs % __rhs
        stack.append(__res)
        __rhs = stack.pop()
        __main__column = __rhs
        stack.append (__main__column)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Method Call - Vector<:int:>::pushBack(int) -> void
        # LHS
        stack.append(__main__x_prev)
        # RHS
        # Arguments
        stack.append(__main__registerx)
        __arg0 = stack.pop ()
        __obj = stack.pop ()
        __retval = __method____main____Vector__int____pushBack__int (__obj, __arg0)
        stack.append (__retval)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '+='
        # RHS
        stack.append(__main__for__76__block__77__elif__78x0__block__84__value)
        __rhs = stack.pop()
        __main__registerx = __main__registerx + __rhs
        stack.append (__main__registerx)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    # Else-Statement
    else:
        #-----------------------------------------------------------------
        # Code Block
        # Statement
        # Function Call - println(char[]) -> void
        # Arguments
        # String Literal
        stack.append("Unknown instruction"+'\0')
        __arg0 = stack.pop ()
        # *** println
        __res = __builtin__println__char__1 (__arg0)
        stack.append (__res) # function call result
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
    #---------------------------------------------------------------------
    # End of if
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    # Update
    # Pre-Increment
    # RHS
    stack.append(__main__for__76__l)
    __rhs = stack.pop ()
    __main__for__76__l = __main__for__76__l + 1
    __res = __main__for__76__l
    stack.append (__res)
#-------------------------------------------------------------------------
# Statement
# Assignment - '='
# RHS
# Array Constructor
# Elements
# Array Constructor
# Elements
# String Literal
stack.append("###."+'\0')
# String Literal
stack.append("#..#"+'\0')
# String Literal
stack.append("#..#"+'\0')
# String Literal
stack.append("###."+'\0')
# String Literal
stack.append("#.#."+'\0')
# String Literal
stack.append("#..#"+'\0')
__elem5 = stack.pop ()
__elem4 = stack.pop ()
__elem3 = stack.pop ()
__elem2 = stack.pop ()
__elem1 = stack.pop ()
__elem0 = stack.pop ()
__list = [0] * 6
__list[0] = __elem0
__list[1] = __elem1
__list[2] = __elem2
__list[3] = __elem3
__list[4] = __elem4
__list[5] = __elem5
stack.append (__list)
# Array Constructor
# Elements
# String Literal
stack.append("#..."+'\0')
# String Literal
stack.append("#..."+'\0')
# String Literal
stack.append("#..."+'\0')
# String Literal
stack.append("#..."+'\0')
# String Literal
stack.append("#..."+'\0')
# String Literal
stack.append("####"+'\0')
__elem5 = stack.pop ()
__elem4 = stack.pop ()
__elem3 = stack.pop ()
__elem2 = stack.pop ()
__elem1 = stack.pop ()
__elem0 = stack.pop ()
__list = [0] * 6
__list[0] = __elem0
__list[1] = __elem1
__list[2] = __elem2
__list[3] = __elem3
__list[4] = __elem4
__list[5] = __elem5
stack.append (__list)
# Array Constructor
# Elements
# String Literal
stack.append("####"+'\0')
# String Literal
stack.append("#..."+'\0')
# String Literal
stack.append("###."+'\0')
# String Literal
stack.append("#..."+'\0')
# String Literal
stack.append("#..."+'\0')
# String Literal
stack.append("####"+'\0')
__elem5 = stack.pop ()
__elem4 = stack.pop ()
__elem3 = stack.pop ()
__elem2 = stack.pop ()
__elem1 = stack.pop ()
__elem0 = stack.pop ()
__list = [0] * 6
__list[0] = __elem0
__list[1] = __elem1
__list[2] = __elem2
__list[3] = __elem3
__list[4] = __elem4
__list[5] = __elem5
stack.append (__list)
# Array Constructor
# Elements
# String Literal
stack.append("####"+'\0')
# String Literal
stack.append("...#"+'\0')
# String Literal
stack.append("..#."+'\0')
# String Literal
stack.append(".#.."+'\0')
# String Literal
stack.append("#..."+'\0')
# String Literal
stack.append("####"+'\0')
__elem5 = stack.pop ()
__elem4 = stack.pop ()
__elem3 = stack.pop ()
__elem2 = stack.pop ()
__elem1 = stack.pop ()
__elem0 = stack.pop ()
__list = [0] * 6
__list[0] = __elem0
__list[1] = __elem1
__list[2] = __elem2
__list[3] = __elem3
__list[4] = __elem4
__list[5] = __elem5
stack.append (__list)
# Array Constructor
# Elements
# String Literal
stack.append("####"+'\0')
# String Literal
stack.append("#..."+'\0')
# String Literal
stack.append("###."+'\0')
# String Literal
stack.append("#..."+'\0')
# String Literal
stack.append("#..."+'\0')
# String Literal
stack.append("#..."+'\0')
__elem5 = stack.pop ()
__elem4 = stack.pop ()
__elem3 = stack.pop ()
__elem2 = stack.pop ()
__elem1 = stack.pop ()
__elem0 = stack.pop ()
__list = [0] * 6
__list[0] = __elem0
__list[1] = __elem1
__list[2] = __elem2
__list[3] = __elem3
__list[4] = __elem4
__list[5] = __elem5
stack.append (__list)
# Array Constructor
# Elements
# String Literal
stack.append(".##."+'\0')
# String Literal
stack.append("#..#"+'\0')
# String Literal
stack.append("#..."+'\0')
# String Literal
stack.append("#.##"+'\0')
# String Literal
stack.append("#..#"+'\0')
# String Literal
stack.append(".###"+'\0')
__elem5 = stack.pop ()
__elem4 = stack.pop ()
__elem3 = stack.pop ()
__elem2 = stack.pop ()
__elem1 = stack.pop ()
__elem0 = stack.pop ()
__list = [0] * 6
__list[0] = __elem0
__list[1] = __elem1
__list[2] = __elem2
__list[3] = __elem3
__list[4] = __elem4
__list[5] = __elem5
stack.append (__list)
__elem5 = stack.pop ()
__elem4 = stack.pop ()
__elem3 = stack.pop ()
__elem2 = stack.pop ()
__elem1 = stack.pop ()
__elem0 = stack.pop ()
__list = [0] * 6
__list[0] = __elem0
__list[1] = __elem1
__list[2] = __elem2
__list[3] = __elem3
__list[4] = __elem4
__list[5] = __elem5
stack.append (__list)
# LHS
__main__ascii_to_char_index = 0
__rhs = stack.pop()
__main__ascii_to_char_index = __rhs
stack.append (__main__ascii_to_char_index)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Assignment - '='
# RHS
# String Literal
stack.append("RLEZFG"+'\0')
# LHS
__main__char_index_to_char = 0
__rhs = stack.pop()
__main__char_index_to_char = __rhs
stack.append (__main__char_index_to_char)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Assignment - '='
# RHS
# Function Call - strlen(char[]) -> int
# Arguments
stack.append(__main__char_index_to_char)
__arg0 = stack.pop ()
# *** strlen
__res = __main____strlen__char__1 (__arg0)
stack.append (__res) # function call result
# LHS
__main__num_known_chars = 0
__rhs = stack.pop()
__main__num_known_chars = __rhs
stack.append (__main__num_known_chars)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Assignment - '='
# RHS
# Int Literal
stack.append(6)
# LHS
__main__char_height = 0
__rhs = stack.pop()
__main__char_height = __rhs
stack.append (__main__char_height)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Assignment - '='
# RHS
# Int Literal
stack.append(4)
# LHS
__main__char_width = 0
__rhs = stack.pop()
__main__char_width = __rhs
stack.append (__main__char_width)
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
__main__for__94__letter_base = 0
__rhs = stack.pop()
__main__for__94__letter_base = __rhs
stack.append (__main__for__94__letter_base)
# Using an infinite loop so we can write a separate multi-line condition
while (1):
    # Condition
    # Less Than
    # LHS
    stack.append(__main__for__94__letter_base)
    # RHS
    # Member Accessor
    # LHS
    # Subscript
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main__output)
    # RHS
    stack.append (__field____main____Vector__Vector____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    # Int Literal
    stack.append(0)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    # RHS
    stack.append (__field____main____Vector__char____size)
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
    #---------------------------------------------------------------------
    # For-Loop
    # Init
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(0)
    # LHS
    __main__for__94__block__95__for__96__c = 0
    __rhs = stack.pop()
    __main__for__94__block__95__for__96__c = __rhs
    stack.append (__main__for__94__block__95__for__96__c)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        stack.append(__main__for__94__block__95__for__96__c)
        # RHS
        stack.append(__main__num_known_chars)
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
        # Int Literal
        stack.append(1)
        # LHS
        __main__for__94__block__95__for__96__block__97__is_match = 0
        __rhs = stack.pop()
        __main__for__94__block__95__for__96__block__97__is_match = __rhs
        stack.append (__main__for__94__block__95__for__96__block__97__is_match)
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
        __main__for__94__block__95__for__96__block__97__for__98__i = 0
        __rhs = stack.pop()
        __main__for__94__block__95__for__96__block__97__for__98__i = __rhs
        stack.append (__main__for__94__block__95__for__96__block__97__for__98__i)
        # Using an infinite loop so we can write a separate multi-line condition
        while (1):
            # Condition
            # Less Than
            # LHS
            stack.append(__main__for__94__block__95__for__96__block__97__for__98__i)
            # RHS
            stack.append(__main__char_height)
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
            # For-Loop
            # Init
            # Assignment - '='
            # RHS
            # Int Literal
            stack.append(0)
            # LHS
            __main__for__94__block__95__for__96__block__97__for__98__block__99__for__100__j = 0
            __rhs = stack.pop()
            __main__for__94__block__95__for__96__block__97__for__98__block__99__for__100__j = __rhs
            stack.append (__main__for__94__block__95__for__96__block__97__for__98__block__99__for__100__j)
            # Using an infinite loop so we can write a separate multi-line condition
            while (1):
                # Condition
                # Less Than
                # LHS
                stack.append(__main__for__94__block__95__for__96__block__97__for__98__block__99__for__100__j)
                # RHS
                stack.append(__main__char_width)
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
                #---------------------------------------------------------
                # If-Statement
                # Precomputing all if/elif conditions and give unique names
                # bc we can't have code between if and elif
                # Condition
                # Not Equal
                # LHS
                # Subscript
                # LHS
                # Member Accessor
                # LHS
                # Subscript
                # LHS
                # Member Accessor
                # LHS
                stack.append(__main__output)
                # RHS
                stack.append (__field____main____Vector__Vector____data)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                # OFFSET
                stack.append(__main__for__94__block__95__for__96__block__97__for__98__i)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # RHS
                stack.append (__field____main____Vector__char____data)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                # OFFSET
                # Addition
                # LHS
                stack.append(__main__for__94__block__95__for__96__block__97__for__98__block__99__for__100__j)
                # RHS
                stack.append(__main__for__94__letter_base)
                __rhs = stack.pop()
                __lhs = stack.pop()
                __res = __lhs + __rhs
                stack.append(__res)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # RHS
                # Subscript
                # LHS
                # Subscript
                # LHS
                # Subscript
                # LHS
                stack.append(__main__ascii_to_char_index)
                # OFFSET
                stack.append(__main__for__94__block__95__for__96__c)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # OFFSET
                stack.append(__main__for__94__block__95__for__96__block__97__for__98__i)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # OFFSET
                stack.append(__main__for__94__block__95__for__96__block__97__for__98__block__99__for__100__j)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs != __rhs
                stack.append (__res)
                __if__102__cond = stack.pop ()
                # get condition from stack
                if (__if__102__cond):
                    # Body
                    #-----------------------------------------------------
                    # Code Block
                    # Statement
                    # Assignment - '='
                    # RHS
                    # Int Literal
                    stack.append(0)
                    __rhs = stack.pop()
                    __main__for__94__block__95__for__96__block__97__is_match = __rhs
                    stack.append (__main__for__94__block__95__for__96__block__97__is_match)
                    # Statement results can be ignored
                    stack.pop ()
                    # End Statement

                    # Break out of __for__100
                    break
                    #-----------------------------------------------------
                # End of if
                #---------------------------------------------------------
                #---------------------------------------------------------
                # Update
                # Pre-Increment
                # RHS
                stack.append(__main__for__94__block__95__for__96__block__97__for__98__block__99__for__100__j)
                __rhs = stack.pop ()
                __main__for__94__block__95__for__96__block__97__for__98__block__99__for__100__j = __main__for__94__block__95__for__96__block__97__for__98__block__99__for__100__j + 1
                __res = __main__for__94__block__95__for__96__block__97__for__98__block__99__for__100__j
                stack.append (__res)
            #-------------------------------------------------------------
            #-------------------------------------------------------------
            # Update
            # Pre-Increment
            # RHS
            stack.append(__main__for__94__block__95__for__96__block__97__for__98__i)
            __rhs = stack.pop ()
            __main__for__94__block__95__for__96__block__97__for__98__i = __main__for__94__block__95__for__96__block__97__for__98__i + 1
            __res = __main__for__94__block__95__for__96__block__97__for__98__i
            stack.append (__res)
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # If-Statement
        # Precomputing all if/elif conditions and give unique names
        # bc we can't have code between if and elif
        # Condition
        stack.append(__main__for__94__block__95__for__96__block__97__is_match)
        __if__104__cond = stack.pop ()
        # get condition from stack
        if (__if__104__cond):
            # Body
            # Statement
            # Function Call - print(char) -> void
            # Arguments
            # Subscript
            # LHS
            stack.append(__main__char_index_to_char)
            # OFFSET
            stack.append(__main__for__94__block__95__for__96__c)
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

        # End of if
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # Update
        # Pre-Increment
        # RHS
        stack.append(__main__for__94__block__95__for__96__c)
        __rhs = stack.pop ()
        __main__for__94__block__95__for__96__c = __main__for__94__block__95__for__96__c + 1
        __res = __main__for__94__block__95__for__96__c
        stack.append (__res)
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    # Update
    # Assignment - '+='
    # RHS
    # Addition
    # LHS
    stack.append(__main__char_width)
    # RHS
    # Int Literal
    stack.append(1)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs + __rhs
    stack.append(__res)
    __rhs = stack.pop()
    __main__for__94__letter_base = __main__for__94__letter_base + __rhs
    stack.append (__main__for__94__letter_base)
#-------------------------------------------------------------------------
# Statement
# Function Call - println() -> void
# Arguments
# *** println
__res = __builtin__println ()
stack.append (__res) # function call result
# Statement results can be ignored
stack.pop ()
# End Statement


#=========================================================================
#### END OF CODE ########################################################
#=========================================================================

