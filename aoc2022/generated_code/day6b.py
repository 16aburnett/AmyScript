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
__main__size = 0
__rhs = stack.pop()
__main__size = __rhs
stack.append (__main__size)
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
    # Post-Increment
    __res = __main__size
    __main__size = __main__size + 1
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
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# For-Loop
# Init
# Assignment - '='
# RHS
# Int Literal
stack.append(0)
# LHS
__main__for__1__i = 0
__rhs = stack.pop()
__main__for__1__i = __rhs
stack.append (__main__for__1__i)
# Using an infinite loop so we can write a separate multi-line condition
while (1):
    # Condition
    # Less Than
    # LHS
    stack.append(__main__for__1__i)
    # RHS
    # Subtraction
    # LHS
    stack.append(__main__size)
    # RHS
    # Int Literal
    stack.append(3)
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
    #---------------------------------------------------------------------
    # Code Block
    # Statement
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(1)
    # LHS
    __main__for__1__block__2__is_unique = 0
    __rhs = stack.pop()
    __main__for__1__block__2__is_unique = __rhs
    stack.append (__main__for__1__block__2__is_unique)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
    # For-Loop
    # Init
    # Assignment - '='
    # RHS
    stack.append(__main__for__1__i)
    # LHS
    __main__for__1__block__2__for__3__j = 0
    __rhs = stack.pop()
    __main__for__1__block__2__for__3__j = __rhs
    stack.append (__main__for__1__block__2__for__3__j)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        stack.append(__main__for__1__block__2__for__3__j)
        # RHS
        # Addition
        # LHS
        stack.append(__main__for__1__i)
        # RHS
        # Int Literal
        stack.append(14)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
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
        # Addition
        # LHS
        stack.append(__main__for__1__block__2__for__3__j)
        # RHS
        # Int Literal
        stack.append(1)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        # LHS
        __main__for__1__block__2__for__3__block__4__for__5__k = 0
        __rhs = stack.pop()
        __main__for__1__block__2__for__3__block__4__for__5__k = __rhs
        stack.append (__main__for__1__block__2__for__3__block__4__for__5__k)
        # Using an infinite loop so we can write a separate multi-line condition
        while (1):
            # Condition
            # Less Than
            # LHS
            stack.append(__main__for__1__block__2__for__3__block__4__for__5__k)
            # RHS
            # Addition
            # LHS
            stack.append(__main__for__1__i)
            # RHS
            # Int Literal
            stack.append(14)
            __rhs = stack.pop()
            __lhs = stack.pop()
            __res = __lhs + __rhs
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
            stack.append(__main__line)
            # OFFSET
            stack.append(__main__for__1__block__2__for__3__j)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            # Subscript
            # LHS
            stack.append(__main__line)
            # OFFSET
            stack.append(__main__for__1__block__2__for__3__block__4__for__5__k)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs == __rhs
            stack.append (__res)
            __if__7__cond = stack.pop ()
            # get condition from stack
            if (__if__7__cond):
                # Body
                #---------------------------------------------------------
                # Code Block
                # Statement
                # Assignment - '='
                # RHS
                # Int Literal
                stack.append(0)
                __rhs = stack.pop()
                __main__for__1__block__2__is_unique = __rhs
                stack.append (__main__for__1__block__2__is_unique)
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                # Break out of __for__5
                break
                #---------------------------------------------------------
            # End of if
            #-------------------------------------------------------------
            #-------------------------------------------------------------
            # Update
            # Pre-Increment
            # RHS
            stack.append(__main__for__1__block__2__for__3__block__4__for__5__k)
            __rhs = stack.pop ()
            __main__for__1__block__2__for__3__block__4__for__5__k = __main__for__1__block__2__for__3__block__4__for__5__k + 1
            __res = __main__for__1__block__2__for__3__block__4__for__5__k
            stack.append (__res)
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # If-Statement
        # Precomputing all if/elif conditions and give unique names
        # bc we can't have code between if and elif
        # Condition
        # Negate
        # RHS
        stack.append(__main__for__1__block__2__is_unique)
        __rhs = stack.pop ()
        __res = not __rhs
        stack.append (__res)
        __if__9__cond = stack.pop ()
        # get condition from stack
        if (__if__9__cond):
            # Body
            # Break out of __for__3
            break
        # End of if
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # Update
        # Pre-Increment
        # RHS
        stack.append(__main__for__1__block__2__for__3__j)
        __rhs = stack.pop ()
        __main__for__1__block__2__for__3__j = __main__for__1__block__2__for__3__j + 1
        __res = __main__for__1__block__2__for__3__j
        stack.append (__res)
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    # If-Statement
    # Precomputing all if/elif conditions and give unique names
    # bc we can't have code between if and elif
    # Condition
    stack.append(__main__for__1__block__2__is_unique)
    __if__10__cond = stack.pop ()
    # get condition from stack
    if (__if__10__cond):
        # Body
        #-----------------------------------------------------------------
        # Code Block
        # Statement
        # Function Call - println(int) -> void
        # Arguments
        # Addition
        # LHS
        stack.append(__main__for__1__i)
        # RHS
        # Int Literal
        stack.append(14)
        __rhs = stack.pop()
        __lhs = stack.pop()
        __res = __lhs + __rhs
        stack.append(__res)
        __arg0 = stack.pop ()
        # *** println
        __res = __builtin__println__int (__arg0)
        stack.append (__res) # function call result
        # Statement results can be ignored
        stack.pop ()
        # End Statement

        # Break out of __for__1
        break
        #-----------------------------------------------------------------
    # End of if
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    # Update
    # Pre-Increment
    # RHS
    stack.append(__main__for__1__i)
    __rhs = stack.pop ()
    __main__for__1__i = __main__for__1__i + 1
    __res = __main__for__1__i
    stack.append (__res)
#-------------------------------------------------------------------------

#=========================================================================
#### END OF CODE ########################################################
#=========================================================================

