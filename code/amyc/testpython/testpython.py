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
# # free__void__: 
# #         push    rbp 
# #         mov     rbp, rsp 
        


# #         pop     rbp 
# #         ret

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

__main__str0 = "Hello,"
__main__c = ' '
__main__str1 = "World!"
print__char__1 (__main__str0)
print__char (__main__c)
println__char__1 (__main__str1)
__main__a = 20
__main__b = 22
println__int (__main__a + __main__b * __main__a)
#=========================================================================
# Function Declaration - sum(int, int) -> int
def __main____sum__int__int (__main__sum__a, __main__sum__b):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    return __main__sum__a + __main__sum__b
    #---------------------------------------------------------------------
# End Function Declaration - __main____sum__int__int
#=========================================================================

println__int (__main____sum__int__int (7, __main__a))
#-------------------------------------------------------------------------
# For-Loop
# Init
__main__for__1__i = 0
while (__main__for__1__i < 10):
    #---------------------------------------------------------------------
    # Code Block
    print__int (__main__for__1__i)
    print__char (' ')
    #---------------------------------------------------------------------
    __main__for__1__i += 1
#-------------------------------------------------------------------------
println ()
__main__x = 1.0
#-------------------------------------------------------------------------
# While-Loop
while (1):
    # Body
    #---------------------------------------------------------------------
    # Code Block
    #---------------------------------------------------------------------
    # If-Statement
    if (__main__x < 0.2):
        # Body
        # Break out of __while__3
        break
    #---------------------------------------------------------------------
    # Elif-Statement
    elif (__main__x == 1.0):
        # Body
        println__char__1 ("yeah")
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    # Else-Statement
    else:
        println__char__1 ("hey")
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    __main__x /= 2.0
    # Continue in __while__3
    continue
    #---------------------------------------------------------------------
#-------------------------------------------------------------------------
println__float (__main__x)
#-------------------------------------------------------------------------
# Code Block
__main__block__6__N = 5
__main__block__6__arr = [None] * __main__block__6__N
#-------------------------------------------------------------------------
# For-Loop
# Init
__main__block__6__for__7__i = 0
while (__main__block__6__for__7__i < __main__block__6__N):
    #---------------------------------------------------------------------
    # Code Block
    __main__block__6__arr[__main__block__6__for__7__i] = __main__block__6__for__7__i * 2
    #---------------------------------------------------------------------
    __main__block__6__for__7__i += 1
#-------------------------------------------------------------------------
print__int (__main__block__6__arr[0])
#-------------------------------------------------------------------------
# For-Loop
# Init
__main__block__6__for__9__i = 1
while (__main__block__6__for__9__i < __main__block__6__N):
    #---------------------------------------------------------------------
    # Code Block
    print__char (' ')
    print__int (__main__block__6__arr[__main__block__6__for__9__i])
    #---------------------------------------------------------------------
    __main__block__6__for__9__i += 1
#-------------------------------------------------------------------------
println ()
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Code Block
print__char__1 ("Enter your name => ")
__main__block__11__line = input ()
print__char__1 ("Hi, ")
println__char__1 (__main__block__11__line)
#-------------------------------------------------------------------------

#=========================================================================
#### END OF CODE ########################################################
#=========================================================================

