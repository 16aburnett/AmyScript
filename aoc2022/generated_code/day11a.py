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
        __main____Vector__int__pushBack__block__14__if__15__block__16__nData = 0
        __rhs = stack.pop()
        __main____Vector__int__pushBack__block__14__if__15__block__16__nData = __rhs
        stack.append (__main____Vector__int__pushBack__block__14__if__15__block__16__nData)
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
        __main____Vector__int__pushBack__block__14__if__15__block__16__for__17__i = 0
        __rhs = stack.pop()
        __main____Vector__int__pushBack__block__14__if__15__block__16__for__17__i = __rhs
        stack.append (__main____Vector__int__pushBack__block__14__if__15__block__16__for__17__i)
        # Using an infinite loop so we can write a separate multi-line condition
        while (1):
            # Condition
            # Less Than
            # LHS
            stack.append(__main____Vector__int__pushBack__block__14__if__15__block__16__for__17__i)
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
            stack.append(__main____Vector__int__pushBack__block__14__if__15__block__16__for__17__i)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # LHS
            # Subscript assignment
            # LHS
            stack.append(__main____Vector__int__pushBack__block__14__if__15__block__16__nData)
            # OFFSET
            stack.append(__main____Vector__int__pushBack__block__14__if__15__block__16__for__17__i)
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
            stack.append(__main____Vector__int__pushBack__block__14__if__15__block__16__for__17__i)
            __rhs = stack.pop ()
            __main____Vector__int__pushBack__block__14__if__15__block__16__for__17__i = __main____Vector__int__pushBack__block__14__if__15__block__16__for__17__i + 1
            __res = __main____Vector__int__pushBack__block__14__if__15__block__16__for__17__i
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
        stack.append(__main____Vector__int__pushBack__block__14__if__15__block__16__nData)
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
# Method Declaration - Vector<:int:>::clear() -> void
def __method____main____Vector__int____clear (this):
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
        stack.append (__field____main____Vector__int____size)
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
        # Method Call - Vector<:int:>::popBack() -> int
        # LHS
        stack.append(this)
        # RHS
        # Arguments
        __obj = stack.pop ()
        __retval = __method____main____Vector__int____popBack (__obj)
        stack.append (__retval)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

    # End of While
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    return 0
# End Method Declaration - __method____main____Vector__int____clear
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
__dtable____main____Vector__int = [__method____main____Vector__int____pushBack__int, __method____main____Vector__int____popBack, __method____main____Vector__int____clear, __method____main____Vector__int____get__int, __method____main____Vector__int____set__int__int]
# End Class Declaration - __main____Vector__int
#=========================================================================

#=========================================================================
# Class Declaration - __main____Vector__Monkey inherits __builtin____main__Object
# Creating Dispatch Table (will be populated later)
__dtable____main____Vector__Monkey = []
#-------------------------------------------------------------------------
# Field - Monkey[] Vector<:Monkey:>::data
__field____main____Vector__Monkey____data = 1
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Field - int Vector<:Monkey:>::size
__field____main____Vector__Monkey____size = 2
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Field - int Vector<:Monkey:>::capacity
__field____main____Vector__Monkey____capacity = 3
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Constructor Declaration - Vector<:Monkey:>::Vector() -> Vector<:Monkey:>
def __ctor____main____Vector__Monkey____Vector ():
    # Creating Class Instance
    this = [0] * 4
    # Add Dispatch Table
    this[0] = __dtable____main____Vector__Monkey
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
    stack.append(__field____main____Vector__Monkey____capacity)
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
    stack.append(__field____main____Vector__Monkey____size)
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
    stack.append (__field____main____Vector__Monkey____capacity)
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
    stack.append(__field____main____Vector__Monkey____data)
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
# End Constructor Declaration - __ctor____main____Vector__Monkey____Vector
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Constructor Declaration - Vector<:Monkey:>::Vector(int) -> Vector<:Monkey:>
def __ctor____main____Vector__Monkey____Vector__int (__main____Vector__Monkey__Vector__size):
    # Creating Class Instance
    this = [0] * 4
    # Add Dispatch Table
    this[0] = __dtable____main____Vector__Monkey
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Assignment - '='
    # RHS
    # Addition
    # LHS
    stack.append(__main____Vector__Monkey__Vector__size)
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
    stack.append(__field____main____Vector__Monkey____capacity)
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
    stack.append(__main____Vector__Monkey__Vector__size)
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append(__field____main____Vector__Monkey____size)
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
    stack.append (__field____main____Vector__Monkey____capacity)
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
    stack.append(__field____main____Vector__Monkey____data)
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
# End Constructor Declaration - __ctor____main____Vector__Monkey____Vector__int
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vector<:Monkey:>::pushBack(Monkey) -> void
def __method____main____Vector__Monkey____pushBack__Monkey (this, __main____Vector__Monkey__pushBack__val):
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
    stack.append (__field____main____Vector__Monkey____size)
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
    stack.append (__field____main____Vector__Monkey____capacity)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs >= __rhs
    stack.append (__res)
    __if__27__cond = stack.pop ()
    # get condition from stack
    if (__if__27__cond):
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
        stack.append (__field____main____Vector__Monkey____capacity)
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
        stack.append(__field____main____Vector__Monkey____capacity)
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
        stack.append (__field____main____Vector__Monkey____capacity)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        __dim = stack.pop ()
        __res = [None] * __dim
        stack.append (__res)
        # LHS
        __main____Vector__Monkey__pushBack__block__26__if__27__block__28__nData = 0
        __rhs = stack.pop()
        __main____Vector__Monkey__pushBack__block__26__if__27__block__28__nData = __rhs
        stack.append (__main____Vector__Monkey__pushBack__block__26__if__27__block__28__nData)
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
        __main____Vector__Monkey__pushBack__block__26__if__27__block__28__for__29__i = 0
        __rhs = stack.pop()
        __main____Vector__Monkey__pushBack__block__26__if__27__block__28__for__29__i = __rhs
        stack.append (__main____Vector__Monkey__pushBack__block__26__if__27__block__28__for__29__i)
        # Using an infinite loop so we can write a separate multi-line condition
        while (1):
            # Condition
            # Less Than
            # LHS
            stack.append(__main____Vector__Monkey__pushBack__block__26__if__27__block__28__for__29__i)
            # RHS
            # Member Accessor
            # LHS
            stack.append(this)
            # RHS
            stack.append (__field____main____Vector__Monkey____size)
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
            stack.append (__field____main____Vector__Monkey____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main____Vector__Monkey__pushBack__block__26__if__27__block__28__for__29__i)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # LHS
            # Subscript assignment
            # LHS
            stack.append(__main____Vector__Monkey__pushBack__block__26__if__27__block__28__nData)
            # OFFSET
            stack.append(__main____Vector__Monkey__pushBack__block__26__if__27__block__28__for__29__i)
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
            stack.append(__main____Vector__Monkey__pushBack__block__26__if__27__block__28__for__29__i)
            __rhs = stack.pop ()
            __main____Vector__Monkey__pushBack__block__26__if__27__block__28__for__29__i = __main____Vector__Monkey__pushBack__block__26__if__27__block__28__for__29__i + 1
            __res = __main____Vector__Monkey__pushBack__block__26__if__27__block__28__for__29__i
            stack.append (__res)
        #-----------------------------------------------------------------
        # Statement
        # Member Accessor
        # LHS
        stack.append(this)
        # RHS
        stack.append (__field____main____Vector__Monkey____data)
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
        stack.append(__main____Vector__Monkey__pushBack__block__26__if__27__block__28__nData)
        # LHS
        # Member Accessor Assignment
        # LHS
        stack.append(this)
        # RHS
        stack.append(__field____main____Vector__Monkey____data)
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
    stack.append(__main____Vector__Monkey__pushBack__val)
    # LHS
    # Subscript assignment
    # LHS
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__Monkey____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__Monkey____size)
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
    stack.append (__field____main____Vector__Monkey____size)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __rhs = stack.pop ()
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__Monkey____size)
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
# End Method Declaration - __method____main____Vector__Monkey____pushBack__Monkey
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vector<:Monkey:>::popBack() -> Monkey
def __method____main____Vector__Monkey____popBack (this):
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
    stack.append (__field____main____Vector__Monkey____data)
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
    stack.append (__field____main____Vector__Monkey____size)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __rhs = stack.pop ()
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__Monkey____size)
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
# End Method Declaration - __method____main____Vector__Monkey____popBack
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vector<:Monkey:>::clear() -> void
def __method____main____Vector__Monkey____clear (this):
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
        stack.append (__field____main____Vector__Monkey____size)
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
        # Method Call - Vector<:Monkey:>::popBack() -> Monkey
        # LHS
        stack.append(this)
        # RHS
        # Arguments
        __obj = stack.pop ()
        __retval = __method____main____Vector__Monkey____popBack (__obj)
        stack.append (__retval)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

    # End of While
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    return 0
# End Method Declaration - __method____main____Vector__Monkey____clear
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vector<:Monkey:>::get(int) -> Monkey
def __method____main____Vector__Monkey____get__int (this, __main____Vector__Monkey__get__index):
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
    stack.append (__field____main____Vector__Monkey____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    stack.append(__main____Vector__Monkey__get__index)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    __rVal = stack.pop ()
    return __rVal
    #---------------------------------------------------------------------
    return 0
# End Method Declaration - __method____main____Vector__Monkey____get__int
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vector<:Monkey:>::set(int, Monkey) -> void
def __method____main____Vector__Monkey____set__int__Monkey (this, __main____Vector__Monkey__set__index, __main____Vector__Monkey__set__value):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main____Vector__Monkey__set__value)
    # LHS
    # Subscript assignment
    # LHS
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__Monkey____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    stack.append(__main____Vector__Monkey__set__index)
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
# End Method Declaration - __method____main____Vector__Monkey____set__int__Monkey
#-------------------------------------------------------------------------

# Populate Dispatch Table
__dtable____main____Vector__Monkey = [__method____main____Vector__Monkey____pushBack__Monkey, __method____main____Vector__Monkey____popBack, __method____main____Vector__Monkey____clear, __method____main____Vector__Monkey____get__int, __method____main____Vector__Monkey____set__int__Monkey]
# End Class Declaration - __main____Vector__Monkey
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
    # Statement
    # Function Call - print(char) -> void
    # Arguments
    # Char Literal
    stack.append('[')
    __arg0 = stack.pop ()
    # *** print
    __res = __builtin__print__char (__arg0)
    stack.append (__res) # function call result
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
    # Member Accessor
    # LHS
    stack.append(__main__print__v)
    # RHS
    stack.append (__field____main____Vector__int____size)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # RHS
    # Int Literal
    stack.append(0)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs != __rhs
    stack.append (__res)
    __if__37__cond = stack.pop ()
    # get condition from stack
    if (__if__37__cond):
        # Body
        # Statement
        # Function Call - print(int) -> void
        # Arguments
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__print__v)
        # RHS
        stack.append (__field____main____Vector__int____data)
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
        # *** print
        __res = __builtin__print__int (__arg0)
        stack.append (__res) # function call result
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
    stack.append(1)
    # LHS
    __main__print__block__36__for__38__i = 0
    __rhs = stack.pop()
    __main__print__block__36__for__38__i = __rhs
    stack.append (__main__print__block__36__for__38__i)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        stack.append(__main__print__block__36__for__38__i)
        # RHS
        # Member Accessor
        # LHS
        stack.append(__main__print__v)
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
        #-----------------------------------------------------------------
        # Code Block
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
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__print__v)
        # RHS
        stack.append (__field____main____Vector__int____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__print__block__36__for__38__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __arg0 = stack.pop ()
        # *** print
        __res = __builtin__print__int (__arg0)
        stack.append (__res) # function call result
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
        # Update
        # Pre-Increment
        # RHS
        stack.append(__main__print__block__36__for__38__i)
        __rhs = stack.pop ()
        __main__print__block__36__for__38__i = __main__print__block__36__for__38__i + 1
        __res = __main__print__block__36__for__38__i
        stack.append (__res)
    #---------------------------------------------------------------------
    # Statement
    # Function Call - print(char) -> void
    # Arguments
    # Char Literal
    stack.append(']')
    __arg0 = stack.pop ()
    # *** print
    __res = __builtin__print__char (__arg0)
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
# End Function Declaration - __main____print__int____Vector__tparam0__int
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
    # Statement
    # Function Call - print<:int:>(Vector<:int:>) -> void
    # Arguments
    stack.append(__main__println__v)
    __arg0 = stack.pop ()
    # *** print
    __res = __main____print__int____Vector__tparam0__int (__arg0)
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

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
# End Function Declaration - __main____println__int____Vector__tparam0__int
#=========================================================================

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
    __if__42__cond = stack.pop ()
    # get condition from stack
    if (__if__42__cond):
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
    __main__strlen__block__41__size = 0
    __rhs = stack.pop()
    __main__strlen__block__41__size = __rhs
    stack.append (__main__strlen__block__41__size)
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
        __res = __main__strlen__block__41__size
        __main__strlen__block__41__size = __main__strlen__block__41__size + 1
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
    stack.append(__main__strlen__block__41__size)
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
    __main__strcmp__block__44__asize = 0
    __rhs = stack.pop()
    __main__strcmp__block__44__asize = __rhs
    stack.append (__main__strcmp__block__44__asize)
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
    __main__strcmp__block__44__bsize = 0
    __rhs = stack.pop()
    __main__strcmp__block__44__bsize = __rhs
    stack.append (__main__strcmp__block__44__bsize)
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
    stack.append(__main__strcmp__block__44__asize)
    # RHS
    stack.append(__main__strcmp__block__44__bsize)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs != __rhs
    stack.append (__res)
    __if__45__cond = stack.pop ()
    # get condition from stack
    if (__if__45__cond):
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
    __main__strcmp__block__44__for__46__i = 0
    __rhs = stack.pop()
    __main__strcmp__block__44__for__46__i = __rhs
    stack.append (__main__strcmp__block__44__for__46__i)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        stack.append(__main__strcmp__block__44__for__46__i)
        # RHS
        stack.append(__main__strcmp__block__44__asize)
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
        stack.append(__main__strcmp__block__44__for__46__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        # Subscript
        # LHS
        stack.append(__main__strcmp__b)
        # OFFSET
        stack.append(__main__strcmp__block__44__for__46__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs != __rhs
        stack.append (__res)
        __if__48__cond = stack.pop ()
        # get condition from stack
        if (__if__48__cond):
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
        stack.append(__main__strcmp__block__44__for__46__i)
        __rhs = stack.pop ()
        __main__strcmp__block__44__for__46__i = __main__strcmp__block__44__for__46__i + 1
        __res = __main__strcmp__block__44__for__46__i
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
    __main__substr__block__50__res = 0
    __rhs = stack.pop()
    __main__substr__block__50__res = __rhs
    stack.append (__main__substr__block__50__res)
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
    __main__substr__block__50__for__51__i = 0
    __rhs = stack.pop()
    __main__substr__block__50__for__51__i = __rhs
    stack.append (__main__substr__block__50__for__51__i)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        stack.append(__main__substr__block__50__for__51__i)
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
        stack.append(__main__substr__block__50__for__51__i)
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
        stack.append(__main__substr__block__50__res)
        # OFFSET
        stack.append(__main__substr__block__50__for__51__i)
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
        stack.append(__main__substr__block__50__for__51__i)
        __rhs = stack.pop ()
        __main__substr__block__50__for__51__i = __main__substr__block__50__for__51__i + 1
        __res = __main__substr__block__50__for__51__i
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
    stack.append(__main__substr__block__50__res)
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
    stack.append(__main__substr__block__50__res)
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
    __main__first_index_of__block__53__size = 0
    __rhs = stack.pop()
    __main__first_index_of__block__53__size = __rhs
    stack.append (__main__first_index_of__block__53__size)
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
    __main__first_index_of__block__53__for__54__i = 0
    __rhs = stack.pop()
    __main__first_index_of__block__53__for__54__i = __rhs
    stack.append (__main__first_index_of__block__53__for__54__i)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        stack.append(__main__first_index_of__block__53__for__54__i)
        # RHS
        stack.append(__main__first_index_of__block__53__size)
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
        stack.append(__main__first_index_of__block__53__for__54__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        stack.append(__main__first_index_of__c)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs == __rhs
        stack.append (__res)
        __if__56__cond = stack.pop ()
        # get condition from stack
        if (__if__56__cond):
            # Body
            # Return
            stack.append(__main__first_index_of__block__53__for__54__i)
            __rVal = stack.pop ()
            return __rVal
        # End of if
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # Update
        # Pre-Increment
        # RHS
        stack.append(__main__first_index_of__block__53__for__54__i)
        __rhs = stack.pop ()
        __main__first_index_of__block__53__for__54__i = __main__first_index_of__block__53__for__54__i + 1
        __res = __main__first_index_of__block__53__for__54__i
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
    __main__split__block__57__tokens = 0
    __rhs = stack.pop()
    __main__split__block__57__tokens = __rhs
    stack.append (__main__split__block__57__tokens)
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
    __main__split__block__57__size = 0
    __rhs = stack.pop()
    __main__split__block__57__size = __rhs
    stack.append (__main__split__block__57__size)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(0)
    # LHS
    __main__split__block__57__i = 0
    __rhs = stack.pop()
    __main__split__block__57__i = __rhs
    stack.append (__main__split__block__57__i)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(0)
    # LHS
    __main__split__block__57__j = 0
    __rhs = stack.pop()
    __main__split__block__57__j = __rhs
    stack.append (__main__split__block__57__j)
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
        stack.append(__main__split__block__57__i)
        # RHS
        stack.append(__main__split__block__57__size)
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
        stack.append(__main__split__block__57__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        stack.append(__main__split__delim)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs != __rhs
        stack.append (__res)
        __if__60__cond = stack.pop ()
        # get condition from stack
        if (__if__60__cond):
            # Body
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Assignment - '='
            # RHS
            # Int Literal
            stack.append(0)
            # LHS
            __main__split__block__57__while__58__block__59__if__60__block__61__count = 0
            __rhs = stack.pop()
            __main__split__block__57__while__58__block__59__if__60__block__61__count = __rhs
            stack.append (__main__split__block__57__while__58__block__59__if__60__block__61__count)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            # Statement
            # Assignment - '='
            # RHS
            stack.append(__main__split__block__57__i)
            # LHS
            __main__split__block__57__while__58__block__59__if__60__block__61__k = 0
            __rhs = stack.pop()
            __main__split__block__57__while__58__block__59__if__60__block__61__k = __rhs
            stack.append (__main__split__block__57__while__58__block__59__if__60__block__61__k)
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
                stack.append(__main__split__block__57__while__58__block__59__if__60__block__61__k)
                # RHS
                stack.append(__main__split__block__57__size)
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
                __res = __main__split__block__57__while__58__block__59__if__60__block__61__k
                __main__split__block__57__while__58__block__59__if__60__block__61__k = __main__split__block__57__while__58__block__59__if__60__block__61__k + 1
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
                __if__63__cond = stack.pop ()
                # get condition from stack
                if (__if__63__cond):
                    # Body
                    # Statement
                    # Pre-Increment
                    # RHS
                    stack.append(__main__split__block__57__while__58__block__59__if__60__block__61__count)
                    __rhs = stack.pop ()
                    __main__split__block__57__while__58__block__59__if__60__block__61__count = __main__split__block__57__while__58__block__59__if__60__block__61__count + 1
                    __res = __main__split__block__57__while__58__block__59__if__60__block__61__count
                    stack.append (__res)
                    # Statement results can be ignored
                    stack.pop ()
                    # End Statement

                #---------------------------------------------------------
                # Else-Statement
                else:
                    # Break out of __while__62
                    break
                #---------------------------------------------------------
                # End of if
                #---------------------------------------------------------
            # End of While
            #-------------------------------------------------------------
            # Statement
            # Method Call - Vector<:char[]:>::pushBack(char[]) -> void
            # LHS
            stack.append(__main__split__block__57__tokens)
            # RHS
            # Arguments
            # Addition
            # LHS
            stack.append(__main__split__block__57__while__58__block__59__if__60__block__61__count)
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
            __main__split__block__57__while__58__block__59__if__60__block__61__for__64__k = 0
            __rhs = stack.pop()
            __main__split__block__57__while__58__block__59__if__60__block__61__for__64__k = __rhs
            stack.append (__main__split__block__57__while__58__block__59__if__60__block__61__for__64__k)
            # Using an infinite loop so we can write a separate multi-line condition
            while (1):
                # Condition
                # Less Than
                # LHS
                stack.append(__main__split__block__57__while__58__block__59__if__60__block__61__for__64__k)
                # RHS
                stack.append(__main__split__block__57__while__58__block__59__if__60__block__61__count)
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
                __res = __main__split__block__57__i
                __main__split__block__57__i = __main__split__block__57__i + 1
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
                stack.append(__main__split__block__57__tokens)
                # RHS
                stack.append (__field____main____Vector__char__1____data)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                # OFFSET
                stack.append(__main__split__block__57__j)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # OFFSET
                stack.append(__main__split__block__57__while__58__block__59__if__60__block__61__for__64__k)
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
                stack.append(__main__split__block__57__while__58__block__59__if__60__block__61__for__64__k)
                __rhs = stack.pop ()
                __main__split__block__57__while__58__block__59__if__60__block__61__for__64__k = __main__split__block__57__while__58__block__59__if__60__block__61__for__64__k + 1
                __res = __main__split__block__57__while__58__block__59__if__60__block__61__for__64__k
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
            stack.append(__main__split__block__57__tokens)
            # RHS
            stack.append (__field____main____Vector__char__1____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main__split__block__57__j)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # OFFSET
            stack.append(__main__split__block__57__while__58__block__59__if__60__block__61__count)
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
            stack.append(__main__split__block__57__j)
            __rhs = stack.pop ()
            __main__split__block__57__j = __main__split__block__57__j + 1
            __res = __main__split__block__57__j
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
        stack.append(__main__split__block__57__i)
        __rhs = stack.pop ()
        __main__split__block__57__i = __main__split__block__57__i + 1
        __res = __main__split__block__57__i
        stack.append (__res)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
    # End of While
    #---------------------------------------------------------------------
    # Return
    stack.append(__main__split__block__57__tokens)
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
    __if__67__cond = stack.pop ()
    # get condition from stack
    if (__if__67__cond):
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
    __if__69__cond = stack.pop ()
    # get condition from stack
    if (__if__69__cond):
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
    __if__71__cond = stack.pop ()
    # get condition from stack
    if (__if__71__cond):
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
    __if__73__cond = stack.pop ()
    # get condition from stack
    if (__if__73__cond):
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
    __if__75__cond = stack.pop ()
    # get condition from stack
    if (__if__75__cond):
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
    __if__77__cond = stack.pop ()
    # get condition from stack
    if (__if__77__cond):
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
__main__OP_MUL = 0
__rhs = stack.pop()
__main__OP_MUL = __rhs
stack.append (__main__OP_MUL)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Assignment - '='
# RHS
# Int Literal
stack.append(1)
# LHS
__main__OP_ADD = 0
__rhs = stack.pop()
__main__OP_ADD = __rhs
stack.append (__main__OP_ADD)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Assignment - '='
# RHS
# Int Literal
stack.append(2)
# LHS
__main__OP_SQUARE = 0
__rhs = stack.pop()
__main__OP_SQUARE = __rhs
stack.append (__main__OP_SQUARE)
# Statement results can be ignored
stack.pop ()
# End Statement

#=========================================================================
# Class Declaration - __main____Monkey inherits __builtin____main__Object
# Creating Dispatch Table (will be populated later)
__dtable____main____Monkey = []
#-------------------------------------------------------------------------
# Field - Vector<:int:> Monkey::items
__field____main____Monkey____items = 1
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Field - int Monkey::op
__field____main____Monkey____op = 2
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Field - int Monkey::operand
__field____main____Monkey____operand = 3
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Field - int Monkey::divisible_by
__field____main____Monkey____divisible_by = 4
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Field - int Monkey::true_monkey_id
__field____main____Monkey____true_monkey_id = 5
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Field - int Monkey::false_monkey_id
__field____main____Monkey____false_monkey_id = 6
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Field - int Monkey::inspected_items
__field____main____Monkey____inspected_items = 7
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Constructor Declaration - Monkey::Monkey() -> Monkey
def __ctor____main____Monkey____Monkey ():
    # Creating Class Instance
    this = [0] * 8
    # Add Dispatch Table
    this[0] = __dtable____main____Monkey
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Assignment - '='
    # RHS
    # Constructor Call - Vector<:int:>::Vector() -> Vector<:int:>
    # Arguments
    __retval = __ctor____main____Vector__int____Vector ()
    stack.append (__retval)
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append(__field____main____Monkey____items)
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
    stack.append(__field____main____Monkey____op)
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
    stack.append(__field____main____Monkey____operand)
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
    stack.append(__field____main____Monkey____divisible_by)
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
    stack.append(__field____main____Monkey____true_monkey_id)
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
    stack.append(__field____main____Monkey____false_monkey_id)
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
    stack.append(__field____main____Monkey____inspected_items)
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
# End Constructor Declaration - __ctor____main____Monkey____Monkey
#-------------------------------------------------------------------------

# Populate Dispatch Table
__dtable____main____Monkey = []
# End Class Declaration - __main____Monkey
#=========================================================================

# Statement
# Assignment - '='
# RHS
# Constructor Call - Vector<:Monkey:>::Vector() -> Vector<:Monkey:>
# Arguments
__retval = __ctor____main____Vector__Monkey____Vector ()
stack.append (__retval)
# LHS
__main__monkeys = 0
__rhs = stack.pop()
__main__monkeys = __rhs
stack.append (__main__monkeys)
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
__main__for__81__l = 0
__rhs = stack.pop()
__main__for__81__l = __rhs
stack.append (__main__for__81__l)
# Using an infinite loop so we can write a separate multi-line condition
while (1):
    # Condition
    # Less Than
    # LHS
    stack.append(__main__for__81__l)
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
    # Constructor Call - Monkey::Monkey() -> Monkey
    # Arguments
    __retval = __ctor____main____Monkey____Monkey ()
    stack.append (__retval)
    # LHS
    __main__for__81__block__82__monkey = 0
    __rhs = stack.pop()
    __main__for__81__block__82__monkey = __rhs
    stack.append (__main__for__81__block__82__monkey)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Function Call - substr(char[], int, int) -> char[]
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
    # Addition
    # LHS
    stack.append(__main__for__81__l)
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
    # Int Literal
    stack.append(17)
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
    # Addition
    # LHS
    stack.append(__main__for__81__l)
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
    __arg0 = stack.pop ()
    # *** strlen
    __res = __main____strlen__char__1 (__arg0)
    stack.append (__res) # function call result
    __arg2 = stack.pop ()
    __arg1 = stack.pop ()
    __arg0 = stack.pop ()
    # *** substr
    __res = __main____substr__char__1__int__int (__arg0, __arg1, __arg2)
    stack.append (__res) # function call result
    # LHS
    __main__for__81__block__82__items_str = 0
    __rhs = stack.pop()
    __main__for__81__block__82__items_str = __rhs
    stack.append (__main__for__81__block__82__items_str)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Function Call - split(char[], char) -> Vector<:char[]:>
    # Arguments
    stack.append(__main__for__81__block__82__items_str)
    # Char Literal
    stack.append(' ')
    __arg1 = stack.pop ()
    __arg0 = stack.pop ()
    # *** split
    __res = __main____split__char__1__char (__arg0, __arg1)
    stack.append (__res) # function call result
    # LHS
    __main__for__81__block__82__tokens0 = 0
    __rhs = stack.pop()
    __main__for__81__block__82__tokens0 = __rhs
    stack.append (__main__for__81__block__82__tokens0)
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
    __main__for__81__block__82__for__83__i = 0
    __rhs = stack.pop()
    __main__for__81__block__82__for__83__i = __rhs
    stack.append (__main__for__81__block__82__for__83__i)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        stack.append(__main__for__81__block__82__for__83__i)
        # RHS
        # Member Accessor
        # LHS
        stack.append(__main__for__81__block__82__tokens0)
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
        #-----------------------------------------------------------------
        # Code Block
        # Statement
        # Assignment - '='
        # RHS
        # Function Call - substr(char[], int, int) -> char[]
        # Arguments
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__for__81__block__82__tokens0)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__for__81__block__82__for__83__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # Int Literal
        stack.append(0)
        # Subtraction
        # LHS
        # Function Call - strlen(char[]) -> int
        # Arguments
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__for__81__block__82__tokens0)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__for__81__block__82__for__83__i)
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
        __arg2 = stack.pop ()
        __arg1 = stack.pop ()
        __arg0 = stack.pop ()
        # *** substr
        __res = __main____substr__char__1__int__int (__arg0, __arg1, __arg2)
        stack.append (__res) # function call result
        # LHS
        __main__for__81__block__82__for__83__block__84__item_str = 0
        __rhs = stack.pop()
        __main__for__81__block__82__for__83__block__84__item_str = __rhs
        stack.append (__main__for__81__block__82__for__83__block__84__item_str)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Function Call - stringToInt(char[]) -> int
        # Arguments
        stack.append(__main__for__81__block__82__for__83__block__84__item_str)
        __arg0 = stack.pop ()
        # *** stringToInt
        __res = __builtin__stringToInt__char__1 (__arg0)
        stack.append (__res) # function call result
        # LHS
        __main__for__81__block__82__for__83__block__84__item = 0
        __rhs = stack.pop()
        __main__for__81__block__82__for__83__block__84__item = __rhs
        stack.append (__main__for__81__block__82__for__83__block__84__item)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Method Call - Vector<:int:>::pushBack(int) -> void
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__for__81__block__82__monkey)
        # RHS
        stack.append (__field____main____Monkey____items)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # RHS
        # Arguments
        stack.append(__main__for__81__block__82__for__83__block__84__item)
        __arg0 = stack.pop ()
        __obj = stack.pop ()
        __retval = __method____main____Vector__int____pushBack__int (__obj, __arg0)
        stack.append (__retval)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        stack.append(__main__for__81__block__82__for__83__block__84__item_str)
        __arr = stack.pop ()
        __builtin__free (__arr)
        stack.append (0)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
        # Update
        # Pre-Increment
        # RHS
        stack.append(__main__for__81__block__82__for__83__i)
        __rhs = stack.pop ()
        __main__for__81__block__82__for__83__i = __main__for__81__block__82__for__83__i + 1
        __res = __main__for__81__block__82__for__83__i
        stack.append (__res)
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    # For-Loop
    # Init
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(0)
    # LHS
    __main__for__81__block__82__for__85__i = 0
    __rhs = stack.pop()
    __main__for__81__block__82__for__85__i = __rhs
    stack.append (__main__for__81__block__82__for__85__i)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        stack.append(__main__for__81__block__82__for__85__i)
        # RHS
        # Member Accessor
        # LHS
        stack.append(__main__for__81__block__82__tokens0)
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
        # Statement
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__for__81__block__82__tokens0)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__for__81__block__82__for__85__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __arr = stack.pop ()
        __builtin__free (__arr)
        stack.append (0)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Update
        # Pre-Increment
        # RHS
        stack.append(__main__for__81__block__82__for__85__i)
        __rhs = stack.pop ()
        __main__for__81__block__82__for__85__i = __main__for__81__block__82__for__85__i + 1
        __res = __main__for__81__block__82__for__85__i
        stack.append (__res)
    #---------------------------------------------------------------------
    # Statement
    stack.append(__main__for__81__block__82__tokens0)
    __arr = stack.pop ()
    __builtin__free (__arr)
    stack.append (0)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    stack.append(__main__for__81__block__82__items_str)
    __arr = stack.pop ()
    __builtin__free (__arr)
    stack.append (0)
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
    # Function Call - first_index_of(char[], char) -> int
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
    # Addition
    # LHS
    stack.append(__main__for__81__l)
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
    # Char Literal
    stack.append('*')
    __arg1 = stack.pop ()
    __arg0 = stack.pop ()
    # *** first_index_of
    __res = __main____first_index_of__char__1__char (__arg0, __arg1)
    stack.append (__res) # function call result
    # RHS
    # Negative
    # RHS
    # Int Literal
    stack.append(1)
    __rhs = stack.pop ()
    __res = -__rhs
    stack.append (__res)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs != __rhs
    stack.append (__res)
    __if__86__cond = stack.pop ()
    # get condition from stack
    if (__if__86__cond):
        # Body
        #-----------------------------------------------------------------
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
        # Addition
        # LHS
        stack.append(__main__for__81__l)
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
        # Char Literal
        stack.append(' ')
        __arg1 = stack.pop ()
        __arg0 = stack.pop ()
        # *** split
        __res = __main____split__char__1__char (__arg0, __arg1)
        stack.append (__res) # function call result
        # LHS
        __main__for__81__block__82__if__86__block__87__tokens1 = 0
        __rhs = stack.pop()
        __main__for__81__block__82__if__86__block__87__tokens1 = __rhs
        stack.append (__main__for__81__block__82__if__86__block__87__tokens1)
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
        stack.append(__main__for__81__block__82__if__86__block__87__tokens1)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Subtraction
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__for__81__block__82__if__86__block__87__tokens1)
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
        stack.append('o')
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs == __rhs
        stack.append (__res)
        __if__88__cond = stack.pop ()
        # get condition from stack
        if (__if__88__cond):
            # Body
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Assignment - '='
            # RHS
            stack.append(__main__OP_SQUARE)
            # LHS
            # Member Accessor Assignment
            # LHS
            stack.append(__main__for__81__block__82__monkey)
            # RHS
            stack.append(__field____main____Monkey____op)
            __child = stack.pop()
            __parent = stack.pop()
            __rhs = stack.pop()
            __parent[__child] = __rhs
            stack.append (__parent[__child])
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
            # Assignment - '='
            # RHS
            stack.append(__main__OP_MUL)
            # LHS
            # Member Accessor Assignment
            # LHS
            stack.append(__main__for__81__block__82__monkey)
            # RHS
            stack.append(__field____main____Monkey____op)
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
            # Function Call - stringToInt(char[]) -> int
            # Arguments
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__for__81__block__82__if__86__block__87__tokens1)
            # RHS
            stack.append (__field____main____Vector__char__1____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            # Subtraction
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__for__81__block__82__if__86__block__87__tokens1)
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
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            __arg0 = stack.pop ()
            # *** stringToInt
            __res = __builtin__stringToInt__char__1 (__arg0)
            stack.append (__res) # function call result
            # LHS
            # Member Accessor Assignment
            # LHS
            stack.append(__main__for__81__block__82__monkey)
            # RHS
            stack.append(__field____main____Monkey____operand)
            __child = stack.pop()
            __parent = stack.pop()
            __rhs = stack.pop()
            __parent[__child] = __rhs
            stack.append (__parent[__child])
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            #-------------------------------------------------------------
        #-----------------------------------------------------------------
        # End of if
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # For-Loop
        # Init
        # Assignment - '='
        # RHS
        # Int Literal
        stack.append(0)
        # LHS
        __main__for__81__block__82__if__86__block__87__for__91__j = 0
        __rhs = stack.pop()
        __main__for__81__block__82__if__86__block__87__for__91__j = __rhs
        stack.append (__main__for__81__block__82__if__86__block__87__for__91__j)
        # Using an infinite loop so we can write a separate multi-line condition
        while (1):
            # Condition
            # Less Than
            # LHS
            stack.append(__main__for__81__block__82__if__86__block__87__for__91__j)
            # RHS
            # Member Accessor
            # LHS
            stack.append(__main__for__81__block__82__if__86__block__87__tokens1)
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
            # Statement
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__for__81__block__82__if__86__block__87__tokens1)
            # RHS
            stack.append (__field____main____Vector__char__1____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main__for__81__block__82__if__86__block__87__for__91__j)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            __arr = stack.pop ()
            __builtin__free (__arr)
            stack.append (0)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            # Update
            # Pre-Increment
            # RHS
            stack.append(__main__for__81__block__82__if__86__block__87__for__91__j)
            __rhs = stack.pop ()
            __main__for__81__block__82__if__86__block__87__for__91__j = __main__for__81__block__82__if__86__block__87__for__91__j + 1
            __res = __main__for__81__block__82__if__86__block__87__for__91__j
            stack.append (__res)
        #-----------------------------------------------------------------
        # Statement
        stack.append(__main__for__81__block__82__if__86__block__87__tokens1)
        __arr = stack.pop ()
        __builtin__free (__arr)
        stack.append (0)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
    #---------------------------------------------------------------------
    # Else-Statement
    else:
        #-----------------------------------------------------------------
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
        # Addition
        # LHS
        stack.append(__main__for__81__l)
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
        # Char Literal
        stack.append(' ')
        __arg1 = stack.pop ()
        __arg0 = stack.pop ()
        # *** split
        __res = __main____split__char__1__char (__arg0, __arg1)
        stack.append (__res) # function call result
        # LHS
        __main__for__81__block__82__else__86__block__92__tokens1 = 0
        __rhs = stack.pop()
        __main__for__81__block__82__else__86__block__92__tokens1 = __rhs
        stack.append (__main__for__81__block__82__else__86__block__92__tokens1)
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
        stack.append(__main__for__81__block__82__else__86__block__92__tokens1)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Subtraction
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__for__81__block__82__else__86__block__92__tokens1)
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
        stack.append('o')
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs == __rhs
        stack.append (__res)
        __if__93__cond = stack.pop ()
        # get condition from stack
        if (__if__93__cond):
            # Body
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Assignment - '='
            # RHS
            stack.append(__main__OP_SQUARE)
            # LHS
            # Member Accessor Assignment
            # LHS
            stack.append(__main__for__81__block__82__monkey)
            # RHS
            stack.append(__field____main____Monkey____op)
            __child = stack.pop()
            __parent = stack.pop()
            __rhs = stack.pop()
            __parent[__child] = __rhs
            stack.append (__parent[__child])
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
            # Assignment - '='
            # RHS
            stack.append(__main__OP_ADD)
            # LHS
            # Member Accessor Assignment
            # LHS
            stack.append(__main__for__81__block__82__monkey)
            # RHS
            stack.append(__field____main____Monkey____op)
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
            # Function Call - stringToInt(char[]) -> int
            # Arguments
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__for__81__block__82__else__86__block__92__tokens1)
            # RHS
            stack.append (__field____main____Vector__char__1____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            # Subtraction
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__for__81__block__82__else__86__block__92__tokens1)
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
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            __arg0 = stack.pop ()
            # *** stringToInt
            __res = __builtin__stringToInt__char__1 (__arg0)
            stack.append (__res) # function call result
            # LHS
            # Member Accessor Assignment
            # LHS
            stack.append(__main__for__81__block__82__monkey)
            # RHS
            stack.append(__field____main____Monkey____operand)
            __child = stack.pop()
            __parent = stack.pop()
            __rhs = stack.pop()
            __parent[__child] = __rhs
            stack.append (__parent[__child])
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            #-------------------------------------------------------------
        #-----------------------------------------------------------------
        # End of if
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # For-Loop
        # Init
        # Assignment - '='
        # RHS
        # Int Literal
        stack.append(0)
        # LHS
        __main__for__81__block__82__else__86__block__92__for__96__j = 0
        __rhs = stack.pop()
        __main__for__81__block__82__else__86__block__92__for__96__j = __rhs
        stack.append (__main__for__81__block__82__else__86__block__92__for__96__j)
        # Using an infinite loop so we can write a separate multi-line condition
        while (1):
            # Condition
            # Less Than
            # LHS
            stack.append(__main__for__81__block__82__else__86__block__92__for__96__j)
            # RHS
            # Member Accessor
            # LHS
            stack.append(__main__for__81__block__82__else__86__block__92__tokens1)
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
            # Statement
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__for__81__block__82__else__86__block__92__tokens1)
            # RHS
            stack.append (__field____main____Vector__char__1____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main__for__81__block__82__else__86__block__92__for__96__j)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            __arr = stack.pop ()
            __builtin__free (__arr)
            stack.append (0)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            # Update
            # Pre-Increment
            # RHS
            stack.append(__main__for__81__block__82__else__86__block__92__for__96__j)
            __rhs = stack.pop ()
            __main__for__81__block__82__else__86__block__92__for__96__j = __main__for__81__block__82__else__86__block__92__for__96__j + 1
            __res = __main__for__81__block__82__else__86__block__92__for__96__j
            stack.append (__res)
        #-----------------------------------------------------------------
        # Statement
        stack.append(__main__for__81__block__82__else__86__block__92__tokens1)
        __arr = stack.pop ()
        __builtin__free (__arr)
        stack.append (0)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
    #---------------------------------------------------------------------
    # End of if
    #---------------------------------------------------------------------
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
    # Addition
    # LHS
    stack.append(__main__for__81__l)
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
    # Char Literal
    stack.append(' ')
    __arg1 = stack.pop ()
    __arg0 = stack.pop ()
    # *** split
    __res = __main____split__char__1__char (__arg0, __arg1)
    stack.append (__res) # function call result
    # LHS
    __main__for__81__block__82__tokens2 = 0
    __rhs = stack.pop()
    __main__for__81__block__82__tokens2 = __rhs
    stack.append (__main__for__81__block__82__tokens2)
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
    stack.append(__main__for__81__block__82__tokens2)
    # RHS
    stack.append (__field____main____Vector__char__1____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    # Subtraction
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main__for__81__block__82__tokens2)
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
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    __arg0 = stack.pop ()
    # *** stringToInt
    __res = __builtin__stringToInt__char__1 (__arg0)
    stack.append (__res) # function call result
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(__main__for__81__block__82__monkey)
    # RHS
    stack.append(__field____main____Monkey____divisible_by)
    __child = stack.pop()
    __parent = stack.pop()
    __rhs = stack.pop()
    __parent[__child] = __rhs
    stack.append (__parent[__child])
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
    __main__for__81__block__82__for__97__j = 0
    __rhs = stack.pop()
    __main__for__81__block__82__for__97__j = __rhs
    stack.append (__main__for__81__block__82__for__97__j)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        stack.append(__main__for__81__block__82__for__97__j)
        # RHS
        # Member Accessor
        # LHS
        stack.append(__main__for__81__block__82__tokens2)
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
        # Statement
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__for__81__block__82__tokens2)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__for__81__block__82__for__97__j)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __arr = stack.pop ()
        __builtin__free (__arr)
        stack.append (0)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Update
        # Pre-Increment
        # RHS
        stack.append(__main__for__81__block__82__for__97__j)
        __rhs = stack.pop ()
        __main__for__81__block__82__for__97__j = __main__for__81__block__82__for__97__j + 1
        __res = __main__for__81__block__82__for__97__j
        stack.append (__res)
    #---------------------------------------------------------------------
    # Statement
    stack.append(__main__for__81__block__82__tokens2)
    __arr = stack.pop ()
    __builtin__free (__arr)
    stack.append (0)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

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
    # Addition
    # LHS
    stack.append(__main__for__81__l)
    # RHS
    # Int Literal
    stack.append(4)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs + __rhs
    stack.append(__res)
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
    __main__for__81__block__82__tokens3 = 0
    __rhs = stack.pop()
    __main__for__81__block__82__tokens3 = __rhs
    stack.append (__main__for__81__block__82__tokens3)
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
    stack.append(__main__for__81__block__82__tokens3)
    # RHS
    stack.append (__field____main____Vector__char__1____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    # Subtraction
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main__for__81__block__82__tokens3)
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
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    __arg0 = stack.pop ()
    # *** stringToInt
    __res = __builtin__stringToInt__char__1 (__arg0)
    stack.append (__res) # function call result
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(__main__for__81__block__82__monkey)
    # RHS
    stack.append(__field____main____Monkey____true_monkey_id)
    __child = stack.pop()
    __parent = stack.pop()
    __rhs = stack.pop()
    __parent[__child] = __rhs
    stack.append (__parent[__child])
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
    __main__for__81__block__82__for__98__j = 0
    __rhs = stack.pop()
    __main__for__81__block__82__for__98__j = __rhs
    stack.append (__main__for__81__block__82__for__98__j)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        stack.append(__main__for__81__block__82__for__98__j)
        # RHS
        # Member Accessor
        # LHS
        stack.append(__main__for__81__block__82__tokens3)
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
        # Statement
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__for__81__block__82__tokens3)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__for__81__block__82__for__98__j)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __arr = stack.pop ()
        __builtin__free (__arr)
        stack.append (0)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Update
        # Pre-Increment
        # RHS
        stack.append(__main__for__81__block__82__for__98__j)
        __rhs = stack.pop ()
        __main__for__81__block__82__for__98__j = __main__for__81__block__82__for__98__j + 1
        __res = __main__for__81__block__82__for__98__j
        stack.append (__res)
    #---------------------------------------------------------------------
    # Statement
    stack.append(__main__for__81__block__82__tokens3)
    __arr = stack.pop ()
    __builtin__free (__arr)
    stack.append (0)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

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
    # Addition
    # LHS
    stack.append(__main__for__81__l)
    # RHS
    # Int Literal
    stack.append(5)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs + __rhs
    stack.append(__res)
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
    __main__for__81__block__82__tokens4 = 0
    __rhs = stack.pop()
    __main__for__81__block__82__tokens4 = __rhs
    stack.append (__main__for__81__block__82__tokens4)
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
    stack.append(__main__for__81__block__82__tokens4)
    # RHS
    stack.append (__field____main____Vector__char__1____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    # Subtraction
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main__for__81__block__82__tokens4)
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
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    __arg0 = stack.pop ()
    # *** stringToInt
    __res = __builtin__stringToInt__char__1 (__arg0)
    stack.append (__res) # function call result
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(__main__for__81__block__82__monkey)
    # RHS
    stack.append(__field____main____Monkey____false_monkey_id)
    __child = stack.pop()
    __parent = stack.pop()
    __rhs = stack.pop()
    __parent[__child] = __rhs
    stack.append (__parent[__child])
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
    __main__for__81__block__82__for__99__j = 0
    __rhs = stack.pop()
    __main__for__81__block__82__for__99__j = __rhs
    stack.append (__main__for__81__block__82__for__99__j)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        stack.append(__main__for__81__block__82__for__99__j)
        # RHS
        # Member Accessor
        # LHS
        stack.append(__main__for__81__block__82__tokens4)
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
        # Statement
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__for__81__block__82__tokens4)
        # RHS
        stack.append (__field____main____Vector__char__1____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__for__81__block__82__for__99__j)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __arr = stack.pop ()
        __builtin__free (__arr)
        stack.append (0)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Update
        # Pre-Increment
        # RHS
        stack.append(__main__for__81__block__82__for__99__j)
        __rhs = stack.pop ()
        __main__for__81__block__82__for__99__j = __main__for__81__block__82__for__99__j + 1
        __res = __main__for__81__block__82__for__99__j
        stack.append (__res)
    #---------------------------------------------------------------------
    # Statement
    stack.append(__main__for__81__block__82__tokens4)
    __arr = stack.pop ()
    __builtin__free (__arr)
    stack.append (0)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Method Call - Vector<:Monkey:>::pushBack(Monkey) -> void
    # LHS
    stack.append(__main__monkeys)
    # RHS
    # Arguments
    stack.append(__main__for__81__block__82__monkey)
    __arg0 = stack.pop ()
    __obj = stack.pop ()
    __retval = __method____main____Vector__Monkey____pushBack__Monkey (__obj, __arg0)
    stack.append (__retval)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
    # Update
    # Assignment - '+='
    # RHS
    # Int Literal
    stack.append(7)
    __rhs = stack.pop()
    __main__for__81__l = __main__for__81__l + __rhs
    stack.append (__main__for__81__l)
#-------------------------------------------------------------------------
#=========================================================================
# Function Declaration - println(Vector<:Monkey:>) -> void
def __main____println__Vector__tparam0__Monkey (__main__println__monkeys):
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
    __main__println__block__100__for__101__i = 0
    __rhs = stack.pop()
    __main__println__block__100__for__101__i = __rhs
    stack.append (__main__println__block__100__for__101__i)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        stack.append(__main__println__block__100__for__101__i)
        # RHS
        # Member Accessor
        # LHS
        stack.append(__main__println__monkeys)
        # RHS
        stack.append (__field____main____Vector__Monkey____size)
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
        # Function Call - print(int) -> void
        # Arguments
        stack.append(__main__println__block__100__for__101__i)
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
        stack.append(':')
        __arg0 = stack.pop ()
        # *** print
        __res = __builtin__print__char (__arg0)
        stack.append (__res) # function call result
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Function Call - println<:int:>(Vector<:int:>) -> void
        # Arguments
        # Member Accessor
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__println__monkeys)
        # RHS
        stack.append (__field____main____Vector__Monkey____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__println__block__100__for__101__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        stack.append (__field____main____Monkey____items)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        __arg0 = stack.pop ()
        # *** println
        __res = __main____println__int____Vector__tparam0__int (__arg0)
        stack.append (__res) # function call result
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
        # Update
        # Pre-Increment
        # RHS
        stack.append(__main__println__block__100__for__101__i)
        __rhs = stack.pop ()
        __main__println__block__100__for__101__i = __main__println__block__100__for__101__i + 1
        __res = __main__println__block__100__for__101__i
        stack.append (__res)
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
# End Function Declaration - __main____println__Vector__tparam0__Monkey
#=========================================================================

#-------------------------------------------------------------------------
# For-Loop
# Init
# Assignment - '='
# RHS
# Int Literal
stack.append(0)
# LHS
__main__for__103__r = 0
__rhs = stack.pop()
__main__for__103__r = __rhs
stack.append (__main__for__103__r)
# Using an infinite loop so we can write a separate multi-line condition
while (1):
    # Condition
    # Less Than
    # LHS
    stack.append(__main__for__103__r)
    # RHS
    # Int Literal
    stack.append(20)
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
    __main__for__103__block__104__for__105__m = 0
    __rhs = stack.pop()
    __main__for__103__block__104__for__105__m = __rhs
    stack.append (__main__for__103__block__104__for__105__m)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        stack.append(__main__for__103__block__104__for__105__m)
        # RHS
        # Member Accessor
        # LHS
        stack.append(__main__monkeys)
        # RHS
        stack.append (__field____main____Vector__Monkey____size)
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
        # Assignment - '='
        # RHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__monkeys)
        # RHS
        stack.append (__field____main____Vector__Monkey____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__for__103__block__104__for__105__m)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # LHS
        __main__for__103__block__104__for__105__block__106__monkey = 0
        __rhs = stack.pop()
        __main__for__103__block__104__for__105__block__106__monkey = __rhs
        stack.append (__main__for__103__block__104__for__105__block__106__monkey)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Member Accessor
        # LHS
        stack.append(__main__for__103__block__104__for__105__block__106__monkey)
        # RHS
        stack.append (__field____main____Monkey____items)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # LHS
        __main__for__103__block__104__for__105__block__106__monkey_items = 0
        __rhs = stack.pop()
        __main__for__103__block__104__for__105__block__106__monkey_items = __rhs
        stack.append (__main__for__103__block__104__for__105__block__106__monkey_items)
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
        __main__for__103__block__104__for__105__block__106__for__107__i = 0
        __rhs = stack.pop()
        __main__for__103__block__104__for__105__block__106__for__107__i = __rhs
        stack.append (__main__for__103__block__104__for__105__block__106__for__107__i)
        # Using an infinite loop so we can write a separate multi-line condition
        while (1):
            # Condition
            # Less Than
            # LHS
            stack.append(__main__for__103__block__104__for__105__block__106__for__107__i)
            # RHS
            # Member Accessor
            # LHS
            stack.append(__main__for__103__block__104__for__105__block__106__monkey_items)
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
            stack.append(__main__for__103__block__104__for__105__block__106__monkey_items)
            # RHS
            stack.append (__field____main____Vector__int____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main__for__103__block__104__for__105__block__106__for__107__i)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # LHS
            __main__for__103__block__104__for__105__block__106__for__107__block__108__worry_level = 0
            __rhs = stack.pop()
            __main__for__103__block__104__for__105__block__106__for__107__block__108__worry_level = __rhs
            stack.append (__main__for__103__block__104__for__105__block__106__for__107__block__108__worry_level)
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
            # Member Accessor
            # LHS
            stack.append(__main__for__103__block__104__for__105__block__106__monkey)
            # RHS
            stack.append (__field____main____Monkey____op)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # RHS
            stack.append(__main__OP_ADD)
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs == __rhs
            stack.append (__res)
            __if__109__cond = stack.pop ()
            # Condition for elif #0
            # Equal
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__for__103__block__104__for__105__block__106__monkey)
            # RHS
            stack.append (__field____main____Monkey____op)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # RHS
            stack.append(__main__OP_MUL)
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs == __rhs
            stack.append (__res)
            __elif__109x0__cond = stack.pop ()
            # get condition from stack
            if (__if__109__cond):
                # Body
                # Statement
                # Assignment - '+='
                # RHS
                # Member Accessor
                # LHS
                stack.append(__main__for__103__block__104__for__105__block__106__monkey)
                # RHS
                stack.append (__field____main____Monkey____operand)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                __rhs = stack.pop()
                __main__for__103__block__104__for__105__block__106__for__107__block__108__worry_level = __main__for__103__block__104__for__105__block__106__for__107__block__108__worry_level + __rhs
                stack.append (__main__for__103__block__104__for__105__block__106__for__107__block__108__worry_level)
                # Statement results can be ignored
                stack.pop ()
                # End Statement

            #-------------------------------------------------------------
            # Elif-Statement
            # Condition
            elif (__elif__109x0__cond):
                # Body
                # Statement
                # Assignment - '*='
                # RHS
                # Member Accessor
                # LHS
                stack.append(__main__for__103__block__104__for__105__block__106__monkey)
                # RHS
                stack.append (__field____main____Monkey____operand)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                __rhs = stack.pop()
                __main__for__103__block__104__for__105__block__106__for__107__block__108__worry_level = __main__for__103__block__104__for__105__block__106__for__107__block__108__worry_level * __rhs
                stack.append (__main__for__103__block__104__for__105__block__106__for__107__block__108__worry_level)
                # Statement results can be ignored
                stack.pop ()
                # End Statement

            #-------------------------------------------------------------
            #-------------------------------------------------------------
            # Else-Statement
            else:
                # Statement
                # Assignment - '*='
                # RHS
                stack.append(__main__for__103__block__104__for__105__block__106__for__107__block__108__worry_level)
                __rhs = stack.pop()
                __main__for__103__block__104__for__105__block__106__for__107__block__108__worry_level = __main__for__103__block__104__for__105__block__106__for__107__block__108__worry_level * __rhs
                stack.append (__main__for__103__block__104__for__105__block__106__for__107__block__108__worry_level)
                # Statement results can be ignored
                stack.pop ()
                # End Statement

            #-------------------------------------------------------------
            # End of if
            #-------------------------------------------------------------
            # Statement
            # Assignment - '='
            # RHS
            # Division
            # LHS
            stack.append(__main__for__103__block__104__for__105__block__106__for__107__block__108__worry_level)
            # RHS
            # Int Literal
            stack.append(3)
            __rhs = stack.pop()
            __lhs = stack.pop()
            __res = __lhs // __rhs
            stack.append(__res)
            __rhs = stack.pop()
            __main__for__103__block__104__for__105__block__106__for__107__block__108__worry_level = __rhs
            stack.append (__main__for__103__block__104__for__105__block__106__for__107__block__108__worry_level)
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
            # Modulus
            # LHS
            stack.append(__main__for__103__block__104__for__105__block__106__for__107__block__108__worry_level)
            # RHS
            # Member Accessor
            # LHS
            stack.append(__main__for__103__block__104__for__105__block__106__monkey)
            # RHS
            stack.append (__field____main____Monkey____divisible_by)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            __rhs = stack.pop()
            __lhs = stack.pop()
            __res = __lhs % __rhs
            stack.append(__res)
            # RHS
            # Int Literal
            stack.append(0)
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs == __rhs
            stack.append (__res)
            __if__110__cond = stack.pop ()
            # get condition from stack
            if (__if__110__cond):
                # Body
                # Statement
                # Method Call - Vector<:int:>::pushBack(int) -> void
                # LHS
                # Member Accessor
                # LHS
                # Subscript
                # LHS
                # Member Accessor
                # LHS
                stack.append(__main__monkeys)
                # RHS
                stack.append (__field____main____Vector__Monkey____data)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                # OFFSET
                # Member Accessor
                # LHS
                stack.append(__main__for__103__block__104__for__105__block__106__monkey)
                # RHS
                stack.append (__field____main____Monkey____true_monkey_id)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # RHS
                stack.append (__field____main____Monkey____items)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                # RHS
                # Arguments
                stack.append(__main__for__103__block__104__for__105__block__106__for__107__block__108__worry_level)
                __arg0 = stack.pop ()
                __obj = stack.pop ()
                __retval = __method____main____Vector__int____pushBack__int (__obj, __arg0)
                stack.append (__retval)
                # Statement results can be ignored
                stack.pop ()
                # End Statement

            #-------------------------------------------------------------
            # Else-Statement
            else:
                # Statement
                # Method Call - Vector<:int:>::pushBack(int) -> void
                # LHS
                # Member Accessor
                # LHS
                # Subscript
                # LHS
                # Member Accessor
                # LHS
                stack.append(__main__monkeys)
                # RHS
                stack.append (__field____main____Vector__Monkey____data)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                # OFFSET
                # Member Accessor
                # LHS
                stack.append(__main__for__103__block__104__for__105__block__106__monkey)
                # RHS
                stack.append (__field____main____Monkey____false_monkey_id)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # RHS
                stack.append (__field____main____Monkey____items)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                # RHS
                # Arguments
                stack.append(__main__for__103__block__104__for__105__block__106__for__107__block__108__worry_level)
                __arg0 = stack.pop ()
                __obj = stack.pop ()
                __retval = __method____main____Vector__int____pushBack__int (__obj, __arg0)
                stack.append (__retval)
                # Statement results can be ignored
                stack.pop ()
                # End Statement

            #-------------------------------------------------------------
            # End of if
            #-------------------------------------------------------------
            # Statement
            # Assignment - '+='
            # RHS
            # Int Literal
            stack.append(1)
            # LHS
            # Member Accessor Assignment
            # LHS
            stack.append(__main__for__103__block__104__for__105__block__106__monkey)
            # RHS
            stack.append(__field____main____Monkey____inspected_items)
            __child = stack.pop()
            __parent = stack.pop()
            __rhs = stack.pop()
            __parent[__child] = __parent[__child] + __rhs
            stack.append (__parent[__child])
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            #-------------------------------------------------------------
            # Update
            # Pre-Increment
            # RHS
            stack.append(__main__for__103__block__104__for__105__block__106__for__107__i)
            __rhs = stack.pop ()
            __main__for__103__block__104__for__105__block__106__for__107__i = __main__for__103__block__104__for__105__block__106__for__107__i + 1
            __res = __main__for__103__block__104__for__105__block__106__for__107__i
            stack.append (__res)
        #-----------------------------------------------------------------
        # Statement
        # Method Call - Vector<:int:>::clear() -> void
        # LHS
        stack.append(__main__for__103__block__104__for__105__block__106__monkey_items)
        # RHS
        # Arguments
        __obj = stack.pop ()
        __retval = __method____main____Vector__int____clear (__obj)
        stack.append (__retval)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
        # Update
        # Pre-Increment
        # RHS
        stack.append(__main__for__103__block__104__for__105__m)
        __rhs = stack.pop ()
        __main__for__103__block__104__for__105__m = __main__for__103__block__104__for__105__m + 1
        __res = __main__for__103__block__104__for__105__m
        stack.append (__res)
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    # Update
    # Pre-Increment
    # RHS
    stack.append(__main__for__103__r)
    __rhs = stack.pop ()
    __main__for__103__r = __main__for__103__r + 1
    __res = __main__for__103__r
    stack.append (__res)
#-------------------------------------------------------------------------
# Statement
# Assignment - '='
# RHS
# Int Literal
stack.append(0)
# LHS
__main__firstmax = 0
__rhs = stack.pop()
__main__firstmax = __rhs
stack.append (__main__firstmax)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Assignment - '='
# RHS
# Int Literal
stack.append(0)
# LHS
__main__secondmax = 0
__rhs = stack.pop()
__main__secondmax = __rhs
stack.append (__main__secondmax)
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
__main__for__111__i = 0
__rhs = stack.pop()
__main__for__111__i = __rhs
stack.append (__main__for__111__i)
# Using an infinite loop so we can write a separate multi-line condition
while (1):
    # Condition
    # Less Than
    # LHS
    stack.append(__main__for__111__i)
    # RHS
    # Member Accessor
    # LHS
    stack.append(__main__monkeys)
    # RHS
    stack.append (__field____main____Vector__Monkey____size)
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
    # Statement
    # Assignment - '='
    # RHS
    # Function Call - max(int, int) -> int
    # Arguments
    # Member Accessor
    # LHS
    # Subscript
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main__monkeys)
    # RHS
    stack.append (__field____main____Vector__Monkey____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    stack.append(__main__for__111__i)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    # RHS
    stack.append (__field____main____Monkey____inspected_items)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    stack.append(__main__firstmax)
    __arg1 = stack.pop ()
    __arg0 = stack.pop ()
    # *** max
    __res = __main____max__int__int (__arg0, __arg1)
    stack.append (__res) # function call result
    __rhs = stack.pop()
    __main__firstmax = __rhs
    stack.append (__main__firstmax)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Update
    # Pre-Increment
    # RHS
    stack.append(__main__for__111__i)
    __rhs = stack.pop ()
    __main__for__111__i = __main__for__111__i + 1
    __res = __main__for__111__i
    stack.append (__res)
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# For-Loop
# Init
# Assignment - '='
# RHS
# Int Literal
stack.append(0)
# LHS
__main__for__112__i = 0
__rhs = stack.pop()
__main__for__112__i = __rhs
stack.append (__main__for__112__i)
# Using an infinite loop so we can write a separate multi-line condition
while (1):
    # Condition
    # Less Than
    # LHS
    stack.append(__main__for__112__i)
    # RHS
    # Member Accessor
    # LHS
    stack.append(__main__monkeys)
    # RHS
    stack.append (__field____main____Vector__Monkey____size)
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
    # If-Statement
    # Precomputing all if/elif conditions and give unique names
    # bc we can't have code between if and elif
    # Condition
    # Not Equal
    # LHS
    # Member Accessor
    # LHS
    # Subscript
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main__monkeys)
    # RHS
    stack.append (__field____main____Vector__Monkey____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    stack.append(__main__for__112__i)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    # RHS
    stack.append (__field____main____Monkey____inspected_items)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # RHS
    stack.append(__main__firstmax)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs != __rhs
    stack.append (__res)
    __if__113__cond = stack.pop ()
    # get condition from stack
    if (__if__113__cond):
        # Body
        # Statement
        # Assignment - '='
        # RHS
        # Function Call - max(int, int) -> int
        # Arguments
        # Member Accessor
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__monkeys)
        # RHS
        stack.append (__field____main____Vector__Monkey____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__for__112__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        stack.append (__field____main____Monkey____inspected_items)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        stack.append(__main__secondmax)
        __arg1 = stack.pop ()
        __arg0 = stack.pop ()
        # *** max
        __res = __main____max__int__int (__arg0, __arg1)
        stack.append (__res) # function call result
        __rhs = stack.pop()
        __main__secondmax = __rhs
        stack.append (__main__secondmax)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

    # End of if
    #---------------------------------------------------------------------
    # Update
    # Pre-Increment
    # RHS
    stack.append(__main__for__112__i)
    __rhs = stack.pop ()
    __main__for__112__i = __main__for__112__i + 1
    __res = __main__for__112__i
    stack.append (__res)
#-------------------------------------------------------------------------
# Statement
# Function Call - println(int) -> void
# Arguments
# Multiplication
# LHS
stack.append(__main__firstmax)
# RHS
stack.append(__main__secondmax)
__rhs = stack.pop()
__lhs = stack.pop()
__res = __lhs * __rhs
stack.append(__res)
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

