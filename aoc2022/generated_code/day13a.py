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
# Class Declaration - __main____Vector__Element inherits __builtin____main__Object
# Creating Dispatch Table (will be populated later)
__dtable____main____Vector__Element = []
#-------------------------------------------------------------------------
# Field - Element[] Vector<:Element:>::data
__field____main____Vector__Element____data = 1
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Field - int Vector<:Element:>::size
__field____main____Vector__Element____size = 2
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Field - int Vector<:Element:>::capacity
__field____main____Vector__Element____capacity = 3
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Constructor Declaration - Vector<:Element:>::Vector() -> Vector<:Element:>
def __ctor____main____Vector__Element____Vector ():
    # Creating Class Instance
    this = [0] * 4
    # Add Dispatch Table
    this[0] = __dtable____main____Vector__Element
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
    stack.append(__field____main____Vector__Element____capacity)
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
    stack.append(__field____main____Vector__Element____size)
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
    stack.append (__field____main____Vector__Element____capacity)
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
    stack.append(__field____main____Vector__Element____data)
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
# End Constructor Declaration - __ctor____main____Vector__Element____Vector
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Constructor Declaration - Vector<:Element:>::Vector(int) -> Vector<:Element:>
def __ctor____main____Vector__Element____Vector__int (__main____Vector__Element__Vector__size):
    # Creating Class Instance
    this = [0] * 4
    # Add Dispatch Table
    this[0] = __dtable____main____Vector__Element
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Assignment - '='
    # RHS
    # Addition
    # LHS
    stack.append(__main____Vector__Element__Vector__size)
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
    stack.append(__field____main____Vector__Element____capacity)
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
    stack.append(__main____Vector__Element__Vector__size)
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append(__field____main____Vector__Element____size)
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
    stack.append (__field____main____Vector__Element____capacity)
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
    stack.append(__field____main____Vector__Element____data)
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
# End Constructor Declaration - __ctor____main____Vector__Element____Vector__int
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vector<:Element:>::pushBack(Element) -> void
def __method____main____Vector__Element____pushBack__Element (this, __main____Vector__Element__pushBack__val):
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
    stack.append (__field____main____Vector__Element____size)
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
    stack.append (__field____main____Vector__Element____capacity)
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
        stack.append (__field____main____Vector__Element____capacity)
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
        stack.append(__field____main____Vector__Element____capacity)
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
        stack.append (__field____main____Vector__Element____capacity)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        __dim = stack.pop ()
        __res = [None] * __dim
        stack.append (__res)
        # LHS
        __main____Vector__Element__pushBack__block__14__if__15__block__16__nData = 0
        __rhs = stack.pop()
        __main____Vector__Element__pushBack__block__14__if__15__block__16__nData = __rhs
        stack.append (__main____Vector__Element__pushBack__block__14__if__15__block__16__nData)
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
        __main____Vector__Element__pushBack__block__14__if__15__block__16__for__17__i = 0
        __rhs = stack.pop()
        __main____Vector__Element__pushBack__block__14__if__15__block__16__for__17__i = __rhs
        stack.append (__main____Vector__Element__pushBack__block__14__if__15__block__16__for__17__i)
        # Using an infinite loop so we can write a separate multi-line condition
        while (1):
            # Condition
            # Less Than
            # LHS
            stack.append(__main____Vector__Element__pushBack__block__14__if__15__block__16__for__17__i)
            # RHS
            # Member Accessor
            # LHS
            stack.append(this)
            # RHS
            stack.append (__field____main____Vector__Element____size)
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
            stack.append (__field____main____Vector__Element____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main____Vector__Element__pushBack__block__14__if__15__block__16__for__17__i)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # LHS
            # Subscript assignment
            # LHS
            stack.append(__main____Vector__Element__pushBack__block__14__if__15__block__16__nData)
            # OFFSET
            stack.append(__main____Vector__Element__pushBack__block__14__if__15__block__16__for__17__i)
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
            stack.append(__main____Vector__Element__pushBack__block__14__if__15__block__16__for__17__i)
            __rhs = stack.pop ()
            __main____Vector__Element__pushBack__block__14__if__15__block__16__for__17__i = __main____Vector__Element__pushBack__block__14__if__15__block__16__for__17__i + 1
            __res = __main____Vector__Element__pushBack__block__14__if__15__block__16__for__17__i
            stack.append (__res)
        #-----------------------------------------------------------------
        # Statement
        # Member Accessor
        # LHS
        stack.append(this)
        # RHS
        stack.append (__field____main____Vector__Element____data)
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
        stack.append(__main____Vector__Element__pushBack__block__14__if__15__block__16__nData)
        # LHS
        # Member Accessor Assignment
        # LHS
        stack.append(this)
        # RHS
        stack.append(__field____main____Vector__Element____data)
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
    stack.append(__main____Vector__Element__pushBack__val)
    # LHS
    # Subscript assignment
    # LHS
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__Element____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__Element____size)
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
    stack.append (__field____main____Vector__Element____size)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __rhs = stack.pop ()
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__Element____size)
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
# End Method Declaration - __method____main____Vector__Element____pushBack__Element
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vector<:Element:>::popBack() -> Element
def __method____main____Vector__Element____popBack (this):
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
    stack.append (__field____main____Vector__Element____data)
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
    stack.append (__field____main____Vector__Element____size)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __rhs = stack.pop ()
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__Element____size)
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
# End Method Declaration - __method____main____Vector__Element____popBack
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vector<:Element:>::clear() -> void
def __method____main____Vector__Element____clear (this):
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
        stack.append (__field____main____Vector__Element____size)
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
        # Method Call - Vector<:Element:>::popBack() -> Element
        # LHS
        stack.append(this)
        # RHS
        # Arguments
        __obj = stack.pop ()
        __retval = __method____main____Vector__Element____popBack (__obj)
        stack.append (__retval)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

    # End of While
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    return 0
# End Method Declaration - __method____main____Vector__Element____clear
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vector<:Element:>::get(int) -> Element
def __method____main____Vector__Element____get__int (this, __main____Vector__Element__get__index):
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
    stack.append (__field____main____Vector__Element____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    stack.append(__main____Vector__Element__get__index)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    __rVal = stack.pop ()
    return __rVal
    #---------------------------------------------------------------------
    return 0
# End Method Declaration - __method____main____Vector__Element____get__int
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vector<:Element:>::set(int, Element) -> void
def __method____main____Vector__Element____set__int__Element (this, __main____Vector__Element__set__index, __main____Vector__Element__set__value):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main____Vector__Element__set__value)
    # LHS
    # Subscript assignment
    # LHS
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____Vector__Element____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    stack.append(__main____Vector__Element__set__index)
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
# End Method Declaration - __method____main____Vector__Element____set__int__Element
#-------------------------------------------------------------------------

# Populate Dispatch Table
__dtable____main____Vector__Element = [__method____main____Vector__Element____pushBack__Element, __method____main____Vector__Element____popBack, __method____main____Vector__Element____clear, __method____main____Vector__Element____get__int, __method____main____Vector__Element____set__int__Element]
# End Class Declaration - __main____Vector__Element
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
        __main____Vector__char__pushBack__block__26__if__27__block__28__nData = 0
        __rhs = stack.pop()
        __main____Vector__char__pushBack__block__26__if__27__block__28__nData = __rhs
        stack.append (__main____Vector__char__pushBack__block__26__if__27__block__28__nData)
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
        __main____Vector__char__pushBack__block__26__if__27__block__28__for__29__i = 0
        __rhs = stack.pop()
        __main____Vector__char__pushBack__block__26__if__27__block__28__for__29__i = __rhs
        stack.append (__main____Vector__char__pushBack__block__26__if__27__block__28__for__29__i)
        # Using an infinite loop so we can write a separate multi-line condition
        while (1):
            # Condition
            # Less Than
            # LHS
            stack.append(__main____Vector__char__pushBack__block__26__if__27__block__28__for__29__i)
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
            stack.append(__main____Vector__char__pushBack__block__26__if__27__block__28__for__29__i)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # LHS
            # Subscript assignment
            # LHS
            stack.append(__main____Vector__char__pushBack__block__26__if__27__block__28__nData)
            # OFFSET
            stack.append(__main____Vector__char__pushBack__block__26__if__27__block__28__for__29__i)
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
            stack.append(__main____Vector__char__pushBack__block__26__if__27__block__28__for__29__i)
            __rhs = stack.pop ()
            __main____Vector__char__pushBack__block__26__if__27__block__28__for__29__i = __main____Vector__char__pushBack__block__26__if__27__block__28__for__29__i + 1
            __res = __main____Vector__char__pushBack__block__26__if__27__block__28__for__29__i
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
        stack.append(__main____Vector__char__pushBack__block__26__if__27__block__28__nData)
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
# Method Declaration - Vector<:char:>::clear() -> void
def __method____main____Vector__char____clear (this):
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
        stack.append (__field____main____Vector__char____size)
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
        # Method Call - Vector<:char:>::popBack() -> char
        # LHS
        stack.append(this)
        # RHS
        # Arguments
        __obj = stack.pop ()
        __retval = __method____main____Vector__char____popBack (__obj)
        stack.append (__retval)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

    # End of While
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    return 0
# End Method Declaration - __method____main____Vector__char____clear
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
__dtable____main____Vector__char = [__method____main____Vector__char____pushBack__char, __method____main____Vector__char____popBack, __method____main____Vector__char____clear, __method____main____Vector__char____get__int, __method____main____Vector__char____set__int__char]
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
    __if__37__cond = stack.pop ()
    # get condition from stack
    if (__if__37__cond):
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
    __main__strlen__block__36__size = 0
    __rhs = stack.pop()
    __main__strlen__block__36__size = __rhs
    stack.append (__main__strlen__block__36__size)
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
        __res = __main__strlen__block__36__size
        __main__strlen__block__36__size = __main__strlen__block__36__size + 1
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
    stack.append(__main__strlen__block__36__size)
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
    __main__strcmp__block__39__asize = 0
    __rhs = stack.pop()
    __main__strcmp__block__39__asize = __rhs
    stack.append (__main__strcmp__block__39__asize)
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
    __main__strcmp__block__39__bsize = 0
    __rhs = stack.pop()
    __main__strcmp__block__39__bsize = __rhs
    stack.append (__main__strcmp__block__39__bsize)
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
    stack.append(__main__strcmp__block__39__asize)
    # RHS
    stack.append(__main__strcmp__block__39__bsize)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs != __rhs
    stack.append (__res)
    __if__40__cond = stack.pop ()
    # get condition from stack
    if (__if__40__cond):
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
    __main__strcmp__block__39__for__41__i = 0
    __rhs = stack.pop()
    __main__strcmp__block__39__for__41__i = __rhs
    stack.append (__main__strcmp__block__39__for__41__i)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        stack.append(__main__strcmp__block__39__for__41__i)
        # RHS
        stack.append(__main__strcmp__block__39__asize)
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
        stack.append(__main__strcmp__block__39__for__41__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        # Subscript
        # LHS
        stack.append(__main__strcmp__b)
        # OFFSET
        stack.append(__main__strcmp__block__39__for__41__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
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
        stack.append(__main__strcmp__block__39__for__41__i)
        __rhs = stack.pop ()
        __main__strcmp__block__39__for__41__i = __main__strcmp__block__39__for__41__i + 1
        __res = __main__strcmp__block__39__for__41__i
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
    __main__substr__block__45__res = 0
    __rhs = stack.pop()
    __main__substr__block__45__res = __rhs
    stack.append (__main__substr__block__45__res)
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
    __main__substr__block__45__for__46__i = 0
    __rhs = stack.pop()
    __main__substr__block__45__for__46__i = __rhs
    stack.append (__main__substr__block__45__for__46__i)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        stack.append(__main__substr__block__45__for__46__i)
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
        stack.append(__main__substr__block__45__for__46__i)
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
        stack.append(__main__substr__block__45__res)
        # OFFSET
        stack.append(__main__substr__block__45__for__46__i)
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
        stack.append(__main__substr__block__45__for__46__i)
        __rhs = stack.pop ()
        __main__substr__block__45__for__46__i = __main__substr__block__45__for__46__i + 1
        __res = __main__substr__block__45__for__46__i
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
    stack.append(__main__substr__block__45__res)
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
    stack.append(__main__substr__block__45__res)
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
    __main__first_index_of__block__48__size = 0
    __rhs = stack.pop()
    __main__first_index_of__block__48__size = __rhs
    stack.append (__main__first_index_of__block__48__size)
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
    __main__first_index_of__block__48__for__49__i = 0
    __rhs = stack.pop()
    __main__first_index_of__block__48__for__49__i = __rhs
    stack.append (__main__first_index_of__block__48__for__49__i)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        stack.append(__main__first_index_of__block__48__for__49__i)
        # RHS
        stack.append(__main__first_index_of__block__48__size)
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
        stack.append(__main__first_index_of__block__48__for__49__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        stack.append(__main__first_index_of__c)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs == __rhs
        stack.append (__res)
        __if__51__cond = stack.pop ()
        # get condition from stack
        if (__if__51__cond):
            # Body
            # Return
            stack.append(__main__first_index_of__block__48__for__49__i)
            __rVal = stack.pop ()
            return __rVal
        # End of if
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # Update
        # Pre-Increment
        # RHS
        stack.append(__main__first_index_of__block__48__for__49__i)
        __rhs = stack.pop ()
        __main__first_index_of__block__48__for__49__i = __main__first_index_of__block__48__for__49__i + 1
        __res = __main__first_index_of__block__48__for__49__i
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
    __main__split__block__52__tokens = 0
    __rhs = stack.pop()
    __main__split__block__52__tokens = __rhs
    stack.append (__main__split__block__52__tokens)
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
    __main__split__block__52__size = 0
    __rhs = stack.pop()
    __main__split__block__52__size = __rhs
    stack.append (__main__split__block__52__size)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(0)
    # LHS
    __main__split__block__52__i = 0
    __rhs = stack.pop()
    __main__split__block__52__i = __rhs
    stack.append (__main__split__block__52__i)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(0)
    # LHS
    __main__split__block__52__j = 0
    __rhs = stack.pop()
    __main__split__block__52__j = __rhs
    stack.append (__main__split__block__52__j)
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
        stack.append(__main__split__block__52__i)
        # RHS
        stack.append(__main__split__block__52__size)
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
        stack.append(__main__split__block__52__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        stack.append(__main__split__delim)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs != __rhs
        stack.append (__res)
        __if__55__cond = stack.pop ()
        # get condition from stack
        if (__if__55__cond):
            # Body
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Assignment - '='
            # RHS
            # Int Literal
            stack.append(0)
            # LHS
            __main__split__block__52__while__53__block__54__if__55__block__56__count = 0
            __rhs = stack.pop()
            __main__split__block__52__while__53__block__54__if__55__block__56__count = __rhs
            stack.append (__main__split__block__52__while__53__block__54__if__55__block__56__count)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            # Statement
            # Assignment - '='
            # RHS
            stack.append(__main__split__block__52__i)
            # LHS
            __main__split__block__52__while__53__block__54__if__55__block__56__k = 0
            __rhs = stack.pop()
            __main__split__block__52__while__53__block__54__if__55__block__56__k = __rhs
            stack.append (__main__split__block__52__while__53__block__54__if__55__block__56__k)
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
                stack.append(__main__split__block__52__while__53__block__54__if__55__block__56__k)
                # RHS
                stack.append(__main__split__block__52__size)
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
                __res = __main__split__block__52__while__53__block__54__if__55__block__56__k
                __main__split__block__52__while__53__block__54__if__55__block__56__k = __main__split__block__52__while__53__block__54__if__55__block__56__k + 1
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
                __if__58__cond = stack.pop ()
                # get condition from stack
                if (__if__58__cond):
                    # Body
                    # Statement
                    # Pre-Increment
                    # RHS
                    stack.append(__main__split__block__52__while__53__block__54__if__55__block__56__count)
                    __rhs = stack.pop ()
                    __main__split__block__52__while__53__block__54__if__55__block__56__count = __main__split__block__52__while__53__block__54__if__55__block__56__count + 1
                    __res = __main__split__block__52__while__53__block__54__if__55__block__56__count
                    stack.append (__res)
                    # Statement results can be ignored
                    stack.pop ()
                    # End Statement

                #---------------------------------------------------------
                # Else-Statement
                else:
                    # Break out of __while__57
                    break
                #---------------------------------------------------------
                # End of if
                #---------------------------------------------------------
            # End of While
            #-------------------------------------------------------------
            # Statement
            # Method Call - Vector<:char[]:>::pushBack(char[]) -> void
            # LHS
            stack.append(__main__split__block__52__tokens)
            # RHS
            # Arguments
            # Addition
            # LHS
            stack.append(__main__split__block__52__while__53__block__54__if__55__block__56__count)
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
            __main__split__block__52__while__53__block__54__if__55__block__56__for__59__k = 0
            __rhs = stack.pop()
            __main__split__block__52__while__53__block__54__if__55__block__56__for__59__k = __rhs
            stack.append (__main__split__block__52__while__53__block__54__if__55__block__56__for__59__k)
            # Using an infinite loop so we can write a separate multi-line condition
            while (1):
                # Condition
                # Less Than
                # LHS
                stack.append(__main__split__block__52__while__53__block__54__if__55__block__56__for__59__k)
                # RHS
                stack.append(__main__split__block__52__while__53__block__54__if__55__block__56__count)
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
                __res = __main__split__block__52__i
                __main__split__block__52__i = __main__split__block__52__i + 1
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
                stack.append(__main__split__block__52__tokens)
                # RHS
                stack.append (__field____main____Vector__char__1____data)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                # OFFSET
                stack.append(__main__split__block__52__j)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                # OFFSET
                stack.append(__main__split__block__52__while__53__block__54__if__55__block__56__for__59__k)
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
                stack.append(__main__split__block__52__while__53__block__54__if__55__block__56__for__59__k)
                __rhs = stack.pop ()
                __main__split__block__52__while__53__block__54__if__55__block__56__for__59__k = __main__split__block__52__while__53__block__54__if__55__block__56__for__59__k + 1
                __res = __main__split__block__52__while__53__block__54__if__55__block__56__for__59__k
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
            stack.append(__main__split__block__52__tokens)
            # RHS
            stack.append (__field____main____Vector__char__1____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main__split__block__52__j)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # OFFSET
            stack.append(__main__split__block__52__while__53__block__54__if__55__block__56__count)
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
            stack.append(__main__split__block__52__j)
            __rhs = stack.pop ()
            __main__split__block__52__j = __main__split__block__52__j + 1
            __res = __main__split__block__52__j
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
        stack.append(__main__split__block__52__i)
        __rhs = stack.pop ()
        __main__split__block__52__i = __main__split__block__52__i + 1
        __res = __main__split__block__52__i
        stack.append (__res)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
    # End of While
    #---------------------------------------------------------------------
    # Return
    stack.append(__main__split__block__52__tokens)
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
    __if__62__cond = stack.pop ()
    # get condition from stack
    if (__if__62__cond):
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
    __if__64__cond = stack.pop ()
    # get condition from stack
    if (__if__64__cond):
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
    __if__66__cond = stack.pop ()
    # get condition from stack
    if (__if__66__cond):
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
    __if__68__cond = stack.pop ()
    # get condition from stack
    if (__if__68__cond):
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
    __if__70__cond = stack.pop ()
    # get condition from stack
    if (__if__70__cond):
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
    __if__72__cond = stack.pop ()
    # get condition from stack
    if (__if__72__cond):
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
#=========================================================================
# Class Declaration - __main____Element inherits __builtin____main__Object
# Creating Dispatch Table (will be populated later)
__dtable____main____Element = []
#-------------------------------------------------------------------------
# Field - int Element::is_list
__field____main____Element____is_list = 1
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Field - int Element::value
__field____main____Element____value = 2
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Field - Vector<:Element:> Element::list
__field____main____Element____list = 3
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Constructor Declaration - Element::Element(int) -> Element
def __ctor____main____Element____Element__int (__main____Element__Element__value):
    # Creating Class Instance
    this = [0] * 4
    # Add Dispatch Table
    this[0] = __dtable____main____Element
    # Body
    #---------------------------------------------------------------------
    # Code Block
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
    stack.append(__field____main____Element____is_list)
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
    stack.append(__main____Element__Element__value)
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append(__field____main____Element____value)
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
    stack.append(__field____main____Element____list)
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
# End Constructor Declaration - __ctor____main____Element____Element__int
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Constructor Declaration - Element::Element(Vector<:Element:>) -> Element
def __ctor____main____Element____Element__Vector (__main____Element__Element__list):
    # Creating Class Instance
    this = [0] * 4
    # Add Dispatch Table
    this[0] = __dtable____main____Element
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(1)
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append(__field____main____Element____is_list)
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
    stack.append(__field____main____Element____value)
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
    stack.append(__main____Element__Element__list)
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append(__field____main____Element____list)
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
# End Constructor Declaration - __ctor____main____Element____Element__Vector
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Element::switch_to_list(Vector<:Element:>) -> void
def __method____main____Element____switch_to_list__Vector (this, __main____Element__switch_to_list__list):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(1)
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append(__field____main____Element____is_list)
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
    stack.append(__field____main____Element____value)
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
    stack.append(__main____Element__switch_to_list__list)
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append(__field____main____Element____list)
    __child = stack.pop()
    __parent = stack.pop()
    __rhs = stack.pop()
    __parent[__child] = __rhs
    stack.append (__parent[__child])
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
    return 0
# End Method Declaration - __method____main____Element____switch_to_list__Vector
#-------------------------------------------------------------------------

# Populate Dispatch Table
__dtable____main____Element = [__method____main____Element____switch_to_list__Vector]
# End Class Declaration - __main____Element
#=========================================================================

#=========================================================================
# Function Declaration - print(Element) -> void
def __main____print__Element (__main__print__e):
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
    stack.append(__main__print__e)
    # RHS
    stack.append (__field____main____Element____is_list)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __if__79__cond = stack.pop ()
    # get condition from stack
    if (__if__79__cond):
        # Body
        #-----------------------------------------------------------------
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

        #-----------------------------------------------------------------
        # If-Statement
        # Precomputing all if/elif conditions and give unique names
        # bc we can't have code between if and elif
        # Condition
        # Greater Than
        # LHS
        # Member Accessor
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__print__e)
        # RHS
        stack.append (__field____main____Element____list)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # RHS
        stack.append (__field____main____Vector__Element____size)
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
        __if__81__cond = stack.pop ()
        # get condition from stack
        if (__if__81__cond):
            # Body
            # Statement
            # Function Call - print(Element) -> void
            # Arguments
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__print__e)
            # RHS
            stack.append (__field____main____Element____list)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # RHS
            stack.append (__field____main____Vector__Element____data)
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
            __res = __main____print__Element (__arg0)
            stack.append (__res) # function call result
            # Statement results can be ignored
            stack.pop ()
            # End Statement

        # End of if
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # For-Loop
        # Init
        # Assignment - '='
        # RHS
        # Int Literal
        stack.append(1)
        # LHS
        __main__print__block__78__if__79__block__80__for__82__i = 0
        __rhs = stack.pop()
        __main__print__block__78__if__79__block__80__for__82__i = __rhs
        stack.append (__main__print__block__78__if__79__block__80__for__82__i)
        # Using an infinite loop so we can write a separate multi-line condition
        while (1):
            # Condition
            # Less Than
            # LHS
            stack.append(__main__print__block__78__if__79__block__80__for__82__i)
            # RHS
            # Member Accessor
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__print__e)
            # RHS
            stack.append (__field____main____Element____list)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # RHS
            stack.append (__field____main____Vector__Element____size)
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
            # Function Call - print(Element) -> void
            # Arguments
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__print__e)
            # RHS
            stack.append (__field____main____Element____list)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # RHS
            stack.append (__field____main____Vector__Element____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main__print__block__78__if__79__block__80__for__82__i)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            __arg0 = stack.pop ()
            # *** print
            __res = __main____print__Element (__arg0)
            stack.append (__res) # function call result
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            #-------------------------------------------------------------
            # Update
            # Pre-Increment
            # RHS
            stack.append(__main__print__block__78__if__79__block__80__for__82__i)
            __rhs = stack.pop ()
            __main__print__block__78__if__79__block__80__for__82__i = __main__print__block__78__if__79__block__80__for__82__i + 1
            __res = __main__print__block__78__if__79__block__80__for__82__i
            stack.append (__res)
        #-----------------------------------------------------------------
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

        # Return
        return
        #-----------------------------------------------------------------
    # End of if
    #---------------------------------------------------------------------
    # Statement
    # Function Call - print(int) -> void
    # Arguments
    # Member Accessor
    # LHS
    stack.append(__main__print__e)
    # RHS
    stack.append (__field____main____Element____value)
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
# End Function Declaration - __main____print__Element
#=========================================================================

#=========================================================================
# Class Template - 
#=========================================================================
# Class Declaration - __main____Pair__Element__int inherits __builtin____main__Object
# Creating Dispatch Table (will be populated later)
__dtable____main____Pair__Element__int = []
#-------------------------------------------------------------------------
# Field - Element Pair<:Element, int:>::a
__field____main____Pair__Element__int____a = 1
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Field - int Pair<:Element, int:>::b
__field____main____Pair__Element__int____b = 2
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Constructor Declaration - Pair<:Element, int:>::Pair(Element, int) -> Pair<:Element, int:>
def __ctor____main____Pair__Element__int____Pair__Element__int (__main____Pair__Element__int__Pair__a, __main____Pair__Element__int__Pair__b):
    # Creating Class Instance
    this = [0] * 3
    # Add Dispatch Table
    this[0] = __dtable____main____Pair__Element__int
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main____Pair__Element__int__Pair__a)
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append(__field____main____Pair__Element__int____a)
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
    stack.append(__main____Pair__Element__int__Pair__b)
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append(__field____main____Pair__Element__int____b)
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
# End Constructor Declaration - __ctor____main____Pair__Element__int____Pair__Element__int
#-------------------------------------------------------------------------

# Populate Dispatch Table
__dtable____main____Pair__Element__int = []
# End Class Declaration - __main____Pair__Element__int
#=========================================================================

# End Class Template - 
#=========================================================================

#=========================================================================
# Function Declaration - build_element(char[], int, int) -> Pair<:Element, int:>
def __main____build_element__char__1__int__int (__main__build_element__line, __main__build_element__i, __main__build_element__line_size):
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
    stack.append(__main__build_element__i)
    # RHS
    stack.append(__main__build_element__line_size)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs >= __rhs
    stack.append (__res)
    __if__86__cond = stack.pop ()
    # get condition from stack
    if (__if__86__cond):
        # Body
        # Return
        # Null Literal
        stack.append (None)
        __rVal = stack.pop ()
        return __rVal
    # End of if
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    # If-Statement
    # Precomputing all if/elif conditions and give unique names
    # bc we can't have code between if and elif
    # Condition
    # Equal
    # LHS
    # Subscript
    # LHS
    stack.append(__main__build_element__line)
    # OFFSET
    stack.append(__main__build_element__i)
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    # RHS
    # Char Literal
    stack.append('[')
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs == __rhs
    stack.append (__res)
    __if__87__cond = stack.pop ()
    # get condition from stack
    if (__if__87__cond):
        # Body
        #-----------------------------------------------------------------
        # Code Block
        # Statement
        # Pre-Increment
        # RHS
        stack.append(__main__build_element__i)
        __rhs = stack.pop ()
        __main__build_element__i = __main__build_element__i + 1
        __res = __main__build_element__i
        stack.append (__res)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Constructor Call - Vector<:Element:>::Vector() -> Vector<:Element:>
        # Arguments
        __retval = __ctor____main____Vector__Element____Vector ()
        stack.append (__retval)
        # LHS
        __main__build_element__block__85__if__87__block__88__sub_elements = 0
        __rhs = stack.pop()
        __main__build_element__block__85__if__87__block__88__sub_elements = __rhs
        stack.append (__main__build_element__block__85__if__87__block__88__sub_elements)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
        # While-Loop
        # Using an infinite loop so we can write a separate multi-line condition
        while (1):
            # Condition
            # Not Equal
            # LHS
            # Subscript
            # LHS
            stack.append(__main__build_element__line)
            # OFFSET
            stack.append(__main__build_element__i)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            # Char Literal
            stack.append(']')
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs != __rhs
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
            # Function Call - build_element(char[], int, int) -> Pair<:Element, int:>
            # Arguments
            stack.append(__main__build_element__line)
            stack.append(__main__build_element__i)
            stack.append(__main__build_element__line_size)
            __arg2 = stack.pop ()
            __arg1 = stack.pop ()
            __arg0 = stack.pop ()
            # *** build_element
            __res = __main____build_element__char__1__int__int (__arg0, __arg1, __arg2)
            stack.append (__res) # function call result
            # LHS
            __main__build_element__block__85__if__87__block__88__while__89__block__90__p = 0
            __rhs = stack.pop()
            __main__build_element__block__85__if__87__block__88__while__89__block__90__p = __rhs
            stack.append (__main__build_element__block__85__if__87__block__88__while__89__block__90__p)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            # Statement
            # Method Call - Vector<:Element:>::pushBack(Element) -> void
            # LHS
            stack.append(__main__build_element__block__85__if__87__block__88__sub_elements)
            # RHS
            # Arguments
            # Member Accessor
            # LHS
            stack.append(__main__build_element__block__85__if__87__block__88__while__89__block__90__p)
            # RHS
            stack.append (__field____main____Pair__Element__int____a)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            __arg0 = stack.pop ()
            __obj = stack.pop ()
            __retval = __method____main____Vector__Element____pushBack__Element (__obj, __arg0)
            stack.append (__retval)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            # Statement
            # Assignment - '='
            # RHS
            # Member Accessor
            # LHS
            stack.append(__main__build_element__block__85__if__87__block__88__while__89__block__90__p)
            # RHS
            stack.append (__field____main____Pair__Element__int____b)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            __rhs = stack.pop()
            __main__build_element__i = __rhs
            stack.append (__main__build_element__i)
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
            stack.append(__main__build_element__line)
            # OFFSET
            stack.append(__main__build_element__i)
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
            __if__91__cond = stack.pop ()
            # get condition from stack
            if (__if__91__cond):
                # Body
                # Statement
                # Pre-Increment
                # RHS
                stack.append(__main__build_element__i)
                __rhs = stack.pop ()
                __main__build_element__i = __main__build_element__i + 1
                __res = __main__build_element__i
                stack.append (__res)
                # Statement results can be ignored
                stack.pop ()
                # End Statement

            # End of if
            #-------------------------------------------------------------
            # Statement
            stack.append(__main__build_element__block__85__if__87__block__88__while__89__block__90__p)
            __arr = stack.pop ()
            __builtin__free (__arr)
            stack.append (0)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            #-------------------------------------------------------------
        # End of While
        #-----------------------------------------------------------------
        # Statement
        # Pre-Increment
        # RHS
        stack.append(__main__build_element__i)
        __rhs = stack.pop ()
        __main__build_element__i = __main__build_element__i + 1
        __res = __main__build_element__i
        stack.append (__res)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Assignment - '='
        # RHS
        # Constructor Call - Element::Element(Vector<:Element:>) -> Element
        # Arguments
        stack.append(__main__build_element__block__85__if__87__block__88__sub_elements)
        __arg0 = stack.pop ()
        __retval = __ctor____main____Element____Element__Vector (__arg0)
        stack.append (__retval)
        # LHS
        __main__build_element__block__85__if__87__block__88__e = 0
        __rhs = stack.pop()
        __main__build_element__block__85__if__87__block__88__e = __rhs
        stack.append (__main__build_element__block__85__if__87__block__88__e)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Return
        # Constructor Call - Pair<:Element, int:>::Pair(Element, int) -> Pair<:Element, int:>
        # Arguments
        stack.append(__main__build_element__block__85__if__87__block__88__e)
        stack.append(__main__build_element__i)
        __arg1 = stack.pop ()
        __arg0 = stack.pop ()
        __retval = __ctor____main____Pair__Element__int____Pair__Element__int (__arg0, __arg1)
        stack.append (__retval)
        __rVal = stack.pop ()
        return __rVal
        #-----------------------------------------------------------------
    # End of if
    #---------------------------------------------------------------------
    # Statement
    # Assignment - '='
    # RHS
    # Constructor Call - Vector<:char:>::Vector() -> Vector<:char:>
    # Arguments
    __retval = __ctor____main____Vector__char____Vector ()
    stack.append (__retval)
    # LHS
    __main__build_element__block__85__str = 0
    __rhs = stack.pop()
    __main__build_element__block__85__str = __rhs
    stack.append (__main__build_element__block__85__str)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
    # While-Loop
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Negate
        # RHS
        # OR
        # LHS
        # Equal
        # LHS
        # Subscript
        # LHS
        stack.append(__main__build_element__line)
        # OFFSET
        stack.append(__main__build_element__i)
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
        # RHS
        # Equal
        # LHS
        # Subscript
        # LHS
        stack.append(__main__build_element__line)
        # OFFSET
        stack.append(__main__build_element__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        # Char Literal
        stack.append(']')
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs == __rhs
        stack.append (__res)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs or __rhs
        stack.append (__res)
        __rhs = stack.pop ()
        __res = not __rhs
        stack.append (__res)
        __cond = stack.pop ()
        # break out of loop if condition is false
        if (__cond == 0): break
        # Body
        #-----------------------------------------------------------------
        # Code Block
        # Statement
        # Method Call - Vector<:char:>::pushBack(char) -> void
        # LHS
        stack.append(__main__build_element__block__85__str)
        # RHS
        # Arguments
        # Subscript
        # LHS
        stack.append(__main__build_element__line)
        # OFFSET
        stack.append(__main__build_element__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __arg0 = stack.pop ()
        __obj = stack.pop ()
        __retval = __method____main____Vector__char____pushBack__char (__obj, __arg0)
        stack.append (__retval)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Pre-Increment
        # RHS
        stack.append(__main__build_element__i)
        __rhs = stack.pop ()
        __main__build_element__i = __main__build_element__i + 1
        __res = __main__build_element__i
        stack.append (__res)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
    # End of While
    #---------------------------------------------------------------------
    # Statement
    # Method Call - Vector<:char:>::pushBack(char) -> void
    # LHS
    stack.append(__main__build_element__block__85__str)
    # RHS
    # Arguments
    # Char Literal
    stack.append('\0')
    __arg0 = stack.pop ()
    __obj = stack.pop ()
    __retval = __method____main____Vector__char____pushBack__char (__obj, __arg0)
    stack.append (__retval)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Function Call - stringToInt(char[]) -> int
    # Arguments
    # Member Accessor
    # LHS
    stack.append(__main__build_element__block__85__str)
    # RHS
    stack.append (__field____main____Vector__char____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __arg0 = stack.pop ()
    # *** stringToInt
    __res = __builtin__stringToInt__char__1 (__arg0)
    stack.append (__res) # function call result
    # LHS
    __main__build_element__block__85__value = 0
    __rhs = stack.pop()
    __main__build_element__block__85__value = __rhs
    stack.append (__main__build_element__block__85__value)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Return
    # Constructor Call - Pair<:Element, int:>::Pair(Element, int) -> Pair<:Element, int:>
    # Arguments
    # Constructor Call - Element::Element(int) -> Element
    # Arguments
    stack.append(__main__build_element__block__85__value)
    __arg0 = stack.pop ()
    __retval = __ctor____main____Element____Element__int (__arg0)
    stack.append (__retval)
    stack.append(__main__build_element__i)
    __arg1 = stack.pop ()
    __arg0 = stack.pop ()
    __retval = __ctor____main____Pair__Element__int____Pair__Element__int (__arg0, __arg1)
    stack.append (__retval)
    __rVal = stack.pop ()
    return __rVal
    #---------------------------------------------------------------------
# End Function Declaration - __main____build_element__char__1__int__int
#=========================================================================

# Statement
# Assignment - '='
# RHS
# Int Literal
stack.append(1)
# LHS
__main__RIGHT_ORDER = 0
__rhs = stack.pop()
__main__RIGHT_ORDER = __rhs
stack.append (__main__RIGHT_ORDER)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Assignment - '='
# RHS
# Negative
# RHS
# Int Literal
stack.append(1)
__rhs = stack.pop ()
__res = -__rhs
stack.append (__res)
# LHS
__main__CONTINUE = 0
__rhs = stack.pop()
__main__CONTINUE = __rhs
stack.append (__main__CONTINUE)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Assignment - '='
# RHS
# Int Literal
stack.append(0)
# LHS
__main__WRONG_ORDER = 0
__rhs = stack.pop()
__main__WRONG_ORDER = __rhs
stack.append (__main__WRONG_ORDER)
# Statement results can be ignored
stack.pop ()
# End Statement

#=========================================================================
# Function Declaration - is_correct_order(Element, Element) -> int
def __main____is_correct_order__Element__Element (__main__is_correct_order__a, __main__is_correct_order__b):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(1)
    # LHS
    __main__is_correct_order__block__94__RIGHT_ORDER = 0
    __rhs = stack.pop()
    __main__is_correct_order__block__94__RIGHT_ORDER = __rhs
    stack.append (__main__is_correct_order__block__94__RIGHT_ORDER)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Negative
    # RHS
    # Int Literal
    stack.append(1)
    __rhs = stack.pop ()
    __res = -__rhs
    stack.append (__res)
    # LHS
    __main__is_correct_order__block__94__CONTINUE = 0
    __rhs = stack.pop()
    __main__is_correct_order__block__94__CONTINUE = __rhs
    stack.append (__main__is_correct_order__block__94__CONTINUE)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(0)
    # LHS
    __main__is_correct_order__block__94__WRONG_ORDER = 0
    __rhs = stack.pop()
    __main__is_correct_order__block__94__WRONG_ORDER = __rhs
    stack.append (__main__is_correct_order__block__94__WRONG_ORDER)
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
    # Negate
    # RHS
    # Member Accessor
    # LHS
    stack.append(__main__is_correct_order__a)
    # RHS
    stack.append (__field____main____Element____is_list)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __rhs = stack.pop ()
    __res = not __rhs
    stack.append (__res)
    # RHS
    # Negate
    # RHS
    # Member Accessor
    # LHS
    stack.append(__main__is_correct_order__b)
    # RHS
    stack.append (__field____main____Element____is_list)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __rhs = stack.pop ()
    __res = not __rhs
    stack.append (__res)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs and __rhs
    stack.append (__res)
    __if__95__cond = stack.pop ()
    # get condition from stack
    if (__if__95__cond):
        # Body
        #-----------------------------------------------------------------
        # Code Block
        #-----------------------------------------------------------------
        # If-Statement
        # Precomputing all if/elif conditions and give unique names
        # bc we can't have code between if and elif
        # Condition
        # Less Than
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__is_correct_order__a)
        # RHS
        stack.append (__field____main____Element____value)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # RHS
        # Member Accessor
        # LHS
        stack.append(__main__is_correct_order__b)
        # RHS
        stack.append (__field____main____Element____value)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs < __rhs
        stack.append (__res)
        __if__97__cond = stack.pop ()
        # Condition for elif #0
        # Greater Than
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__is_correct_order__a)
        # RHS
        stack.append (__field____main____Element____value)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # RHS
        # Member Accessor
        # LHS
        stack.append(__main__is_correct_order__b)
        # RHS
        stack.append (__field____main____Element____value)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs > __rhs
        stack.append (__res)
        __elif__97x0__cond = stack.pop ()
        # get condition from stack
        if (__if__97__cond):
            # Body
            # Return
            stack.append(__main__is_correct_order__block__94__RIGHT_ORDER)
            __rVal = stack.pop ()
            return __rVal
        #-----------------------------------------------------------------
        # Elif-Statement
        # Condition
        elif (__elif__97x0__cond):
            # Body
            # Return
            stack.append(__main__is_correct_order__block__94__WRONG_ORDER)
            __rVal = stack.pop ()
            return __rVal
        #-----------------------------------------------------------------
        # End of if
        #-----------------------------------------------------------------
        # Return
        stack.append(__main__is_correct_order__block__94__CONTINUE)
        __rVal = stack.pop ()
        return __rVal
        #-----------------------------------------------------------------
    # End of if
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    # If-Statement
    # Precomputing all if/elif conditions and give unique names
    # bc we can't have code between if and elif
    # Condition
    # AND
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main__is_correct_order__a)
    # RHS
    stack.append (__field____main____Element____is_list)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # RHS
    # Member Accessor
    # LHS
    stack.append(__main__is_correct_order__b)
    # RHS
    stack.append (__field____main____Element____is_list)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs and __rhs
    stack.append (__res)
    __if__98__cond = stack.pop ()
    # get condition from stack
    if (__if__98__cond):
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
        __main__is_correct_order__block__94__if__98__block__99__for__100__i = 0
        __rhs = stack.pop()
        __main__is_correct_order__block__94__if__98__block__99__for__100__i = __rhs
        stack.append (__main__is_correct_order__block__94__if__98__block__99__for__100__i)
        # Using an infinite loop so we can write a separate multi-line condition
        while (1):
            # Condition
            # AND
            # LHS
            # Less Than
            # LHS
            stack.append(__main__is_correct_order__block__94__if__98__block__99__for__100__i)
            # RHS
            # Member Accessor
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__is_correct_order__a)
            # RHS
            stack.append (__field____main____Element____list)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # RHS
            stack.append (__field____main____Vector__Element____size)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs < __rhs
            stack.append (__res)
            # RHS
            # Less Than
            # LHS
            stack.append(__main__is_correct_order__block__94__if__98__block__99__for__100__i)
            # RHS
            # Member Accessor
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__is_correct_order__b)
            # RHS
            stack.append (__field____main____Element____list)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # RHS
            stack.append (__field____main____Vector__Element____size)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs < __rhs
            stack.append (__res)
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs and __rhs
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
            # Function Call - is_correct_order(Element, Element) -> int
            # Arguments
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__is_correct_order__a)
            # RHS
            stack.append (__field____main____Element____list)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # RHS
            stack.append (__field____main____Vector__Element____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main__is_correct_order__block__94__if__98__block__99__for__100__i)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__is_correct_order__b)
            # RHS
            stack.append (__field____main____Element____list)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # RHS
            stack.append (__field____main____Vector__Element____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main__is_correct_order__block__94__if__98__block__99__for__100__i)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            __arg1 = stack.pop ()
            __arg0 = stack.pop ()
            # *** is_correct_order
            __res = __main____is_correct_order__Element__Element (__arg0, __arg1)
            stack.append (__res) # function call result
            # LHS
            __main__is_correct_order__block__94__if__98__block__99__for__100__block__101__res = 0
            __rhs = stack.pop()
            __main__is_correct_order__block__94__if__98__block__99__for__100__block__101__res = __rhs
            stack.append (__main__is_correct_order__block__94__if__98__block__99__for__100__block__101__res)
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
            stack.append(__main__is_correct_order__block__94__if__98__block__99__for__100__block__101__res)
            # RHS
            stack.append(__main__is_correct_order__block__94__RIGHT_ORDER)
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs == __rhs
            stack.append (__res)
            __if__102__cond = stack.pop ()
            # get condition from stack
            if (__if__102__cond):
                # Body
                # Return
                stack.append(__main__is_correct_order__block__94__RIGHT_ORDER)
                __rVal = stack.pop ()
                return __rVal
            # End of if
            #-------------------------------------------------------------
            #-------------------------------------------------------------
            # If-Statement
            # Precomputing all if/elif conditions and give unique names
            # bc we can't have code between if and elif
            # Condition
            # Equal
            # LHS
            stack.append(__main__is_correct_order__block__94__if__98__block__99__for__100__block__101__res)
            # RHS
            stack.append(__main__is_correct_order__block__94__WRONG_ORDER)
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs == __rhs
            stack.append (__res)
            __if__103__cond = stack.pop ()
            # get condition from stack
            if (__if__103__cond):
                # Body
                # Return
                stack.append(__main__is_correct_order__block__94__WRONG_ORDER)
                __rVal = stack.pop ()
                return __rVal
            # End of if
            #-------------------------------------------------------------
            #-------------------------------------------------------------
            # Update
            # Pre-Increment
            # RHS
            stack.append(__main__is_correct_order__block__94__if__98__block__99__for__100__i)
            __rhs = stack.pop ()
            __main__is_correct_order__block__94__if__98__block__99__for__100__i = __main__is_correct_order__block__94__if__98__block__99__for__100__i + 1
            __res = __main__is_correct_order__block__94__if__98__block__99__for__100__i
            stack.append (__res)
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # If-Statement
        # Precomputing all if/elif conditions and give unique names
        # bc we can't have code between if and elif
        # Condition
        # Less Than
        # LHS
        # Member Accessor
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__is_correct_order__a)
        # RHS
        stack.append (__field____main____Element____list)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # RHS
        stack.append (__field____main____Vector__Element____size)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # RHS
        # Member Accessor
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__is_correct_order__b)
        # RHS
        stack.append (__field____main____Element____list)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # RHS
        stack.append (__field____main____Vector__Element____size)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs < __rhs
        stack.append (__res)
        __if__104__cond = stack.pop ()
        # get condition from stack
        if (__if__104__cond):
            # Body
            # Return
            stack.append(__main__is_correct_order__block__94__RIGHT_ORDER)
            __rVal = stack.pop ()
            return __rVal
        # End of if
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # If-Statement
        # Precomputing all if/elif conditions and give unique names
        # bc we can't have code between if and elif
        # Condition
        # Greater Than
        # LHS
        # Member Accessor
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__is_correct_order__a)
        # RHS
        stack.append (__field____main____Element____list)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # RHS
        stack.append (__field____main____Vector__Element____size)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # RHS
        # Member Accessor
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__is_correct_order__b)
        # RHS
        stack.append (__field____main____Element____list)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # RHS
        stack.append (__field____main____Vector__Element____size)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs > __rhs
        stack.append (__res)
        __if__105__cond = stack.pop ()
        # get condition from stack
        if (__if__105__cond):
            # Body
            # Return
            stack.append(__main__is_correct_order__block__94__WRONG_ORDER)
            __rVal = stack.pop ()
            return __rVal
        # End of if
        #-----------------------------------------------------------------
        # Return
        stack.append(__main__is_correct_order__block__94__CONTINUE)
        __rVal = stack.pop ()
        return __rVal
        #-----------------------------------------------------------------
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
    stack.append(__main__is_correct_order__a)
    # RHS
    stack.append (__field____main____Element____is_list)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __rhs = stack.pop ()
    __res = not __rhs
    stack.append (__res)
    __if__106__cond = stack.pop ()
    # get condition from stack
    if (__if__106__cond):
        # Body
        #-----------------------------------------------------------------
        # Code Block
        # Statement
        # Assignment - '='
        # RHS
        # Constructor Call - Element::Element(int) -> Element
        # Arguments
        # Member Accessor
        # LHS
        stack.append(__main__is_correct_order__a)
        # RHS
        stack.append (__field____main____Element____value)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        __arg0 = stack.pop ()
        __retval = __ctor____main____Element____Element__int (__arg0)
        stack.append (__retval)
        # LHS
        __main__is_correct_order__block__94__if__106__block__107__newnum = 0
        __rhs = stack.pop()
        __main__is_correct_order__block__94__if__106__block__107__newnum = __rhs
        stack.append (__main__is_correct_order__block__94__if__106__block__107__newnum)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Method Call - Element::switch_to_list(Vector<:Element:>) -> void
        # LHS
        stack.append(__main__is_correct_order__a)
        # RHS
        # Arguments
        # Constructor Call - Vector<:Element:>::Vector() -> Vector<:Element:>
        # Arguments
        __retval = __ctor____main____Vector__Element____Vector ()
        stack.append (__retval)
        __arg0 = stack.pop ()
        __obj = stack.pop ()
        __retval = __method____main____Element____switch_to_list__Vector (__obj, __arg0)
        stack.append (__retval)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Method Call - Vector<:Element:>::pushBack(Element) -> void
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__is_correct_order__a)
        # RHS
        stack.append (__field____main____Element____list)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # RHS
        # Arguments
        stack.append(__main__is_correct_order__block__94__if__106__block__107__newnum)
        __arg0 = stack.pop ()
        __obj = stack.pop ()
        __retval = __method____main____Vector__Element____pushBack__Element (__obj, __arg0)
        stack.append (__retval)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
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
    stack.append(__main__is_correct_order__b)
    # RHS
    stack.append (__field____main____Element____is_list)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __rhs = stack.pop ()
    __res = not __rhs
    stack.append (__res)
    __if__108__cond = stack.pop ()
    # get condition from stack
    if (__if__108__cond):
        # Body
        #-----------------------------------------------------------------
        # Code Block
        # Statement
        # Assignment - '='
        # RHS
        # Constructor Call - Element::Element(int) -> Element
        # Arguments
        # Member Accessor
        # LHS
        stack.append(__main__is_correct_order__b)
        # RHS
        stack.append (__field____main____Element____value)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        __arg0 = stack.pop ()
        __retval = __ctor____main____Element____Element__int (__arg0)
        stack.append (__retval)
        # LHS
        __main__is_correct_order__block__94__if__108__block__109__newnum = 0
        __rhs = stack.pop()
        __main__is_correct_order__block__94__if__108__block__109__newnum = __rhs
        stack.append (__main__is_correct_order__block__94__if__108__block__109__newnum)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Method Call - Element::switch_to_list(Vector<:Element:>) -> void
        # LHS
        stack.append(__main__is_correct_order__b)
        # RHS
        # Arguments
        # Constructor Call - Vector<:Element:>::Vector() -> Vector<:Element:>
        # Arguments
        __retval = __ctor____main____Vector__Element____Vector ()
        stack.append (__retval)
        __arg0 = stack.pop ()
        __obj = stack.pop ()
        __retval = __method____main____Element____switch_to_list__Vector (__obj, __arg0)
        stack.append (__retval)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Method Call - Vector<:Element:>::pushBack(Element) -> void
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__is_correct_order__b)
        # RHS
        stack.append (__field____main____Element____list)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # RHS
        # Arguments
        stack.append(__main__is_correct_order__block__94__if__108__block__109__newnum)
        __arg0 = stack.pop ()
        __obj = stack.pop ()
        __retval = __method____main____Vector__Element____pushBack__Element (__obj, __arg0)
        stack.append (__retval)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
    # End of if
    #---------------------------------------------------------------------
    # Return
    # Function Call - is_correct_order(Element, Element) -> int
    # Arguments
    stack.append(__main__is_correct_order__a)
    stack.append(__main__is_correct_order__b)
    __arg1 = stack.pop ()
    __arg0 = stack.pop ()
    # *** is_correct_order
    __res = __main____is_correct_order__Element__Element (__arg0, __arg1)
    stack.append (__res) # function call result
    __rVal = stack.pop ()
    return __rVal
    #---------------------------------------------------------------------
# End Function Declaration - __main____is_correct_order__Element__Element
#=========================================================================

# Statement
# Assignment - '='
# RHS
# Int Literal
stack.append(1)
# LHS
__main__pair_index = 0
__rhs = stack.pop()
__main__pair_index = __rhs
stack.append (__main__pair_index)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Assignment - '='
# RHS
# Int Literal
stack.append(0)
# LHS
__main__pair_sum = 0
__rhs = stack.pop()
__main__pair_sum = __rhs
stack.append (__main__pair_sum)
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
__main__for__110__l = 0
__rhs = stack.pop()
__main__for__110__l = __rhs
stack.append (__main__for__110__l)
# Using an infinite loop so we can write a separate multi-line condition
while (1):
    # Condition
    # Less Than
    # LHS
    stack.append(__main__for__110__l)
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
    # Function Call - build_element(char[], int, int) -> Pair<:Element, int:>
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
    stack.append(__main__for__110__l)
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
    stack.append(__main__lines)
    # RHS
    stack.append (__field____main____Vector__char__1____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    # Addition
    # LHS
    stack.append(__main__for__110__l)
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
    # *** build_element
    __res = __main____build_element__char__1__int__int (__arg0, __arg1, __arg2)
    stack.append (__res) # function call result
    # LHS
    __main__for__110__block__111__p0 = 0
    __rhs = stack.pop()
    __main__for__110__block__111__p0 = __rhs
    stack.append (__main__for__110__block__111__p0)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Function Call - build_element(char[], int, int) -> Pair<:Element, int:>
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
    stack.append(__main__for__110__l)
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
    stack.append(0)
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
    # Addition
    # LHS
    stack.append(__main__for__110__l)
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
    # *** build_element
    __res = __main____build_element__char__1__int__int (__arg0, __arg1, __arg2)
    stack.append (__res) # function call result
    # LHS
    __main__for__110__block__111__p1 = 0
    __rhs = stack.pop()
    __main__for__110__block__111__p1 = __rhs
    stack.append (__main__for__110__block__111__p1)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Function Call - is_correct_order(Element, Element) -> int
    # Arguments
    # Member Accessor
    # LHS
    stack.append(__main__for__110__block__111__p0)
    # RHS
    stack.append (__field____main____Pair__Element__int____a)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # Member Accessor
    # LHS
    stack.append(__main__for__110__block__111__p1)
    # RHS
    stack.append (__field____main____Pair__Element__int____a)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __arg1 = stack.pop ()
    __arg0 = stack.pop ()
    # *** is_correct_order
    __res = __main____is_correct_order__Element__Element (__arg0, __arg1)
    stack.append (__res) # function call result
    # LHS
    __main__for__110__block__111__res = 0
    __rhs = stack.pop()
    __main__for__110__block__111__res = __rhs
    stack.append (__main__for__110__block__111__res)
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
    stack.append(__main__for__110__block__111__res)
    # RHS
    stack.append(__main__RIGHT_ORDER)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs == __rhs
    stack.append (__res)
    __if__112__cond = stack.pop ()
    # get condition from stack
    if (__if__112__cond):
        # Body
        # Statement
        # Assignment - '+='
        # RHS
        stack.append(__main__pair_index)
        __rhs = stack.pop()
        __main__pair_sum = __main__pair_sum + __rhs
        stack.append (__main__pair_sum)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

    # End of if
    #---------------------------------------------------------------------
    # Statement
    # Post-Increment
    __res = __main__pair_index
    __main__pair_index = __main__pair_index + 1
    stack.append (__res)
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
    __main__for__110__l = __main__for__110__l + __rhs
    stack.append (__main__for__110__l)
#-------------------------------------------------------------------------
# Statement
# Function Call - println(int) -> void
# Arguments
stack.append(__main__pair_sum)
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

