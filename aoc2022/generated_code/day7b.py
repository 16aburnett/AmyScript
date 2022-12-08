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
    print (v)

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
# Class Declaration - __main____Vector__File inherits __builtin____main__Object
# Creating Dispatch Table (will be populated later)
__dtable____main____Vector__File = []
#-------------------------------------------------------------------------
# Field - File[] Vector<:File:>::data
__field____main____Vector__File____data = 1
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Field - int Vector<:File:>::size
__field____main____Vector__File____size = 2
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Field - int Vector<:File:>::capacity
__field____main____Vector__File____capacity = 3
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Constructor Declaration - Vector<:File:>::Vector() -> Vector<:File:>
def __ctor____main____Vector__File____Vector ():
    # Creating Class Instance
    this = [0] * 4
    # Add Dispatch Table
    this[0] = __dtable____main____Vector__File
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
    stack.append(__field____main____Vector__File____capacity)
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
    stack.append(__field____main____Vector__File____size)
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
    stack.append (__field____main____Vector__File____capacity)
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
    stack.append(__field____main____Vector__File____data)
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
# End Constructor Declaration - __ctor____main____Vector__File____Vector
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Constructor Declaration - Vector<:File:>::Vector(int) -> Vector<:File:>
def __ctor____main____Vector__File____Vector__int (__main____Vector__File__Vector__size):
    # Creating Class Instance
    this = [0] * 4
    # Add Dispatch Table
    this[0] = __dtable____main____Vector__File
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Assignment - '='
    # RHS
    # Addition
    # LHS
    stack.append(__main____Vector__File__Vector__size)
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
    stack.append(__field____main____Vector__File____capacity)
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
    stack.append(__main____Vector__File__Vector__size)
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append(__field____main____Vector__File____size)
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
    stack.append (__field____main____Vector__File____capacity)
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
    stack.append(__field____main____Vector__File____data)
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
# End Constructor Declaration - __ctor____main____Vector__File____Vector__int
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vector<:File:>::pushBack(File) -> void
def __method____main____Vector__File____pushBack__File (this, __main____Vector__File__pushBack__val):
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
    stack.append (__field____main____Vector__File____size)
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
    stack.append (__field____main____Vector__File____capacity)
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
        stack.append (__field____main____Vector__File____capacity)
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
        stack.append(__field____main____Vector__File____capacity)
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
        stack.append (__field____main____Vector__File____capacity)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        __dim = stack.pop ()
        __res = [None] * __dim
        stack.append (__res)
        # LHS
        __main____Vector__File__pushBack__block__12__if__13__block__14__nData = 0
        __rhs = stack.pop()
        __main____Vector__File__pushBack__block__12__if__13__block__14__nData = __rhs
        stack.append (__main____Vector__File__pushBack__block__12__if__13__block__14__nData)
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
        __main____Vector__File__pushBack__block__12__if__13__block__14__for__15__i = 0
        __rhs = stack.pop()
        __main____Vector__File__pushBack__block__12__if__13__block__14__for__15__i = __rhs
        stack.append (__main____Vector__File__pushBack__block__12__if__13__block__14__for__15__i)
        # Using an infinite loop so we can write a separate multi-line condition
        while (1):
            # Condition
            # Less Than
            # LHS
            stack.append(__main____Vector__File__pushBack__block__12__if__13__block__14__for__15__i)
            # RHS
            # Member Accessor
            # LHS
            stack.append(this)
            # RHS
            stack.append (__field____main____Vector__File____size)
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
            stack.append (__field____main____Vector__File____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main____Vector__File__pushBack__block__12__if__13__block__14__for__15__i)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # LHS
            # Subscript assignment
            # LHS
            stack.append(__main____Vector__File__pushBack__block__12__if__13__block__14__nData)
            # OFFSET
            stack.append(__main____Vector__File__pushBack__block__12__if__13__block__14__for__15__i)
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
            stack.append(__main____Vector__File__pushBack__block__12__if__13__block__14__for__15__i)
            __rhs = stack.pop ()
            __main____Vector__File__pushBack__block__12__if__13__block__14__for__15__i = __main____Vector__File__pushBack__block__12__if__13__block__14__for__15__i + 1
            __res = __main____Vector__File__pushBack__block__12__if__13__block__14__for__15__i
            stack.append (__res)
        #-----------------------------------------------------------------
        # Statement
        # Member Accessor
        # LHS
        stack.append(this)
        # RHS
        stack.append (__field____main____Vector__File____data)
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
        stack.append(__main____Vector__File__pushBack__block__12__if__13__block__14__nData)
        # LHS
        # Member Accessor Assignment
        # LHS
        stack.append(this)
        # RHS
        stack.append(__field____main____Vector__File____data)
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
    stack.append(__main____Vector__File__pushBack__val)
    # LHS
    # Subscript assignment
    # LHS
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__File____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__File____size)
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
    stack.append (__field____main____Vector__File____size)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __rhs = stack.pop ()
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__File____size)
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
# End Method Declaration - __method____main____Vector__File____pushBack__File
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vector<:File:>::popBack() -> File
def __method____main____Vector__File____popBack (this):
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
    stack.append (__field____main____Vector__File____data)
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
    stack.append (__field____main____Vector__File____size)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __rhs = stack.pop ()
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__File____size)
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
# End Method Declaration - __method____main____Vector__File____popBack
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vector<:File:>::get(int) -> File
def __method____main____Vector__File____get__int (this, __main____Vector__File__get__index):
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
    stack.append (__field____main____Vector__File____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    stack.append(__main____Vector__File__get__index)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    __rVal = stack.pop ()
    return __rVal
    #---------------------------------------------------------------------
    return 0
# End Method Declaration - __method____main____Vector__File____get__int
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vector<:File:>::set(int, File) -> void
def __method____main____Vector__File____set__int__File (this, __main____Vector__File__set__index, __main____Vector__File__set__value):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main____Vector__File__set__value)
    # LHS
    # Subscript assignment
    # LHS
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__File____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    stack.append(__main____Vector__File__set__index)
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
# End Method Declaration - __method____main____Vector__File____set__int__File
#-------------------------------------------------------------------------

# Populate Dispatch Table
__dtable____main____Vector__File = [__method____main____Vector__File____pushBack__File, __method____main____Vector__File____popBack, __method____main____Vector__File____get__int, __method____main____Vector__File____set__int__File]
# End Class Declaration - __main____Vector__File
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
# Class Declaration - __main____File inherits __builtin____main__Object
# Creating Dispatch Table (will be populated later)
__dtable____main____File = []
#-------------------------------------------------------------------------
# Field - char[] File::name
__field____main____File____name = 1
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Field - File File::parent
__field____main____File____parent = 2
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Field - Vector<:File:> File::children
__field____main____File____children = 3
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Field - int File::size
__field____main____File____size = 4
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Field - int File::is_dir
__field____main____File____is_dir = 5
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Constructor Declaration - File::File(char[]) -> File
def __ctor____main____File____File__char__1 (__main____File__File__name):
    # Creating Class Instance
    this = [0] * 6
    # Add Dispatch Table
    this[0] = __dtable____main____File
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main____File__File__name)
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append(__field____main____File____name)
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
    # Null Literal
    stack.append (None)
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append(__field____main____File____parent)
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
    # Constructor Call - Vector<:File:>::Vector() -> Vector<:File:>
    # Arguments
    __retval = __ctor____main____Vector__File____Vector ()
    stack.append (__retval)
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append(__field____main____File____children)
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
    stack.append(__field____main____File____size)
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
    stack.append(__field____main____File____is_dir)
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
# End Constructor Declaration - __ctor____main____File____File__char__1
#-------------------------------------------------------------------------

# Populate Dispatch Table
__dtable____main____File = []
# End Class Declaration - __main____File
#=========================================================================

# Statement
# Assignment - '='
# RHS
# Constructor Call - File::File(char[]) -> File
# Arguments
# String Literal
stack.append("/\n")
__arg0 = stack.pop ()
__retval = __ctor____main____File____File__char__1 (__arg0)
stack.append (__retval)
# LHS
__main__root = 0
__rhs = stack.pop()
__main__root = __rhs
stack.append (__main__root)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Assignment - '='
# RHS
# Int Literal
stack.append(1)
# LHS
# Member Accessor Assignment
# LHS
stack.append(__main__root)
# RHS
stack.append(__field____main____File____is_dir)
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
stack.append(__main__root)
# LHS
__main__workingdir = 0
__rhs = stack.pop()
__main__workingdir = __rhs
stack.append (__main__workingdir)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Assignment - '='
# RHS
# Constructor Call - Vector<:File:>::Vector() -> Vector<:File:>
# Arguments
__retval = __ctor____main____Vector__File____Vector ()
stack.append (__retval)
# LHS
__main__all_files = 0
__rhs = stack.pop()
__main__all_files = __rhs
stack.append (__main__all_files)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Method Call - Vector<:File:>::pushBack(File) -> void
# LHS
stack.append(__main__all_files)
# RHS
# Arguments
stack.append(__main__root)
__arg0 = stack.pop ()
__obj = stack.pop ()
__retval = __method____main____Vector__File____pushBack__File (__obj, __arg0)
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
__main__for__45__i = 0
__rhs = stack.pop()
__main__for__45__i = __rhs
stack.append (__main__for__45__i)
# Using an infinite loop so we can write a separate multi-line condition
while (1):
    # Condition
    # Less Than
    # LHS
    stack.append(__main__for__45__i)
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
    stack.append(__main__for__45__i)
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
    __main__for__45__block__46__tokens = 0
    __rhs = stack.pop()
    __main__for__45__block__46__tokens = __rhs
    stack.append (__main__for__45__block__46__tokens)
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
    stack.append(__main__lines)
    # RHS
    stack.append (__field____main____Vector__char__1____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    stack.append(__main__for__45__i)
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
    stack.append('$')
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs == __rhs
    stack.append (__res)
    __if__47__cond = stack.pop ()
    # get condition from stack
    if (__if__47__cond):
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
        stack.append(__main__for__45__block__46__tokens)
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
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        # Char Literal
        stack.append('c')
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs == __rhs
        stack.append (__res)
        __if__49__cond = stack.pop ()
        # Condition for elif #0
        # Equal
        # LHS
        # Subscript
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__for__45__block__46__tokens)
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
        # OFFSET
        # Int Literal
        stack.append(0)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        # Char Literal
        stack.append('l')
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs == __rhs
        stack.append (__res)
        __elif__49x0__cond = stack.pop ()
        # get condition from stack
        if (__if__49__cond):
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
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__for__45__block__46__tokens)
            # RHS
            stack.append (__field____main____Vector__char__1____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            # Int Literal
            stack.append(2)
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
            stack.append('/')
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs == __rhs
            stack.append (__res)
            __if__51__cond = stack.pop ()
            # Condition for elif #0
            # Equal
            # LHS
            # Subscript
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__for__45__block__46__tokens)
            # RHS
            stack.append (__field____main____Vector__char__1____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            # Int Literal
            stack.append(2)
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
            stack.append('.')
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs == __rhs
            stack.append (__res)
            __elif__51x0__cond = stack.pop ()
            # get condition from stack
            if (__if__51__cond):
                # Body
                #---------------------------------------------------------
                # Code Block
                # Statement
                # Assignment - '='
                # RHS
                stack.append(__main__root)
                __rhs = stack.pop()
                __main__workingdir = __rhs
                stack.append (__main__workingdir)
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                #---------------------------------------------------------
            #-------------------------------------------------------------
            # Elif-Statement
            # Condition
            elif (__elif__51x0__cond):
                # Body
                #---------------------------------------------------------
                # Code Block
                # Statement
                # Assignment - '='
                # RHS
                # Member Accessor
                # LHS
                stack.append(__main__workingdir)
                # RHS
                stack.append (__field____main____File____parent)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                __rhs = stack.pop()
                __main__workingdir = __rhs
                stack.append (__main__workingdir)
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                #---------------------------------------------------------
            #-------------------------------------------------------------
            #-------------------------------------------------------------
            # Else-Statement
            else:
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
                __main__for__45__block__46__if__47__block__48__if__49__block__50__else__51__block__54__for__55__j = 0
                __rhs = stack.pop()
                __main__for__45__block__46__if__47__block__48__if__49__block__50__else__51__block__54__for__55__j = __rhs
                stack.append (__main__for__45__block__46__if__47__block__48__if__49__block__50__else__51__block__54__for__55__j)
                # Using an infinite loop so we can write a separate multi-line condition
                while (1):
                    # Condition
                    # Less Than
                    # LHS
                    stack.append(__main__for__45__block__46__if__47__block__48__if__49__block__50__else__51__block__54__for__55__j)
                    # RHS
                    # Member Accessor
                    # LHS
                    # Member Accessor
                    # LHS
                    stack.append(__main__workingdir)
                    # RHS
                    stack.append (__field____main____File____children)
                    __child = stack.pop ()
                    __parent = stack.pop ()
                    stack.append (__parent[__child])
                    # RHS
                    stack.append (__field____main____Vector__File____size)
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
                    #-----------------------------------------------------
                    # Code Block
                    #-----------------------------------------------------
                    # If-Statement
                    # Precomputing all if/elif conditions and give unique names
                    # bc we can't have code between if and elif
                    # Condition
                    # Function Call - strcmp(char[], char[]) -> int
                    # Arguments
                    # Subscript
                    # LHS
                    # Member Accessor
                    # LHS
                    stack.append(__main__for__45__block__46__tokens)
                    # RHS
                    stack.append (__field____main____Vector__char__1____data)
                    __child = stack.pop ()
                    __parent = stack.pop ()
                    stack.append (__parent[__child])
                    # OFFSET
                    # Int Literal
                    stack.append(2)
                    __offset = stack.pop ()
                    __pointer = stack.pop ()
                    stack.append (__pointer[__offset])
                    # Member Accessor
                    # LHS
                    # Subscript
                    # LHS
                    # Member Accessor
                    # LHS
                    # Member Accessor
                    # LHS
                    stack.append(__main__workingdir)
                    # RHS
                    stack.append (__field____main____File____children)
                    __child = stack.pop ()
                    __parent = stack.pop ()
                    stack.append (__parent[__child])
                    # RHS
                    stack.append (__field____main____Vector__File____data)
                    __child = stack.pop ()
                    __parent = stack.pop ()
                    stack.append (__parent[__child])
                    # OFFSET
                    stack.append(__main__for__45__block__46__if__47__block__48__if__49__block__50__else__51__block__54__for__55__j)
                    __offset = stack.pop ()
                    __pointer = stack.pop ()
                    stack.append (__pointer[__offset])
                    # RHS
                    stack.append (__field____main____File____name)
                    __child = stack.pop ()
                    __parent = stack.pop ()
                    stack.append (__parent[__child])
                    __arg1 = stack.pop ()
                    __arg0 = stack.pop ()
                    # *** strcmp
                    __res = __main____strcmp__char__1__char__1 (__arg0, __arg1)
                    stack.append (__res) # function call result
                    __if__57__cond = stack.pop ()
                    # get condition from stack
                    if (__if__57__cond):
                        # Body
                        #-------------------------------------------------
                        # Code Block
                        # Statement
                        # Assignment - '='
                        # RHS
                        # Subscript
                        # LHS
                        # Member Accessor
                        # LHS
                        # Member Accessor
                        # LHS
                        stack.append(__main__workingdir)
                        # RHS
                        stack.append (__field____main____File____children)
                        __child = stack.pop ()
                        __parent = stack.pop ()
                        stack.append (__parent[__child])
                        # RHS
                        stack.append (__field____main____Vector__File____data)
                        __child = stack.pop ()
                        __parent = stack.pop ()
                        stack.append (__parent[__child])
                        # OFFSET
                        stack.append(__main__for__45__block__46__if__47__block__48__if__49__block__50__else__51__block__54__for__55__j)
                        __offset = stack.pop ()
                        __pointer = stack.pop ()
                        stack.append (__pointer[__offset])
                        __rhs = stack.pop()
                        __main__workingdir = __rhs
                        stack.append (__main__workingdir)
                        # Statement results can be ignored
                        stack.pop ()
                        # End Statement

                        # Break out of __for__55
                        break
                        #-------------------------------------------------
                    # End of if
                    #-----------------------------------------------------
                    #-----------------------------------------------------
                    # Update
                    # Pre-Increment
                    # RHS
                    stack.append(__main__for__45__block__46__if__47__block__48__if__49__block__50__else__51__block__54__for__55__j)
                    __rhs = stack.pop ()
                    __main__for__45__block__46__if__47__block__48__if__49__block__50__else__51__block__54__for__55__j = __main__for__45__block__46__if__47__block__48__if__49__block__50__else__51__block__54__for__55__j + 1
                    __res = __main__for__45__block__46__if__47__block__48__if__49__block__50__else__51__block__54__for__55__j
                    stack.append (__res)
                #---------------------------------------------------------
                #---------------------------------------------------------
            #-------------------------------------------------------------
            # End of if
            #-------------------------------------------------------------
            #-------------------------------------------------------------
        #-----------------------------------------------------------------
        # Elif-Statement
        # Condition
        elif (__elif__49x0__cond):
            # Body
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Pre-Increment
            # RHS
            stack.append(__main__for__45__i)
            __rhs = stack.pop ()
            __main__for__45__i = __main__for__45__i + 1
            __res = __main__for__45__i
            stack.append (__res)
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
                stack.append(__main__for__45__i)
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
                #---------------------------------------------------------
                # Code Block
                #---------------------------------------------------------
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
                stack.append(__main__for__45__i)
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
                stack.append('$')
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs == __rhs
                stack.append (__res)
                __if__62__cond = stack.pop ()
                # get condition from stack
                if (__if__62__cond):
                    # Body
                    # Break out of __while__60
                    break
                # End of if
                #---------------------------------------------------------
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
                stack.append(__main__for__45__i)
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
                __main__for__45__block__46__if__47__block__48__elif__49x0__block__59__while__60__block__61__tokens = 0
                __rhs = stack.pop()
                __main__for__45__block__46__if__47__block__48__elif__49x0__block__59__while__60__block__61__tokens = __rhs
                stack.append (__main__for__45__block__46__if__47__block__48__elif__49x0__block__59__while__60__block__61__tokens)
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                #---------------------------------------------------------
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
                stack.append(__main__for__45__block__46__if__47__block__48__elif__49x0__block__59__while__60__block__61__tokens)
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
                stack.append('d')
                __rhs = stack.pop ()
                __lhs = stack.pop ()
                __res = __lhs == __rhs
                stack.append (__res)
                __if__63__cond = stack.pop ()
                # get condition from stack
                if (__if__63__cond):
                    # Body
                    #-----------------------------------------------------
                    # Code Block
                    # Statement
                    # Assignment - '='
                    # RHS
                    # Constructor Call - File::File(char[]) -> File
                    # Arguments
                    # Subscript
                    # LHS
                    # Member Accessor
                    # LHS
                    stack.append(__main__for__45__block__46__if__47__block__48__elif__49x0__block__59__while__60__block__61__tokens)
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
                    __retval = __ctor____main____File____File__char__1 (__arg0)
                    stack.append (__retval)
                    # LHS
                    __main__for__45__block__46__if__47__block__48__elif__49x0__block__59__while__60__block__61__if__63__block__64__dir = 0
                    __rhs = stack.pop()
                    __main__for__45__block__46__if__47__block__48__elif__49x0__block__59__while__60__block__61__if__63__block__64__dir = __rhs
                    stack.append (__main__for__45__block__46__if__47__block__48__elif__49x0__block__59__while__60__block__61__if__63__block__64__dir)
                    # Statement results can be ignored
                    stack.pop ()
                    # End Statement

                    # Statement
                    # Assignment - '='
                    # RHS
                    stack.append(__main__workingdir)
                    # LHS
                    # Member Accessor Assignment
                    # LHS
                    stack.append(__main__for__45__block__46__if__47__block__48__elif__49x0__block__59__while__60__block__61__if__63__block__64__dir)
                    # RHS
                    stack.append(__field____main____File____parent)
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
                    stack.append(1)
                    # LHS
                    # Member Accessor Assignment
                    # LHS
                    stack.append(__main__for__45__block__46__if__47__block__48__elif__49x0__block__59__while__60__block__61__if__63__block__64__dir)
                    # RHS
                    stack.append(__field____main____File____is_dir)
                    __child = stack.pop()
                    __parent = stack.pop()
                    __rhs = stack.pop()
                    __parent[__child] = __rhs
                    stack.append (__parent[__child])
                    # Statement results can be ignored
                    stack.pop ()
                    # End Statement

                    # Statement
                    # Method Call - Vector<:File:>::pushBack(File) -> void
                    # LHS
                    # Member Accessor
                    # LHS
                    stack.append(__main__workingdir)
                    # RHS
                    stack.append (__field____main____File____children)
                    __child = stack.pop ()
                    __parent = stack.pop ()
                    stack.append (__parent[__child])
                    # RHS
                    # Arguments
                    stack.append(__main__for__45__block__46__if__47__block__48__elif__49x0__block__59__while__60__block__61__if__63__block__64__dir)
                    __arg0 = stack.pop ()
                    __obj = stack.pop ()
                    __retval = __method____main____Vector__File____pushBack__File (__obj, __arg0)
                    stack.append (__retval)
                    # Statement results can be ignored
                    stack.pop ()
                    # End Statement

                    # Statement
                    # Method Call - Vector<:File:>::pushBack(File) -> void
                    # LHS
                    stack.append(__main__all_files)
                    # RHS
                    # Arguments
                    stack.append(__main__for__45__block__46__if__47__block__48__elif__49x0__block__59__while__60__block__61__if__63__block__64__dir)
                    __arg0 = stack.pop ()
                    __obj = stack.pop ()
                    __retval = __method____main____Vector__File____pushBack__File (__obj, __arg0)
                    stack.append (__retval)
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
                    # Assignment - '='
                    # RHS
                    # Function Call - stringToInt(char[]) -> int
                    # Arguments
                    # Subscript
                    # LHS
                    # Member Accessor
                    # LHS
                    stack.append(__main__for__45__block__46__if__47__block__48__elif__49x0__block__59__while__60__block__61__tokens)
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
                    # *** stringToInt
                    __res = __builtin__stringToInt__char__1 (__arg0)
                    stack.append (__res) # function call result
                    # LHS
                    __main__for__45__block__46__if__47__block__48__elif__49x0__block__59__while__60__block__61__else__63__block__65__size = 0
                    __rhs = stack.pop()
                    __main__for__45__block__46__if__47__block__48__elif__49x0__block__59__while__60__block__61__else__63__block__65__size = __rhs
                    stack.append (__main__for__45__block__46__if__47__block__48__elif__49x0__block__59__while__60__block__61__else__63__block__65__size)
                    # Statement results can be ignored
                    stack.pop ()
                    # End Statement

                    # Statement
                    # Assignment - '='
                    # RHS
                    # Constructor Call - File::File(char[]) -> File
                    # Arguments
                    # Subscript
                    # LHS
                    # Member Accessor
                    # LHS
                    stack.append(__main__for__45__block__46__if__47__block__48__elif__49x0__block__59__while__60__block__61__tokens)
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
                    __retval = __ctor____main____File____File__char__1 (__arg0)
                    stack.append (__retval)
                    # LHS
                    __main__for__45__block__46__if__47__block__48__elif__49x0__block__59__while__60__block__61__else__63__block__65__f = 0
                    __rhs = stack.pop()
                    __main__for__45__block__46__if__47__block__48__elif__49x0__block__59__while__60__block__61__else__63__block__65__f = __rhs
                    stack.append (__main__for__45__block__46__if__47__block__48__elif__49x0__block__59__while__60__block__61__else__63__block__65__f)
                    # Statement results can be ignored
                    stack.pop ()
                    # End Statement

                    # Statement
                    # Assignment - '='
                    # RHS
                    stack.append(__main__for__45__block__46__if__47__block__48__elif__49x0__block__59__while__60__block__61__else__63__block__65__size)
                    # LHS
                    # Member Accessor Assignment
                    # LHS
                    stack.append(__main__for__45__block__46__if__47__block__48__elif__49x0__block__59__while__60__block__61__else__63__block__65__f)
                    # RHS
                    stack.append(__field____main____File____size)
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
                    stack.append(__main__workingdir)
                    # LHS
                    # Member Accessor Assignment
                    # LHS
                    stack.append(__main__for__45__block__46__if__47__block__48__elif__49x0__block__59__while__60__block__61__else__63__block__65__f)
                    # RHS
                    stack.append(__field____main____File____parent)
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
                    stack.append(__main__for__45__block__46__if__47__block__48__elif__49x0__block__59__while__60__block__61__else__63__block__65__f)
                    # RHS
                    stack.append(__field____main____File____is_dir)
                    __child = stack.pop()
                    __parent = stack.pop()
                    __rhs = stack.pop()
                    __parent[__child] = __rhs
                    stack.append (__parent[__child])
                    # Statement results can be ignored
                    stack.pop ()
                    # End Statement

                    # Statement
                    # Method Call - Vector<:File:>::pushBack(File) -> void
                    # LHS
                    # Member Accessor
                    # LHS
                    stack.append(__main__workingdir)
                    # RHS
                    stack.append (__field____main____File____children)
                    __child = stack.pop ()
                    __parent = stack.pop ()
                    stack.append (__parent[__child])
                    # RHS
                    # Arguments
                    stack.append(__main__for__45__block__46__if__47__block__48__elif__49x0__block__59__while__60__block__61__else__63__block__65__f)
                    __arg0 = stack.pop ()
                    __obj = stack.pop ()
                    __retval = __method____main____Vector__File____pushBack__File (__obj, __arg0)
                    stack.append (__retval)
                    # Statement results can be ignored
                    stack.pop ()
                    # End Statement

                    # Statement
                    # Method Call - Vector<:File:>::pushBack(File) -> void
                    # LHS
                    stack.append(__main__all_files)
                    # RHS
                    # Arguments
                    stack.append(__main__for__45__block__46__if__47__block__48__elif__49x0__block__59__while__60__block__61__else__63__block__65__f)
                    __arg0 = stack.pop ()
                    __obj = stack.pop ()
                    __retval = __method____main____Vector__File____pushBack__File (__obj, __arg0)
                    stack.append (__retval)
                    # Statement results can be ignored
                    stack.pop ()
                    # End Statement

                    #-----------------------------------------------------
                #---------------------------------------------------------
                # End of if
                #---------------------------------------------------------
                # Statement
                # Pre-Increment
                # RHS
                stack.append(__main__for__45__i)
                __rhs = stack.pop ()
                __main__for__45__i = __main__for__45__i + 1
                __res = __main__for__45__i
                stack.append (__res)
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                #---------------------------------------------------------
            # End of While
            #-------------------------------------------------------------
            # Statement
            # Pre-Decrement
            # RHS
            stack.append(__main__for__45__i)
            __rhs = stack.pop ()
            __main__for__45__i = __main__for__45__i - 1
            __res = __main__for__45__i
            stack.append (__res)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            #-------------------------------------------------------------
        #-----------------------------------------------------------------
        # End of if
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
    # End of if
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    # Update
    # Pre-Increment
    # RHS
    stack.append(__main__for__45__i)
    __rhs = stack.pop ()
    __main__for__45__i = __main__for__45__i + 1
    __res = __main__for__45__i
    stack.append (__res)
#-------------------------------------------------------------------------
#=========================================================================
# Function Declaration - printfs(File, int) -> void
def __main____printfs__File__int (__main__printfs__fs, __main__printfs__indent):
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
    stack.append(__main__printfs__fs)
    # RHS
    # Null Literal
    stack.append (None)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs == __rhs
    stack.append (__res)
    __if__67__cond = stack.pop ()
    # get condition from stack
    if (__if__67__cond):
        # Body
        # Return
        return
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
    __main__printfs__block__66__for__68__i = 0
    __rhs = stack.pop()
    __main__printfs__block__66__for__68__i = __rhs
    stack.append (__main__printfs__block__66__for__68__i)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        stack.append(__main__printfs__block__66__for__68__i)
        # RHS
        stack.append(__main__printfs__indent)
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

        #-----------------------------------------------------------------
        # Update
        # Pre-Increment
        # RHS
        stack.append(__main__printfs__block__66__for__68__i)
        __rhs = stack.pop ()
        __main__printfs__block__66__for__68__i = __main__printfs__block__66__for__68__i + 1
        __res = __main__printfs__block__66__for__68__i
        stack.append (__res)
    #---------------------------------------------------------------------
    # Statement
    # Function Call - print(char[]) -> void
    # Arguments
    # Member Accessor
    # LHS
    stack.append(__main__printfs__fs)
    # RHS
    stack.append (__field____main____File____name)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __arg0 = stack.pop ()
    # *** print
    __res = __builtin__print__char__1 (__arg0)
    stack.append (__res) # function call result
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
    # Member Accessor
    # LHS
    stack.append(__main__printfs__fs)
    # RHS
    stack.append (__field____main____File____size)
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
    # Function Call - print(int) -> void
    # Arguments
    # Member Accessor
    # LHS
    stack.append(__main__printfs__fs)
    # RHS
    stack.append (__field____main____File____is_dir)
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

    #---------------------------------------------------------------------
    # For-Loop
    # Init
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(0)
    # LHS
    __main__printfs__block__66__for__70__i = 0
    __rhs = stack.pop()
    __main__printfs__block__66__for__70__i = __rhs
    stack.append (__main__printfs__block__66__for__70__i)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        stack.append(__main__printfs__block__66__for__70__i)
        # RHS
        # Member Accessor
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__printfs__fs)
        # RHS
        stack.append (__field____main____File____children)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # RHS
        stack.append (__field____main____Vector__File____size)
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
        #-----------------------------------------------------------------
        # Code Block
        # Statement
        # Function Call - printfs(File, int) -> void
        # Arguments
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__printfs__fs)
        # RHS
        stack.append (__field____main____File____children)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # RHS
        stack.append (__field____main____Vector__File____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__printfs__block__66__for__70__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # Addition
        # LHS
        stack.append(__main__printfs__indent)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __arg1 = stack.pop ()
        __arg0 = stack.pop ()
        # *** printfs
        __res = __main____printfs__File__int (__arg0, __arg1)
        stack.append (__res) # function call result
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
        # Update
        # Pre-Increment
        # RHS
        stack.append(__main__printfs__block__66__for__70__i)
        __rhs = stack.pop ()
        __main__printfs__block__66__for__70__i = __main__printfs__block__66__for__70__i + 1
        __res = __main__printfs__block__66__for__70__i
        stack.append (__res)
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
# End Function Declaration - __main____printfs__File__int
#=========================================================================

#=========================================================================
# Function Declaration - sum_sizes(File) -> void
def __main____sum_sizes__File (__main__sum_sizes__fs):
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
    stack.append(__main__sum_sizes__fs)
    # RHS
    # Null Literal
    stack.append (None)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs == __rhs
    stack.append (__res)
    __if__73__cond = stack.pop ()
    # get condition from stack
    if (__if__73__cond):
        # Body
        # Return
        return
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
    __main__sum_sizes__block__72__for__74__i = 0
    __rhs = stack.pop()
    __main__sum_sizes__block__72__for__74__i = __rhs
    stack.append (__main__sum_sizes__block__72__for__74__i)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        stack.append(__main__sum_sizes__block__72__for__74__i)
        # RHS
        # Member Accessor
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__sum_sizes__fs)
        # RHS
        stack.append (__field____main____File____children)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # RHS
        stack.append (__field____main____Vector__File____size)
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
        #-----------------------------------------------------------------
        # Code Block
        # Statement
        # Function Call - sum_sizes(File) -> void
        # Arguments
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__sum_sizes__fs)
        # RHS
        stack.append (__field____main____File____children)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # RHS
        stack.append (__field____main____Vector__File____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__sum_sizes__block__72__for__74__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __arg0 = stack.pop ()
        # *** sum_sizes
        __res = __main____sum_sizes__File (__arg0)
        stack.append (__res) # function call result
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '+='
        # RHS
        # Member Accessor
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__sum_sizes__fs)
        # RHS
        stack.append (__field____main____File____children)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # RHS
        stack.append (__field____main____Vector__File____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__sum_sizes__block__72__for__74__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        stack.append (__field____main____File____size)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # LHS
        # Member Accessor Assignment
        # LHS
        stack.append(__main__sum_sizes__fs)
        # RHS
        stack.append(__field____main____File____size)
        __child = stack.pop()
        __parent = stack.pop()
        __rhs = stack.pop()
        __parent[__child] = __parent[__child] + __rhs
        stack.append (__parent[__child])
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
        # Update
        # Pre-Increment
        # RHS
        stack.append(__main__sum_sizes__block__72__for__74__i)
        __rhs = stack.pop ()
        __main__sum_sizes__block__72__for__74__i = __main__sum_sizes__block__72__for__74__i + 1
        __res = __main__sum_sizes__block__72__for__74__i
        stack.append (__res)
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
# End Function Declaration - __main____sum_sizes__File
#=========================================================================

# Statement
# Function Call - sum_sizes(File) -> void
# Arguments
stack.append(__main__root)
__arg0 = stack.pop ()
# *** sum_sizes
__res = __main____sum_sizes__File (__arg0)
stack.append (__res) # function call result
# Statement results can be ignored
stack.pop ()
# End Statement

#=========================================================================
# Function Declaration - sum_small_dirs(File) -> int
def __main____sum_small_dirs__File (__main__sum_small_dirs__fs):
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
    stack.append(__main__sum_small_dirs__fs)
    # RHS
    # Null Literal
    stack.append (None)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs == __rhs
    stack.append (__res)
    __if__77__cond = stack.pop ()
    # get condition from stack
    if (__if__77__cond):
        # Body
        # Return
        # Int Literal
        stack.append(0)
        __rVal = stack.pop ()
        return __rVal
    # End of if
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    # If-Statement
    # Precomputing all if/elif conditions and give unique names
    # bc we can't have code between if and elif
    # Condition
    # Negate
    # RHS
    # Member Accessor
    # LHS
    stack.append(__main__sum_small_dirs__fs)
    # RHS
    stack.append (__field____main____File____is_dir)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __rhs = stack.pop ()
    __res = not __rhs
    stack.append (__res)
    __if__78__cond = stack.pop ()
    # get condition from stack
    if (__if__78__cond):
        # Body
        # Return
        # Int Literal
        stack.append(0)
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
    __main__sum_small_dirs__block__76__sum = 0
    __rhs = stack.pop()
    __main__sum_small_dirs__block__76__sum = __rhs
    stack.append (__main__sum_small_dirs__block__76__sum)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
    # If-Statement
    # Precomputing all if/elif conditions and give unique names
    # bc we can't have code between if and elif
    # Condition
    # Less Than
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main__sum_small_dirs__fs)
    # RHS
    stack.append (__field____main____File____size)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # RHS
    # Int Literal
    stack.append(100000)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs < __rhs
    stack.append (__res)
    __if__79__cond = stack.pop ()
    # get condition from stack
    if (__if__79__cond):
        # Body
        # Statement
        # Assignment - '+='
        # RHS
        # Member Accessor
        # LHS
        stack.append(__main__sum_small_dirs__fs)
        # RHS
        stack.append (__field____main____File____size)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        __rhs = stack.pop()
        __main__sum_small_dirs__block__76__sum = __main__sum_small_dirs__block__76__sum + __rhs
        stack.append (__main__sum_small_dirs__block__76__sum)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

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
    __main__sum_small_dirs__block__76__for__80__i = 0
    __rhs = stack.pop()
    __main__sum_small_dirs__block__76__for__80__i = __rhs
    stack.append (__main__sum_small_dirs__block__76__for__80__i)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        stack.append(__main__sum_small_dirs__block__76__for__80__i)
        # RHS
        # Member Accessor
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__sum_small_dirs__fs)
        # RHS
        stack.append (__field____main____File____children)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # RHS
        stack.append (__field____main____Vector__File____size)
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
        #-----------------------------------------------------------------
        # Code Block
        # Statement
        # Assignment - '+='
        # RHS
        # Function Call - sum_small_dirs(File) -> int
        # Arguments
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__sum_small_dirs__fs)
        # RHS
        stack.append (__field____main____File____children)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # RHS
        stack.append (__field____main____Vector__File____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__sum_small_dirs__block__76__for__80__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __arg0 = stack.pop ()
        # *** sum_small_dirs
        __res = __main____sum_small_dirs__File (__arg0)
        stack.append (__res) # function call result
        __rhs = stack.pop()
        __main__sum_small_dirs__block__76__sum = __main__sum_small_dirs__block__76__sum + __rhs
        stack.append (__main__sum_small_dirs__block__76__sum)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
        # Update
        # Pre-Increment
        # RHS
        stack.append(__main__sum_small_dirs__block__76__for__80__i)
        __rhs = stack.pop ()
        __main__sum_small_dirs__block__76__for__80__i = __main__sum_small_dirs__block__76__for__80__i + 1
        __res = __main__sum_small_dirs__block__76__for__80__i
        stack.append (__res)
    #---------------------------------------------------------------------
    # Return
    stack.append(__main__sum_small_dirs__block__76__sum)
    __rVal = stack.pop ()
    return __rVal
    #---------------------------------------------------------------------
# End Function Declaration - __main____sum_small_dirs__File
#=========================================================================

# Statement
# Assignment - '='
# RHS
# Int Literal
stack.append(70000000)
# LHS
__main__total_space = 0
__rhs = stack.pop()
__main__total_space = __rhs
stack.append (__main__total_space)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Assignment - '='
# RHS
# Int Literal
stack.append(30000000)
# LHS
__main__unused_space_needed = 0
__rhs = stack.pop()
__main__unused_space_needed = __rhs
stack.append (__main__unused_space_needed)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Assignment - '='
# RHS
# Subtraction
# LHS
stack.append(__main__total_space)
# RHS
stack.append(__main__unused_space_needed)
__rhs = stack.pop()
__lhs = stack.pop()
__res = __lhs - __rhs
stack.append(__res)
# LHS
__main__effective_space = 0
__rhs = stack.pop()
__main__effective_space = __rhs
stack.append (__main__effective_space)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Assignment - '='
# RHS
# Subtraction
# LHS
# Member Accessor
# LHS
stack.append(__main__root)
# RHS
stack.append (__field____main____File____size)
__child = stack.pop ()
__parent = stack.pop ()
stack.append (__parent[__child])
# RHS
stack.append(__main__effective_space)
__rhs = stack.pop()
__lhs = stack.pop()
__res = __lhs - __rhs
stack.append(__res)
# LHS
__main__min_space_to_remove = 0
__rhs = stack.pop()
__main__min_space_to_remove = __rhs
stack.append (__main__min_space_to_remove)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Assignment - '='
# RHS
stack.append(__main__total_space)
# LHS
__main__smallest = 0
__rhs = stack.pop()
__main__smallest = __rhs
stack.append (__main__smallest)
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
__main__for__82__i = 0
__rhs = stack.pop()
__main__for__82__i = __rhs
stack.append (__main__for__82__i)
# Using an infinite loop so we can write a separate multi-line condition
while (1):
    # Condition
    # Less Than
    # LHS
    stack.append(__main__for__82__i)
    # RHS
    # Member Accessor
    # LHS
    stack.append(__main__all_files)
    # RHS
    stack.append (__field____main____Vector__File____size)
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
    # If-Statement
    # Precomputing all if/elif conditions and give unique names
    # bc we can't have code between if and elif
    # Condition
    # Member Accessor
    # LHS
    # Subscript
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main__all_files)
    # RHS
    stack.append (__field____main____Vector__File____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    stack.append(__main__for__82__i)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    # RHS
    stack.append (__field____main____File____is_dir)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __if__84__cond = stack.pop ()
    # get condition from stack
    if (__if__84__cond):
        # Body
        #-----------------------------------------------------------------
        # Code Block
        #-----------------------------------------------------------------
        # If-Statement
        # Precomputing all if/elif conditions and give unique names
        # bc we can't have code between if and elif
        # Condition
        # Greater Than or Equal to
        # LHS
        # Member Accessor
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__all_files)
        # RHS
        stack.append (__field____main____Vector__File____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__for__82__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        stack.append (__field____main____File____size)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # RHS
        stack.append(__main__min_space_to_remove)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs >= __rhs
        stack.append (__res)
        __if__86__cond = stack.pop ()
        # get condition from stack
        if (__if__86__cond):
            # Body
            #-------------------------------------------------------------
            # Code Block
            #-------------------------------------------------------------
            # If-Statement
            # Precomputing all if/elif conditions and give unique names
            # bc we can't have code between if and elif
            # Condition
            # Less Than
            # LHS
            # Member Accessor
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__all_files)
            # RHS
            stack.append (__field____main____Vector__File____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main__for__82__i)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            stack.append (__field____main____File____size)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # RHS
            stack.append(__main__smallest)
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs < __rhs
            stack.append (__res)
            __if__88__cond = stack.pop ()
            # get condition from stack
            if (__if__88__cond):
                # Body
                #---------------------------------------------------------
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
                stack.append(__main__all_files)
                # RHS
                stack.append (__field____main____Vector__File____data)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                # OFFSET
                stack.append(__main__for__82__i)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # RHS
                stack.append (__field____main____File____size)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                __rhs = stack.pop()
                __main__smallest = __rhs
                stack.append (__main__smallest)
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                #---------------------------------------------------------
            # End of if
            #-------------------------------------------------------------
            #-------------------------------------------------------------
        # End of if
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
    # End of if
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    # Update
    # Pre-Increment
    # RHS
    stack.append(__main__for__82__i)
    __rhs = stack.pop ()
    __main__for__82__i = __main__for__82__i + 1
    __res = __main__for__82__i
    stack.append (__res)
#-------------------------------------------------------------------------
# Statement
# Function Call - println(int) -> void
# Arguments
stack.append(__main__smallest)
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

