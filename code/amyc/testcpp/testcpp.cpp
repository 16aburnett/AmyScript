// Generated C++ code compiled from AmyScript
//=========================================================================

//=========================================================================
//### LIBRARY CODE #######################################################
//=========================================================================

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
//=========================================================================
//### All code must be in main ###########################################
//=========================================================================

int main () {
    //=====================================================================
    //### SETUP EXPRESSION RESULT STACK ##################################
    //=====================================================================

    // Function Header
    // This stack is used to store results of expressions
    std::vector<long> stack;
    // Declare general purpose variables
    // These are longs and can store anything up to 8 bytes via casting
    long __lhs = 0;
    long __rhs = 0;
    long __res = 0;
    long __stackval = 0;
    long __pointer = 0;
    long __offset = 0;
    long __parent = 0;
    long __child = 0;
    //=====================================================================
    //### COMPILED CODE ##################################################
    //=====================================================================

    // Statement
    // Assignment - '='
    // RHS
    // Int Literal
    stack.push_back (42);
    // LHS
    // Variable declaration
    long __main__x;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__x = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__x));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Assignment - '='
    // RHS
    // Float Literal
    {
        double float_literal = 3.14;
        stack.push_back (*reinterpret_cast<long*>(&float_literal));
    }
    // LHS
    // Variable declaration
    double __main__y;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__y = *reinterpret_cast<double*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__y));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Assignment - '='
    // RHS
    // Char Literal
    stack.push_back (static_cast<long>(static_cast<unsigned char>('X')));
    // LHS
    // Variable declaration
    char __main__c;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__c = static_cast<char>(static_cast<unsigned char>(__rhs));
    // Result of assignment
    stack.push_back (static_cast<long>(static_cast<unsigned char>(__main__c)));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(int) -> void
    {
        // Arguments
        stack.push_back (*reinterpret_cast<long*>(&__main__x));
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        long __arg0 = *reinterpret_cast<long*>(&__stackval);
        // println
        __builtin__println__int (__arg0);
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(float) -> void
    {
        // Arguments
        stack.push_back (*reinterpret_cast<long*>(&__main__y));
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        double __arg0 = *reinterpret_cast<double*>(&__stackval);
        // println
        __builtin__println__float (__arg0);
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(char) -> void
    {
        // Arguments
        stack.push_back (static_cast<long>(static_cast<unsigned char>(__main__c)));
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        char __arg0 = static_cast<char>(static_cast<unsigned char>(__stackval));
        // println
        __builtin__println__char (__arg0);
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    //---------------------------------------------------------------------
    // Code Block
    // Statement
    // Assignment - '='
    // RHS
    // Int Literal
    stack.push_back (21);
    // LHS
    // Variable declaration
    long __main__block__0__a;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__0__a = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__0__a));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Assignment - '='
    // RHS
    // Int Literal
    stack.push_back (39);
    // LHS
    // Variable declaration
    long __main__block__0__b;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__0__b = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__0__b));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Assignment - '='
    // RHS
    // Addition
    {
        // LHS
        stack.push_back (*reinterpret_cast<long*>(&__main__block__0__a));
        // RHS
        stack.push_back (*reinterpret_cast<long*>(&__main__block__0__b));
        __rhs = stack.back ();
        stack.pop_back ();
        __lhs = stack.back ();
        stack.pop_back ();
        long __res = *reinterpret_cast<long*>(&__lhs) + *reinterpret_cast<long*>(&__rhs);
        stack.push_back (*reinterpret_cast<long*>(&__res));
    }
    // LHS
    // Variable declaration
    long __main__block__0__c;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__0__c = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__0__c));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(int) -> void
    {
        // Arguments
        stack.push_back (*reinterpret_cast<long*>(&__main__block__0__c));
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        long __arg0 = *reinterpret_cast<long*>(&__stackval);
        // println
        __builtin__println__int (__arg0);
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    //---------------------------------------------------------------------
    //---------------------------------------------------------------------
    // Code Block
    // Statement
    // Assignment - '='
    // RHS
    // Float Literal
    {
        double float_literal = 0.25;
        stack.push_back (*reinterpret_cast<long*>(&float_literal));
    }
    // LHS
    // Variable declaration
    double __main__block__1__a;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__1__a = *reinterpret_cast<double*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__1__a));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Assignment - '='
    // RHS
    // Float Literal
    {
        double float_literal = 3.53;
        stack.push_back (*reinterpret_cast<long*>(&float_literal));
    }
    // LHS
    // Variable declaration
    double __main__block__1__b;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__1__b = *reinterpret_cast<double*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__1__b));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Assignment - '='
    // RHS
    // Addition
    {
        // LHS
        stack.push_back (*reinterpret_cast<long*>(&__main__block__1__a));
        // RHS
        stack.push_back (*reinterpret_cast<long*>(&__main__block__1__b));
        __rhs = stack.back ();
        stack.pop_back ();
        __lhs = stack.back ();
        stack.pop_back ();
        double __res = *reinterpret_cast<double*>(&__lhs) + *reinterpret_cast<double*>(&__rhs);
        stack.push_back (*reinterpret_cast<long*>(&__res));
    }
    // LHS
    // Variable declaration
    double __main__block__1__c;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__1__c = *reinterpret_cast<double*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__1__c));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(float) -> void
    {
        // Arguments
        stack.push_back (*reinterpret_cast<long*>(&__main__block__1__c));
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        double __arg0 = *reinterpret_cast<double*>(&__stackval);
        // println
        __builtin__println__float (__arg0);
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    //---------------------------------------------------------------------
    //---------------------------------------------------------------------
    // Code Block
    // Statement
    // Assignment - '='
    // RHS
    // Float Literal
    {
        double float_literal = 0.25;
        stack.push_back (*reinterpret_cast<long*>(&float_literal));
    }
    // LHS
    // Variable declaration
    double __main__block__2__a;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__2__a = *reinterpret_cast<double*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__2__a));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Assignment - '='
    // RHS
    // Float Literal
    {
        double float_literal = 100.0;
        stack.push_back (*reinterpret_cast<long*>(&float_literal));
    }
    // LHS
    // Variable declaration
    double __main__block__2__b;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__2__b = *reinterpret_cast<double*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__2__b));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Assignment - '='
    // RHS
    // Multiplication
    {
        // LHS
        stack.push_back (*reinterpret_cast<long*>(&__main__block__2__a));
        // RHS
        stack.push_back (*reinterpret_cast<long*>(&__main__block__2__b));
        __rhs = stack.back ();
        stack.pop_back ();
        __lhs = stack.back ();
        stack.pop_back ();
        double __res = *reinterpret_cast<double*>(&__lhs) * *reinterpret_cast<double*>(&__rhs);
        stack.push_back (*reinterpret_cast<long*>(&__res));
    }
    // LHS
    // Variable declaration
    double __main__block__2__c;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__2__c = *reinterpret_cast<double*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__2__c));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(float) -> void
    {
        // Arguments
        stack.push_back (*reinterpret_cast<long*>(&__main__block__2__c));
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        double __arg0 = *reinterpret_cast<double*>(&__stackval);
        // println
        __builtin__println__float (__arg0);
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(float) -> void
    {
        // Arguments
        // Division
        {
            // LHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__2__a));
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__2__b));
            __rhs = stack.back ();
            stack.pop_back ();
            __lhs = stack.back ();
            stack.pop_back ();
            double __res = *reinterpret_cast<double*>(&__lhs) / *reinterpret_cast<double*>(&__rhs);
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        double __arg0 = *reinterpret_cast<double*>(&__stackval);
        // println
        __builtin__println__float (__arg0);
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(int) -> void
    {
        // Arguments
        // Modulus
        {
            // LHS
            // Int Literal
            stack.push_back (21);
            // RHS
            // Int Literal
            stack.push_back (2);
            __rhs = stack.back ();
            stack.pop_back ();
            __lhs = stack.back ();
            stack.pop_back ();
            long __res = *reinterpret_cast<long*>(&__lhs) % *reinterpret_cast<long*>(&__rhs);
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        long __arg0 = *reinterpret_cast<long*>(&__stackval);
        // println
        __builtin__println__int (__arg0);
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(int) -> void
    {
        // Arguments
        // Modulus
        {
            // LHS
            // Int Literal
            stack.push_back (34);
            // RHS
            // Int Literal
            stack.push_back (7);
            __rhs = stack.back ();
            stack.pop_back ();
            __lhs = stack.back ();
            stack.pop_back ();
            long __res = *reinterpret_cast<long*>(&__lhs) % *reinterpret_cast<long*>(&__rhs);
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        long __arg0 = *reinterpret_cast<long*>(&__stackval);
        // println
        __builtin__println__int (__arg0);
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    //---------------------------------------------------------------------
    //---------------------------------------------------------------------
    // Code Block
    // Statement
    // Assignment - '='
    // RHS
    // Int Literal
    stack.push_back (0);
    // LHS
    // Variable declaration
    long __main__block__3__x;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__3__x = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__3__x));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(int) -> void
    {
        // Arguments
        // Pre-Increment
        {
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__3__x));
            __rhs = stack.back ();
            stack.pop_back ();
            __main__block__3__x = __main__block__3__x + 1;
            __res = __main__block__3__x;
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        long __arg0 = *reinterpret_cast<long*>(&__stackval);
        // println
        __builtin__println__int (__arg0);
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(int) -> void
    {
        // Arguments
        stack.push_back (*reinterpret_cast<long*>(&__main__block__3__x));
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        long __arg0 = *reinterpret_cast<long*>(&__stackval);
        // println
        __builtin__println__int (__arg0);
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(int) -> void
    {
        // Arguments
        // Pre-Increment
        {
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__3__x));
            __rhs = stack.back ();
            stack.pop_back ();
            __main__block__3__x = __main__block__3__x + 1;
            __res = __main__block__3__x;
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        long __arg0 = *reinterpret_cast<long*>(&__stackval);
        // println
        __builtin__println__int (__arg0);
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(int) -> void
    {
        // Arguments
        // Pre-Decrement
        {
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__3__x));
            __rhs = stack.back ();
            stack.pop_back ();
            __main__block__3__x = __main__block__3__x - 1;
            __res = __main__block__3__x;
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        long __arg0 = *reinterpret_cast<long*>(&__stackval);
        // println
        __builtin__println__int (__arg0);
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(int) -> void
    {
        // Arguments
        stack.push_back (*reinterpret_cast<long*>(&__main__block__3__x));
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        long __arg0 = *reinterpret_cast<long*>(&__stackval);
        // println
        __builtin__println__int (__arg0);
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(int) -> void
    {
        // Arguments
        // Negative
        {
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__3__x));
            __rhs = stack.back ();
            stack.pop_back ();
            long __res = -*reinterpret_cast<long*>(&__rhs);
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        long __arg0 = *reinterpret_cast<long*>(&__stackval);
        // println
        __builtin__println__int (__arg0);
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(int) -> void
    {
        // Arguments
        // Negate
        {
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__3__x));
            __rhs = stack.back ();
            stack.pop_back ();
            long __res = !*reinterpret_cast<long*>(&__rhs);
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        long __arg0 = *reinterpret_cast<long*>(&__stackval);
        // println
        __builtin__println__int (__arg0);
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(int) -> void
    {
        // Arguments
        // Bitwise Negation
        {
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__3__x));
            __rhs = stack.back ();
            stack.pop_back ();
            long __res = ~*reinterpret_cast<long*>(&__rhs);
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        long __arg0 = *reinterpret_cast<long*>(&__stackval);
        // println
        __builtin__println__int (__arg0);
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Assignment - '='
    // RHS
    // Int Literal
    stack.push_back (0);
    // LHS
    // Variable declaration
    long __main__block__3__y;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__3__y = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__3__y));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(int) -> void
    {
        // Arguments
        // Assignment - '='
        // RHS
        // Pre-Increment
        {
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__3__x));
            __rhs = stack.back ();
            stack.pop_back ();
            __main__block__3__x = __main__block__3__x + 1;
            __res = __main__block__3__x;
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        __rhs = stack.back ();
        stack.pop_back ();
        __main__block__3__y = *reinterpret_cast<long*>(&__rhs);
        // Result of assignment
        stack.push_back (*reinterpret_cast<long*>(&__main__block__3__y));
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        long __arg0 = *reinterpret_cast<long*>(&__stackval);
        // println
        __builtin__println__int (__arg0);
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(int) -> void
    {
        // Arguments
        stack.push_back (*reinterpret_cast<long*>(&__main__block__3__y));
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        long __arg0 = *reinterpret_cast<long*>(&__stackval);
        // println
        __builtin__println__int (__arg0);
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    //---------------------------------------------------------------------
    //---------------------------------------------------------------------
    // Code Block
    // Statement
    // Assignment - '='
    // RHS
    // Int Literal
    stack.push_back (7);
    // LHS
    // Variable declaration
    long __main__block__4__x;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__4__x = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__4__x));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(int) -> void
    {
        // Arguments
        // Post-Increment
        {
            long __res = __main__block__4__x;
            __main__block__4__x = __main__block__4__x + 1;
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        long __arg0 = *reinterpret_cast<long*>(&__stackval);
        // println
        __builtin__println__int (__arg0);
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(int) -> void
    {
        // Arguments
        stack.push_back (*reinterpret_cast<long*>(&__main__block__4__x));
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        long __arg0 = *reinterpret_cast<long*>(&__stackval);
        // println
        __builtin__println__int (__arg0);
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(int) -> void
    {
        // Arguments
        // Post-Decrement
        {
            long __res = __main__block__4__x;
            __main__block__4__x = __main__block__4__x - 1;
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        long __arg0 = *reinterpret_cast<long*>(&__stackval);
        // println
        __builtin__println__int (__arg0);
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(int) -> void
    {
        // Arguments
        stack.push_back (*reinterpret_cast<long*>(&__main__block__4__x));
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        long __arg0 = *reinterpret_cast<long*>(&__stackval);
        // println
        __builtin__println__int (__arg0);
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    //---------------------------------------------------------------------
    //---------------------------------------------------------------------
    // Code Block
    //=====================================================================
    // Function Declaration - sum(int, int) -> int
    auto __main__block__5____sum__int__int = [&stack] (long __main__block__5__sum__a, long __main__block__5__sum__b)
    {
        // Function Header
        // This stack is used to store results of expressions
        std::vector<long> stack;
        // Declare general purpose variables
        // These are longs and can store anything up to 8 bytes via casting
        long __lhs = 0;
        long __rhs = 0;
        long __res = 0;
        long __stackval = 0;
        long __pointer = 0;
        long __offset = 0;
        long __parent = 0;
        long __child = 0;
        // Body
        //-----------------------------------------------------------------
        // Code Block
        // Return
        // Addition
        {
            // LHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__5__sum__a));
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__5__sum__b));
            __rhs = stack.back ();
            stack.pop_back ();
            __lhs = stack.back ();
            stack.pop_back ();
            long __res = *reinterpret_cast<long*>(&__lhs) + *reinterpret_cast<long*>(&__rhs);
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        __res = stack.back ();
        stack.pop_back ();
        return *reinterpret_cast<long*>(&__res);
        //-----------------------------------------------------------------
    };
    // End Function Declaration - __main__block__5____sum__int__int
    //=====================================================================

    // Statement
    // Function Call - println(int) -> void
    {
        // Arguments
        // Function Call - sum(int, int) -> int
        {
            // Arguments
            // Int Literal
            stack.push_back (7);
            // Int Literal
            stack.push_back (4);
            
            __stackval = stack.back ();
            stack.pop_back ();
            // Reinterpret from general register
            long __arg1 = *reinterpret_cast<long*>(&__stackval);
            
            __stackval = stack.back ();
            stack.pop_back ();
            // Reinterpret from general register
            long __arg0 = *reinterpret_cast<long*>(&__stackval);
            // sum
            long __res = __main__block__5____sum__int__int (__arg0, __arg1);
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        long __arg0 = *reinterpret_cast<long*>(&__stackval);
        // println
        __builtin__println__int (__arg0);
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    //=====================================================================
    // Function Declaration - sum(float, float) -> float
    auto __main__block__5____sum__float__float = [&stack] (double __main__block__5__sum__a, double __main__block__5__sum__b)
    {
        // Function Header
        // This stack is used to store results of expressions
        std::vector<long> stack;
        // Declare general purpose variables
        // These are longs and can store anything up to 8 bytes via casting
        long __lhs = 0;
        long __rhs = 0;
        long __res = 0;
        long __stackval = 0;
        long __pointer = 0;
        long __offset = 0;
        long __parent = 0;
        long __child = 0;
        // Body
        //-----------------------------------------------------------------
        // Code Block
        // Return
        // Addition
        {
            // LHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__5__sum__a));
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__5__sum__b));
            __rhs = stack.back ();
            stack.pop_back ();
            __lhs = stack.back ();
            stack.pop_back ();
            double __res = *reinterpret_cast<double*>(&__lhs) + *reinterpret_cast<double*>(&__rhs);
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        __res = stack.back ();
        stack.pop_back ();
        return *reinterpret_cast<double*>(&__res);
        //-----------------------------------------------------------------
    };
    // End Function Declaration - __main__block__5____sum__float__float
    //=====================================================================

    // Statement
    // Function Call - println(float) -> void
    {
        // Arguments
        // Function Call - sum(float, float) -> float
        {
            // Arguments
            // Float Literal
            {
                double float_literal = 0.25;
                stack.push_back (*reinterpret_cast<long*>(&float_literal));
            }
            // Float Literal
            {
                double float_literal = 0.05;
                stack.push_back (*reinterpret_cast<long*>(&float_literal));
            }
            
            __stackval = stack.back ();
            stack.pop_back ();
            // Reinterpret from general register
            double __arg1 = *reinterpret_cast<double*>(&__stackval);
            
            __stackval = stack.back ();
            stack.pop_back ();
            // Reinterpret from general register
            double __arg0 = *reinterpret_cast<double*>(&__stackval);
            // sum
            double __res = __main__block__5____sum__float__float (__arg0, __arg1);
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        double __arg0 = *reinterpret_cast<double*>(&__stackval);
        // println
        __builtin__println__float (__arg0);
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    //---------------------------------------------------------------------
    //---------------------------------------------------------------------
    // Code Block
    // Statement
    // Assignment - '='
    // RHS
    // String Literal
    {
        char str_literal[] = "Hello, world!";
        // convert to a heap string
        char* str = new char[14];
        // copy string to heap allocation
        std::memcpy (str, &str_literal, 14);
        stack.push_back (reinterpret_cast<long> (str));
    }
    // LHS
    // Variable declaration
    char* __main__block__8__str;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__8__str = *reinterpret_cast<char**>(&__rhs);
    // Result of assignment
    stack.push_back (reinterpret_cast<long>(__main__block__8__str));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(char[]) -> void
    {
        // Arguments
        stack.push_back (reinterpret_cast<long>(__main__block__8__str));
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        char* __arg0 = *reinterpret_cast<char**>(&__stackval);
        // println
        __builtin__println__char__1 (__arg0);
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    stack.push_back (reinterpret_cast<long>(__main__block__8__str));
    __stackval = stack.back ();
    stack.pop_back ();
    delete *reinterpret_cast<char**>(&__stackval);
    stack.push_back (0);
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(char[]) -> void
    {
        // Arguments
        stack.push_back (reinterpret_cast<long>(__main__block__8__str));
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        char* __arg0 = *reinterpret_cast<char**>(&__stackval);
        // println
        __builtin__println__char__1 (__arg0);
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    //---------------------------------------------------------------------
    //---------------------------------------------------------------------
    // Code Block
    // Statement
    // Function Call - print(char[]) -> void
    {
        // Arguments
        // String Literal
        {
            char str_literal[] = "Enter name => ";
            // convert to a heap string
            char* str = new char[15];
            // copy string to heap allocation
            std::memcpy (str, &str_literal, 15);
            stack.push_back (reinterpret_cast<long> (str));
        }
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        char* __arg0 = *reinterpret_cast<char**>(&__stackval);
        // print
        __builtin__print__char__1 (__arg0);
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Assignment - '='
    // RHS
    // Function Call - input() -> char[]
    {
        // Arguments
        // input
        char* __res = __builtin__input ();
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // LHS
    // Variable declaration
    char* __main__block__9__name;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__9__name = *reinterpret_cast<char**>(&__rhs);
    // Result of assignment
    stack.push_back (reinterpret_cast<long>(__main__block__9__name));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - print(char[]) -> void
    {
        // Arguments
        // String Literal
        {
            char str_literal[] = "Hello, ";
            // convert to a heap string
            char* str = new char[8];
            // copy string to heap allocation
            std::memcpy (str, &str_literal, 8);
            stack.push_back (reinterpret_cast<long> (str));
        }
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        char* __arg0 = *reinterpret_cast<char**>(&__stackval);
        // print
        __builtin__print__char__1 (__arg0);
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(char[]) -> void
    {
        // Arguments
        stack.push_back (reinterpret_cast<long>(__main__block__9__name));
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        char* __arg0 = *reinterpret_cast<char**>(&__stackval);
        // println
        __builtin__println__char__1 (__arg0);
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    //---------------------------------------------------------------------
    //---------------------------------------------------------------------
    // Code Block
    // Statement
    // Function Call - println(char[]) -> void
    {
        // Arguments
        // String Literal
        {
            char str_literal[] = "=== If statements";
            // convert to a heap string
            char* str = new char[18];
            // copy string to heap allocation
            std::memcpy (str, &str_literal, 18);
            stack.push_back (reinterpret_cast<long> (str));
        }
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        char* __arg0 = *reinterpret_cast<char**>(&__stackval);
        // println
        __builtin__println__char__1 (__arg0);
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Assignment - '='
    // RHS
    // Float Literal
    {
        double float_literal = 3.14;
        stack.push_back (*reinterpret_cast<long*>(&float_literal));
    }
    // LHS
    // Variable declaration
    double __main__block__10__x;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__10__x = *reinterpret_cast<double*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__10__x));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    //---------------------------------------------------------------------
    // If-Statement
    // Precomputing all if/elif conditions and give unique names
    // bc we can't have code between if and elif
    // Condition
    // Equal
    {
        // LHS
        stack.push_back (*reinterpret_cast<long*>(&__main__block__10__x));
        // RHS
        // Float Literal
        {
            double float_literal = 0.0;
            stack.push_back (*reinterpret_cast<long*>(&float_literal));
        }
        __rhs = stack.back ();
        stack.pop_back ();
        __lhs = stack.back ();
        stack.pop_back ();
        long __res = *reinterpret_cast<double*>(&__lhs) == *reinterpret_cast<double*>(&__rhs);
        stack.push_back (*reinterpret_cast<long*>(&__res));
    }
    long __if__11__cond = stack.back ();
    stack.pop_back ();
    // Condition for elif #0
    // Greater Than
    {
        // LHS
        stack.push_back (*reinterpret_cast<long*>(&__main__block__10__x));
        // RHS
        // Float Literal
        {
            double float_literal = 0.0;
            stack.push_back (*reinterpret_cast<long*>(&float_literal));
        }
        __rhs = stack.back ();
        stack.pop_back ();
        __lhs = stack.back ();
        stack.pop_back ();
        long __res = *reinterpret_cast<double*>(&__lhs) > *reinterpret_cast<double*>(&__rhs);
        stack.push_back (*reinterpret_cast<long*>(&__res));
    }
    long __elif__11x0__cond = stack.back ();
    stack.pop_back ();
    // get condition from stack
    if (__if__11__cond)
    {
        // Body
        //-----------------------------------------------------------------
        // Code Block
        // Statement
        // Function Call - println(char[]) -> void
        {
            // Arguments
            // String Literal
            {
                char str_literal[] = "x == 0.0";
                // convert to a heap string
                char* str = new char[9];
                // copy string to heap allocation
                std::memcpy (str, &str_literal, 9);
                stack.push_back (reinterpret_cast<long> (str));
            }
            
            __stackval = stack.back ();
            stack.pop_back ();
            // Reinterpret from general register
            char* __arg0 = *reinterpret_cast<char**>(&__stackval);
            // println
            __builtin__println__char__1 (__arg0);
            stack.push_back (reinterpret_cast<long>(__res));
        }
        // Statement results can be ignored
        stack.pop_back ();
        // End Statement

        //-----------------------------------------------------------------
    }
    //---------------------------------------------------------------------
    // Elif-Statement
    // Condition
    else if (__elif__11x0__cond)
    {
        // Body
        //-----------------------------------------------------------------
        // Code Block
        // Statement
        // Function Call - println(char[]) -> void
        {
            // Arguments
            // String Literal
            {
                char str_literal[] = "x > 0.0";
                // convert to a heap string
                char* str = new char[8];
                // copy string to heap allocation
                std::memcpy (str, &str_literal, 8);
                stack.push_back (reinterpret_cast<long> (str));
            }
            
            __stackval = stack.back ();
            stack.pop_back ();
            // Reinterpret from general register
            char* __arg0 = *reinterpret_cast<char**>(&__stackval);
            // println
            __builtin__println__char__1 (__arg0);
            stack.push_back (reinterpret_cast<long>(__res));
        }
        // Statement results can be ignored
        stack.pop_back ();
        // End Statement

        //-----------------------------------------------------------------
    }
    //---------------------------------------------------------------------
    //---------------------------------------------------------------------
    // Else-Statement
    else
    {
        //-----------------------------------------------------------------
        // Code Block
        // Statement
        // Function Call - println(char[]) -> void
        {
            // Arguments
            // String Literal
            {
                char str_literal[] = "x < 0.0";
                // convert to a heap string
                char* str = new char[8];
                // copy string to heap allocation
                std::memcpy (str, &str_literal, 8);
                stack.push_back (reinterpret_cast<long> (str));
            }
            
            __stackval = stack.back ();
            stack.pop_back ();
            // Reinterpret from general register
            char* __arg0 = *reinterpret_cast<char**>(&__stackval);
            // println
            __builtin__println__char__1 (__arg0);
            stack.push_back (reinterpret_cast<long>(__res));
        }
        // Statement results can be ignored
        stack.pop_back ();
        // End Statement

        //-----------------------------------------------------------------
    }
    //---------------------------------------------------------------------
    // End of if
    //---------------------------------------------------------------------
    //=====================================================================
    // Function Declaration - max(int, int) -> int
    auto __main__block__10____max__int__int = [&stack] (long __main__block__10__max__a, long __main__block__10__max__b)
    {
        // Function Header
        // This stack is used to store results of expressions
        std::vector<long> stack;
        // Declare general purpose variables
        // These are longs and can store anything up to 8 bytes via casting
        long __lhs = 0;
        long __rhs = 0;
        long __res = 0;
        long __stackval = 0;
        long __pointer = 0;
        long __offset = 0;
        long __parent = 0;
        long __child = 0;
        // Body
        //-----------------------------------------------------------------
        // Code Block
        //-----------------------------------------------------------------
        // If-Statement
        // Precomputing all if/elif conditions and give unique names
        // bc we can't have code between if and elif
        // Condition
        // Greater Than or Equal to
        {
            // LHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__10__max__a));
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__10__max__b));
            __rhs = stack.back ();
            stack.pop_back ();
            __lhs = stack.back ();
            stack.pop_back ();
            long __res = *reinterpret_cast<long*>(&__lhs) >= *reinterpret_cast<long*>(&__rhs);
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        long __if__16__cond = stack.back ();
        stack.pop_back ();
        // get condition from stack
        if (__if__16__cond)
        {
            // Body
            // Return
            stack.push_back (*reinterpret_cast<long*>(&__main__block__10__max__a));
            __res = stack.back ();
            stack.pop_back ();
            return *reinterpret_cast<long*>(&__res);
        }
        // End of if
        //-----------------------------------------------------------------
        // Return
        stack.push_back (*reinterpret_cast<long*>(&__main__block__10__max__b));
        __res = stack.back ();
        stack.pop_back ();
        return *reinterpret_cast<long*>(&__res);
        //-----------------------------------------------------------------
    };
    // End Function Declaration - __main__block__10____max__int__int
    //=====================================================================

    // Statement
    // Function Call - println(int) -> void
    {
        // Arguments
        // Function Call - max(int, int) -> int
        {
            // Arguments
            // Int Literal
            stack.push_back (7);
            // Int Literal
            stack.push_back (4);
            
            __stackval = stack.back ();
            stack.pop_back ();
            // Reinterpret from general register
            long __arg1 = *reinterpret_cast<long*>(&__stackval);
            
            __stackval = stack.back ();
            stack.pop_back ();
            // Reinterpret from general register
            long __arg0 = *reinterpret_cast<long*>(&__stackval);
            // max
            long __res = __main__block__10____max__int__int (__arg0, __arg1);
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        long __arg0 = *reinterpret_cast<long*>(&__stackval);
        // println
        __builtin__println__int (__arg0);
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(int) -> void
    {
        // Arguments
        // Function Call - max(int, int) -> int
        {
            // Arguments
            // Int Literal
            stack.push_back (4);
            // Int Literal
            stack.push_back (7);
            
            __stackval = stack.back ();
            stack.pop_back ();
            // Reinterpret from general register
            long __arg1 = *reinterpret_cast<long*>(&__stackval);
            
            __stackval = stack.back ();
            stack.pop_back ();
            // Reinterpret from general register
            long __arg0 = *reinterpret_cast<long*>(&__stackval);
            // max
            long __res = __main__block__10____max__int__int (__arg0, __arg1);
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        long __arg0 = *reinterpret_cast<long*>(&__stackval);
        // println
        __builtin__println__int (__arg0);
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(int) -> void
    {
        // Arguments
        // Function Call - max(int, int) -> int
        {
            // Arguments
            // Negative
            {
                // RHS
                // Int Literal
                stack.push_back (4);
                __rhs = stack.back ();
                stack.pop_back ();
                long __res = -*reinterpret_cast<long*>(&__rhs);
                stack.push_back (*reinterpret_cast<long*>(&__res));
            }
            // Negative
            {
                // RHS
                // Int Literal
                stack.push_back (7);
                __rhs = stack.back ();
                stack.pop_back ();
                long __res = -*reinterpret_cast<long*>(&__rhs);
                stack.push_back (*reinterpret_cast<long*>(&__res));
            }
            
            __stackval = stack.back ();
            stack.pop_back ();
            // Reinterpret from general register
            long __arg1 = *reinterpret_cast<long*>(&__stackval);
            
            __stackval = stack.back ();
            stack.pop_back ();
            // Reinterpret from general register
            long __arg0 = *reinterpret_cast<long*>(&__stackval);
            // max
            long __res = __main__block__10____max__int__int (__arg0, __arg1);
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        long __arg0 = *reinterpret_cast<long*>(&__stackval);
        // println
        __builtin__println__int (__arg0);
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(int) -> void
    {
        // Arguments
        // Function Call - max(int, int) -> int
        {
            // Arguments
            // Int Literal
            stack.push_back (4);
            // Int Literal
            stack.push_back (4);
            
            __stackval = stack.back ();
            stack.pop_back ();
            // Reinterpret from general register
            long __arg1 = *reinterpret_cast<long*>(&__stackval);
            
            __stackval = stack.back ();
            stack.pop_back ();
            // Reinterpret from general register
            long __arg0 = *reinterpret_cast<long*>(&__stackval);
            // max
            long __res = __main__block__10____max__int__int (__arg0, __arg1);
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        long __arg0 = *reinterpret_cast<long*>(&__stackval);
        // println
        __builtin__println__int (__arg0);
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    //---------------------------------------------------------------------
    //---------------------------------------------------------------------
    // Code Block
    // Statement
    // Function Call - println(char[]) -> void
    {
        // Arguments
        // String Literal
        {
            char str_literal[] = "=== for loop";
            // convert to a heap string
            char* str = new char[13];
            // copy string to heap allocation
            std::memcpy (str, &str_literal, 13);
            stack.push_back (reinterpret_cast<long> (str));
        }
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        char* __arg0 = *reinterpret_cast<char**>(&__stackval);
        // println
        __builtin__println__char__1 (__arg0);
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    //---------------------------------------------------------------------
    // For-Loop
    // Init
    // Assignment - '='
    // RHS
    // Int Literal
    stack.push_back (0);
    // LHS
    // Variable declaration
    long __main__block__17__for__18__i;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__17__for__18__i = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__17__for__18__i));
    // Using an infinite loop so we can write a separate multi-line condition
    while (1)
    {
        // Condition
        // Less Than
        {
            // LHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__17__for__18__i));
            // RHS
            // Int Literal
            stack.push_back (10);
            __rhs = stack.back ();
            stack.pop_back ();
            __lhs = stack.back ();
            stack.pop_back ();
            long __res = *reinterpret_cast<long*>(&__lhs) < *reinterpret_cast<long*>(&__rhs);
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        long __cond = stack.back ();
        stack.pop_back ();
        // break out of loop if condition is false
        if (__cond == 0) break;
        // Body
        //-----------------------------------------------------------------
        // Code Block
        // Statement
        // Function Call - print(char) -> void
        {
            // Arguments
            // Char Literal
            stack.push_back (static_cast<long>(static_cast<unsigned char>(' ')));
            
            __stackval = stack.back ();
            stack.pop_back ();
            // Reinterpret from general register
            char __arg0 = static_cast<char>(static_cast<unsigned char>(__stackval));
            // print
            __builtin__print__char (__arg0);
            stack.push_back (reinterpret_cast<long>(__res));
        }
        // Statement results can be ignored
        stack.pop_back ();
        // End Statement

        // Statement
        // Function Call - print(int) -> void
        {
            // Arguments
            stack.push_back (*reinterpret_cast<long*>(&__main__block__17__for__18__i));
            
            __stackval = stack.back ();
            stack.pop_back ();
            // Reinterpret from general register
            long __arg0 = *reinterpret_cast<long*>(&__stackval);
            // print
            __builtin__print__int (__arg0);
            stack.push_back (reinterpret_cast<long>(__res));
        }
        // Statement results can be ignored
        stack.pop_back ();
        // End Statement

        //-----------------------------------------------------------------
        // Update
        // Pre-Increment
        {
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__17__for__18__i));
            __rhs = stack.back ();
            stack.pop_back ();
            __main__block__17__for__18__i = __main__block__17__for__18__i + 1;
            __res = __main__block__17__for__18__i;
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
    }
    //---------------------------------------------------------------------
    // Statement
    // Function Call - println() -> void
    {
        // Arguments
        // println
        __builtin__println ();
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    //---------------------------------------------------------------------
    //---------------------------------------------------------------------
    // Code Block
    // Statement
    // Function Call - println(char[]) -> void
    {
        // Arguments
        // String Literal
        {
            char str_literal[] = "=== while loop";
            // convert to a heap string
            char* str = new char[15];
            // copy string to heap allocation
            std::memcpy (str, &str_literal, 15);
            stack.push_back (reinterpret_cast<long> (str));
        }
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        char* __arg0 = *reinterpret_cast<char**>(&__stackval);
        // println
        __builtin__println__char__1 (__arg0);
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Assignment - '='
    // RHS
    // Int Literal
    stack.push_back (0);
    // LHS
    // Variable declaration
    long __main__block__20__i;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__20__i = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__20__i));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    //---------------------------------------------------------------------
    // While-Loop
    // Using an infinite loop so we can write a separate multi-line condition
    while (1)
    {
        // Condition
        // Less Than
        {
            // LHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__20__i));
            // RHS
            // Int Literal
            stack.push_back (21);
            __rhs = stack.back ();
            stack.pop_back ();
            __lhs = stack.back ();
            stack.pop_back ();
            long __res = *reinterpret_cast<long*>(&__lhs) < *reinterpret_cast<long*>(&__rhs);
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        long __cond = stack.back ();
        stack.pop_back ();
        // break out of loop if condition is false
        if (__cond == 0) break;
        // Body
        //-----------------------------------------------------------------
        // Code Block
        // Statement
        // Function Call - print(char) -> void
        {
            // Arguments
            // Char Literal
            stack.push_back (static_cast<long>(static_cast<unsigned char>(' ')));
            
            __stackval = stack.back ();
            stack.pop_back ();
            // Reinterpret from general register
            char __arg0 = static_cast<char>(static_cast<unsigned char>(__stackval));
            // print
            __builtin__print__char (__arg0);
            stack.push_back (reinterpret_cast<long>(__res));
        }
        // Statement results can be ignored
        stack.pop_back ();
        // End Statement

        // Statement
        // Function Call - print(int) -> void
        {
            // Arguments
            stack.push_back (*reinterpret_cast<long*>(&__main__block__20__i));
            
            __stackval = stack.back ();
            stack.pop_back ();
            // Reinterpret from general register
            long __arg0 = *reinterpret_cast<long*>(&__stackval);
            // print
            __builtin__print__int (__arg0);
            stack.push_back (reinterpret_cast<long>(__res));
        }
        // Statement results can be ignored
        stack.pop_back ();
        // End Statement

        // Statement
        // Pre-Increment
        {
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__20__i));
            __rhs = stack.back ();
            stack.pop_back ();
            __main__block__20__i = __main__block__20__i + 1;
            __res = __main__block__20__i;
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        // Statement results can be ignored
        stack.pop_back ();
        // End Statement

        //-----------------------------------------------------------------
    }
    // End of While
    //---------------------------------------------------------------------
    // Statement
    // Function Call - print(char) -> void
    {
        // Arguments
        // Char Literal
        stack.push_back (static_cast<long>(static_cast<unsigned char>('\n')));
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        char __arg0 = static_cast<char>(static_cast<unsigned char>(__stackval));
        // print
        __builtin__print__char (__arg0);
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    //---------------------------------------------------------------------
    //---------------------------------------------------------------------
    // Code Block
    // Statement
    // Function Call - println(char[]) -> void
    {
        // Arguments
        // String Literal
        {
            char str_literal[] = "=== arrays";
            // convert to a heap string
            char* str = new char[11];
            // copy string to heap allocation
            std::memcpy (str, &str_literal, 11);
            stack.push_back (reinterpret_cast<long> (str));
        }
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        char* __arg0 = *reinterpret_cast<char**>(&__stackval);
        // println
        __builtin__println__char__1 (__arg0);
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Assignment - '='
    // RHS
    // Int Literal
    stack.push_back (10);
    // LHS
    // Variable declaration
    long __main__block__23__size;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__23__size = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__23__size));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Assignment - '='
    // RHS
    // Array Allocator
    {
        stack.push_back (*reinterpret_cast<long*>(&__main__block__23__size));
        __stackval = stack.back ();
        stack.pop_back ();
        long* __res = new long[__stackval];
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // LHS
    // Variable declaration
    long* __main__block__23__arr;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__23__arr = *reinterpret_cast<long**>(&__rhs);
    // Result of assignment
    stack.push_back (reinterpret_cast<long>(__main__block__23__arr));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    //---------------------------------------------------------------------
    // For-Loop
    // Init
    // Assignment - '='
    // RHS
    // Int Literal
    stack.push_back (0);
    // LHS
    // Variable declaration
    long __main__block__23__for__24__i;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__23__for__24__i = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__23__for__24__i));
    // Using an infinite loop so we can write a separate multi-line condition
    while (1)
    {
        // Condition
        // Less Than
        {
            // LHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__23__for__24__i));
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__23__size));
            __rhs = stack.back ();
            stack.pop_back ();
            __lhs = stack.back ();
            stack.pop_back ();
            long __res = *reinterpret_cast<long*>(&__lhs) < *reinterpret_cast<long*>(&__rhs);
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        long __cond = stack.back ();
        stack.pop_back ();
        // break out of loop if condition is false
        if (__cond == 0) break;
        // Body
        //-----------------------------------------------------------------
        // Code Block
        // Statement
        // Assignment - '='
        // RHS
        // Multiplication
        {
            // LHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__23__for__24__i));
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__23__for__24__i));
            __rhs = stack.back ();
            stack.pop_back ();
            __lhs = stack.back ();
            stack.pop_back ();
            long __res = *reinterpret_cast<long*>(&__lhs) * *reinterpret_cast<long*>(&__rhs);
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        // LHS
        // Subscript assignment
        // LHS
        stack.push_back (reinterpret_cast<long>(__main__block__23__arr));
        // OFFSET
        stack.push_back (*reinterpret_cast<long*>(&__main__block__23__for__24__i));
        __offset = stack.back ();
        stack.pop_back ();
        __pointer = stack.back ();
        stack.pop_back ();
        __rhs = stack.back ();
        stack.pop_back ();
        (*reinterpret_cast<long**>(&__pointer))[__offset] = *reinterpret_cast<long*>(&__rhs);
        // Result of assignment
        stack.push_back (*reinterpret_cast<long*>(&(*reinterpret_cast<long**>(&__pointer))[__offset]));
        // Statement results can be ignored
        stack.pop_back ();
        // End Statement

        //-----------------------------------------------------------------
        // Update
        // Pre-Increment
        {
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__23__for__24__i));
            __rhs = stack.back ();
            stack.pop_back ();
            __main__block__23__for__24__i = __main__block__23__for__24__i + 1;
            __res = __main__block__23__for__24__i;
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
    }
    //---------------------------------------------------------------------
    //---------------------------------------------------------------------
    // For-Loop
    // Init
    // Assignment - '='
    // RHS
    // Int Literal
    stack.push_back (0);
    // LHS
    // Variable declaration
    long __main__block__23__for__26__i;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__23__for__26__i = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__23__for__26__i));
    // Using an infinite loop so we can write a separate multi-line condition
    while (1)
    {
        // Condition
        // Less Than
        {
            // LHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__23__for__26__i));
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__23__size));
            __rhs = stack.back ();
            stack.pop_back ();
            __lhs = stack.back ();
            stack.pop_back ();
            long __res = *reinterpret_cast<long*>(&__lhs) < *reinterpret_cast<long*>(&__rhs);
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        long __cond = stack.back ();
        stack.pop_back ();
        // break out of loop if condition is false
        if (__cond == 0) break;
        // Body
        //-----------------------------------------------------------------
        // Code Block
        // Statement
        // Function Call - print(char) -> void
        {
            // Arguments
            // Char Literal
            stack.push_back (static_cast<long>(static_cast<unsigned char>(' ')));
            
            __stackval = stack.back ();
            stack.pop_back ();
            // Reinterpret from general register
            char __arg0 = static_cast<char>(static_cast<unsigned char>(__stackval));
            // print
            __builtin__print__char (__arg0);
            stack.push_back (reinterpret_cast<long>(__res));
        }
        // Statement results can be ignored
        stack.pop_back ();
        // End Statement

        // Statement
        // Function Call - print(int) -> void
        {
            // Arguments
            // Subscript
            {
                // LHS
                stack.push_back (reinterpret_cast<long>(__main__block__23__arr));
                // OFFSET
                stack.push_back (*reinterpret_cast<long*>(&__main__block__23__for__26__i));
                __offset = stack.back ();
                stack.pop_back ();
                __pointer = stack.back ();
                stack.pop_back ();
                stack.push_back (*reinterpret_cast<long*>(&(*reinterpret_cast<long**>(&__pointer))[*reinterpret_cast<long*>(&__offset)]));
            }
            
            __stackval = stack.back ();
            stack.pop_back ();
            // Reinterpret from general register
            long __arg0 = *reinterpret_cast<long*>(&__stackval);
            // print
            __builtin__print__int (__arg0);
            stack.push_back (reinterpret_cast<long>(__res));
        }
        // Statement results can be ignored
        stack.pop_back ();
        // End Statement

        //-----------------------------------------------------------------
        // Update
        // Pre-Increment
        {
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__23__for__26__i));
            __rhs = stack.back ();
            stack.pop_back ();
            __main__block__23__for__26__i = __main__block__23__for__26__i + 1;
            __res = __main__block__23__for__26__i;
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
    }
    //---------------------------------------------------------------------
    // Statement
    // Function Call - println() -> void
    {
        // Arguments
        // println
        __builtin__println ();
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    //---------------------------------------------------------------------
    //---------------------------------------------------------------------
    // Code Block
    // Statement
    // Assignment - '='
    // RHS
    // Array Constructor
    {
        // Elements
        // Float Literal
        {
            double float_literal = 3.14;
            stack.push_back (*reinterpret_cast<long*>(&float_literal));
        }
        // Float Literal
        {
            double float_literal = 0.25;
            stack.push_back (*reinterpret_cast<long*>(&float_literal));
        }
        // Float Literal
        {
            double float_literal = 0.0004;
            stack.push_back (*reinterpret_cast<long*>(&float_literal));
        }
        // Float Literal
        {
            double float_literal = 10000.25;
            stack.push_back (*reinterpret_cast<long*>(&float_literal));
        }
        long __elem3 = stack.back ();
        stack.pop_back ();
        long __elem2 = stack.back ();
        stack.pop_back ();
        long __elem1 = stack.back ();
        stack.pop_back ();
        long __elem0 = stack.back ();
        stack.pop_back ();
        double* __list = new double[4];
        __list[0] = *reinterpret_cast<double*>(&__elem0);
        __list[1] = *reinterpret_cast<double*>(&__elem1);
        __list[2] = *reinterpret_cast<double*>(&__elem2);
        __list[3] = *reinterpret_cast<double*>(&__elem3);
        stack.push_back (reinterpret_cast<long>(__list));
    }
    // LHS
    // Variable declaration
    double* __main__block__28__arr;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__28__arr = *reinterpret_cast<double**>(&__rhs);
    // Result of assignment
    stack.push_back (reinterpret_cast<long>(__main__block__28__arr));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    //---------------------------------------------------------------------
    // For-Loop
    // Init
    // Assignment - '='
    // RHS
    // Int Literal
    stack.push_back (0);
    // LHS
    // Variable declaration
    long __main__block__28__for__29__i;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__28__for__29__i = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__28__for__29__i));
    // Using an infinite loop so we can write a separate multi-line condition
    while (1)
    {
        // Condition
        // Less Than
        {
            // LHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__28__for__29__i));
            // RHS
            // Int Literal
            stack.push_back (4);
            __rhs = stack.back ();
            stack.pop_back ();
            __lhs = stack.back ();
            stack.pop_back ();
            long __res = *reinterpret_cast<long*>(&__lhs) < *reinterpret_cast<long*>(&__rhs);
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        long __cond = stack.back ();
        stack.pop_back ();
        // break out of loop if condition is false
        if (__cond == 0) break;
        // Body
        //-----------------------------------------------------------------
        // Code Block
        // Statement
        // Function Call - print(char) -> void
        {
            // Arguments
            // Char Literal
            stack.push_back (static_cast<long>(static_cast<unsigned char>(' ')));
            
            __stackval = stack.back ();
            stack.pop_back ();
            // Reinterpret from general register
            char __arg0 = static_cast<char>(static_cast<unsigned char>(__stackval));
            // print
            __builtin__print__char (__arg0);
            stack.push_back (reinterpret_cast<long>(__res));
        }
        // Statement results can be ignored
        stack.pop_back ();
        // End Statement

        // Statement
        // Function Call - print(float) -> void
        {
            // Arguments
            // Subscript
            {
                // LHS
                stack.push_back (reinterpret_cast<long>(__main__block__28__arr));
                // OFFSET
                stack.push_back (*reinterpret_cast<long*>(&__main__block__28__for__29__i));
                __offset = stack.back ();
                stack.pop_back ();
                __pointer = stack.back ();
                stack.pop_back ();
                stack.push_back (*reinterpret_cast<long*>(&(*reinterpret_cast<double**>(&__pointer))[*reinterpret_cast<long*>(&__offset)]));
            }
            
            __stackval = stack.back ();
            stack.pop_back ();
            // Reinterpret from general register
            double __arg0 = *reinterpret_cast<double*>(&__stackval);
            // print
            __builtin__print__float (__arg0);
            stack.push_back (reinterpret_cast<long>(__res));
        }
        // Statement results can be ignored
        stack.pop_back ();
        // End Statement

        //-----------------------------------------------------------------
        // Update
        // Pre-Increment
        {
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__28__for__29__i));
            __rhs = stack.back ();
            stack.pop_back ();
            __main__block__28__for__29__i = __main__block__28__for__29__i + 1;
            __res = __main__block__28__for__29__i;
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
    }
    //---------------------------------------------------------------------
    // Statement
    // Function Call - println() -> void
    {
        // Arguments
        // println
        __builtin__println ();
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    //---------------------------------------------------------------------
    //---------------------------------------------------------------------
    // Code Block
    // Statement
    // Assignment - '='
    // RHS
    // String Literal
    {
        char str_literal[] = "AAA";
        // convert to a heap string
        char* str = new char[4];
        // copy string to heap allocation
        std::memcpy (str, &str_literal, 4);
        stack.push_back (reinterpret_cast<long> (str));
    }
    // LHS
    // Variable declaration
    char* __main__block__31__line;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__31__line = *reinterpret_cast<char**>(&__rhs);
    // Result of assignment
    stack.push_back (reinterpret_cast<long>(__main__block__31__line));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(char[]) -> void
    {
        // Arguments
        stack.push_back (reinterpret_cast<long>(__main__block__31__line));
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        char* __arg0 = *reinterpret_cast<char**>(&__stackval);
        // println
        __builtin__println__char__1 (__arg0);
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Assignment - '='
    // RHS
    // Char Literal
    stack.push_back (static_cast<long>(static_cast<unsigned char>('m')));
    // LHS
    // Subscript assignment
    // LHS
    stack.push_back (reinterpret_cast<long>(__main__block__31__line));
    // OFFSET
    // Int Literal
    stack.push_back (1);
    __offset = stack.back ();
    stack.pop_back ();
    __pointer = stack.back ();
    stack.pop_back ();
    __rhs = stack.back ();
    stack.pop_back ();
    (*reinterpret_cast<char**>(&__pointer))[__offset] = static_cast<char>(static_cast<unsigned char>(__rhs));
    // Result of assignment
    stack.push_back (static_cast<long>(static_cast<unsigned char>((*reinterpret_cast<char**>(&__pointer))[__offset])));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(char[]) -> void
    {
        // Arguments
        stack.push_back (reinterpret_cast<long>(__main__block__31__line));
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        char* __arg0 = *reinterpret_cast<char**>(&__stackval);
        // println
        __builtin__println__char__1 (__arg0);
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Assignment - '='
    // RHS
    // Char Literal
    stack.push_back (static_cast<long>(static_cast<unsigned char>('y')));
    // LHS
    // Subscript assignment
    // LHS
    stack.push_back (reinterpret_cast<long>(__main__block__31__line));
    // OFFSET
    // Int Literal
    stack.push_back (2);
    __offset = stack.back ();
    stack.pop_back ();
    __pointer = stack.back ();
    stack.pop_back ();
    __rhs = stack.back ();
    stack.pop_back ();
    (*reinterpret_cast<char**>(&__pointer))[__offset] = static_cast<char>(static_cast<unsigned char>(__rhs));
    // Result of assignment
    stack.push_back (static_cast<long>(static_cast<unsigned char>((*reinterpret_cast<char**>(&__pointer))[__offset])));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(char[]) -> void
    {
        // Arguments
        stack.push_back (reinterpret_cast<long>(__main__block__31__line));
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        char* __arg0 = *reinterpret_cast<char**>(&__stackval);
        // println
        __builtin__println__char__1 (__arg0);
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    //---------------------------------------------------------------------
    //---------------------------------------------------------------------
    // Code Block
    // Statement
    // Function Call - println(char[]) -> void
    {
        // Arguments
        // String Literal
        {
            char str_literal[] = "=== 2D array";
            // convert to a heap string
            char* str = new char[13];
            // copy string to heap allocation
            std::memcpy (str, &str_literal, 13);
            stack.push_back (reinterpret_cast<long> (str));
        }
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        char* __arg0 = *reinterpret_cast<char**>(&__stackval);
        // println
        __builtin__println__char__1 (__arg0);
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Assignment - '='
    // RHS
    // Int Literal
    stack.push_back (5);
    // LHS
    // Variable declaration
    long __main__block__32__rows;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__32__rows = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__32__rows));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Assignment - '='
    // RHS
    // Int Literal
    stack.push_back (5);
    // LHS
    // Variable declaration
    long __main__block__32__cols;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__32__cols = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__32__cols));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Assignment - '='
    // RHS
    // Array Allocator
    {
        stack.push_back (*reinterpret_cast<long*>(&__main__block__32__rows));
        __stackval = stack.back ();
        stack.pop_back ();
        char** __res = new char*[__stackval];
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // LHS
    // Variable declaration
    char** __main__block__32__board;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__32__board = *reinterpret_cast<char***>(&__rhs);
    // Result of assignment
    stack.push_back (reinterpret_cast<long>(__main__block__32__board));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    //---------------------------------------------------------------------
    // For-Loop
    // Init
    // Assignment - '='
    // RHS
    // Int Literal
    stack.push_back (0);
    // LHS
    // Variable declaration
    long __main__block__32__for__33__i;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__32__for__33__i = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__32__for__33__i));
    // Using an infinite loop so we can write a separate multi-line condition
    while (1)
    {
        // Condition
        // Less Than
        {
            // LHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__32__for__33__i));
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__32__rows));
            __rhs = stack.back ();
            stack.pop_back ();
            __lhs = stack.back ();
            stack.pop_back ();
            long __res = *reinterpret_cast<long*>(&__lhs) < *reinterpret_cast<long*>(&__rhs);
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        long __cond = stack.back ();
        stack.pop_back ();
        // break out of loop if condition is false
        if (__cond == 0) break;
        // Body
        //-----------------------------------------------------------------
        // Code Block
        // Statement
        // Assignment - '='
        // RHS
        // Array Allocator
        {
            stack.push_back (*reinterpret_cast<long*>(&__main__block__32__cols));
            __stackval = stack.back ();
            stack.pop_back ();
            char* __res = new char[__stackval];
            stack.push_back (reinterpret_cast<long>(__res));
        }
        // LHS
        // Subscript assignment
        // LHS
        stack.push_back (reinterpret_cast<long>(__main__block__32__board));
        // OFFSET
        stack.push_back (*reinterpret_cast<long*>(&__main__block__32__for__33__i));
        __offset = stack.back ();
        stack.pop_back ();
        __pointer = stack.back ();
        stack.pop_back ();
        __rhs = stack.back ();
        stack.pop_back ();
        (*reinterpret_cast<char***>(&__pointer))[__offset] = *reinterpret_cast<char**>(&__rhs);
        // Result of assignment
        stack.push_back (reinterpret_cast<long>((*reinterpret_cast<char***>(&__pointer))[__offset]));
        // Statement results can be ignored
        stack.pop_back ();
        // End Statement

        //-----------------------------------------------------------------
        // For-Loop
        // Init
        // Assignment - '='
        // RHS
        // Int Literal
        stack.push_back (0);
        // LHS
        // Variable declaration
        long __main__block__32__for__33__block__34__for__35__j;
        __rhs = stack.back ();
        stack.pop_back ();
        __main__block__32__for__33__block__34__for__35__j = *reinterpret_cast<long*>(&__rhs);
        // Result of assignment
        stack.push_back (*reinterpret_cast<long*>(&__main__block__32__for__33__block__34__for__35__j));
        // Using an infinite loop so we can write a separate multi-line condition
        while (1)
        {
            // Condition
            // Less Than
            {
                // LHS
                stack.push_back (*reinterpret_cast<long*>(&__main__block__32__for__33__block__34__for__35__j));
                // RHS
                stack.push_back (*reinterpret_cast<long*>(&__main__block__32__cols));
                __rhs = stack.back ();
                stack.pop_back ();
                __lhs = stack.back ();
                stack.pop_back ();
                long __res = *reinterpret_cast<long*>(&__lhs) < *reinterpret_cast<long*>(&__rhs);
                stack.push_back (*reinterpret_cast<long*>(&__res));
            }
            long __cond = stack.back ();
            stack.pop_back ();
            // break out of loop if condition is false
            if (__cond == 0) break;
            // Body
            //-------------------------------------------------------------
            // Code Block
            // Statement
            // Assignment - '='
            // RHS
            // Char Literal
            stack.push_back (static_cast<long>(static_cast<unsigned char>('.')));
            // LHS
            // Subscript assignment
            // LHS
            // Subscript
            {
                // LHS
                stack.push_back (reinterpret_cast<long>(__main__block__32__board));
                // OFFSET
                stack.push_back (*reinterpret_cast<long*>(&__main__block__32__for__33__i));
                __offset = stack.back ();
                stack.pop_back ();
                __pointer = stack.back ();
                stack.pop_back ();
                stack.push_back (reinterpret_cast<long>((*reinterpret_cast<char***>(&__pointer))[*reinterpret_cast<long*>(&__offset)]));
            }
            // OFFSET
            stack.push_back (*reinterpret_cast<long*>(&__main__block__32__for__33__block__34__for__35__j));
            __offset = stack.back ();
            stack.pop_back ();
            __pointer = stack.back ();
            stack.pop_back ();
            __rhs = stack.back ();
            stack.pop_back ();
            (*reinterpret_cast<char**>(&__pointer))[__offset] = static_cast<char>(static_cast<unsigned char>(__rhs));
            // Result of assignment
            stack.push_back (static_cast<long>(static_cast<unsigned char>((*reinterpret_cast<char**>(&__pointer))[__offset])));
            // Statement results can be ignored
            stack.pop_back ();
            // End Statement

            //-------------------------------------------------------------
            // Update
            // Pre-Increment
            {
                // RHS
                stack.push_back (*reinterpret_cast<long*>(&__main__block__32__for__33__block__34__for__35__j));
                __rhs = stack.back ();
                stack.pop_back ();
                __main__block__32__for__33__block__34__for__35__j = __main__block__32__for__33__block__34__for__35__j + 1;
                __res = __main__block__32__for__33__block__34__for__35__j;
                stack.push_back (*reinterpret_cast<long*>(&__res));
            }
        }
        //-----------------------------------------------------------------
        //-----------------------------------------------------------------
        // Update
        // Pre-Increment
        {
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__32__for__33__i));
            __rhs = stack.back ();
            stack.pop_back ();
            __main__block__32__for__33__i = __main__block__32__for__33__i + 1;
            __res = __main__block__32__for__33__i;
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
    }
    //---------------------------------------------------------------------
    //---------------------------------------------------------------------
    // For-Loop
    // Init
    // Assignment - '='
    // RHS
    // Int Literal
    stack.push_back (0);
    // LHS
    // Variable declaration
    long __main__block__32__for__37__i;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__32__for__37__i = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__32__for__37__i));
    // Using an infinite loop so we can write a separate multi-line condition
    while (1)
    {
        // Condition
        // Less Than
        {
            // LHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__32__for__37__i));
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__32__rows));
            __rhs = stack.back ();
            stack.pop_back ();
            __lhs = stack.back ();
            stack.pop_back ();
            long __res = *reinterpret_cast<long*>(&__lhs) < *reinterpret_cast<long*>(&__rhs);
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        long __cond = stack.back ();
        stack.pop_back ();
        // break out of loop if condition is false
        if (__cond == 0) break;
        // Body
        //-----------------------------------------------------------------
        // Code Block
        //-----------------------------------------------------------------
        // For-Loop
        // Init
        // Assignment - '='
        // RHS
        // Int Literal
        stack.push_back (0);
        // LHS
        // Variable declaration
        long __main__block__32__for__37__block__38__for__39__j;
        __rhs = stack.back ();
        stack.pop_back ();
        __main__block__32__for__37__block__38__for__39__j = *reinterpret_cast<long*>(&__rhs);
        // Result of assignment
        stack.push_back (*reinterpret_cast<long*>(&__main__block__32__for__37__block__38__for__39__j));
        // Using an infinite loop so we can write a separate multi-line condition
        while (1)
        {
            // Condition
            // Less Than
            {
                // LHS
                stack.push_back (*reinterpret_cast<long*>(&__main__block__32__for__37__block__38__for__39__j));
                // RHS
                stack.push_back (*reinterpret_cast<long*>(&__main__block__32__cols));
                __rhs = stack.back ();
                stack.pop_back ();
                __lhs = stack.back ();
                stack.pop_back ();
                long __res = *reinterpret_cast<long*>(&__lhs) < *reinterpret_cast<long*>(&__rhs);
                stack.push_back (*reinterpret_cast<long*>(&__res));
            }
            long __cond = stack.back ();
            stack.pop_back ();
            // break out of loop if condition is false
            if (__cond == 0) break;
            // Body
            //-------------------------------------------------------------
            // Code Block
            // Statement
            // Function Call - print(char) -> void
            {
                // Arguments
                // Subscript
                {
                    // LHS
                    // Subscript
                    {
                        // LHS
                        stack.push_back (reinterpret_cast<long>(__main__block__32__board));
                        // OFFSET
                        stack.push_back (*reinterpret_cast<long*>(&__main__block__32__for__37__i));
                        __offset = stack.back ();
                        stack.pop_back ();
                        __pointer = stack.back ();
                        stack.pop_back ();
                        stack.push_back (reinterpret_cast<long>((*reinterpret_cast<char***>(&__pointer))[*reinterpret_cast<long*>(&__offset)]));
                    }
                    // OFFSET
                    stack.push_back (*reinterpret_cast<long*>(&__main__block__32__for__37__block__38__for__39__j));
                    __offset = stack.back ();
                    stack.pop_back ();
                    __pointer = stack.back ();
                    stack.pop_back ();
                    stack.push_back (static_cast<long>(static_cast<unsigned char>((*reinterpret_cast<char**>(&__pointer))[*reinterpret_cast<long*>(&__offset)])));
                }
                
                __stackval = stack.back ();
                stack.pop_back ();
                // Reinterpret from general register
                char __arg0 = static_cast<char>(static_cast<unsigned char>(__stackval));
                // print
                __builtin__print__char (__arg0);
                stack.push_back (reinterpret_cast<long>(__res));
            }
            // Statement results can be ignored
            stack.pop_back ();
            // End Statement

            //-------------------------------------------------------------
            // Update
            // Pre-Increment
            {
                // RHS
                stack.push_back (*reinterpret_cast<long*>(&__main__block__32__for__37__block__38__for__39__j));
                __rhs = stack.back ();
                stack.pop_back ();
                __main__block__32__for__37__block__38__for__39__j = __main__block__32__for__37__block__38__for__39__j + 1;
                __res = __main__block__32__for__37__block__38__for__39__j;
                stack.push_back (*reinterpret_cast<long*>(&__res));
            }
        }
        //-----------------------------------------------------------------
        // Statement
        // Function Call - println() -> void
        {
            // Arguments
            // println
            __builtin__println ();
            stack.push_back (reinterpret_cast<long>(__res));
        }
        // Statement results can be ignored
        stack.pop_back ();
        // End Statement

        //-----------------------------------------------------------------
        // Update
        // Pre-Increment
        {
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__32__for__37__i));
            __rhs = stack.back ();
            stack.pop_back ();
            __main__block__32__for__37__i = __main__block__32__for__37__i + 1;
            __res = __main__block__32__for__37__i;
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
    }
    //---------------------------------------------------------------------
    // Statement
    // Function Call - println() -> void
    {
        // Arguments
        // println
        __builtin__println ();
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    //---------------------------------------------------------------------
    // For-Loop
    // Init
    // Assignment - '='
    // RHS
    // Int Literal
    stack.push_back (0);
    // LHS
    // Variable declaration
    long __main__block__32__for__41__i;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__32__for__41__i = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__32__for__41__i));
    // Using an infinite loop so we can write a separate multi-line condition
    while (1)
    {
        // Condition
        // Less Than
        {
            // LHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__32__for__41__i));
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__32__rows));
            __rhs = stack.back ();
            stack.pop_back ();
            __lhs = stack.back ();
            stack.pop_back ();
            long __res = *reinterpret_cast<long*>(&__lhs) < *reinterpret_cast<long*>(&__rhs);
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        long __cond = stack.back ();
        stack.pop_back ();
        // break out of loop if condition is false
        if (__cond == 0) break;
        // Body
        //-----------------------------------------------------------------
        // Code Block
        //-----------------------------------------------------------------
        // For-Loop
        // Init
        // Assignment - '='
        // RHS
        // Int Literal
        stack.push_back (0);
        // LHS
        // Variable declaration
        long __main__block__32__for__41__block__42__for__43__j;
        __rhs = stack.back ();
        stack.pop_back ();
        __main__block__32__for__41__block__42__for__43__j = *reinterpret_cast<long*>(&__rhs);
        // Result of assignment
        stack.push_back (*reinterpret_cast<long*>(&__main__block__32__for__41__block__42__for__43__j));
        // Using an infinite loop so we can write a separate multi-line condition
        while (1)
        {
            // Condition
            // Less Than
            {
                // LHS
                stack.push_back (*reinterpret_cast<long*>(&__main__block__32__for__41__block__42__for__43__j));
                // RHS
                stack.push_back (*reinterpret_cast<long*>(&__main__block__32__cols));
                __rhs = stack.back ();
                stack.pop_back ();
                __lhs = stack.back ();
                stack.pop_back ();
                long __res = *reinterpret_cast<long*>(&__lhs) < *reinterpret_cast<long*>(&__rhs);
                stack.push_back (*reinterpret_cast<long*>(&__res));
            }
            long __cond = stack.back ();
            stack.pop_back ();
            // break out of loop if condition is false
            if (__cond == 0) break;
            // Body
            //-------------------------------------------------------------
            // Code Block
            //-------------------------------------------------------------
            // If-Statement
            // Precomputing all if/elif conditions and give unique names
            // bc we can't have code between if and elif
            // Condition
            // Equal
            {
                // LHS
                // Modulus
                {
                    // LHS
                    // Addition
                    {
                        // LHS
                        stack.push_back (*reinterpret_cast<long*>(&__main__block__32__for__41__i));
                        // RHS
                        stack.push_back (*reinterpret_cast<long*>(&__main__block__32__for__41__block__42__for__43__j));
                        __rhs = stack.back ();
                        stack.pop_back ();
                        __lhs = stack.back ();
                        stack.pop_back ();
                        long __res = *reinterpret_cast<long*>(&__lhs) + *reinterpret_cast<long*>(&__rhs);
                        stack.push_back (*reinterpret_cast<long*>(&__res));
                    }
                    // RHS
                    // Int Literal
                    stack.push_back (2);
                    __rhs = stack.back ();
                    stack.pop_back ();
                    __lhs = stack.back ();
                    stack.pop_back ();
                    long __res = *reinterpret_cast<long*>(&__lhs) % *reinterpret_cast<long*>(&__rhs);
                    stack.push_back (*reinterpret_cast<long*>(&__res));
                }
                // RHS
                // Int Literal
                stack.push_back (0);
                __rhs = stack.back ();
                stack.pop_back ();
                __lhs = stack.back ();
                stack.pop_back ();
                long __res = *reinterpret_cast<long*>(&__lhs) == *reinterpret_cast<long*>(&__rhs);
                stack.push_back (*reinterpret_cast<long*>(&__res));
            }
            long __if__45__cond = stack.back ();
            stack.pop_back ();
            // get condition from stack
            if (__if__45__cond)
            {
                // Body
                // Statement
                // Assignment - '='
                // RHS
                // Char Literal
                stack.push_back (static_cast<long>(static_cast<unsigned char>('x')));
                // LHS
                // Subscript assignment
                // LHS
                // Subscript
                {
                    // LHS
                    stack.push_back (reinterpret_cast<long>(__main__block__32__board));
                    // OFFSET
                    stack.push_back (*reinterpret_cast<long*>(&__main__block__32__for__41__i));
                    __offset = stack.back ();
                    stack.pop_back ();
                    __pointer = stack.back ();
                    stack.pop_back ();
                    stack.push_back (reinterpret_cast<long>((*reinterpret_cast<char***>(&__pointer))[*reinterpret_cast<long*>(&__offset)]));
                }
                // OFFSET
                stack.push_back (*reinterpret_cast<long*>(&__main__block__32__for__41__block__42__for__43__j));
                __offset = stack.back ();
                stack.pop_back ();
                __pointer = stack.back ();
                stack.pop_back ();
                __rhs = stack.back ();
                stack.pop_back ();
                (*reinterpret_cast<char**>(&__pointer))[__offset] = static_cast<char>(static_cast<unsigned char>(__rhs));
                // Result of assignment
                stack.push_back (static_cast<long>(static_cast<unsigned char>((*reinterpret_cast<char**>(&__pointer))[__offset])));
                // Statement results can be ignored
                stack.pop_back ();
                // End Statement

            }
            // End of if
            //-------------------------------------------------------------
            //-------------------------------------------------------------
            // Update
            // Pre-Increment
            {
                // RHS
                stack.push_back (*reinterpret_cast<long*>(&__main__block__32__for__41__block__42__for__43__j));
                __rhs = stack.back ();
                stack.pop_back ();
                __main__block__32__for__41__block__42__for__43__j = __main__block__32__for__41__block__42__for__43__j + 1;
                __res = __main__block__32__for__41__block__42__for__43__j;
                stack.push_back (*reinterpret_cast<long*>(&__res));
            }
        }
        //-----------------------------------------------------------------
        //-----------------------------------------------------------------
        // Update
        // Pre-Increment
        {
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__32__for__41__i));
            __rhs = stack.back ();
            stack.pop_back ();
            __main__block__32__for__41__i = __main__block__32__for__41__i + 1;
            __res = __main__block__32__for__41__i;
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
    }
    //---------------------------------------------------------------------
    //---------------------------------------------------------------------
    // For-Loop
    // Init
    // Assignment - '='
    // RHS
    // Int Literal
    stack.push_back (0);
    // LHS
    // Variable declaration
    long __main__block__32__for__46__i;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__32__for__46__i = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__32__for__46__i));
    // Using an infinite loop so we can write a separate multi-line condition
    while (1)
    {
        // Condition
        // Less Than
        {
            // LHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__32__for__46__i));
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__32__rows));
            __rhs = stack.back ();
            stack.pop_back ();
            __lhs = stack.back ();
            stack.pop_back ();
            long __res = *reinterpret_cast<long*>(&__lhs) < *reinterpret_cast<long*>(&__rhs);
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        long __cond = stack.back ();
        stack.pop_back ();
        // break out of loop if condition is false
        if (__cond == 0) break;
        // Body
        //-----------------------------------------------------------------
        // Code Block
        //-----------------------------------------------------------------
        // For-Loop
        // Init
        // Assignment - '='
        // RHS
        // Int Literal
        stack.push_back (0);
        // LHS
        // Variable declaration
        long __main__block__32__for__46__block__47__for__48__j;
        __rhs = stack.back ();
        stack.pop_back ();
        __main__block__32__for__46__block__47__for__48__j = *reinterpret_cast<long*>(&__rhs);
        // Result of assignment
        stack.push_back (*reinterpret_cast<long*>(&__main__block__32__for__46__block__47__for__48__j));
        // Using an infinite loop so we can write a separate multi-line condition
        while (1)
        {
            // Condition
            // Less Than
            {
                // LHS
                stack.push_back (*reinterpret_cast<long*>(&__main__block__32__for__46__block__47__for__48__j));
                // RHS
                stack.push_back (*reinterpret_cast<long*>(&__main__block__32__cols));
                __rhs = stack.back ();
                stack.pop_back ();
                __lhs = stack.back ();
                stack.pop_back ();
                long __res = *reinterpret_cast<long*>(&__lhs) < *reinterpret_cast<long*>(&__rhs);
                stack.push_back (*reinterpret_cast<long*>(&__res));
            }
            long __cond = stack.back ();
            stack.pop_back ();
            // break out of loop if condition is false
            if (__cond == 0) break;
            // Body
            //-------------------------------------------------------------
            // Code Block
            // Statement
            // Function Call - print(char) -> void
            {
                // Arguments
                // Subscript
                {
                    // LHS
                    // Subscript
                    {
                        // LHS
                        stack.push_back (reinterpret_cast<long>(__main__block__32__board));
                        // OFFSET
                        stack.push_back (*reinterpret_cast<long*>(&__main__block__32__for__46__i));
                        __offset = stack.back ();
                        stack.pop_back ();
                        __pointer = stack.back ();
                        stack.pop_back ();
                        stack.push_back (reinterpret_cast<long>((*reinterpret_cast<char***>(&__pointer))[*reinterpret_cast<long*>(&__offset)]));
                    }
                    // OFFSET
                    stack.push_back (*reinterpret_cast<long*>(&__main__block__32__for__46__block__47__for__48__j));
                    __offset = stack.back ();
                    stack.pop_back ();
                    __pointer = stack.back ();
                    stack.pop_back ();
                    stack.push_back (static_cast<long>(static_cast<unsigned char>((*reinterpret_cast<char**>(&__pointer))[*reinterpret_cast<long*>(&__offset)])));
                }
                
                __stackval = stack.back ();
                stack.pop_back ();
                // Reinterpret from general register
                char __arg0 = static_cast<char>(static_cast<unsigned char>(__stackval));
                // print
                __builtin__print__char (__arg0);
                stack.push_back (reinterpret_cast<long>(__res));
            }
            // Statement results can be ignored
            stack.pop_back ();
            // End Statement

            //-------------------------------------------------------------
            // Update
            // Pre-Increment
            {
                // RHS
                stack.push_back (*reinterpret_cast<long*>(&__main__block__32__for__46__block__47__for__48__j));
                __rhs = stack.back ();
                stack.pop_back ();
                __main__block__32__for__46__block__47__for__48__j = __main__block__32__for__46__block__47__for__48__j + 1;
                __res = __main__block__32__for__46__block__47__for__48__j;
                stack.push_back (*reinterpret_cast<long*>(&__res));
            }
        }
        //-----------------------------------------------------------------
        // Statement
        // Function Call - println() -> void
        {
            // Arguments
            // println
            __builtin__println ();
            stack.push_back (reinterpret_cast<long>(__res));
        }
        // Statement results can be ignored
        stack.pop_back ();
        // End Statement

        //-----------------------------------------------------------------
        // Update
        // Pre-Increment
        {
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__32__for__46__i));
            __rhs = stack.back ();
            stack.pop_back ();
            __main__block__32__for__46__i = __main__block__32__for__46__i + 1;
            __res = __main__block__32__for__46__i;
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
    }
    //---------------------------------------------------------------------
    //---------------------------------------------------------------------

    //=====================================================================
    //### END OF CODE ####################################################
    //=====================================================================

}
//=========================================================================
//### END OF MAIN ########################################################
//=========================================================================

