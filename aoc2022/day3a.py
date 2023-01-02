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
def exit__int (exit_code):
    exit (exit_code)

# # ========================================================================

# # Frees memory of the given pointer
# # void free()
# # - exit_code : [rbp + 16]
# # - uses external exit function from libc
def free (ptr):
    # do nothing, python has its own garbage collection
    pass

# # ========================================================================
# # Prints a given string to the screen
# # void print (char[] stringToPrint)#
# # stringToPrint : [rbp + 16]
def print__char__1 (s):
    print (s, end="")

# # ========================================================================

# # Prints an int to the screen
# # Utilizes printf "%d"
# # void print (int valueToPrint)#
# # valueToPrint : [rbp + 16]
def print__int (v):
    print (v, end="")

# # ========================================================================

# # Prints a char to the screen
# # Utilizes printf "%c"
# # void print (char valueToPrint)#
# # valueToPrint : [rbp + 16]
def print__char (v):
    print (v, end="")

# # ========================================================================

# # Prints a float to the screen
# # void print (float valueToPrint)
def print__float (v):
    print (v, end="")

# # //========================================================================
# # // Prints a given string to the screen with a newline at the end
# # // void println (char[] stringToPrint)#
# # stringToPrint : [rbp + 16]
def println__char__1 (v):
    print (v)

# # ========================================================================

# # Prints an int to the screen with a newline
# # Utilizes printf "%d"
# # void println (int valueToPrint)#
# # valueToPrint : [rbp + 16]
def println__int (v):
    print (v)

# # ========================================================================
# # // Prints a float to the screen with a newline
# # // void println (float floatToPrint)#
# # valueToPrint : [rbp + 16]
def println__float (v):
    print (v)

# # //========================================================================
# # // Prints a char to the screen with a newline
# # // void println (char charToPrint)#
def println__char (v):
    print (v)

# # //========================================================================
# # // Prints an enum's integer value with a newline
# # // void println (Enum e)#
def println__Enum (v):
    print (v)

# # //========================================================================
# # // Prints a newline to the console
# # // void println ()#
def println ():
    print ()

# # //========================================================================
# # // grabs input from the console 
# # this waits for a line if there isnt one
# # // char[] input ()#
def _input ():
    return input ()

# # //========================================================================
# # // returns default float value
# # // float float ()#
def float ():
    return 0.0

# # //========================================================================
# # // converts int to float
# # // float intToFloat (int value)#
# # value : [rbp + 16]
def intToFloat__int (v):
    return float (v)

# # //========================================================================
# # // parses a float from a given char[]
# # // float stringToFloat (char[])#
# # str : [rbp + 16]
def stringToFloat__char__1 (s):
    return float (s)

# # //========================================================================
# # // returns default int value
# # // int int ()#
def int ():
    return 0

# # //========================================================================
# # // returns default char value
# # // char char ()#
def char ():
 return '0'

# # //========================================================================
# # // converts float to int
# # // int floatToInt (float)#
def floatToInt__float (f):
    return int(f)

# # //========================================================================
# # // parses an int from a given char[]
# # // int stringToInt (char[] str)#
# # str : [rbp + 16]
def stringToInt__char__1 (s):
    return int(s)

# # //========================================================================
# # // parses an int from a given char
# # // int charToInt (char)#
def charToInt__char (c):
    return int(c)

# # //========================================================================
# # // converts int to string
# # // char[] string (int)#
def string__int (i):
    return str(i)

# # //========================================================================
# # // converts float to string
# # // char[] string (float)#
def string__float (f):
    return str(f)

# # //========================================================================

# # // returns default value for array and object (null)
# # // null null ()#
def null ():
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
# End Class Template - 
#=========================================================================

# Statement
# Assignment - '='
# RHS
stack.append(" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
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
# Function Call - input() -> char[]
# Arguments
# *** input
__res = input ()
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
    # Assignment - '='
    # RHS
    stack.append(__main__line)
    __arr = stack.pop ()
    __res = len (__arr)
    stack.append (__res)
    # LHS
    __main__while__0__block__1__size = 0
    __rhs = stack.pop()
    __main__while__0__block__1__size = __rhs
    stack.append (__main__while__0__block__1__size)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(0)
    # LHS
    __main__while__0__block__1__c0 = 0
    __rhs = stack.pop()
    __main__while__0__block__1__c0 = __rhs
    stack.append (__main__while__0__block__1__c0)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Division
    # LHS
    stack.append(__main__while__0__block__1__size)
    # RHS
    # Int Literal
    stack.append(2)
    __rhs = stack.pop()
    __lhs = stack.pop()
    __res = __lhs // __rhs
    stack.append(__res)
    # LHS
    __main__while__0__block__1__e0 = 0
    __rhs = stack.pop()
    __main__while__0__block__1__e0 = __rhs
    stack.append (__main__while__0__block__1__e0)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main__while__0__block__1__e0)
    # LHS
    __main__while__0__block__1__c1 = 0
    __rhs = stack.pop()
    __main__while__0__block__1__c1 = __rhs
    stack.append (__main__while__0__block__1__c1)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    stack.append(__main__while__0__block__1__size)
    # LHS
    __main__while__0__block__1__e1 = 0
    __rhs = stack.pop()
    __main__while__0__block__1__e1 = __rhs
    stack.append (__main__while__0__block__1__e1)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Char Literal
    stack.append('0')
    # LHS
    __main__while__0__block__1__common = 0
    __rhs = stack.pop()
    __main__while__0__block__1__common = __rhs
    stack.append (__main__while__0__block__1__common)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    #---------------------------------------------------------------------
    # For-Loop
    # Init
    # Assignment - '='
    # RHS
    stack.append(__main__while__0__block__1__c0)
    # LHS
    __main__while__0__block__1__for__2__i = 0
    __rhs = stack.pop()
    __main__while__0__block__1__for__2__i = __rhs
    stack.append (__main__while__0__block__1__for__2__i)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        stack.append(__main__while__0__block__1__for__2__i)
        # RHS
        stack.append(__main__while__0__block__1__e0)
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
        stack.append(__main__while__0__block__1__c1)
        # LHS
        __main__while__0__block__1__for__2__block__3__for__4__j = 0
        __rhs = stack.pop()
        __main__while__0__block__1__for__2__block__3__for__4__j = __rhs
        stack.append (__main__while__0__block__1__for__2__block__3__for__4__j)
        # Using an infinite loop so we can write a separate multi-line condition
        while (1):
            # Condition
            # Less Than
            # LHS
            stack.append(__main__while__0__block__1__for__2__block__3__for__4__j)
            # RHS
            stack.append(__main__while__0__block__1__e1)
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
            stack.append(__main__while__0__block__1__for__2__i)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            # RHS
            # Subscript
            # LHS
            stack.append(__main__line)
            # OFFSET
            stack.append(__main__while__0__block__1__for__2__block__3__for__4__j)
            __offset = stack.pop ()
            __pointer = stack.pop ()
            stack.append (__pointer[__offset])
            __rhs = stack.pop ()
            __lhs = stack.pop ()
            __res = __lhs == __rhs
            stack.append (__res)
            __if__6__cond = stack.pop ()
            # get condition from stack
            if (__if__6__cond):
                # Body
                #---------------------------------------------------------
                # Code Block
                # Statement
                # Assignment - '='
                # RHS
                # Subscript
                # LHS
                stack.append(__main__line)
                # OFFSET
                stack.append(__main__while__0__block__1__for__2__i)
                __offset = stack.pop ()
                __pointer = stack.pop ()
                stack.append (__pointer[__offset])
                __rhs = stack.pop()
                __main__while__0__block__1__common = __rhs
                stack.append (__main__while__0__block__1__common)
                # Statement results can be ignored
                stack.pop ()
                # End Statement

                #---------------------------------------------------------
            # End of if
            #-------------------------------------------------------------
            #-------------------------------------------------------------
            # Update
            # Pre-Increment
            # RHS
            stack.append(__main__while__0__block__1__for__2__block__3__for__4__j)
            __rhs = stack.pop ()
            __main__while__0__block__1__for__2__block__3__for__4__j = __main__while__0__block__1__for__2__block__3__for__4__j + 1
            __res = __main__while__0__block__1__for__2__block__3__for__4__j
            stack.append (__res)
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # Update
        # Pre-Increment
        # RHS
        stack.append(__main__while__0__block__1__for__2__i)
        __rhs = stack.pop ()
        __main__while__0__block__1__for__2__i = __main__while__0__block__1__for__2__i + 1
        __res = __main__while__0__block__1__for__2__i
        stack.append (__res)
    #---------------------------------------------------------------------
    # Statement
    # Function Call - println(char) -> void
    # Arguments
    stack.append(__main__while__0__block__1__common)
    __arg0 = stack.pop ()
    # *** println
    __res = println__char (__arg0)
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Int Literal
    stack.append(0)
    # LHS
    __main__while__0__block__1__score = 0
    __rhs = stack.pop()
    __main__while__0__block__1__score = __rhs
    stack.append (__main__while__0__block__1__score)
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
    __main__while__0__block__1__for__8__i = 0
    __rhs = stack.pop()
    __main__while__0__block__1__for__8__i = __rhs
    stack.append (__main__while__0__block__1__for__8__i)
    # Using an infinite loop so we can write a separate multi-line condition
    while (1):
        # Condition
        # Less Than
        # LHS
        stack.append(__main__while__0__block__1__for__8__i)
        # RHS
        stack.append(__main__letters)
        __arr = stack.pop ()
        __res = len (__arr)
        stack.append (__res)
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
        stack.append(__main__while__0__block__1__for__8__i)
        __offset = stack.pop ()
        __pointer = stack.pop ()
        stack.append (__pointer[__offset])
        # RHS
        stack.append(__main__while__0__block__1__common)
        __rhs = stack.pop ()
        __lhs = stack.pop ()
        __res = __lhs == __rhs
        stack.append (__res)
        __if__10__cond = stack.pop ()
        # get condition from stack
        if (__if__10__cond):
            # Body
            # Statement
            # Assignment - '='
            # RHS
            stack.append(__main__while__0__block__1__for__8__i)
            __rhs = stack.pop()
            __main__while__0__block__1__score = __rhs
            stack.append (__main__while__0__block__1__score)
            # Statement results can be ignored
            stack.pop ()
            # End Statement

        # End of if
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
        # Update
        # Pre-Increment
        # RHS
        stack.append(__main__while__0__block__1__for__8__i)
        __rhs = stack.pop ()
        __main__while__0__block__1__for__8__i = __main__while__0__block__1__for__8__i + 1
        __res = __main__while__0__block__1__for__8__i
        stack.append (__res)
    #---------------------------------------------------------------------
    # Statement
    # Function Call - println(int) -> void
    # Arguments
    stack.append(__main__while__0__block__1__score)
    __arg0 = stack.pop ()
    # *** println
    __res = println__int (__arg0)
    stack.append (__res) # function call result
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '+='
    # RHS
    stack.append(__main__while__0__block__1__score)
    __rhs = stack.pop()
    __main__total = __main__total + __rhs
    stack.append (__main__total)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    stack.append(__main__line)
    __arr = stack.pop ()
    free (__arr)
    stack.append (0)
    # Statement results can be ignored
    stack.pop ()
    # End Statement

    # Statement
    # Assignment - '='
    # RHS
    # Function Call - input() -> char[]
    # Arguments
    # *** input
    __res = input ()
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
# Function Call - println(int) -> void
# Arguments
stack.append(__main__total)
__arg0 = stack.pop ()
# *** println
__res = println__int (__arg0)
stack.append (__res) # function call result
# Statement results can be ignored
stack.pop ()
# End Statement


#=========================================================================
#### END OF CODE ########################################################
#=========================================================================

