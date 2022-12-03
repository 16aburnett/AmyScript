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
#### COMPILED CODE ######################################################
#=========================================================================

#=========================================================================
# Class Template - 
    # Instances:
        #=================================================================
        # Class Declaration - __main____Vector__int inherits __main__Object
            # Creating Dispatch Table
MALLOC __dtable____main____Vector__int 4                # Populate Dispatch Table
ASSIGN __dtable____main____Vector__int[0] __method____main____Vector__int____pushBack__intASSIGN __dtable____main____Vector__int[1] __method____main____Vector__int____popBackASSIGN __dtable____main____Vector__int[2] __method____main____Vector__int____get__intASSIGN __dtable____main____Vector__int[3] __method____main____Vector__int____set__int__int            #-------------------------------------------------------------
            # Field - int[] Vector<:int:>::data
ASSIGN __field____main____Vector__int____data 1            #-------------------------------------------------------------
            #-------------------------------------------------------------
            # Field - int Vector<:int:>::size
ASSIGN __field____main____Vector__int____size 2            #-------------------------------------------------------------
            #-------------------------------------------------------------
            # Field - int Vector<:int:>::capacity
ASSIGN __field____main____Vector__int____capacity 3            #-------------------------------------------------------------
        # skip over class methods
JUMP __endclass____main____Vector__int            #-------------------------------------------------------------
            # Constructor Declaration - Vector<:int:>::Vector() -> Vector<:int:>
JUMP __end__ctor____main____Vector__int____Vector__ctor____main____Vector__int____Vector:                # Creating Class Instance
MALLOC __this 4                    # Add Dispatch Table
ASSIGN __this[0] __dtable____main____Vector__int                # Parameters
                # Body
                    #-----------------------------------------------------
                    # Code Block
                                        # LHS
                        # Member Accessor Assignment
                            # LHS
                                # This keyword
PUSH __this                            # RHS
PUSH __field____main____Vector__int____capacityPOP __childPOP __parentPOP __rhs = 10
                                        # LHS
                        # Member Accessor Assignment
                            # LHS
                                # This keyword
PUSH __this                            # RHS
PUSH __field____main____Vector__int____sizePOP __childPOP __parentPOP __rhs = 0
                                        # LHS
                        # Member Accessor Assignment
                            # LHS
                                # This keyword
PUSH __this                            # RHS
PUSH __field____main____Vector__int____dataPOP __childPOP __parentPOP __rhs = [None] *                     # Member Accessor
                        # LHS
                            # This keyword
PUSH __this                        # RHS
PUSH __field____main____Vector__int____capacityPOP __childPOP __parentPUSH __parent[__child]
                    #-----------------------------------------------------
RETURN __this__end__ctor____main____Vector__int____Vector:            # End Constructor Declaration - __ctor____main____Vector__int____Vector
            #-------------------------------------------------------------

            #-------------------------------------------------------------
            # Method Declaration - Vector<:int:>::pushBack(int) -> void
JUMP __end__method____main____Vector__int____pushBack__int__method____main____Vector__int____pushBack__int:                # Class Instance
STACKGET __this 0                # Parameters
                    # Param: val
__main____Vector__int__pushBack__valSTACKGET __main____Vector__int__pushBack__val 1                # Body
                    #-----------------------------------------------------
                    # Code Block
                    #-----------------------------------------------------
                    # If-Statement
                    if (                    # Member Accessor
                        # LHS
                            # This keyword
PUSH __this                        # RHS
PUSH __field____main____Vector__int____sizePOP __childPOP __parentPUSH __parent[__child] + 1 >=                     # Member Accessor
                        # LHS
                            # This keyword
PUSH __this                        # RHS
PUSH __field____main____Vector__int____capacityPOP __childPOP __parentPUSH __parent[__child]):
                        # Body
                        #-------------------------------------------------
                        # Code Block
                                                # LHS
                            # Member Accessor Assignment
                                # LHS
                                    # This keyword
PUSH __this                                # RHS
PUSH __field____main____Vector__int____capacityPOP __childPOP __parentPOP __rhs =                         # Member Accessor
                            # LHS
                                # This keyword
PUSH __this                            # RHS
PUSH __field____main____Vector__int____capacityPOP __childPOP __parentPUSH __parent[__child] * 2
                        __main____Vector__int__pushBack__block__1__if__2__block__3__nData = [None] *                         # Member Accessor
                            # LHS
                                # This keyword
PUSH __this                            # RHS
PUSH __field____main____Vector__int____capacityPOP __childPOP __parentPUSH __parent[__child]
                        #-------------------------------------------------
                        # For-Loop
                        # Init
__main____Vector__int__pushBack__block__1__if__2__block__3__for__4__i = 0
                        while (__main____Vector__int__pushBack__block__1__if__2__block__3__for__4__i <                         # Member Accessor
                            # LHS
                                # This keyword
PUSH __this                            # RHS
PUSH __field____main____Vector__int____sizePOP __childPOP __parentPUSH __parent[__child]):
                            #---------------------------------------------
                            # Code Block
                            __main____Vector__int__pushBack__block__1__if__2__block__3__nData[__main____Vector__int__pushBack__block__1__if__2__block__3__for__4__i] =                             # Member Accessor
                                # LHS
                                    # This keyword
PUSH __this                                # RHS
PUSH __field____main____Vector__int____dataPOP __childPOP __parentPUSH __parent[__child][__main____Vector__int__pushBack__block__1__if__2__block__3__for__4__i]
                            #---------------------------------------------
                            __main____Vector__int__pushBack__block__1__if__2__block__3__for__4__i += 1
                        #-------------------------------------------------
                        free (                        # Member Accessor
                            # LHS
                                # This keyword
PUSH __this                            # RHS
PUSH __field____main____Vector__int____dataPOP __childPOP __parentPUSH __parent[__child])
                                                # LHS
                            # Member Accessor Assignment
                                # LHS
                                    # This keyword
PUSH __this                                # RHS
PUSH __field____main____Vector__int____dataPOP __childPOP __parentPOP __rhs = __main____Vector__int__pushBack__block__1__if__2__block__3__nData
                        #-------------------------------------------------
                    #-----------------------------------------------------
                                        # Member Accessor
                        # LHS
                            # This keyword
PUSH __this                        # RHS
PUSH __field____main____Vector__int____dataPOP __childPOP __parentPUSH __parent[__child][                    # Member Accessor
                        # LHS
                            # This keyword
PUSH __this                        # RHS
PUSH __field____main____Vector__int____sizePOP __childPOP __parentPUSH __parent[__child]] = __main____Vector__int__pushBack__val
                                        # Member Accessor
                        # LHS
                            # This keyword
PUSH __this                        # RHS
PUSH __field____main____Vector__int____sizePOP __childPOP __parentPUSH __parent[__child] += 1
                    #-----------------------------------------------------
RETURN 0__end__method____main____Vector__int____pushBack__int:            # End Method Declaration - __method____main____Vector__int____pushBack__int
            #-------------------------------------------------------------

            #-------------------------------------------------------------
            # Method Declaration - Vector<:int:>::popBack() -> int
JUMP __end__method____main____Vector__int____popBack__method____main____Vector__int____popBack:                # Class Instance
STACKGET __this 0                # Parameters
                # Body
                    #-----------------------------------------------------
                    # Code Block
                    return                     # Member Accessor
                        # LHS
                            # This keyword
PUSH __this                        # RHS
PUSH __field____main____Vector__int____dataPOP __childPOP __parentPUSH __parent[__child][                    # Member Accessor
                        # LHS
                            # This keyword
PUSH __this                        # RHS
PUSH __field____main____Vector__int____sizePOP __childPOP __parentPUSH __parent[__child] -= 1]
                    #-----------------------------------------------------
RETURN 0__end__method____main____Vector__int____popBack:            # End Method Declaration - __method____main____Vector__int____popBack
            #-------------------------------------------------------------

            #-------------------------------------------------------------
            # Method Declaration - Vector<:int:>::get(int) -> int
JUMP __end__method____main____Vector__int____get__int__method____main____Vector__int____get__int:                # Class Instance
STACKGET __this 0                # Parameters
                    # Param: index
__main____Vector__int__get__indexSTACKGET __main____Vector__int__get__index 1                # Body
                    #-----------------------------------------------------
                    # Code Block
                    return                     # Member Accessor
                        # LHS
                            # This keyword
PUSH __this                        # RHS
PUSH __field____main____Vector__int____dataPOP __childPOP __parentPUSH __parent[__child][__main____Vector__int__get__index]
                    #-----------------------------------------------------
RETURN 0__end__method____main____Vector__int____get__int:            # End Method Declaration - __method____main____Vector__int____get__int
            #-------------------------------------------------------------

            #-------------------------------------------------------------
            # Method Declaration - Vector<:int:>::set(int, int) -> void
JUMP __end__method____main____Vector__int____set__int__int__method____main____Vector__int____set__int__int:                # Class Instance
STACKGET __this 0                # Parameters
                    # Param: index
__main____Vector__int__set__indexSTACKGET __main____Vector__int__set__index 1                    # Param: value
__main____Vector__int__set__valueSTACKGET __main____Vector__int__set__value 2                # Body
                    #-----------------------------------------------------
                    # Code Block
                                        # Member Accessor
                        # LHS
                            # This keyword
PUSH __this                        # RHS
PUSH __field____main____Vector__int____dataPOP __childPOP __parentPUSH __parent[__child][__main____Vector__int__set__index] = __main____Vector__int__set__value
                    #-----------------------------------------------------
RETURN 0__end__method____main____Vector__int____set__int__int:            # End Method Declaration - __method____main____Vector__int____set__int__int
            #-------------------------------------------------------------

__endclass____main____Vector__int:        # End Class Declaration - __main____Vector__int
        #=================================================================

# End Class Template - 
#=========================================================================

__main__elfCalories = # Constructor Call - Vector<:int:>::Vector() -> Vector<:int:>
    # Arguments
    # Pushing args in reverse order
CALL __ctor____main____Vector__int____Vector    # Remove args
RESPONSE __retvalPUSH __retval
__main__line = input ()
#-------------------------------------------------------------------------
# While-Loop
while (__main__line[0] != '$'):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    __main__while__9__block__10__calorieTotal = 0
    #---------------------------------------------------------------------
    # While-Loop
    while (__main__line[0] != '\n' and __main__line[0] != '$'):
        # Body
        #-----------------------------------------------------------------
        # Code Block
        __main__while__9__block__10__calorieTotal += stringToInt__char__1 (__main__line)
        free (__main__line)
        __main__line = input ()
        #-----------------------------------------------------------------
    #---------------------------------------------------------------------
        # Method Call - Vector<:int:>::pushBack(int) -> void
        # LHS
__main__elfCalories        # RHS
        # Arguments
__main__while__9__block__10__calorieTotalPOP __arg0POP __obj        # Pushing args in reverse order
PUSH __arg0PUSH __objCALL __method____main____Vector__int____pushBack__intPOP __void        # Remove args
POP __voidRESPONSE __retvalPUSH __retval
    #---------------------------------------------------------------------
    # If-Statement
    if (__main__line[0] == '$'):
        # Body
        # Break out of __while__9
        break
    #---------------------------------------------------------------------
    free (__main__line)
    __main__line = input ()
    #---------------------------------------------------------------------
#-------------------------------------------------------------------------
__main__maxCalories = 0
#-------------------------------------------------------------------------
# For-Loop
# Init
__main__for__14__i = 0
while (__main__for__14__i < # Member Accessor
    # LHS
__main__elfCalories    # RHS
PUSH __field____main____Vector__int____sizePOP __childPOP __parentPUSH __parent[__child]):
    #---------------------------------------------------------------------
    # If-Statement
    if (    # Method Call - Vector<:int:>::get(int) -> int
        # LHS
__main__elfCalories        # RHS
        # Arguments
__main__for__14__iPOP __arg0POP __obj        # Pushing args in reverse order
PUSH __arg0PUSH __objCALL __method____main____Vector__int____get__intPOP __void        # Remove args
POP __voidRESPONSE __retvalPUSH __retval > __main__maxCalories):
        # Body
        __main__maxCalories =         # Method Call - Vector<:int:>::get(int) -> int
            # LHS
__main__elfCalories            # RHS
            # Arguments
__main__for__14__iPOP __arg0POP __obj            # Pushing args in reverse order
PUSH __arg0PUSH __objCALL __method____main____Vector__int____get__intPOP __void            # Remove args
POP __voidRESPONSE __retvalPUSH __retval
    #---------------------------------------------------------------------
    __main__for__14__i += 1
#-------------------------------------------------------------------------
println__int (__main__maxCalories)

#=========================================================================
#### END OF CODE ########################################################
#=========================================================================

