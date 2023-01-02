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
# Class Declaration - __main____Vector__Vector inherits __builtin____main__Object
# Creating Dispatch Table (will be populated later)
__dtable____main____Vector__Vector = []
#-------------------------------------------------------------------------
# Field - Vector<:int:>[] Vector<:Vector<:int:>:>::data
__field____main____Vector__Vector____data = 1
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Field - int Vector<:Vector<:int:>:>::size
__field____main____Vector__Vector____size = 2
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Field - int Vector<:Vector<:int:>:>::capacity
__field____main____Vector__Vector____capacity = 3
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Constructor Declaration - Vector<:Vector<:int:>:>::Vector() -> Vector<:Vector<:int:>:>
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
# Constructor Declaration - Vector<:Vector<:int:>:>::Vector(int) -> Vector<:Vector<:int:>:>
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
# Method Declaration - Vector<:Vector<:int:>:>::pushBack(Vector<:int:>) -> void
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
        __main____Vector__Vector__pushBack__block__14__if__15__block__16__nData = 0
        __rhs = stack.pop()
        __main____Vector__Vector__pushBack__block__14__if__15__block__16__nData = __rhs
        stack.append (__main____Vector__Vector__pushBack__block__14__if__15__block__16__nData)
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
        __main____Vector__Vector__pushBack__block__14__if__15__block__16__for__17__i = 0
        __rhs = stack.pop()
        __main____Vector__Vector__pushBack__block__14__if__15__block__16__for__17__i = __rhs
        stack.append (__main____Vector__Vector__pushBack__block__14__if__15__block__16__for__17__i)
        # Using an infinite loop so we can write a separate multi-line condition
        while (1):
            # Condition
            # Less Than
            # LHS
            stack.append(__main____Vector__Vector__pushBack__block__14__if__15__block__16__for__17__i)
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
            stack.append(__main____Vector__Vector__pushBack__block__14__if__15__block__16__for__17__i)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # LHS
            # Subscript assignment
            # LHS
            stack.append(__main____Vector__Vector__pushBack__block__14__if__15__block__16__nData)
            # OFFSET
            stack.append(__main____Vector__Vector__pushBack__block__14__if__15__block__16__for__17__i)
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
            stack.append(__main____Vector__Vector__pushBack__block__14__if__15__block__16__for__17__i)
            __rhs = stack.pop ()
            __main____Vector__Vector__pushBack__block__14__if__15__block__16__for__17__i = __main____Vector__Vector__pushBack__block__14__if__15__block__16__for__17__i + 1
            __res = __main____Vector__Vector__pushBack__block__14__if__15__block__16__for__17__i
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
        stack.append(__main____Vector__Vector__pushBack__block__14__if__15__block__16__nData)
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
# Method Declaration - Vector<:Vector<:int:>:>::popBack() -> Vector<:int:>
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
# Method Declaration - Vector<:Vector<:int:>:>::clear() -> void
def __method____main____Vector__Vector____clear (this):
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
        stack.append (__field____main____Vector__Vector____size)
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
        # Method Call - Vector<:Vector<:int:>:>::popBack() -> Vector<:int:>
        # LHS
        stack.append(this)
        # RHS
        # Arguments
        __obj = stack.pop ()
        __retval = __method____main____Vector__Vector____popBack (__obj)
        stack.append (__retval)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

    # End of While
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    return 0
# End Method Declaration - __method____main____Vector__Vector____clear
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - Vector<:Vector<:int:>:>::get(int) -> Vector<:int:>
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
# Method Declaration - Vector<:Vector<:int:>:>::set(int, Vector<:int:>) -> void
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
__dtable____main____Vector__Vector = [__method____main____Vector__Vector____pushBack__Vector, __method____main____Vector__Vector____popBack, __method____main____Vector__Vector____clear, __method____main____Vector__Vector____get__int, __method____main____Vector__Vector____set__int__Vector]
# End Class Declaration - __main____Vector__Vector
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
        __main____Vector__int__pushBack__block__26__if__27__block__28__nData = 0
        __rhs = stack.pop()
        __main____Vector__int__pushBack__block__26__if__27__block__28__nData = __rhs
        stack.append (__main____Vector__int__pushBack__block__26__if__27__block__28__nData)
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
        __main____Vector__int__pushBack__block__26__if__27__block__28__for__29__i = 0
        __rhs = stack.pop()
        __main____Vector__int__pushBack__block__26__if__27__block__28__for__29__i = __rhs
        stack.append (__main____Vector__int__pushBack__block__26__if__27__block__28__for__29__i)
        # Using an infinite loop so we can write a separate multi-line condition
        while (1):
            # Condition
            # Less Than
            # LHS
            stack.append(__main____Vector__int__pushBack__block__26__if__27__block__28__for__29__i)
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
            stack.append(__main____Vector__int__pushBack__block__26__if__27__block__28__for__29__i)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # LHS
            # Subscript assignment
            # LHS
            stack.append(__main____Vector__int__pushBack__block__26__if__27__block__28__nData)
            # OFFSET
            stack.append(__main____Vector__int__pushBack__block__26__if__27__block__28__for__29__i)
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
            stack.append(__main____Vector__int__pushBack__block__26__if__27__block__28__for__29__i)
            __rhs = stack.pop ()
            __main____Vector__int__pushBack__block__26__if__27__block__28__for__29__i = __main____Vector__int__pushBack__block__26__if__27__block__28__for__29__i + 1
            __res = __main____Vector__int__pushBack__block__26__if__27__block__28__for__29__i
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
        stack.append(__main____Vector__int__pushBack__block__26__if__27__block__28__nData)
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
# Class Declaration - __main____Vec inherits __builtin____main__Object
# Creating Dispatch Table (will be populated later)
__dtable____main____Vec = []
#-------------------------------------------------------------------------
# Field - int Vec::i
__field____main____Vec____i = 1
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Field - int Vec::j
__field____main____Vec____j = 2
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Field - int Vec::time
__field____main____Vec____time = 3
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Constructor Declaration - Vec::Vec() -> Vec
def __ctor____main____Vec____Vec ():
    # Creating Class Instance
    this = [0] * 4
    # Add Dispatch Table
    this[0] = __dtable____main____Vec
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
    stack.append(__field____main____Vec____i)
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
    stack.append(__field____main____Vec____j)
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
    stack.append(__field____main____Vec____time)
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
# End Constructor Declaration - __ctor____main____Vec____Vec
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Constructor Declaration - Vec::Vec(int, int) -> Vec
def __ctor____main____Vec____Vec__int__int (__main____Vec__Vec__i, __main____Vec__Vec__j):
    # Creating Class Instance
    this = [0] * 4
    # Add Dispatch Table
    this[0] = __dtable____main____Vec
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main____Vec__Vec__i)
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append(__field____main____Vec____i)
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
    stack.append(__main____Vec__Vec__j)
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append(__field____main____Vec____j)
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
    stack.append(__field____main____Vec____time)
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
# End Constructor Declaration - __ctor____main____Vec____Vec__int__int
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Constructor Declaration - Vec::Vec(int, int, int) -> Vec
def __ctor____main____Vec____Vec__int__int__int (__main____Vec__Vec__i, __main____Vec__Vec__j, __main____Vec__Vec__time):
    # Creating Class Instance
    this = [0] * 4
    # Add Dispatch Table
    this[0] = __dtable____main____Vec
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main____Vec__Vec__i)
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append(__field____main____Vec____i)
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
    stack.append(__main____Vec__Vec__j)
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append(__field____main____Vec____j)
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
    stack.append(__main____Vec__Vec__time)
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append(__field____main____Vec____time)
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
# End Constructor Declaration - __ctor____main____Vec____Vec__int__int__int
#-------------------------------------------------------------------------

# Populate Dispatch Table
__dtable____main____Vec = []
# End Class Declaration - __main____Vec
#=========================================================================

#=========================================================================
# Function Declaration - print(Vec) -> void
def __main____print__Vec (__main__print__p):
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
    stack.append (__field____main____Vec____i)
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
    stack.append (__field____main____Vec____j)
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
# End Function Declaration - __main____print__Vec
#=========================================================================

#=========================================================================
# Function Declaration - println(Vec) -> void
def __main____println__Vec (__main__println__p):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Function Call - print(Vec) -> void
    # Arguments
    stack.append(__main__println__p)
    __arg0 = stack.pop ()
    # *** print
    __res = __main____print__Vec (__arg0)
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
# End Function Declaration - __main____println__Vec
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
# Class Template - 
#=========================================================================
# Class Declaration - __main____Node__Vec inherits __builtin____main__Object
# Creating Dispatch Table (will be populated later)
__dtable____main____Node__Vec = []
#-------------------------------------------------------------------------
# Field - Vec Node<:Vec:>::data
__field____main____Node__Vec____data = 1
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Field - Node<:Vec:> Node<:Vec:>::prev
__field____main____Node__Vec____prev = 2
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Field - Node<:Vec:> Node<:Vec:>::next
__field____main____Node__Vec____next = 3
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Constructor Declaration - Node<:Vec:>::Node(Vec, Node<:Vec:>, Node<:Vec:>) -> Node<:Vec:>
def __ctor____main____Node__Vec____Node__Vec__Node__Node (__main____Node__Vec__Node__data, __main____Node__Vec__Node__prev, __main____Node__Vec__Node__next):
    # Creating Class Instance
    this = [0] * 4
    # Add Dispatch Table
    this[0] = __dtable____main____Node__Vec
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main____Node__Vec__Node__data)
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append(__field____main____Node__Vec____data)
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
    stack.append(__main____Node__Vec__Node__prev)
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append(__field____main____Node__Vec____prev)
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
    stack.append(__main____Node__Vec__Node__next)
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append(__field____main____Node__Vec____next)
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
# End Constructor Declaration - __ctor____main____Node__Vec____Node__Vec__Node__Node
#-------------------------------------------------------------------------

# Populate Dispatch Table
__dtable____main____Node__Vec = []
# End Class Declaration - __main____Node__Vec
#=========================================================================

# End Class Template - 
#=========================================================================

#=========================================================================
# Class Template - 
#=========================================================================
# Class Declaration - __main____LinkedList__Vec inherits __builtin____main__Object
# Creating Dispatch Table (will be populated later)
__dtable____main____LinkedList__Vec = []
#-------------------------------------------------------------------------
# Field - Node<:Vec:> LinkedList<:Vec:>::header
__field____main____LinkedList__Vec____header = 1
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Field - int LinkedList<:Vec:>::size
__field____main____LinkedList__Vec____size = 2
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Constructor Declaration - LinkedList<:Vec:>::LinkedList() -> LinkedList<:Vec:>
def __ctor____main____LinkedList__Vec____LinkedList ():
    # Creating Class Instance
    this = [0] * 3
    # Add Dispatch Table
    this[0] = __dtable____main____LinkedList__Vec
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Assignment - '='
    # RHS
    # Constructor Call - Node<:Vec:>::Node(Vec, Node<:Vec:>, Node<:Vec:>) -> Node<:Vec:>
    # Arguments
    # Function Call - Vec::Vec() -> Vec
    # Arguments
    # *** Vec::Vec
    __res = __ctor____main____Vec____Vec ()
    stack.append (__res) # function call result
    # Null Literal
    stack.append (None)
    # Null Literal
    stack.append (None)
    __arg2 = stack.pop ()
    __arg1 = stack.pop ()
    __arg0 = stack.pop ()
    __retval = __ctor____main____Node__Vec____Node__Vec__Node__Node (__arg0, __arg1, __arg2)
    stack.append (__retval)
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append(__field____main____LinkedList__Vec____header)
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
    stack.append (__field____main____LinkedList__Vec____header)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # LHS
    # Member Accessor Assignment
    # LHS
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____LinkedList__Vec____header)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # RHS
    stack.append(__field____main____Node__Vec____next)
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
    stack.append (__field____main____LinkedList__Vec____header)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # LHS
    # Member Accessor Assignment
    # LHS
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____LinkedList__Vec____header)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # RHS
    stack.append(__field____main____Node__Vec____prev)
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
    stack.append(__field____main____LinkedList__Vec____size)
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
# End Constructor Declaration - __ctor____main____LinkedList__Vec____LinkedList
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - LinkedList<:Vec:>::pushBack(Vec) -> void
def __method____main____LinkedList__Vec____pushBack__Vec (this, __main____LinkedList__Vec__pushBack__val):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Assignment - '='
    # RHS
    # Member Accessor
    # LHS
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____LinkedList__Vec____header)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # RHS
    stack.append (__field____main____Node__Vec____prev)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # LHS
    __main____LinkedList__Vec__pushBack__block__83__tail = 0
    __rhs = stack.pop()
    __main____LinkedList__Vec__pushBack__block__83__tail = __rhs
    stack.append (__main____LinkedList__Vec__pushBack__block__83__tail)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Constructor Call - Node<:Vec:>::Node(Vec, Node<:Vec:>, Node<:Vec:>) -> Node<:Vec:>
    # Arguments
    stack.append(__main____LinkedList__Vec__pushBack__val)
    stack.append(__main____LinkedList__Vec__pushBack__block__83__tail)
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____LinkedList__Vec____header)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __arg2 = stack.pop ()
    __arg1 = stack.pop ()
    __arg0 = stack.pop ()
    __retval = __ctor____main____Node__Vec____Node__Vec__Node__Node (__arg0, __arg1, __arg2)
    stack.append (__retval)
    # LHS
    __main____LinkedList__Vec__pushBack__block__83__node = 0
    __rhs = stack.pop()
    __main____LinkedList__Vec__pushBack__block__83__node = __rhs
    stack.append (__main____LinkedList__Vec__pushBack__block__83__node)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main____LinkedList__Vec__pushBack__block__83__node)
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(__main____LinkedList__Vec__pushBack__block__83__tail)
    # RHS
    stack.append(__field____main____Node__Vec____next)
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
    stack.append(__main____LinkedList__Vec__pushBack__block__83__node)
    # LHS
    # Member Accessor Assignment
    # LHS
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____LinkedList__Vec____header)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # RHS
    stack.append(__field____main____Node__Vec____prev)
    __child = stack.pop()
    __parent = stack.pop()
    __rhs = stack.pop()
    __parent[__child] = __rhs
    stack.append (__parent[__child])
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
    stack.append (__field____main____LinkedList__Vec____size)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __rhs = stack.pop ()
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____LinkedList__Vec____size)
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
# End Method Declaration - __method____main____LinkedList__Vec____pushBack__Vec
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - LinkedList<:Vec:>::pushFront(Vec) -> void
def __method____main____LinkedList__Vec____pushFront__Vec (this, __main____LinkedList__Vec__pushFront__val):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Assignment - '='
    # RHS
    # Member Accessor
    # LHS
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____LinkedList__Vec____header)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # RHS
    stack.append (__field____main____Node__Vec____next)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # LHS
    __main____LinkedList__Vec__pushFront__block__84__head = 0
    __rhs = stack.pop()
    __main____LinkedList__Vec__pushFront__block__84__head = __rhs
    stack.append (__main____LinkedList__Vec__pushFront__block__84__head)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Constructor Call - Node<:Vec:>::Node(Vec, Node<:Vec:>, Node<:Vec:>) -> Node<:Vec:>
    # Arguments
    stack.append(__main____LinkedList__Vec__pushFront__val)
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____LinkedList__Vec____header)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    stack.append(__main____LinkedList__Vec__pushFront__block__84__head)
    __arg2 = stack.pop ()
    __arg1 = stack.pop ()
    __arg0 = stack.pop ()
    __retval = __ctor____main____Node__Vec____Node__Vec__Node__Node (__arg0, __arg1, __arg2)
    stack.append (__retval)
    # LHS
    __main____LinkedList__Vec__pushFront__block__84__node = 0
    __rhs = stack.pop()
    __main____LinkedList__Vec__pushFront__block__84__node = __rhs
    stack.append (__main____LinkedList__Vec__pushFront__block__84__node)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main____LinkedList__Vec__pushFront__block__84__node)
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(__main____LinkedList__Vec__pushFront__block__84__head)
    # RHS
    stack.append(__field____main____Node__Vec____prev)
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
    stack.append(__main____LinkedList__Vec__pushFront__block__84__node)
    # LHS
    # Member Accessor Assignment
    # LHS
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____LinkedList__Vec____header)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # RHS
    stack.append(__field____main____Node__Vec____next)
    __child = stack.pop()
    __parent = stack.pop()
    __rhs = stack.pop()
    __parent[__child] = __rhs
    stack.append (__parent[__child])
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
    stack.append (__field____main____LinkedList__Vec____size)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __rhs = stack.pop ()
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____LinkedList__Vec____size)
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
# End Method Declaration - __method____main____LinkedList__Vec____pushFront__Vec
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - LinkedList<:Vec:>::popBack() -> Vec
def __method____main____LinkedList__Vec____popBack (this):
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
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____LinkedList__Vec____size)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # RHS
    # Int Literal
    stack.append(0)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs <= __rhs
    stack.append (__res)
    __if__86__cond = stack.pop ()
    # get condition from stack
    if (__if__86__cond):
        # Body
        # Return
        # Function Call - Vec::Vec() -> Vec
        # Arguments
        # *** Vec::Vec
        __res = __ctor____main____Vec____Vec ()
        stack.append (__res) # function call result
        __rVal = stack.pop ()
        return __rVal
    # End of if
    #---------------------------------------------------------------------
    # Statement
    # Assignment - '='
    # RHS
    # Member Accessor
    # LHS
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____LinkedList__Vec____header)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # RHS
    stack.append (__field____main____Node__Vec____prev)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # LHS
    __main____LinkedList__Vec__popBack__block__85__tail = 0
    __rhs = stack.pop()
    __main____LinkedList__Vec__popBack__block__85__tail = __rhs
    stack.append (__main____LinkedList__Vec__popBack__block__85__tail)
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
    stack.append (__field____main____LinkedList__Vec____header)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # LHS
    # Member Accessor Assignment
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main____LinkedList__Vec__popBack__block__85__tail)
    # RHS
    stack.append (__field____main____Node__Vec____prev)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # RHS
    stack.append(__field____main____Node__Vec____next)
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
    stack.append(__main____LinkedList__Vec__popBack__block__85__tail)
    # RHS
    stack.append (__field____main____Node__Vec____prev)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # LHS
    # Member Accessor Assignment
    # LHS
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____LinkedList__Vec____header)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # RHS
    stack.append(__field____main____Node__Vec____prev)
    __child = stack.pop()
    __parent = stack.pop()
    __rhs = stack.pop()
    __parent[__child] = __rhs
    stack.append (__parent[__child])
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Pre-Decrement
    # RHS
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____LinkedList__Vec____size)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __rhs = stack.pop ()
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____LinkedList__Vec____size)
    __child = stack.pop ()
    __parent = stack.pop ()
    __parent[__child] = __parent[__child] - 1
    __res = __parent[__child]
    stack.append (__res)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Return
    # Member Accessor
    # LHS
    stack.append(__main____LinkedList__Vec__popBack__block__85__tail)
    # RHS
    stack.append (__field____main____Node__Vec____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __rVal = stack.pop ()
    return __rVal
    #---------------------------------------------------------------------
    return 0
# End Method Declaration - __method____main____LinkedList__Vec____popBack
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - LinkedList<:Vec:>::popFront() -> Vec
def __method____main____LinkedList__Vec____popFront (this):
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
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____LinkedList__Vec____size)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # RHS
    # Int Literal
    stack.append(0)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs <= __rhs
    stack.append (__res)
    __if__88__cond = stack.pop ()
    # get condition from stack
    if (__if__88__cond):
        # Body
        # Return
        # Function Call - Vec::Vec() -> Vec
        # Arguments
        # *** Vec::Vec
        __res = __ctor____main____Vec____Vec ()
        stack.append (__res) # function call result
        __rVal = stack.pop ()
        return __rVal
    # End of if
    #---------------------------------------------------------------------
    # Statement
    # Assignment - '='
    # RHS
    # Member Accessor
    # LHS
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____LinkedList__Vec____header)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # RHS
    stack.append (__field____main____Node__Vec____next)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # LHS
    __main____LinkedList__Vec__popFront__block__87__head = 0
    __rhs = stack.pop()
    __main____LinkedList__Vec__popFront__block__87__head = __rhs
    stack.append (__main____LinkedList__Vec__popFront__block__87__head)
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
    stack.append (__field____main____LinkedList__Vec____header)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # LHS
    # Member Accessor Assignment
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main____LinkedList__Vec__popFront__block__87__head)
    # RHS
    stack.append (__field____main____Node__Vec____next)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # RHS
    stack.append(__field____main____Node__Vec____prev)
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
    stack.append(__main____LinkedList__Vec__popFront__block__87__head)
    # RHS
    stack.append (__field____main____Node__Vec____next)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # LHS
    # Member Accessor Assignment
    # LHS
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____LinkedList__Vec____header)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # RHS
    stack.append(__field____main____Node__Vec____next)
    __child = stack.pop()
    __parent = stack.pop()
    __rhs = stack.pop()
    __parent[__child] = __rhs
    stack.append (__parent[__child])
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Pre-Decrement
    # RHS
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____LinkedList__Vec____size)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __rhs = stack.pop ()
    # LHS
    # Member Accessor Assignment
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____LinkedList__Vec____size)
    __child = stack.pop ()
    __parent = stack.pop ()
    __parent[__child] = __parent[__child] - 1
    __res = __parent[__child]
    stack.append (__res)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Return
    # Member Accessor
    # LHS
    stack.append(__main____LinkedList__Vec__popFront__block__87__head)
    # RHS
    stack.append (__field____main____Node__Vec____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __rVal = stack.pop ()
    return __rVal
    #---------------------------------------------------------------------
    return 0
# End Method Declaration - __method____main____LinkedList__Vec____popFront
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - LinkedList<:Vec:>::begin() -> Node<:Vec:>
def __method____main____LinkedList__Vec____begin (this):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Return
    # Member Accessor
    # LHS
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____LinkedList__Vec____header)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # RHS
    stack.append (__field____main____Node__Vec____next)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __rVal = stack.pop ()
    return __rVal
    #---------------------------------------------------------------------
    return 0
# End Method Declaration - __method____main____LinkedList__Vec____begin
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - LinkedList<:Vec:>::end() -> Node<:Vec:>
def __method____main____LinkedList__Vec____end (this):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Return
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____LinkedList__Vec____header)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __rVal = stack.pop ()
    return __rVal
    #---------------------------------------------------------------------
    return 0
# End Method Declaration - __method____main____LinkedList__Vec____end
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - LinkedList<:Vec:>::rbegin() -> Node<:Vec:>
def __method____main____LinkedList__Vec____rbegin (this):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Return
    # Member Accessor
    # LHS
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____LinkedList__Vec____header)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # RHS
    stack.append (__field____main____Node__Vec____prev)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __rVal = stack.pop ()
    return __rVal
    #---------------------------------------------------------------------
    return 0
# End Method Declaration - __method____main____LinkedList__Vec____rbegin
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - LinkedList<:Vec:>::rend() -> Node<:Vec:>
def __method____main____LinkedList__Vec____rend (this):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Return
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____LinkedList__Vec____header)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __rVal = stack.pop ()
    return __rVal
    #---------------------------------------------------------------------
    return 0
# End Method Declaration - __method____main____LinkedList__Vec____rend
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Method Declaration - LinkedList<:Vec:>::isEmpty() -> int
def __method____main____LinkedList__Vec____isEmpty (this):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Return
    # Equal
    # LHS
    # Member Accessor
    # LHS
    stack.append(this)
    # RHS
    stack.append (__field____main____LinkedList__Vec____size)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # RHS
    # Int Literal
    stack.append(0)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs == __rhs
    stack.append (__res)
    __rVal = stack.pop ()
    return __rVal
    #---------------------------------------------------------------------
    return 0
# End Method Declaration - __method____main____LinkedList__Vec____isEmpty
#-------------------------------------------------------------------------

# Populate Dispatch Table
__dtable____main____LinkedList__Vec = [__method____main____LinkedList__Vec____pushBack__Vec, __method____main____LinkedList__Vec____pushFront__Vec, __method____main____LinkedList__Vec____popBack, __method____main____LinkedList__Vec____popFront, __method____main____LinkedList__Vec____begin, __method____main____LinkedList__Vec____end, __method____main____LinkedList__Vec____rbegin, __method____main____LinkedList__Vec____rend, __method____main____LinkedList__Vec____isEmpty]
# End Class Declaration - __main____LinkedList__Vec
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
# Constructor Call - Vector<:Vector<:int:>:>::Vector() -> Vector<:Vector<:int:>:>
# Arguments
__retval = __ctor____main____Vector__Vector____Vector ()
stack.append (__retval)
# LHS
__main__elevations = 0
__rhs = stack.pop()
__main__elevations = __rhs
stack.append (__main__elevations)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Assignment - '='
# RHS
# Constructor Call - Vector<:Vector<:int:>:>::Vector() -> Vector<:Vector<:int:>:>
# Arguments
__retval = __ctor____main____Vector__Vector____Vector ()
stack.append (__retval)
# LHS
__main__was_visited = 0
__rhs = stack.pop()
__main__was_visited = __rhs
stack.append (__main__was_visited)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Assignment - '='
# RHS
# String Literal
stack.append("abcdefghijklmnopqrstuvwxyzSE"+'\0')
# LHS
__main__alphabet = 0
__rhs = stack.pop()
__main__alphabet = __rhs
stack.append (__main__alphabet)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Assignment - '='
# RHS
# Constructor Call - Vec::Vec(int, int) -> Vec
# Arguments
# Int Literal
stack.append(0)
# Int Literal
stack.append(0)
__arg1 = stack.pop ()
__arg0 = stack.pop ()
__retval = __ctor____main____Vec____Vec__int__int (__arg0, __arg1)
stack.append (__retval)
# LHS
__main__start_pos = 0
__rhs = stack.pop()
__main__start_pos = __rhs
stack.append (__main__start_pos)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Assignment - '='
# RHS
# Constructor Call - Vec::Vec(int, int) -> Vec
# Arguments
# Int Literal
stack.append(0)
# Int Literal
stack.append(0)
__arg1 = stack.pop ()
__arg0 = stack.pop ()
__retval = __ctor____main____Vec____Vec__int__int (__arg0, __arg1)
stack.append (__retval)
# LHS
__main__end_pos = 0
__rhs = stack.pop()
__main__end_pos = __rhs
stack.append (__main__end_pos)
# Statement results can be ignored
stack.pop ()
# End Statement

# Statement
# Assignment - '='
# RHS
# Constructor Call - LinkedList<:Vec:>::LinkedList() -> LinkedList<:Vec:>
# Arguments
__retval = __ctor____main____LinkedList__Vec____LinkedList ()
stack.append (__retval)
# LHS
__main__starting_positions = 0
__rhs = stack.pop()
__main__starting_positions = __rhs
stack.append (__main__starting_positions)
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
__main__for__94__l = 0
__rhs = stack.pop()
__main__for__94__l = __rhs
stack.append (__main__for__94__l)
# Using an infinite loop so we can write a separate multi-line condition
while (1):
    # Condition
    # Less Than
    # LHS
    stack.append(__main__for__94__l)
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
    # Method Call - Vector<:Vector<:int:>:>::pushBack(Vector<:int:>) -> void
    # LHS
    stack.append(__main__elevations)
    # RHS
    # Arguments
    # Constructor Call - Vector<:int:>::Vector() -> Vector<:int:>
    # Arguments
    __retval = __ctor____main____Vector__int____Vector ()
    stack.append (__retval)
    __arg0 = stack.pop ()
    __obj = stack.pop ()
    __retval = __method____main____Vector__Vector____pushBack__Vector (__obj, __arg0)
    stack.append (__retval)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Method Call - Vector<:Vector<:int:>:>::pushBack(Vector<:int:>) -> void
    # LHS
    stack.append(__main__was_visited)
    # RHS
    # Arguments
    # Constructor Call - Vector<:int:>::Vector() -> Vector<:int:>
    # Arguments
    __retval = __ctor____main____Vector__int____Vector ()
    stack.append (__retval)
    __arg0 = stack.pop ()
    __obj = stack.pop ()
    __retval = __method____main____Vector__Vector____pushBack__Vector (__obj, __arg0)
    stack.append (__retval)
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
    stack.append(__main__for__94__l)
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
    __main__for__94__block__95__size = 0
    __rhs = stack.pop()
    __main__for__94__block__95__size = __rhs
    stack.append (__main__for__94__block__95__size)
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
        stack.append(__main__for__94__block__95__size)
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
        # Function Call - first_index_of(char[], char) -> int
        # Arguments
        stack.append(__main__alphabet)
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
        stack.append(__main__for__94__l)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # OFFSET
        stack.append(__main__for__94__block__95__for__96__c)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        __arg1 = stack.pop ()
        __arg0 = stack.pop ()
        # *** first_index_of
        __res = __main____first_index_of__char__1__char (__arg0, __arg1)
        stack.append (__res) # function call result
        # LHS
        __main__for__94__block__95__for__96__block__97__val = 0
        __rhs = stack.pop()
        __main__for__94__block__95__for__96__block__97__val = __rhs
        stack.append (__main__for__94__block__95__for__96__block__97__val)
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
        stack.append(__main__for__94__block__95__for__96__block__97__val)
        # RHS
        # Int Literal
        stack.append(26)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs == __rhs
        stack.append (__res)
        __if__98__cond = stack.pop ()
        # Condition for elif #0
        # Equal
        # LHS
        stack.append(__main__for__94__block__95__for__96__block__97__val)
        # RHS
        # Int Literal
        stack.append(27)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs == __rhs
        stack.append (__res)
        __elif__98x0__cond = stack.pop ()
        # get condition from stack
        if (__if__98__cond):
            # Body
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Assignment - '='
            # RHS
            # Int Literal
            stack.append(0)
            __rhs = stack.pop()
            __main__for__94__block__95__for__96__block__97__val = __rhs
            stack.append (__main__for__94__block__95__for__96__block__97__val)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            # Statement
            # Assignment - '='
            # RHS
            stack.append(__main__for__94__l)
            # LHS
            # Member Accessor Assignment
            # LHS
            stack.append(__main__start_pos)
            # RHS
            stack.append(__field____main____Vec____i)
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
            stack.append(__main__for__94__block__95__for__96__c)
            # LHS
            # Member Accessor Assignment
            # LHS
            stack.append(__main__start_pos)
            # RHS
            stack.append(__field____main____Vec____j)
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
        # Elif-Statement
        # Condition
        elif (__elif__98x0__cond):
            # Body
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Assignment - '='
            # RHS
            # Int Literal
            stack.append(25)
            __rhs = stack.pop()
            __main__for__94__block__95__for__96__block__97__val = __rhs
            stack.append (__main__for__94__block__95__for__96__block__97__val)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            # Statement
            # Assignment - '='
            # RHS
            stack.append(__main__for__94__l)
            # LHS
            # Member Accessor Assignment
            # LHS
            stack.append(__main__end_pos)
            # RHS
            stack.append(__field____main____Vec____i)
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
            stack.append(__main__for__94__block__95__for__96__c)
            # LHS
            # Member Accessor Assignment
            # LHS
            stack.append(__main__end_pos)
            # RHS
            stack.append(__field____main____Vec____j)
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
        # If-Statement
        # Precomputing all if/elif conditions and give unique names
        # bc we can't have code between if and elif
        # Condition
        # Equal
        # LHS
        stack.append(__main__for__94__block__95__for__96__block__97__val)
        # RHS
        # Int Literal
        stack.append(0)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs == __rhs
        stack.append (__res)
        __if__101__cond = stack.pop ()
        # get condition from stack
        if (__if__101__cond):
            # Body
            #-------------------------------------------------------------
            # Code Block
            # Statement
            # Method Call - LinkedList<:Vec:>::pushBack(Vec) -> void
            # LHS
            stack.append(__main__starting_positions)
            # RHS
            # Arguments
            # Constructor Call - Vec::Vec(int, int) -> Vec
            # Arguments
            stack.append(__main__for__94__l)
            stack.append(__main__for__94__block__95__for__96__c)
            __arg1 = stack.pop ()
            __arg0 = stack.pop ()
            __retval = __ctor____main____Vec____Vec__int__int (__arg0, __arg1)
            stack.append (__retval)
            __arg0 = stack.pop ()
            __obj = stack.pop ()
            __retval = __method____main____LinkedList__Vec____pushBack__Vec (__obj, __arg0)
            stack.append (__retval)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

            #-------------------------------------------------------------
        # End of if
        #-----------------------------------------------------------------
        # Statement
        # Method Call - Vector<:int:>::pushBack(int) -> void
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__elevations)
        # RHS
        stack.append (__field____main____Vector__Vector____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__for__94__l)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        # Arguments
        stack.append(__main__for__94__block__95__for__96__block__97__val)
        __arg0 = stack.pop ()
        __obj = stack.pop ()
        __retval = __method____main____Vector__int____pushBack__int (__obj, __arg0)
        stack.append (__retval)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Statement
        # Method Call - Vector<:int:>::pushBack(int) -> void
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__was_visited)
        # RHS
        stack.append (__field____main____Vector__Vector____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        stack.append(__main__for__94__l)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        # Arguments
        # Negative
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop ()
        __res = -__rhs
        stack.append (__res)
        __arg0 = stack.pop ()
        __obj = stack.pop ()
        __retval = __method____main____Vector__int____pushBack__int (__obj, __arg0)
        stack.append (__retval)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

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
    # Int Literal
    stack.append(1)
    __rhs = stack.pop()
    __main__for__94__l = __main__for__94__l + __rhs
    stack.append (__main__for__94__l)
#-------------------------------------------------------------------------
#=========================================================================
# Function Declaration - bfs(Vector<:Vector<:int:>:>, Vector<:Vector<:int:>:>, Vec, Vec) -> int
def __main____bfs__Vector__tparam0__Vector__Vector__tparam0__Vector__Vec__Vec (__main__bfs__elevations, __main__bfs__board, __main__bfs__start_pos, __main__bfs__end_pos):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Assignment - '='
    # RHS
    # Constructor Call - LinkedList<:Vec:>::LinkedList() -> LinkedList<:Vec:>
    # Arguments
    __retval = __ctor____main____LinkedList__Vec____LinkedList ()
    stack.append (__retval)
    # LHS
    __main__bfs__block__103__frontier = 0
    __rhs = stack.pop()
    __main__bfs__block__103__frontier = __rhs
    stack.append (__main__bfs__block__103__frontier)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Method Call - LinkedList<:Vec:>::pushBack(Vec) -> void
    # LHS
    stack.append(__main__bfs__block__103__frontier)
    # RHS
    # Arguments
    # Constructor Call - Vec::Vec(int, int, int) -> Vec
    # Arguments
    # Member Accessor
    # LHS
    stack.append(__main__bfs__start_pos)
    # RHS
    stack.append (__field____main____Vec____i)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # Member Accessor
    # LHS
    stack.append(__main__bfs__start_pos)
    # RHS
    stack.append (__field____main____Vec____j)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # Int Literal
    stack.append(0)
    __arg2 = stack.pop ()
    __arg1 = stack.pop ()
    __arg0 = stack.pop ()
    __retval = __ctor____main____Vec____Vec__int__int__int (__arg0, __arg1, __arg2)
    stack.append (__retval)
    __arg0 = stack.pop ()
    __obj = stack.pop ()
    __retval = __method____main____LinkedList__Vec____pushBack__Vec (__obj, __arg0)
    stack.append (__retval)
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
        # Method Call - LinkedList<:Vec:>::isEmpty() -> int
        # LHS
        stack.append(__main__bfs__block__103__frontier)
        # RHS
        # Arguments
        __obj = stack.pop ()
        __retval = __method____main____LinkedList__Vec____isEmpty (__obj)
        stack.append (__retval)
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
        # Assignment - '='
        # RHS
        # Method Call - LinkedList<:Vec:>::popFront() -> Vec
        # LHS
        stack.append(__main__bfs__block__103__frontier)
        # RHS
        # Arguments
        __obj = stack.pop ()
        __retval = __method____main____LinkedList__Vec____popFront (__obj)
        stack.append (__retval)
        # LHS
        __main__bfs__block__103__while__104__block__105__pos = 0
        __rhs = stack.pop()
        __main__bfs__block__103__while__104__block__105__pos = __rhs
        stack.append (__main__bfs__block__103__while__104__block__105__pos)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
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
        stack.append(__main__bfs__board)
        # RHS
        stack.append (__field____main____Vector__Vector____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Member Accessor
        # LHS
        stack.append(__main__bfs__block__103__while__104__block__105__pos)
        # RHS
        stack.append (__field____main____Vec____i)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        stack.append (__field____main____Vector__int____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Member Accessor
        # LHS
        stack.append(__main__bfs__block__103__while__104__block__105__pos)
        # RHS
        stack.append (__field____main____Vec____j)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
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
        __if__106__cond = stack.pop ()
        # get condition from stack
        if (__if__106__cond):
            # Body
            #-------------------------------------------------------------
            # Code Block
            # Continue in __while__104
            continue
            #-------------------------------------------------------------
        # End of if
        #-----------------------------------------------------------------
        # Statement
        # Assignment - '='
        # RHS
        # Member Accessor
        # LHS
        stack.append(__main__bfs__block__103__while__104__block__105__pos)
        # RHS
        stack.append (__field____main____Vec____time)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # LHS
        # Subscript assignment
        # LHS
        # Member Accessor
        # LHS
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__bfs__board)
        # RHS
        stack.append (__field____main____Vector__Vector____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Member Accessor
        # LHS
        stack.append(__main__bfs__block__103__while__104__block__105__pos)
        # RHS
        stack.append (__field____main____Vec____i)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        stack.append (__field____main____Vector__int____data)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        # OFFSET
        # Member Accessor
        # LHS
        stack.append(__main__bfs__block__103__while__104__block__105__pos)
        # RHS
        stack.append (__field____main____Vec____j)
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

        #-----------------------------------------------------------------
        # If-Statement
        # Precomputing all if/elif conditions and give unique names
        # bc we can't have code between if and elif
        # Condition
        # Greater Than or Equal to
        # LHS
        # Subtraction
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__bfs__block__103__while__104__block__105__pos)
        # RHS
        stack.append (__field____main____Vec____i)
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
        # Int Literal
        stack.append(0)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs >= __rhs
        stack.append (__res)
        __if__108__cond = stack.pop ()
        # get condition from stack
        if (__if__108__cond):
            # Body
            #-------------------------------------------------------------
            # If-Statement
            # Precomputing all if/elif conditions and give unique names
            # bc we can't have code between if and elif
            # Condition
            # Less Than or Equal to
            # LHS
            # Subtraction
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__bfs__elevations)
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
            stack.append(__main__bfs__block__103__while__104__block__105__pos)
            # RHS
            stack.append (__field____main____Vec____i)
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
            stack.append (__field____main____Vector__int____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            # Member Accessor
            # LHS
            stack.append(__main__bfs__block__103__while__104__block__105__pos)
            # RHS
            stack.append (__field____main____Vec____j)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__bfs__elevations)
            # RHS
            stack.append (__field____main____Vector__Vector____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            # Member Accessor
            # LHS
            stack.append(__main__bfs__block__103__while__104__block__105__pos)
            # RHS
            stack.append (__field____main____Vec____i)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            stack.append (__field____main____Vector__int____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            # Member Accessor
            # LHS
            stack.append(__main__bfs__block__103__while__104__block__105__pos)
            # RHS
            stack.append (__field____main____Vec____j)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            __rhs = stack.pop()
            __lhs = stack.pop()
            __res = __lhs - __rhs
            stack.append(__res)
            # RHS
            # Int Literal
            stack.append(1)
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs <= __rhs
            stack.append (__res)
            __if__109__cond = stack.pop ()
            # get condition from stack
            if (__if__109__cond):
                # Body
                # Statement
                # Method Call - LinkedList<:Vec:>::pushBack(Vec) -> void
                # LHS
                stack.append(__main__bfs__block__103__frontier)
                # RHS
                # Arguments
                # Constructor Call - Vec::Vec(int, int, int) -> Vec
                # Arguments
                # Subtraction
                # LHS
                # Member Accessor
                # LHS
                stack.append(__main__bfs__block__103__while__104__block__105__pos)
                # RHS
                stack.append (__field____main____Vec____i)
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
                # Member Accessor
                # LHS
                stack.append(__main__bfs__block__103__while__104__block__105__pos)
                # RHS
                stack.append (__field____main____Vec____j)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                # Addition
                # LHS
                # Member Accessor
                # LHS
                stack.append(__main__bfs__block__103__while__104__block__105__pos)
                # RHS
                stack.append (__field____main____Vec____time)
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
                __arg2 = stack.pop ()
                __arg1 = stack.pop ()
                __arg0 = stack.pop ()
                __retval = __ctor____main____Vec____Vec__int__int__int (__arg0, __arg1, __arg2)
                stack.append (__retval)
                __arg0 = stack.pop ()
                __obj = stack.pop ()
                __retval = __method____main____LinkedList__Vec____pushBack__Vec (__obj, __arg0)
                stack.append (__retval)
                # Statement results can be ignored
                stack.pop ()
                # End Statement

            # End of if
            #-------------------------------------------------------------
        # End of if
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # If-Statement
        # Precomputing all if/elif conditions and give unique names
        # bc we can't have code between if and elif
        # Condition
        # Less Than
        # LHS
        # Addition
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__bfs__block__103__while__104__block__105__pos)
        # RHS
        stack.append (__field____main____Vec____j)
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
        # Subscript
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__bfs__elevations)
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
        stack.append (__field____main____Vector__int____size)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs < __rhs
        stack.append (__res)
        __if__110__cond = stack.pop ()
        # get condition from stack
        if (__if__110__cond):
            # Body
            #-------------------------------------------------------------
            # If-Statement
            # Precomputing all if/elif conditions and give unique names
            # bc we can't have code between if and elif
            # Condition
            # Less Than or Equal to
            # LHS
            # Subtraction
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__bfs__elevations)
            # RHS
            stack.append (__field____main____Vector__Vector____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            # Member Accessor
            # LHS
            stack.append(__main__bfs__block__103__while__104__block__105__pos)
            # RHS
            stack.append (__field____main____Vec____i)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            stack.append (__field____main____Vector__int____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            # Addition
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__bfs__block__103__while__104__block__105__pos)
            # RHS
            stack.append (__field____main____Vec____j)
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
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__bfs__elevations)
            # RHS
            stack.append (__field____main____Vector__Vector____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            # Member Accessor
            # LHS
            stack.append(__main__bfs__block__103__while__104__block__105__pos)
            # RHS
            stack.append (__field____main____Vec____i)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            stack.append (__field____main____Vector__int____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            # Member Accessor
            # LHS
            stack.append(__main__bfs__block__103__while__104__block__105__pos)
            # RHS
            stack.append (__field____main____Vec____j)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            __rhs = stack.pop()
            __lhs = stack.pop()
            __res = __lhs - __rhs
            stack.append(__res)
            # RHS
            # Int Literal
            stack.append(1)
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs <= __rhs
            stack.append (__res)
            __if__111__cond = stack.pop ()
            # get condition from stack
            if (__if__111__cond):
                # Body
                # Statement
                # Method Call - LinkedList<:Vec:>::pushBack(Vec) -> void
                # LHS
                stack.append(__main__bfs__block__103__frontier)
                # RHS
                # Arguments
                # Constructor Call - Vec::Vec(int, int, int) -> Vec
                # Arguments
                # Member Accessor
                # LHS
                stack.append(__main__bfs__block__103__while__104__block__105__pos)
                # RHS
                stack.append (__field____main____Vec____i)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                # Addition
                # LHS
                # Member Accessor
                # LHS
                stack.append(__main__bfs__block__103__while__104__block__105__pos)
                # RHS
                stack.append (__field____main____Vec____j)
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
                # Addition
                # LHS
                # Member Accessor
                # LHS
                stack.append(__main__bfs__block__103__while__104__block__105__pos)
                # RHS
                stack.append (__field____main____Vec____time)
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
                __arg2 = stack.pop ()
                __arg1 = stack.pop ()
                __arg0 = stack.pop ()
                __retval = __ctor____main____Vec____Vec__int__int__int (__arg0, __arg1, __arg2)
                stack.append (__retval)
                __arg0 = stack.pop ()
                __obj = stack.pop ()
                __retval = __method____main____LinkedList__Vec____pushBack__Vec (__obj, __arg0)
                stack.append (__retval)
                # Statement results can be ignored
                stack.pop ()
                # End Statement

            # End of if
            #-------------------------------------------------------------
        # End of if
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # If-Statement
        # Precomputing all if/elif conditions and give unique names
        # bc we can't have code between if and elif
        # Condition
        # Less Than
        # LHS
        # Addition
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__bfs__block__103__while__104__block__105__pos)
        # RHS
        stack.append (__field____main____Vec____i)
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
        stack.append(__main__bfs__elevations)
        # RHS
        stack.append (__field____main____Vector__Vector____size)
        __child = stack.pop ()
        __parent = stack.pop ()
        stack.append (__parent[__child])
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs < __rhs
        stack.append (__res)
        __if__112__cond = stack.pop ()
        # get condition from stack
        if (__if__112__cond):
            # Body
            #-------------------------------------------------------------
            # If-Statement
            # Precomputing all if/elif conditions and give unique names
            # bc we can't have code between if and elif
            # Condition
            # Less Than or Equal to
            # LHS
            # Subtraction
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__bfs__elevations)
            # RHS
            stack.append (__field____main____Vector__Vector____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            # Addition
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__bfs__block__103__while__104__block__105__pos)
            # RHS
            stack.append (__field____main____Vec____i)
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
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            stack.append (__field____main____Vector__int____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            # Member Accessor
            # LHS
            stack.append(__main__bfs__block__103__while__104__block__105__pos)
            # RHS
            stack.append (__field____main____Vec____j)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__bfs__elevations)
            # RHS
            stack.append (__field____main____Vector__Vector____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            # Member Accessor
            # LHS
            stack.append(__main__bfs__block__103__while__104__block__105__pos)
            # RHS
            stack.append (__field____main____Vec____i)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            stack.append (__field____main____Vector__int____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            # Member Accessor
            # LHS
            stack.append(__main__bfs__block__103__while__104__block__105__pos)
            # RHS
            stack.append (__field____main____Vec____j)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            __rhs = stack.pop()
            __lhs = stack.pop()
            __res = __lhs - __rhs
            stack.append(__res)
            # RHS
            # Int Literal
            stack.append(1)
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs <= __rhs
            stack.append (__res)
            __if__113__cond = stack.pop ()
            # get condition from stack
            if (__if__113__cond):
                # Body
                # Statement
                # Method Call - LinkedList<:Vec:>::pushBack(Vec) -> void
                # LHS
                stack.append(__main__bfs__block__103__frontier)
                # RHS
                # Arguments
                # Constructor Call - Vec::Vec(int, int, int) -> Vec
                # Arguments
                # Addition
                # LHS
                # Member Accessor
                # LHS
                stack.append(__main__bfs__block__103__while__104__block__105__pos)
                # RHS
                stack.append (__field____main____Vec____i)
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
                # Member Accessor
                # LHS
                stack.append(__main__bfs__block__103__while__104__block__105__pos)
                # RHS
                stack.append (__field____main____Vec____j)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                # Addition
                # LHS
                # Member Accessor
                # LHS
                stack.append(__main__bfs__block__103__while__104__block__105__pos)
                # RHS
                stack.append (__field____main____Vec____time)
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
                __arg2 = stack.pop ()
                __arg1 = stack.pop ()
                __arg0 = stack.pop ()
                __retval = __ctor____main____Vec____Vec__int__int__int (__arg0, __arg1, __arg2)
                stack.append (__retval)
                __arg0 = stack.pop ()
                __obj = stack.pop ()
                __retval = __method____main____LinkedList__Vec____pushBack__Vec (__obj, __arg0)
                stack.append (__retval)
                # Statement results can be ignored
                stack.pop ()
                # End Statement

            # End of if
            #-------------------------------------------------------------
        # End of if
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # If-Statement
        # Precomputing all if/elif conditions and give unique names
        # bc we can't have code between if and elif
        # Condition
        # Greater Than or Equal to
        # LHS
        # Subtraction
        # LHS
        # Member Accessor
        # LHS
        stack.append(__main__bfs__block__103__while__104__block__105__pos)
        # RHS
        stack.append (__field____main____Vec____j)
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
        # Int Literal
        stack.append(0)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs >= __rhs
        stack.append (__res)
        __if__114__cond = stack.pop ()
        # get condition from stack
        if (__if__114__cond):
            # Body
            #-------------------------------------------------------------
            # If-Statement
            # Precomputing all if/elif conditions and give unique names
            # bc we can't have code between if and elif
            # Condition
            # Less Than or Equal to
            # LHS
            # Subtraction
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__bfs__elevations)
            # RHS
            stack.append (__field____main____Vector__Vector____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            # Member Accessor
            # LHS
            stack.append(__main__bfs__block__103__while__104__block__105__pos)
            # RHS
            stack.append (__field____main____Vec____i)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            stack.append (__field____main____Vector__int____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            # Subtraction
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__bfs__block__103__while__104__block__105__pos)
            # RHS
            stack.append (__field____main____Vec____j)
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
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__bfs__elevations)
            # RHS
            stack.append (__field____main____Vector__Vector____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            # Member Accessor
            # LHS
            stack.append(__main__bfs__block__103__while__104__block__105__pos)
            # RHS
            stack.append (__field____main____Vec____i)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            stack.append (__field____main____Vector__int____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            # Member Accessor
            # LHS
            stack.append(__main__bfs__block__103__while__104__block__105__pos)
            # RHS
            stack.append (__field____main____Vec____j)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            __rhs = stack.pop()
            __lhs = stack.pop()
            __res = __lhs - __rhs
            stack.append(__res)
            # RHS
            # Int Literal
            stack.append(1)
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs <= __rhs
            stack.append (__res)
            __if__115__cond = stack.pop ()
            # get condition from stack
            if (__if__115__cond):
                # Body
                # Statement
                # Method Call - LinkedList<:Vec:>::pushBack(Vec) -> void
                # LHS
                stack.append(__main__bfs__block__103__frontier)
                # RHS
                # Arguments
                # Constructor Call - Vec::Vec(int, int, int) -> Vec
                # Arguments
                # Member Accessor
                # LHS
                stack.append(__main__bfs__block__103__while__104__block__105__pos)
                # RHS
                stack.append (__field____main____Vec____i)
                __child = stack.pop ()
                __parent = stack.pop ()
                stack.append (__parent[__child])
                # Subtraction
                # LHS
                # Member Accessor
                # LHS
                stack.append(__main__bfs__block__103__while__104__block__105__pos)
                # RHS
                stack.append (__field____main____Vec____j)
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
                # Addition
                # LHS
                # Member Accessor
                # LHS
                stack.append(__main__bfs__block__103__while__104__block__105__pos)
                # RHS
                stack.append (__field____main____Vec____time)
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
                __arg2 = stack.pop ()
                __arg1 = stack.pop ()
                __arg0 = stack.pop ()
                __retval = __ctor____main____Vec____Vec__int__int__int (__arg0, __arg1, __arg2)
                stack.append (__retval)
                __arg0 = stack.pop ()
                __obj = stack.pop ()
                __retval = __method____main____LinkedList__Vec____pushBack__Vec (__obj, __arg0)
                stack.append (__retval)
                # Statement results can be ignored
                stack.pop ()
                # End Statement

            # End of if
            #-------------------------------------------------------------
        # End of if
        #-----------------------------------------------------------------
        # Statement
        stack.append(__main__bfs__block__103__while__104__block__105__pos)
        __arr = stack.pop ()
        __builtin__free (__arr)
        stack.append (0)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        #-----------------------------------------------------------------
    # End of While
    #---------------------------------------------------------------------
    # Return
    # Subscript
    # LHS
    # Member Accessor
    # LHS
    # Subscript
    # LHS
    # Member Accessor
    # LHS
    stack.append(__main__bfs__board)
    # RHS
    stack.append (__field____main____Vector__Vector____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    # Member Accessor
    # LHS
    stack.append(__main__bfs__end_pos)
    # RHS
    stack.append (__field____main____Vec____i)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    # RHS
    stack.append (__field____main____Vector__int____data)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # OFFSET
    # Member Accessor
    # LHS
    stack.append(__main__bfs__end_pos)
    # RHS
    stack.append (__field____main____Vec____j)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __offset = stack.pop ()
    __pointer = stack.pop ()
    stack.append (__pointer[__offset])
    __rVal = stack.pop ()
    return __rVal
    #---------------------------------------------------------------------
# End Function Declaration - __main____bfs__Vector__tparam0__Vector__Vector__tparam0__Vector__Vec__Vec
#=========================================================================

# Statement
# Assignment - '='
# RHS
# Multiplication
# LHS
# Member Accessor
# LHS
stack.append(__main__elevations)
# RHS
stack.append (__field____main____Vector__Vector____size)
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
stack.append(__main__elevations)
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
stack.append (__field____main____Vector__int____size)
__child = stack.pop ()
__parent = stack.pop ()
stack.append (__parent[__child])
__rhs = stack.pop()
__lhs = stack.pop()
__res = __lhs * __rhs
stack.append(__res)
# LHS
__main__min_moves = 0
__rhs = stack.pop()
__main__min_moves = __rhs
stack.append (__main__min_moves)
# Statement results can be ignored
stack.pop ()
# End Statement

#-------------------------------------------------------------------------
# While-Loop
# Using an infinite loop so we can write a separate multi-line condition
while (1):
    # Condition
    # Negate
    # RHS
    # Method Call - LinkedList<:Vec:>::isEmpty() -> int
    # LHS
    stack.append(__main__starting_positions)
    # RHS
    # Arguments
    __obj = stack.pop ()
    __retval = __method____main____LinkedList__Vec____isEmpty (__obj)
    stack.append (__retval)
    __rhs = stack.pop ()
    __res = not __rhs
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
    # Method Call - LinkedList<:Vec:>::popFront() -> Vec
    # LHS
    stack.append(__main__starting_positions)
    # RHS
    # Arguments
    __obj = stack.pop ()
    __retval = __method____main____LinkedList__Vec____popFront (__obj)
    stack.append (__retval)
    # LHS
    __main__while__116__block__117__starting_pos = 0
    __rhs = stack.pop()
    __main__while__116__block__117__starting_pos = __rhs
    stack.append (__main__while__116__block__117__starting_pos)
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
    # Function Call - manhattan(int, int, int, int) -> int
    # Arguments
    # Member Accessor
    # LHS
    stack.append(__main__while__116__block__117__starting_pos)
    # RHS
    stack.append (__field____main____Vec____i)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # Member Accessor
    # LHS
    stack.append(__main__while__116__block__117__starting_pos)
    # RHS
    stack.append (__field____main____Vec____j)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # Member Accessor
    # LHS
    stack.append(__main__end_pos)
    # RHS
    stack.append (__field____main____Vec____i)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    # Member Accessor
    # LHS
    stack.append(__main__end_pos)
    # RHS
    stack.append (__field____main____Vec____j)
    __child = stack.pop ()
    __parent = stack.pop ()
    stack.append (__parent[__child])
    __arg3 = stack.pop ()
    __arg2 = stack.pop ()
    __arg1 = stack.pop ()
    __arg0 = stack.pop ()
    # *** manhattan
    __res = __main____manhattan__int__int__int__int (__arg0, __arg1, __arg2, __arg3)
    stack.append (__res) # function call result
    # RHS
    stack.append(__main__min_moves)
    __rhs = stack.pop ()
    __lhs = stack.pop ()
    __res = __lhs >= __rhs
    stack.append (__res)
    __if__118__cond = stack.pop ()
    # get condition from stack
    if (__if__118__cond):
        # Body
        #-----------------------------------------------------------------
        # Code Block
        # Statement
        stack.append(__main__while__116__block__117__starting_pos)
        __arr = stack.pop ()
        __builtin__free (__arr)
        stack.append (0)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Continue in __while__116
        continue
        #-----------------------------------------------------------------
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
    __main__while__116__block__117__for__120__i = 0
    __rhs = stack.pop()
    __main__while__116__block__117__for__120__i = __rhs
    stack.append (__main__while__116__block__117__for__120__i)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        stack.append(__main__while__116__block__117__for__120__i)
        # RHS
        # Member Accessor
        # LHS
        stack.append(__main__was_visited)
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
        __main__while__116__block__117__for__120__block__121__for__122__j = 0
        __rhs = stack.pop()
        __main__while__116__block__117__for__120__block__121__for__122__j = __rhs
        stack.append (__main__while__116__block__117__for__120__block__121__for__122__j)
        # Using an infinite loop so we can write a separate multi-line condition
        while (1):
            # Condition
            # Less Than
            # LHS
            stack.append(__main__while__116__block__117__for__120__block__121__for__122__j)
            # RHS
            # Member Accessor
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__was_visited)
            # RHS
            stack.append (__field____main____Vector__Vector____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main__while__116__block__117__for__120__i)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
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
            # Negative
            # RHS
            # Int Literal
            stack.append(1)
            __rhs = stack.pop ()
            __res = -__rhs
            stack.append (__res)
            # LHS
            # Subscript assignment
            # LHS
            # Member Accessor
            # LHS
            # Subscript
            # LHS
            # Member Accessor
            # LHS
            stack.append(__main__was_visited)
            # RHS
            stack.append (__field____main____Vector__Vector____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main__while__116__block__117__for__120__i)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            stack.append (__field____main____Vector__int____data)
            __child = stack.pop ()
            __parent = stack.pop ()
            stack.append (__parent[__child])
            # OFFSET
            stack.append(__main__while__116__block__117__for__120__block__121__for__122__j)
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
            stack.append(__main__while__116__block__117__for__120__block__121__for__122__j)
            __rhs = stack.pop ()
            __main__while__116__block__117__for__120__block__121__for__122__j = __main__while__116__block__117__for__120__block__121__for__122__j + 1
            __res = __main__while__116__block__117__for__120__block__121__for__122__j
            stack.append (__res)
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # Update
        # Pre-Increment
        # RHS
        stack.append(__main__while__116__block__117__for__120__i)
        __rhs = stack.pop ()
        __main__while__116__block__117__for__120__i = __main__while__116__block__117__for__120__i + 1
        __res = __main__while__116__block__117__for__120__i
        stack.append (__res)
    #---------------------------------------------------------------------
    # Statement
    # Assignment - '='
    # RHS
    # Function Call - bfs(Vector<:Vector<:int:>:>, Vector<:Vector<:int:>:>, Vec, Vec) -> int
    # Arguments
    stack.append(__main__elevations)
    stack.append(__main__was_visited)
    stack.append(__main__while__116__block__117__starting_pos)
    stack.append(__main__end_pos)
    __arg3 = stack.pop ()
    __arg2 = stack.pop ()
    __arg1 = stack.pop ()
    __arg0 = stack.pop ()
    # *** bfs
    __res = __main____bfs__Vector__tparam0__Vector__Vector__tparam0__Vector__Vec__Vec (__arg0, __arg1, __arg2, __arg3)
    stack.append (__res) # function call result
    # LHS
    __main__while__116__block__117__res = 0
    __rhs = stack.pop()
    __main__while__116__block__117__res = __rhs
    stack.append (__main__while__116__block__117__res)
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
    stack.append(__main__while__116__block__117__res)
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
    __res = __lhs == __rhs
    stack.append (__res)
    __if__124__cond = stack.pop ()
    # get condition from stack
    if (__if__124__cond):
        # Body
        #-----------------------------------------------------------------
        # Code Block
        # Statement
        stack.append(__main__while__116__block__117__starting_pos)
        __arr = stack.pop ()
        __builtin__free (__arr)
        stack.append (0)
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Continue in __while__116
        continue
        #-----------------------------------------------------------------
    # End of if
    #---------------------------------------------------------------------
    # Statement
    # Assignment - '='
    # RHS
    # Function Call - min(int, int) -> int
    # Arguments
    stack.append(__main__while__116__block__117__res)
    stack.append(__main__min_moves)
    __arg1 = stack.pop ()
    __arg0 = stack.pop ()
    # *** min
    __res = __main____min__int__int (__arg0, __arg1)
    stack.append (__res) # function call result
    __rhs = stack.pop()
    __main__min_moves = __rhs
    stack.append (__main__min_moves)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    stack.append(__main__while__116__block__117__starting_pos)
    __arr = stack.pop ()
    __builtin__free (__arr)
    stack.append (0)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
# End of While
#-------------------------------------------------------------------------
# Statement
# Function Call - println(int) -> void
# Arguments
stack.append(__main__min_moves)
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

