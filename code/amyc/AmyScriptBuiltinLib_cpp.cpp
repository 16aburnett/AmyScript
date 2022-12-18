// AmyScript Built-in library
// Author: Amy Burnett
// ========================================================================

#include <vector>
#include <iostream>
// for recursive lambdas with std::function<>
#include <functional>
// std::memcpy
#include <cstring>

// ========================================================================

// Exits the program with the given exit code 
// void exit(int exit_code)
// - exit_code : [rbp + 16]
// - uses external exit function from libc
// def __builtin__exit__int (exit_code):
//     exit (exit_code)

// ========================================================================

// Frees memory of the given pointer
// *this is not used - delete keyword is used instead
// void free()
// - exit_code : [rbp + 16]
// - uses external exit function from libc
// def __builtin__free (ptr):
//     # do nothing, python has its own garbage collection
//     pass

// ========================================================================
// Prints a given string to the screen
// void print (char[] stringToPrint)
void __builtin__print__char__1 (char* v) {
    printf ("%s", v);
}

// ========================================================================

// Prints an int to the screen
// Utilizes printf "%d"
// void print (int valueToPrint)
void __builtin__print__int (long v) {
    printf ("%ld", v);
}

// ========================================================================

// Prints a char to the screen
// void print (char valueToPrint)
void __builtin__print__char (char v) {
    printf ("%c", v);
}

// ========================================================================

// Prints a float to the screen
// void print (float valueToPrint)
void __builtin__print__float (double v) {
    printf ("%f", v);
}

//========================================================================
// Prints a given string to the screen with a newline at the end
// void println (char[] stringToPrint)
void __builtin__println__char__1 (char* v) {
    printf ("%s\n", v);
}

// ========================================================================

// Prints an int to the screen with a newline
// Utilizes printf "%d"
// void println (int valueToPrint)
void __builtin__println__int (long v) {
    printf ("%ld\n", v);
}

// ========================================================================
// Prints a float to the screen with a newline
// void println (float floatToPrint)
void __builtin__println__float (double v) {
    printf ("%f\n", v);
}

//========================================================================
// Prints a char to the screen with a newline
// void println (char charToPrint)
void __builtin__println__char (char v) {
    printf ("%c\n", v);
}

//========================================================================
// Prints an enum's integer value with a newline
// void println (Enum e)#
// def __builtin__println__Enum (v):
//     print (v)

//========================================================================
// Prints a newline to the console
// void println ()
void __builtin__println () {
    printf ("\n");
}

//========================================================================
// grabs input from the console 
// this waits for a line if there isnt one
// char[] input ()
char* __builtin__input ()
{
    char* buffer = nullptr;
    size_t buflen = 0;
    long num_chars = getline (&buffer, &buflen, stdin);
    // check for eof
    if (num_chars == -1)
        // return null for eof
        return nullptr;
    // return line
    return buffer;
}

//========================================================================
// returns default float value
// float float ()#
// def __builtin__float ():
//     return 0.0

//========================================================================
// converts int to float
// float intToFloat (int value)#
// value : [rbp + 16]
// def __builtin__intToFloat__int (v):
//     return float (v)

//========================================================================
// parses a float from a given char[]
// float stringToFloat (char[])#
// str : [rbp + 16]
// def __builtin__stringToFloat__char__1 (s):
//     return float (s)

//========================================================================
// returns default int value
// int int ()#
// def __builtin__int ():
//     return 0

//========================================================================
// returns default char value
// char char ()#
// def __builtin__char ():
//  return '0'

//========================================================================
// converts float to int
// int floatToInt (float)#
// def __builtin__floatToInt__float (f):
//     # -1 to ignore the null terminator
//     if f[-1] == '\0':
//         return int(''.join(f[:-1]))
//     return int(''.join(f))

//========================================================================
// parses an int from a given char[]
// int stringToInt (char[] str)#
// str : [rbp + 16]
// def __builtin__stringToInt__char__1 (s):
//     # print (s)
//     # try:
//     #     res = int(''.join(s))
//     # except:
//     #     res = 0
//     # return res
//     # -1 to ignore the null terminator
//     if s[-1] == '\0':
//         return int(''.join(s[:-1]))
//     return int(''.join(s))


//========================================================================
// parses an int from a given char
// int charToInt (char)#
// def __builtin__charToInt__char (c):
//     return int(c)

//========================================================================
// converts int to string
// char[] string (int)#
// def __builtin__string__int (i):
//     return str(i)

//========================================================================
// converts float to string
// char[] string (float)#
// def __builtin__string__float (f):
//     return str(f)

//========================================================================

// returns default value for array and object (null)
// null null ()#
// def __builtin__null ():
//     return None

//========================================================================
