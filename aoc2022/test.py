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
    print (s, end="")

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
        __main____Vector__Point__pushBack__block__12__if__13__block__14__nData = 0
        __rhs = stack.pop()
        __main____Vector__Point__pushBack__block__12__if__13__block__14__nData = __rhs
        stack.append (__main____Vector__Point__pushBack__block__12__if__13__block__14__nData)
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
        __main____Vector__Point__pushBack__block__12__if__13__block__14__for__15__i = 0
        __rhs = stack.pop()
        __main____Vector__Point__pushBack__block__12__if__13__block__14__for__15__i = __rhs
        stack.append (__main____Vector__Point__pushBack__block__12__if__13__block__14__for__15__i)
        # Using an infinite loop so we can write a separate multi-line condition
        while (1):
            # Condition
            # Less Than
            # LHS
            stack.append(__main____Vector__Point__pushBack__block__12__if__13__block__14__for__15__i)
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
            stack.append(__main____Vector__Point__pushBack__block__12__if__13__block__14__for__15__i)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # LHS
            # Subscript assignment
            # LHS
            stack.append(__main____Vector__Point__pushBack__block__12__if__13__block__14__nData)
            # OFFSET
            stack.append(__main____Vector__Point__pushBack__block__12__if__13__block__14__for__15__i)
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
            stack.append(__main____Vector__Point__pushBack__block__12__if__13__block__14__for__15__i)
            __rhs = stack.pop ()
            __main____Vector__Point__pushBack__block__12__if__13__block__14__for__15__i = __main____Vector__Point__pushBack__block__12__if__13__block__14__for__15__i + 1
            __res = __main____Vector__Point__pushBack__block__12__if__13__block__14__for__15__i
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
        stack.append(__main____Vector__Point__pushBack__block__12__if__13__block__14__nData)
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
__dtable____main____Vector__Point = [__method____main____Vector__Point____pushBack__Point, __method____main____Vector__Point____popBack, __method____main____Vector__Point____get__int, __method____main____Vector__Point____set__int__Point]
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
    __if__21__cond = stack.pop ()
    # get condition from stack
    if (__if__21__cond):
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
    __main__strlen__block__20__size = 0
    __rhs = stack.pop()
    __main__strlen__block__20__size = __rhs
    stack.append (__main__strlen__block__20__size)
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
        __res = __main__strlen__block__20__size
        __main__strlen__block__20__size = __main__strlen__block__20__size + 1
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
    stack.append(__main__strlen__block__20__size)
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
    __main__strcmp__block__23__asize = 0
    __rhs = stack.pop()
    __main__strcmp__block__23__asize = __rhs
    stack.append (__main__strcmp__block__23__asize)
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
    __main__strcmp__block__23__bsize = 0
    __rhs = stack.pop()
    __main__strcmp__block__23__bsize = __rhs
    stack.append (__main__strcmp__block__23__bsize)
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
    stack.append(__main__strcmp__block__23__asize)
    # RHS
    stack.append(__main__strcmp__block__23__bsize)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs != __rhs
    stack.append (__res)
    __if__24__cond = stack.pop ()
    # get condition from stack
    if (__if__24__cond):
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
    __main__strcmp__block__23__for__25__i = 0
    __rhs = stack.pop()
    __main__strcmp__block__23__for__25__i = __rhs
    stack.append (__main__strcmp__block__23__for__25__i)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        stack.append(__main__strcmp__block__23__for__25__i)
        # RHS
        stack.append(__main__strcmp__block__23__asize)
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
        stack.append(__main__strcmp__block__23__for__25__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        # Subscript
        # LHS
        stack.append(__main__strcmp__b)
        # OFFSET
        stack.append(__main__strcmp__block__23__for__25__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs != __rhs
        stack.append (__res)
        __if__27__cond = stack.pop ()
        # get condition from stack
        if (__if__27__cond):
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
        stack.append(__main__strcmp__block__23__for__25__i)
        __rhs = stack.pop ()
        __main__strcmp__block__23__for__25__i = __main__strcmp__block__23__for__25__i + 1
        __res = __main__strcmp__block__23__for__25__i
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
    __main__first_index_of__block__29__size = 0
    __rhs = stack.pop()
    __main__first_index_of__block__29__size = __rhs
    stack.append (__main__first_index_of__block__29__size)
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
    __main__first_index_of__block__29__for__30__i = 0
    __rhs = stack.pop()
    __main__first_index_of__block__29__for__30__i = __rhs
    stack.append (__main__first_index_of__block__29__for__30__i)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        stack.append(__main__first_index_of__block__29__for__30__i)
        # RHS
        stack.append(__main__first_index_of__block__29__size)
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
        stack.append(__main__first_index_of__block__29__for__30__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        stack.append(__main__first_index_of__c)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs == __rhs
        stack.append (__res)
        __if__32__cond = stack.pop ()
        # get condition from stack
        if (__if__32__cond):
            # Body
            # Return
            stack.append(__main__first_index_of__block__29__for__30__i)
            __rVal = stack.pop ()
            return __rVal
        # End of if
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # Update
        # Pre-Increment
        # RHS
        stack.append(__main__first_index_of__block__29__for__30__i)
        __rhs = stack.pop ()
        __main__first_index_of__block__29__for__30__i = __main__first_index_of__block__29__for__30__i + 1
        __res = __main__first_index_of__block__29__for__30__i
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
    __main__split__block__33__tokens = 0
    __rhs = stack.pop()
    __main__split__block__33__tokens = __rhs
    stack.append (__main__split__block__33__tokens)
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
    __main__split__block__33__size = 0
    __rhs = stack.pop()
    __main__split__block__33__size = __rhs
    stack.append (__main__split__block__33__size)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(0)
    # LHS
    __main__split__block__33__i = 0
    __rhs = stack.pop()
    __main__split__block__33__i = __rhs
    stack.append (__main__split__block__33__i)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(0)
    # LHS
    __main__split__block__33__j = 0
    __rhs = stack.pop()
    __main__split__block__33__j = __rhs
    stack.append (__main__split__block__33__j)
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
        stack.append(__main__split__block__33__i)
        # RHS
        stack.append(__main__split__block__33__size)
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
        stack.append(__main__split__block__33__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        stack.append(__main__split__delim)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs != __rhs
        stack.append (__res)
        __if__36__cond = stack.pop ()
        # get condition from stack
        if (__if__36__cond):
            # Body
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Assignment - '='
            # RHS
            # Int Literal
            stack.append(0)
            # LHS
            __main__split__block__33__while__34__block__35__if__36__block__37__count = 0
            __rhs = stack.pop()
            __main__split__block__33__while__34__block__35__if__36__block__37__count = __rhs
            stack.append (__main__split__block__33__while__34__block__35__if__36__block__37__count)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            # Statement
            # Assignment - '='
            # RHS
            stack.append(__main__split__block__33__i)
            # LHS
            __main__split__block__33__while__34__block__35__if__36__block__37__k = 0
            __rhs = stack.pop()
            __main__split__block__33__while__34__block__35__if__36__block__37__k = __rhs
            stack.append (__main__split__block__33__while__34__block__35__if__36__block__37__k)
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
                stack.append(__main__split__block__33__while__34__block__35__if__36__block__37__k)
                # RHS
                stack.append(__main__split__block__33__size)
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
                __res = __main__split__block__33__while__34__block__35__if__36__block__37__k
                __main__split__block__33__while__34__block__35__if__36__block__37__k = __main__split__block__33__while__34__block__35__if__36__block__37__k + 1
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
                __if__39__cond = stack.pop ()
                # get condition from stack
                if (__if__39__cond):
                    # Body
                    # Statement
                    # Pre-Increment
                    # RHS
                    stack.append(__main__split__block__33__while__34__block__35__if__36__block__37__count)
                    __rhs = stack.pop ()
                    __main__split__block__33__while__34__block__35__if__36__block__37__count = __main__split__block__33__while__34__block__35__if__36__block__37__count + 1
                    __res = __main__split__block__33__while__34__block__35__if__36__block__37__count
                    stack.append (__res)
                    # Statement results can be ignored
                    stack.pop ()
                    # End Statement

                #---------------------------------------------------------
                # Else-Statement
                else:
                    # Break out of __while__38
                    break
                #---------------------------------------------------------
                # End of if
                #---------------------------------------------------------
            # End of While
            #-------------------------------------------------------------
            # Statement
            # Method Call - Vector<:char[]:>::pushBack(char[]) -> void
            # LHS
            stack.append(__main__split__block__33__tokens)
            # RHS
            # Arguments
            # Addition
            # LHS
            stack.append(__main__split__block__33__while__34__block__35__if__36__block__37__count)
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
            __main__split__block__33__while__34__block__35__if__36__block__37__for__40__k = 0
            __rhs = stack.pop()
            __main__split__block__33__while__34__block__35__if__36__block__37__for__40__k = __rhs
            stack.append (__main__split__block__33__while__34__block__35__if__36__block__37__for__40__k)
            # Using an infinite loop so we can write a separate multi-line condition
            while (1):
                # Condition
                # Less Than
                # LHS
                stack.append(__main__split__block__33__while__34__block__35__if__36__block__37__for__40__k)
                # RHS
                stack.append(__main__split__block__33__while__34__block__35__if__36__block__37__count)
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
                __res = __main__split__block__33__i
                __main__split__block__33__i = __main__split__block__33__i + 1
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
                stack.append(__main__split__block__33__tokens)
                # RHS
                stack.append (__field____main____Vector__char__1____data)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                # OFFSET
                stack.append(__main__split__block__33__j)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # OFFSET
                stack.append(__main__split__block__33__while__34__block__35__if__36__block__37__for__40__k)
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
                stack.append(__main__split__block__33__while__34__block__35__if__36__block__37__for__40__k)
                __rhs = stack.pop ()
                __main__split__block__33__while__34__block__35__if__36__block__37__for__40__k = __main__split__block__33__while__34__block__35__if__36__block__37__for__40__k + 1
                __res = __main__split__block__33__while__34__block__35__if__36__block__37__for__40__k
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
            stack.append(__main__split__block__33__tokens)
            # RHS
            stack.append (__field____main____Vector__char__1____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main__split__block__33__j)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # OFFSET
            stack.append(__main__split__block__33__while__34__block__35__if__36__block__37__count)
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
            stack.append(__main__split__block__33__j)
            __rhs = stack.pop ()
            __main__split__block__33__j = __main__split__block__33__j + 1
            __res = __main__split__block__33__j
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
        stack.append(__main__split__block__33__i)
        __rhs = stack.pop ()
        __main__split__block__33__i = __main__split__block__33__i + 1
        __res = __main__split__block__33__i
        stack.append (__res)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
    # End of While
    #---------------------------------------------------------------------
    # Return
    stack.append(__main__split__block__33__tokens)
    __rVal = stack.pop ()
    return __rVal
    #---------------------------------------------------------------------
# End Function Declaration - __main____split__char__1__char
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
    __if__45__cond = stack.pop ()
    # get condition from stack
    if (__if__45__cond):
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
    __if__47__cond = stack.pop ()
    # get condition from stack
    if (__if__47__cond):
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
    __if__49__cond = stack.pop ()
    # get condition from stack
    if (__if__49__cond):
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
__main__knot_positions = 0
__rhs = stack.pop()
__main__knot_positions = __rhs
stack.append (__main__knot_positions)
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
__main__for__53__i = 0
__rhs = stack.pop()
__main__for__53__i = __rhs
stack.append (__main__for__53__i)
# Using an infinite loop so we can write a separate multi-line condition
while (1):
    # Condition
    # Less Than
    # LHS
    stack.append(__main__for__53__i)
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
    # Statement
    # Method Call - Vector<:Point:>::pushBack(Point) -> void
    # LHS
    stack.append(__main__knot_positions)
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

    # Update
    # Pre-Increment
    # RHS
    stack.append(__main__for__53__i)
    __rhs = stack.pop ()
    __main__for__53__i = __main__for__53__i + 1
    __res = __main__for__53__i
    stack.append (__res)
#-------------------------------------------------------------------------
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
__main__for__54__i = 0
__rhs = stack.pop()
__main__for__54__i = __rhs
stack.append (__main__for__54__i)
# Using an infinite loop so we can write a separate multi-line condition
while (1):
    # Condition
    # Less Than
    # LHS
    stack.append(__main__for__54__i)
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
    stack.append(__main__for__54__i)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    # LHS
    __main__for__54__block__55__line = 0
    __rhs = stack.pop()
    __main__for__54__block__55__line = __rhs
    stack.append (__main__for__54__block__55__line)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Function Call - split(char[], char) -> Vector<:char[]:>
    # Arguments
    stack.append(__main__for__54__block__55__line)
    # Char Literal
    stack.append(' ')
    __arg1 = stack.pop ()
    __arg0 = stack.pop ()
    # *** split
    __res = __main____split__char__1__char (__arg0, __arg1)
    stack.append (__res) # function call result
    # LHS
    __main__for__54__block__55__tokens = 0
    __rhs = stack.pop()
    __main__for__54__block__55__tokens = __rhs
    stack.append (__main__for__54__block__55__tokens)
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
    stack.append(__main__for__54__block__55__tokens)
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
    __main__for__54__block__55__amt = 0
    __rhs = stack.pop()
    __main__for__54__block__55__amt = __rhs
    stack.append (__main__for__54__block__55__amt)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

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
    stack.append(__main__for__54__i)
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
    stack.append('/')
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
    stack.append(__main__lines)
    # RHS
    stack.append (__field____main____Vector__char__1____size)
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
    # Function Call - println(char[]) -> void
    # Arguments
    # Subscript
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main__for__54__block__55__tokens)
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
    # *** println
    __res = __builtin__println__char__1 (__arg0)
    stack.append (__res) # function call result
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
    __main__for__54__block__55__for__56__j = 0
    __rhs = stack.pop()
    __main__for__54__block__55__for__56__j = __rhs
    stack.append (__main__for__54__block__55__for__56__j)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        stack.append(__main__for__54__block__55__for__56__j)
        # RHS
        stack.append(__main__for__54__block__55__amt)
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
        stack.append(__main__for__54__block__55__tokens)
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
        __if__58__cond = stack.pop ()
        # Condition for elif #0
        # Equal
        # LHS
        # Subscript
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__for__54__block__55__tokens)
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
        __elif__58x0__cond = stack.pop ()
        # Condition for elif #1
        # Equal
        # LHS
        # Subscript
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__for__54__block__55__tokens)
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
        __elif__58x1__cond = stack.pop ()
        # Condition for elif #2
        # Equal
        # LHS
        # Subscript
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__for__54__block__55__tokens)
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
        __elif__58x2__cond = stack.pop ()
        # get condition from stack
        if (__if__58__cond):
            # Body
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Assignment - '+='
            # RHS
            # Int Literal
            stack.append(1)
            # LHS
            # Member Accessor Assignment
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__knot_positions)
            # RHS
            stack.append (__field____main____Vector__Point____data)
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
            stack.append(__field____main____Point____y)
            __child = stack.pop()
            __parent = stack.pop()
            __rhs = stack.pop()
            __parent[__child] = __parent[__child] + __rhs
            stack.append (__parent[__child])
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            #-------------------------------------------------------------
        #-----------------------------------------------------------------
        # Elif-Statement
        # Condition
        elif (__elif__58x0__cond):
            # Body
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Assignment - '+='
            # RHS
            # Int Literal
            stack.append(1)
            # LHS
            # Member Accessor Assignment
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__knot_positions)
            # RHS
            stack.append (__field____main____Vector__Point____data)
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
            stack.append(__field____main____Point____x)
            __child = stack.pop()
            __parent = stack.pop()
            __rhs = stack.pop()
            __parent[__child] = __parent[__child] + __rhs
            stack.append (__parent[__child])
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            #-------------------------------------------------------------
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # Elif-Statement
        # Condition
        elif (__elif__58x1__cond):
            # Body
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Assignment - '-='
            # RHS
            # Int Literal
            stack.append(1)
            # LHS
            # Member Accessor Assignment
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__knot_positions)
            # RHS
            stack.append (__field____main____Vector__Point____data)
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
            stack.append(__field____main____Point____y)
            __child = stack.pop()
            __parent = stack.pop()
            __rhs = stack.pop()
            __parent[__child] = __parent[__child] - __rhs
            stack.append (__parent[__child])
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            #-------------------------------------------------------------
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # Elif-Statement
        # Condition
        elif (__elif__58x2__cond):
            # Body
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Assignment - '-='
            # RHS
            # Int Literal
            stack.append(1)
            # LHS
            # Member Accessor Assignment
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__knot_positions)
            # RHS
            stack.append (__field____main____Vector__Point____data)
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
            stack.append(__field____main____Point____x)
            __child = stack.pop()
            __parent = stack.pop()
            __rhs = stack.pop()
            __parent[__child] = __parent[__child] - __rhs
            stack.append (__parent[__child])
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
        __main__for__54__block__55__for__56__block__57__tail_moved = 0
        __rhs = stack.pop()
        __main__for__54__block__55__for__56__block__57__tail_moved = __rhs
        stack.append (__main__for__54__block__55__for__56__block__57__tail_moved)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
        # For-Loop
        # Init
        # Assignment - '='
        # RHS
        # Int Literal
        stack.append(1)
        # LHS
        __main__for__54__block__55__for__56__block__57__for__63__w = 0
        __rhs = stack.pop()
        __main__for__54__block__55__for__56__block__57__for__63__w = __rhs
        stack.append (__main__for__54__block__55__for__56__block__57__for__63__w)
        # Using an infinite loop so we can write a separate multi-line condition
        while (1):
            # Condition
            # Less Than
            # LHS
            stack.append(__main__for__54__block__55__for__56__block__57__for__63__w)
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
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Assignment - '='
            # RHS
            # Member Accessor
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__knot_positions)
            # RHS
            stack.append (__field____main____Vector__Point____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            # Subtraction
            # LHS
            stack.append(__main__for__54__block__55__for__56__block__57__for__63__w)
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
            stack.append (__field____main____Point____x)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # LHS
            __main__for__54__block__55__for__56__block__57__for__63__block__64__hx = 0
            __rhs = stack.pop()
            __main__for__54__block__55__for__56__block__57__for__63__block__64__hx = __rhs
            stack.append (__main__for__54__block__55__for__56__block__57__for__63__block__64__hx)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            # Statement
            # Assignment - '='
            # RHS
            # Member Accessor
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__knot_positions)
            # RHS
            stack.append (__field____main____Vector__Point____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            # Subtraction
            # LHS
            stack.append(__main__for__54__block__55__for__56__block__57__for__63__w)
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
            stack.append (__field____main____Point____y)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # LHS
            __main__for__54__block__55__for__56__block__57__for__63__block__64__hy = 0
            __rhs = stack.pop()
            __main__for__54__block__55__for__56__block__57__for__63__block__64__hy = __rhs
            stack.append (__main__for__54__block__55__for__56__block__57__for__63__block__64__hy)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            # Statement
            # Assignment - '='
            # RHS
            # Member Accessor
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__knot_positions)
            # RHS
            stack.append (__field____main____Vector__Point____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main__for__54__block__55__for__56__block__57__for__63__w)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            stack.append (__field____main____Point____x)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # LHS
            __main__for__54__block__55__for__56__block__57__for__63__block__64__tx = 0
            __rhs = stack.pop()
            __main__for__54__block__55__for__56__block__57__for__63__block__64__tx = __rhs
            stack.append (__main__for__54__block__55__for__56__block__57__for__63__block__64__tx)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            # Statement
            # Assignment - '='
            # RHS
            # Member Accessor
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__knot_positions)
            # RHS
            stack.append (__field____main____Vector__Point____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main__for__54__block__55__for__56__block__57__for__63__w)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            stack.append (__field____main____Point____y)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # LHS
            __main__for__54__block__55__for__56__block__57__for__63__block__64__ty = 0
            __rhs = stack.pop()
            __main__for__54__block__55__for__56__block__57__for__63__block__64__ty = __rhs
            stack.append (__main__for__54__block__55__for__56__block__57__for__63__block__64__ty)
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
            stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__hx)
            # RHS
            stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__tx)
            __rhs = stack.pop()
            __lhs = stack.pop()
            __res = __lhs - __rhs
            stack.append(__res)
            __arg0 = stack.pop ()
            # *** abs
            __res = __main____abs__int (__arg0)
            stack.append (__res) # function call result
            # LHS
            __main__for__54__block__55__for__56__block__57__for__63__block__64__deltax = 0
            __rhs = stack.pop()
            __main__for__54__block__55__for__56__block__57__for__63__block__64__deltax = __rhs
            stack.append (__main__for__54__block__55__for__56__block__57__for__63__block__64__deltax)
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
            stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__hy)
            # RHS
            stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__ty)
            __rhs = stack.pop()
            __lhs = stack.pop()
            __res = __lhs - __rhs
            stack.append(__res)
            __arg0 = stack.pop ()
            # *** abs
            __res = __main____abs__int (__arg0)
            stack.append (__res) # function call result
            # LHS
            __main__for__54__block__55__for__56__block__57__for__63__block__64__deltay = 0
            __rhs = stack.pop()
            __main__for__54__block__55__for__56__block__57__for__63__block__64__deltay = __rhs
            stack.append (__main__for__54__block__55__for__56__block__57__for__63__block__64__deltay)
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
            stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__hx)
            # RHS
            stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__tx)
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs == __rhs
            stack.append (__res)
            # RHS
            # Greater Than or Equal to
            # LHS
            stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__deltay)
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
            __if__65__cond = stack.pop ()
            # Condition for elif #0
            # AND
            # LHS
            # Equal
            # LHS
            stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__hy)
            # RHS
            stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__ty)
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs == __rhs
            stack.append (__res)
            # RHS
            # Greater Than or Equal to
            # LHS
            stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__deltax)
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
            __elif__65x0__cond = stack.pop ()
            # Condition for elif #1
            # AND
            # LHS
            # AND
            # LHS
            # Not Equal
            # LHS
            stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__hx)
            # RHS
            stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__tx)
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs != __rhs
            stack.append (__res)
            # RHS
            # Not Equal
            # LHS
            stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__hy)
            # RHS
            stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__ty)
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
            stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__hx)
            stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__hy)
            stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__tx)
            stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__ty)
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
            __elif__65x1__cond = stack.pop ()
            # get condition from stack
            if (__if__65__cond):
                # Body
                #---------------------------------------------------------
                # Code Block
                # Statement
                # Assignment - '='
                # RHS
                # Greater Than
                # LHS
                stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__hy)
                # RHS
                stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__ty)
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs > __rhs
                stack.append (__res)
                # LHS
                __main__for__54__block__55__for__56__block__57__for__63__block__64__if__65__block__66__isup = 0
                __rhs = stack.pop()
                __main__for__54__block__55__for__56__block__57__for__63__block__64__if__65__block__66__isup = __rhs
                stack.append (__main__for__54__block__55__for__56__block__57__for__63__block__64__if__65__block__66__isup)
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                #---------------------------------------------------------
                # If-Statement
                # Precomputing all if/elif conditions and give unique names
                # bc we can't have code between if and elif
                # Condition
                stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__if__65__block__66__isup)
                __if__67__cond = stack.pop ()
                # get condition from stack
                if (__if__67__cond):
                    # Body
                    #-----------------------------------------------------
                    # Code Block
                    # Statement
                    # Assignment - '+='
                    # RHS
                    # Int Literal
                    stack.append(1)
                    __rhs = stack.pop()
                    __main__for__54__block__55__for__56__block__57__for__63__block__64__ty = __main__for__54__block__55__for__56__block__57__for__63__block__64__ty + __rhs
                    stack.append (__main__for__54__block__55__for__56__block__57__for__63__block__64__ty)
                    # Statement results can be ignored
                    stack.pop ()
                    # End Statement

                    #-----------------------------------------------------
                #---------------------------------------------------------
                # Else-Statement
                else:
                    #-----------------------------------------------------
                    # Code Block
                    # Statement
                    # Assignment - '-='
                    # RHS
                    # Int Literal
                    stack.append(1)
                    __rhs = stack.pop()
                    __main__for__54__block__55__for__56__block__57__for__63__block__64__ty = __main__for__54__block__55__for__56__block__57__for__63__block__64__ty - __rhs
                    stack.append (__main__for__54__block__55__for__56__block__57__for__63__block__64__ty)
                    # Statement results can be ignored
                    stack.pop ()
                    # End Statement

                    #-----------------------------------------------------
                #---------------------------------------------------------
                # End of if
                #---------------------------------------------------------
                # Statement
                # Assignment - '='
                # RHS
                # Int Literal
                stack.append(1)
                __rhs = stack.pop()
                __main__for__54__block__55__for__56__block__57__tail_moved = __rhs
                stack.append (__main__for__54__block__55__for__56__block__57__tail_moved)
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                #---------------------------------------------------------
            #-------------------------------------------------------------
            # Elif-Statement
            # Condition
            elif (__elif__65x0__cond):
                # Body
                #---------------------------------------------------------
                # Code Block
                # Statement
                # Assignment - '='
                # RHS
                # Greater Than
                # LHS
                stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__hx)
                # RHS
                stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__tx)
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs > __rhs
                stack.append (__res)
                # LHS
                __main__for__54__block__55__for__56__block__57__for__63__block__64__elif__65x0__block__70__isright = 0
                __rhs = stack.pop()
                __main__for__54__block__55__for__56__block__57__for__63__block__64__elif__65x0__block__70__isright = __rhs
                stack.append (__main__for__54__block__55__for__56__block__57__for__63__block__64__elif__65x0__block__70__isright)
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                #---------------------------------------------------------
                # If-Statement
                # Precomputing all if/elif conditions and give unique names
                # bc we can't have code between if and elif
                # Condition
                stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__elif__65x0__block__70__isright)
                __if__71__cond = stack.pop ()
                # get condition from stack
                if (__if__71__cond):
                    # Body
                    #-----------------------------------------------------
                    # Code Block
                    # Statement
                    # Assignment - '+='
                    # RHS
                    # Int Literal
                    stack.append(1)
                    __rhs = stack.pop()
                    __main__for__54__block__55__for__56__block__57__for__63__block__64__tx = __main__for__54__block__55__for__56__block__57__for__63__block__64__tx + __rhs
                    stack.append (__main__for__54__block__55__for__56__block__57__for__63__block__64__tx)
                    # Statement results can be ignored
                    stack.pop ()
                    # End Statement

                    #-----------------------------------------------------
                #---------------------------------------------------------
                # Else-Statement
                else:
                    #-----------------------------------------------------
                    # Code Block
                    # Statement
                    # Assignment - '-='
                    # RHS
                    # Int Literal
                    stack.append(1)
                    __rhs = stack.pop()
                    __main__for__54__block__55__for__56__block__57__for__63__block__64__tx = __main__for__54__block__55__for__56__block__57__for__63__block__64__tx - __rhs
                    stack.append (__main__for__54__block__55__for__56__block__57__for__63__block__64__tx)
                    # Statement results can be ignored
                    stack.pop ()
                    # End Statement

                    #-----------------------------------------------------
                #---------------------------------------------------------
                # End of if
                #---------------------------------------------------------
                # Statement
                # Assignment - '='
                # RHS
                # Int Literal
                stack.append(1)
                __rhs = stack.pop()
                __main__for__54__block__55__for__56__block__57__tail_moved = __rhs
                stack.append (__main__for__54__block__55__for__56__block__57__tail_moved)
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                #---------------------------------------------------------
            #-------------------------------------------------------------
            #-------------------------------------------------------------
            # Elif-Statement
            # Condition
            elif (__elif__65x1__cond):
                # Body
                #---------------------------------------------------------
                # Code Block
                # Statement
                # Assignment - '='
                # RHS
                # Greater Than
                # LHS
                stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__hy)
                # RHS
                stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__ty)
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs > __rhs
                stack.append (__res)
                # LHS
                __main__for__54__block__55__for__56__block__57__for__63__block__64__elif__65x1__block__74__isup = 0
                __rhs = stack.pop()
                __main__for__54__block__55__for__56__block__57__for__63__block__64__elif__65x1__block__74__isup = __rhs
                stack.append (__main__for__54__block__55__for__56__block__57__for__63__block__64__elif__65x1__block__74__isup)
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Statement
                # Assignment - '='
                # RHS
                # Greater Than
                # LHS
                stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__hx)
                # RHS
                stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__tx)
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs > __rhs
                stack.append (__res)
                # LHS
                __main__for__54__block__55__for__56__block__57__for__63__block__64__elif__65x1__block__74__isright = 0
                __rhs = stack.pop()
                __main__for__54__block__55__for__56__block__57__for__63__block__64__elif__65x1__block__74__isright = __rhs
                stack.append (__main__for__54__block__55__for__56__block__57__for__63__block__64__elif__65x1__block__74__isright)
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
                stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__elif__65x1__block__74__isup)
                # RHS
                stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__elif__65x1__block__74__isright)
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs and __rhs
                stack.append (__res)
                __if__75__cond = stack.pop ()
                # Condition for elif #0
                # AND
                # LHS
                # Negate
                # RHS
                stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__elif__65x1__block__74__isup)
                __rhs = stack.pop ()
                __res = not __rhs
                stack.append (__res)
                # RHS
                stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__elif__65x1__block__74__isright)
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs and __rhs
                stack.append (__res)
                __elif__75x0__cond = stack.pop ()
                # Condition for elif #1
                # AND
                # LHS
                # Negate
                # RHS
                stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__elif__65x1__block__74__isup)
                __rhs = stack.pop ()
                __res = not __rhs
                stack.append (__res)
                # RHS
                # Negate
                # RHS
                stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__elif__65x1__block__74__isright)
                __rhs = stack.pop ()
                __res = not __rhs
                stack.append (__res)
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs and __rhs
                stack.append (__res)
                __elif__75x1__cond = stack.pop ()
                # Condition for elif #2
                # AND
                # LHS
                stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__elif__65x1__block__74__isup)
                # RHS
                # Negate
                # RHS
                stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__elif__65x1__block__74__isright)
                __rhs = stack.pop ()
                __res = not __rhs
                stack.append (__res)
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs and __rhs
                stack.append (__res)
                __elif__75x2__cond = stack.pop ()
                # get condition from stack
                if (__if__75__cond):
                    # Body
                    #-----------------------------------------------------
                    # Code Block
                    # Statement
                    # Pre-Increment
                    # RHS
                    stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__ty)
                    __rhs = stack.pop ()
                    __main__for__54__block__55__for__56__block__57__for__63__block__64__ty = __main__for__54__block__55__for__56__block__57__for__63__block__64__ty + 1
                    __res = __main__for__54__block__55__for__56__block__57__for__63__block__64__ty
                    stack.append (__res)
                    # Statement results can be ignored
                    stack.pop ()
                    # End Statement

                    # Statement
                    # Pre-Increment
                    # RHS
                    stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__tx)
                    __rhs = stack.pop ()
                    __main__for__54__block__55__for__56__block__57__for__63__block__64__tx = __main__for__54__block__55__for__56__block__57__for__63__block__64__tx + 1
                    __res = __main__for__54__block__55__for__56__block__57__for__63__block__64__tx
                    stack.append (__res)
                    # Statement results can be ignored
                    stack.pop ()
                    # End Statement

                    #-----------------------------------------------------
                #---------------------------------------------------------
                # Elif-Statement
                # Condition
                elif (__elif__75x0__cond):
                    # Body
                    #-----------------------------------------------------
                    # Code Block
                    # Statement
                    # Pre-Decrement
                    # RHS
                    stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__ty)
                    __rhs = stack.pop ()
                    __main__for__54__block__55__for__56__block__57__for__63__block__64__ty = __main__for__54__block__55__for__56__block__57__for__63__block__64__ty - 1
                    __res = __main__for__54__block__55__for__56__block__57__for__63__block__64__ty
                    stack.append (__res)
                    # Statement results can be ignored
                    stack.pop ()
                    # End Statement

                    # Statement
                    # Pre-Increment
                    # RHS
                    stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__tx)
                    __rhs = stack.pop ()
                    __main__for__54__block__55__for__56__block__57__for__63__block__64__tx = __main__for__54__block__55__for__56__block__57__for__63__block__64__tx + 1
                    __res = __main__for__54__block__55__for__56__block__57__for__63__block__64__tx
                    stack.append (__res)
                    # Statement results can be ignored
                    stack.pop ()
                    # End Statement

                    #-----------------------------------------------------
                #---------------------------------------------------------
                #---------------------------------------------------------
                # Elif-Statement
                # Condition
                elif (__elif__75x1__cond):
                    # Body
                    #-----------------------------------------------------
                    # Code Block
                    # Statement
                    # Pre-Decrement
                    # RHS
                    stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__ty)
                    __rhs = stack.pop ()
                    __main__for__54__block__55__for__56__block__57__for__63__block__64__ty = __main__for__54__block__55__for__56__block__57__for__63__block__64__ty - 1
                    __res = __main__for__54__block__55__for__56__block__57__for__63__block__64__ty
                    stack.append (__res)
                    # Statement results can be ignored
                    stack.pop ()
                    # End Statement

                    # Statement
                    # Pre-Decrement
                    # RHS
                    stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__tx)
                    __rhs = stack.pop ()
                    __main__for__54__block__55__for__56__block__57__for__63__block__64__tx = __main__for__54__block__55__for__56__block__57__for__63__block__64__tx - 1
                    __res = __main__for__54__block__55__for__56__block__57__for__63__block__64__tx
                    stack.append (__res)
                    # Statement results can be ignored
                    stack.pop ()
                    # End Statement

                    #-----------------------------------------------------
                #---------------------------------------------------------
                #---------------------------------------------------------
                # Elif-Statement
                # Condition
                elif (__elif__75x2__cond):
                    # Body
                    #-----------------------------------------------------
                    # Code Block
                    # Statement
                    # Pre-Increment
                    # RHS
                    stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__ty)
                    __rhs = stack.pop ()
                    __main__for__54__block__55__for__56__block__57__for__63__block__64__ty = __main__for__54__block__55__for__56__block__57__for__63__block__64__ty + 1
                    __res = __main__for__54__block__55__for__56__block__57__for__63__block__64__ty
                    stack.append (__res)
                    # Statement results can be ignored
                    stack.pop ()
                    # End Statement

                    # Statement
                    # Pre-Decrement
                    # RHS
                    stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__tx)
                    __rhs = stack.pop ()
                    __main__for__54__block__55__for__56__block__57__for__63__block__64__tx = __main__for__54__block__55__for__56__block__57__for__63__block__64__tx - 1
                    __res = __main__for__54__block__55__for__56__block__57__for__63__block__64__tx
                    stack.append (__res)
                    # Statement results can be ignored
                    stack.pop ()
                    # End Statement

                    #-----------------------------------------------------
                #---------------------------------------------------------
                # End of if
                #---------------------------------------------------------
                # Statement
                # Assignment - '='
                # RHS
                # Int Literal
                stack.append(1)
                __rhs = stack.pop()
                __main__for__54__block__55__for__56__block__57__tail_moved = __rhs
                stack.append (__main__for__54__block__55__for__56__block__57__tail_moved)
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
            stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__tx)
            # LHS
            # Member Accessor Assignment
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__knot_positions)
            # RHS
            stack.append (__field____main____Vector__Point____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main__for__54__block__55__for__56__block__57__for__63__w)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
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
            stack.append(__main__for__54__block__55__for__56__block__57__for__63__block__64__ty)
            # LHS
            # Member Accessor Assignment
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__knot_positions)
            # RHS
            stack.append (__field____main____Vector__Point____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main__for__54__block__55__for__56__block__57__for__63__w)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
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

            #-------------------------------------------------------------
            # If-Statement
            # Precomputing all if/elif conditions and give unique names
            # bc we can't have code between if and elif
            # Condition
            # Not Equal
            # LHS
            stack.append(__main__for__54__block__55__for__56__block__57__for__63__w)
            # RHS
            # Int Literal
            stack.append(9)
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs != __rhs
            stack.append (__res)
            __if__80__cond = stack.pop ()
            # get condition from stack
            if (__if__80__cond):
                # Body
                # Statement
                # Assignment - '='
                # RHS
                # Int Literal
                stack.append(0)
                __rhs = stack.pop()
                __main__for__54__block__55__for__56__block__57__tail_moved = __rhs
                stack.append (__main__for__54__block__55__for__56__block__57__tail_moved)
                # Statement results can be ignored
                stack.pop ()
                # End Statement

            # End of if
            #-------------------------------------------------------------
            #-------------------------------------------------------------
            # Update
            # Pre-Increment
            # RHS
            stack.append(__main__for__54__block__55__for__56__block__57__for__63__w)
            __rhs = stack.pop ()
            __main__for__54__block__55__for__56__block__57__for__63__w = __main__for__54__block__55__for__56__block__57__for__63__w + 1
            __res = __main__for__54__block__55__for__56__block__57__for__63__w
            stack.append (__res)
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # If-Statement
        # Precomputing all if/elif conditions and give unique names
        # bc we can't have code between if and elif
        # Condition
        stack.append(__main__for__54__block__55__for__56__block__57__tail_moved)
        __if__81__cond = stack.pop ()
        # get condition from stack
        if (__if__81__cond):
            # Body
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Assignment - '='
            # RHS
            # Int Literal
            stack.append(0)
            # LHS
            __main__for__54__block__55__for__56__block__57__if__81__block__82__exists = 0
            __rhs = stack.pop()
            __main__for__54__block__55__for__56__block__57__if__81__block__82__exists = __rhs
            stack.append (__main__for__54__block__55__for__56__block__57__if__81__block__82__exists)
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
            __main__for__54__block__55__for__56__block__57__if__81__block__82__for__83__k = 0
            __rhs = stack.pop()
            __main__for__54__block__55__for__56__block__57__if__81__block__82__for__83__k = __rhs
            stack.append (__main__for__54__block__55__for__56__block__57__if__81__block__82__for__83__k)
            # Using an infinite loop so we can write a separate multi-line condition
            while (1):
                # Condition
                # Less Than
                # LHS
                stack.append(__main__for__54__block__55__for__56__block__57__if__81__block__82__for__83__k)
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
                stack.append(__main__for__54__block__55__for__56__block__57__if__81__block__82__for__83__k)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # RHS
                stack.append (__field____main____Point____x)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                # RHS
                # Member Accessor
                # LHS
                # Subscript
                # LHS
                # Member Accessor
                # LHS
                stack.append(__main__knot_positions)
                # RHS
                stack.append (__field____main____Vector__Point____data)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                # OFFSET
                # Int Literal
                stack.append(9)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # RHS
                stack.append (__field____main____Point____x)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs == __rhs
                stack.append (__res)
                # RHS
                # Equal
                # LHS
                # Member Accessor
                # LHS
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
                stack.append(__main__for__54__block__55__for__56__block__57__if__81__block__82__for__83__k)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # RHS
                stack.append (__field____main____Point____y)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                # RHS
                # Member Accessor
                # LHS
                # Subscript
                # LHS
                # Member Accessor
                # LHS
                stack.append(__main__knot_positions)
                # RHS
                stack.append (__field____main____Vector__Point____data)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                # OFFSET
                # Int Literal
                stack.append(9)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # RHS
                stack.append (__field____main____Point____y)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs == __rhs
                stack.append (__res)
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs and __rhs
                stack.append (__res)
                __if__85__cond = stack.pop ()
                # get condition from stack
                if (__if__85__cond):
                    # Body
                    #-----------------------------------------------------
                    # Code Block
                    # Statement
                    # Assignment - '='
                    # RHS
                    # Int Literal
                    stack.append(1)
                    __rhs = stack.pop()
                    __main__for__54__block__55__for__56__block__57__if__81__block__82__exists = __rhs
                    stack.append (__main__for__54__block__55__for__56__block__57__if__81__block__82__exists)
                    # Statement results can be ignored
                    stack.pop ()
                    # End Statement

                    # Break out of __for__83
                    break
                    #-----------------------------------------------------
                # End of if
                #---------------------------------------------------------
                #---------------------------------------------------------
                # Update
                # Pre-Increment
                # RHS
                stack.append(__main__for__54__block__55__for__56__block__57__if__81__block__82__for__83__k)
                __rhs = stack.pop ()
                __main__for__54__block__55__for__56__block__57__if__81__block__82__for__83__k = __main__for__54__block__55__for__56__block__57__if__81__block__82__for__83__k + 1
                __res = __main__for__54__block__55__for__56__block__57__if__81__block__82__for__83__k
                stack.append (__res)
            #-------------------------------------------------------------
            #-------------------------------------------------------------
            # If-Statement
            # Precomputing all if/elif conditions and give unique names
            # bc we can't have code between if and elif
            # Condition
            # Negate
            # RHS
            stack.append(__main__for__54__block__55__for__56__block__57__if__81__block__82__exists)
            __rhs = stack.pop ()
            __res = not __rhs
            stack.append (__res)
            __if__87__cond = stack.pop ()
            # get condition from stack
            if (__if__87__cond):
                # Body
                # Statement
                # Method Call - Vector<:Point:>::pushBack(Point) -> void
                # LHS
                stack.append(__main__tail_positions)
                # RHS
                # Arguments
                # Constructor Call - Point::Point(int, int) -> Point
                # Arguments
                # Member Accessor
                # LHS
                # Subscript
                # LHS
                # Member Accessor
                # LHS
                stack.append(__main__knot_positions)
                # RHS
                stack.append (__field____main____Vector__Point____data)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                # OFFSET
                # Int Literal
                stack.append(9)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # RHS
                stack.append (__field____main____Point____x)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                # Member Accessor
                # LHS
                # Subscript
                # LHS
                # Member Accessor
                # LHS
                stack.append(__main__knot_positions)
                # RHS
                stack.append (__field____main____Vector__Point____data)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                # OFFSET
                # Int Literal
                stack.append(9)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # RHS
                stack.append (__field____main____Point____y)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
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
        #-----------------------------------------------------------------
        # Update
        # Pre-Increment
        # RHS
        stack.append(__main__for__54__block__55__for__56__j)
        __rhs = stack.pop ()
        __main__for__54__block__55__for__56__j = __main__for__54__block__55__for__56__j + 1
        __res = __main__for__54__block__55__for__56__j
        stack.append (__res)
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    # Update
    # Pre-Increment
    # RHS
    stack.append(__main__for__54__i)
    __rhs = stack.pop ()
    __main__for__54__i = __main__for__54__i + 1
    __res = __main__for__54__i
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

