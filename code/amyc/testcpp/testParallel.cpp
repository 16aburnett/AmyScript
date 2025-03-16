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
// std::memcpy
#include <cstring>

// ========================================================================

// Exits the program with the given exit code 
// void exit(int exit_code)
// - exit_code : [rbp + 16]
// - uses external exit function from libc
void __builtin__exit__int (long exit_code) {
    exit ((int) exit_code);
}

// ========================================================================

// Frees memory of the given pointer
// *this is not used - delete keyword is used instead
// void free()
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
    // printf ("%f", v);
    // this removes trailing zeros
    std::cout << v;
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
    // printf ("%f\n", v);
    // this removes trailing zeros
    std::cout << v << std::endl;
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
// float float ()
double __builtin__float () {
    return 0.0;
}

//========================================================================
// returns default int value
// int int ()
long __builtin__int () {
    return 0l;
}

//========================================================================
// returns default char value
// char char ()
char __builtin__char () {
    return 0;
}

//========================================================================
// converts int to float
// float intToFloat (int value)
double __builtin__intToFloat__int (long v)
{
    return double (v);
}

//========================================================================
// parses a float from a given char[]
// float stringToFloat (char[])
double __builtin__stringToFloat__char__1 (char* s)
{
    return std::atof (s);
}

//========================================================================
// converts float to int
// int floatToInt (float)
long __builtin__floatToInt__float (double f)
{
    return long (f);
}


//========================================================================
// parses an int from a given char[]
// int stringToInt (char[] str)
long __builtin__stringToInt__char__1 (char* s)
{
    return std::atoi (s);
}


//========================================================================
// parses an int from a given char
// int charToInt (char)
long __builtin__charToInt__char (char c)
{
    return long (c);
}

//========================================================================
// converts int to string
// char[] string (int)
char* __builtin__string__int (long i)
{
    std::string str = std::to_string (i);
    // convert to heap string
    char* c_str = new char[str.length()];
    std::memcpy (c_str, str.c_str(), str.length());
    return c_str;
}

//========================================================================
// converts float to string
// char[] string (float)
char* __builtin__string__float (double f)
{
    std::string str = std::to_string (f);
    // convert to heap string
    char* c_str = new char[str.length()];
    std::memcpy (c_str, str.c_str(), str.length());
    return c_str;
}

//========================================================================

// returns default value for array and object (null)
// null null ()
// def __builtin__null ():
//     return None

//========================================================================

// the root class of all objects
class __builtin____main__Object
{
    public:
    // all objects will have a dispatch table
    void** dtable;
};
//=========================================================================
//### Header section #####################################################
//=========================================================================


//=========================================================================
//### Functions section ##################################################
//=========================================================================

//=========================================================================
//### Main function ######################################################
//=========================================================================

int main () {
    // Function Header
    // This stack is used to store results of expressions
    std::vector<long> stack;
    // Declare general purpose variables
    // These are longs and can store anything up to 8 bytes via casting
    long __stackval = 0;
    long __pointer = 0;
    long __offset = 0;
    long __parent = 0;
    long __child = 0;
    long __obj = 0;
    long __lhs = 0;
    long __rhs = 0;
    long __res = 0;

    // Main body
    //---------------------------------------------------------------------
    // Statement
    // Function Call - print(char[]) -> void
    {
        // Arguments
        // String Literal
        {
            char str_literal[] = "Input N => ";
            // convert to a heap string
            char* str = new char[12];
            // copy string to heap allocation
            std::memcpy (str, &str_literal, 12);
            stack.push_back (reinterpret_cast<long> (str));
        }
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        char* __arg0 = *reinterpret_cast<char**>(&__stackval);
        // print
        __builtin__print__char__1 (__arg0);
        // push dummy value - funcall returns void
        stack.push_back (0);
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Assignment - '='
    // RHS
    // Function Call - stringToInt(char[]) -> int
    {
        // Arguments
        // Function Call - input() -> char[]
        {
            // Arguments
            // input
            char* __res = __builtin__input ();
            stack.push_back (reinterpret_cast<long>(__res));
        }
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        char* __arg0 = *reinterpret_cast<char**>(&__stackval);
        // stringToInt
        long __res = __builtin__stringToInt__char__1 (__arg0);
        stack.push_back (*reinterpret_cast<long*>(&__res));
    }
    // LHS
    // Variable declaration
    long __main__N;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__N = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__N));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - print(char[]) -> void
    {
        // Arguments
        // String Literal
        {
            char str_literal[] = "Allocating arrays with ";
            // convert to a heap string
            char* str = new char[24];
            // copy string to heap allocation
            std::memcpy (str, &str_literal, 24);
            stack.push_back (reinterpret_cast<long> (str));
        }
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        char* __arg0 = *reinterpret_cast<char**>(&__stackval);
        // print
        __builtin__print__char__1 (__arg0);
        // push dummy value - funcall returns void
        stack.push_back (0);
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - print(int) -> void
    {
        // Arguments
        stack.push_back (*reinterpret_cast<long*>(&__main__N));
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        long __arg0 = *reinterpret_cast<long*>(&__stackval);
        // print
        __builtin__print__int (__arg0);
        // push dummy value - funcall returns void
        stack.push_back (0);
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(char[]) -> void
    {
        // Arguments
        // String Literal
        {
            char str_literal[] = " elements...";
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
        // push dummy value - funcall returns void
        stack.push_back (0);
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Assignment - '='
    // RHS
    // Array Allocator
    {
        stack.push_back (*reinterpret_cast<long*>(&__main__N));
        __stackval = stack.back ();
        stack.pop_back ();
        long* __res = new long[__stackval];
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // LHS
    // Variable declaration
    long* __main__A;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__A = *reinterpret_cast<long**>(&__rhs);
    // Result of assignment
    stack.push_back (reinterpret_cast<long>(__main__A));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Assignment - '='
    // RHS
    // Array Allocator
    {
        stack.push_back (*reinterpret_cast<long*>(&__main__N));
        __stackval = stack.back ();
        stack.pop_back ();
        long* __res = new long[__stackval];
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // LHS
    // Variable declaration
    long* __main__B_serial;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__B_serial = *reinterpret_cast<long**>(&__rhs);
    // Result of assignment
    stack.push_back (reinterpret_cast<long>(__main__B_serial));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Assignment - '='
    // RHS
    // Array Allocator
    {
        stack.push_back (*reinterpret_cast<long*>(&__main__N));
        __stackval = stack.back ();
        stack.pop_back ();
        long* __res = new long[__stackval];
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // LHS
    // Variable declaration
    long* __main__B_parallel;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__B_parallel = *reinterpret_cast<long**>(&__rhs);
    // Result of assignment
    stack.push_back (reinterpret_cast<long>(__main__B_parallel));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(char[]) -> void
    {
        // Arguments
        // String Literal
        {
            char str_literal[] = "Filling array, A...";
            // convert to a heap string
            char* str = new char[20];
            // copy string to heap allocation
            std::memcpy (str, &str_literal, 20);
            stack.push_back (reinterpret_cast<long> (str));
        }
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        char* __arg0 = *reinterpret_cast<char**>(&__stackval);
        // println
        __builtin__println__char__1 (__arg0);
        // push dummy value - funcall returns void
        stack.push_back (0);
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
    long __main__for__0__i;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__for__0__i = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__for__0__i));
    // We can ignore the init result
    stack.pop_back ();
    // Using an infinite loop so we can write a separate multi-line condition
    while (1)
    {
        // Condition
        // Less Than
        {
            // LHS
            stack.push_back (*reinterpret_cast<long*>(&__main__for__0__i));
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__N));
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
            stack.push_back (*reinterpret_cast<long*>(&__main__for__0__i));
            // RHS
            // Int Literal
            stack.push_back (2);
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
        stack.push_back (reinterpret_cast<long>(__main__A));
        // OFFSET
        stack.push_back (*reinterpret_cast<long*>(&__main__for__0__i));
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
            stack.push_back (*reinterpret_cast<long*>(&__main__for__0__i));
            __rhs = stack.back ();
            stack.pop_back ();
            __main__for__0__i = __main__for__0__i + 1;
            __res = __main__for__0__i;
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        // We can ignore the update result
        stack.pop_back ();
    }
    //---------------------------------------------------------------------
    // Statement
    // Function Call - println(char[]) -> void
    {
        // Arguments
        // String Literal
        {
            char str_literal[] = "Serial copy (B_serial = A)...";
            // convert to a heap string
            char* str = new char[30];
            // copy string to heap allocation
            std::memcpy (str, &str_literal, 30);
            stack.push_back (reinterpret_cast<long> (str));
        }
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        char* __arg0 = *reinterpret_cast<char**>(&__stackval);
        // println
        __builtin__println__char__1 (__arg0);
        // push dummy value - funcall returns void
        stack.push_back (0);
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
    long __main__for__2__i;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__for__2__i = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__for__2__i));
    // We can ignore the init result
    stack.pop_back ();
    // Using an infinite loop so we can write a separate multi-line condition
    while (1)
    {
        // Condition
        // Less Than
        {
            // LHS
            stack.push_back (*reinterpret_cast<long*>(&__main__for__2__i));
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__N));
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
        // Subscript Expression
        {
            // LHS
            stack.push_back (reinterpret_cast<long>(__main__A));
            // OFFSET
            stack.push_back (*reinterpret_cast<long*>(&__main__for__2__i));
            __offset = stack.back ();
            stack.pop_back ();
            __pointer = stack.back ();
            stack.pop_back ();
            long __res = (*reinterpret_cast<long**>(&__pointer))[*reinterpret_cast<long*>(&__offset)];
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        // LHS
        // Subscript assignment
        // LHS
        stack.push_back (reinterpret_cast<long>(__main__B_serial));
        // OFFSET
        stack.push_back (*reinterpret_cast<long*>(&__main__for__2__i));
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
            stack.push_back (*reinterpret_cast<long*>(&__main__for__2__i));
            __rhs = stack.back ();
            stack.pop_back ();
            __main__for__2__i = __main__for__2__i + 1;
            __res = __main__for__2__i;
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        // We can ignore the update result
        stack.pop_back ();
    }
    //---------------------------------------------------------------------
    // Statement
    // Function Call - println(char[]) -> void
    {
        // Arguments
        // String Literal
        {
            char str_literal[] = "Parallel copy (B_parallel = A)...";
            // convert to a heap string
            char* str = new char[34];
            // copy string to heap allocation
            std::memcpy (str, &str_literal, 34);
            stack.push_back (reinterpret_cast<long> (str));
        }
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        char* __arg0 = *reinterpret_cast<char**>(&__stackval);
        // println
        __builtin__println__char__1 (__arg0);
        // push dummy value - funcall returns void
        stack.push_back (0);
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    //---------------------------------------------------------------------
    // Parallel For-Loop
    #pragma omp parallel for
    for (long __main__parallel_for__4__i = 0; __main__parallel_for__4__i < __main__N; ++__main__parallel_for__4__i)
    {
        // Parallel Loop setup
        // Function Header
        // Declare general purpose variables
        // These are longs and can store anything up to 8 bytes via casting
        long __stackval = 0;
        long __pointer = 0;
        long __offset = 0;
        long __parent = 0;
        long __child = 0;
        long __obj = 0;
        long __lhs = 0;
        long __rhs = 0;
        long __res = 0;
        //-----------------------------------------------------------------
        // Parallel Loop's Body
        //-----------------------------------------------------------------
        // Code Block
        __main__B_parallel[__main__parallel_for__4__i] = __main__A[__main__parallel_for__4__i];
        //-----------------------------------------------------------------
    }
    //---------------------------------------------------------------------
    // Statement
    // Function Call - println(char[]) -> void
    {
        // Arguments
        // String Literal
        {
            char str_literal[] = "Verifying result (B_serial == B_parallel)...";
            // convert to a heap string
            char* str = new char[45];
            // copy string to heap allocation
            std::memcpy (str, &str_literal, 45);
            stack.push_back (reinterpret_cast<long> (str));
        }
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        char* __arg0 = *reinterpret_cast<char**>(&__stackval);
        // println
        __builtin__println__char__1 (__arg0);
        // push dummy value - funcall returns void
        stack.push_back (0);
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Assignment - '='
    // RHS
    // Int Literal
    stack.push_back (1);
    // LHS
    // Variable declaration
    long __main__do_arrays_match;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__do_arrays_match = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__do_arrays_match));
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
    long __main__for__6__i;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__for__6__i = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__for__6__i));
    // We can ignore the init result
    stack.pop_back ();
    // Using an infinite loop so we can write a separate multi-line condition
    while (1)
    {
        // Condition
        // Less Than
        {
            // LHS
            stack.push_back (*reinterpret_cast<long*>(&__main__for__6__i));
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__N));
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
        // If-Statement
        // Precomputing all if/elif conditions and give unique names
        // bc we can't have code between if and elif
        // Condition
        // Not Equal
        {
            // LHS
            // Subscript Expression
            {
                // LHS
                stack.push_back (reinterpret_cast<long>(__main__B_parallel));
                // OFFSET
                stack.push_back (*reinterpret_cast<long*>(&__main__for__6__i));
                __offset = stack.back ();
                stack.pop_back ();
                __pointer = stack.back ();
                stack.pop_back ();
                long __res = (*reinterpret_cast<long**>(&__pointer))[*reinterpret_cast<long*>(&__offset)];
                stack.push_back (*reinterpret_cast<long*>(&__res));
            }
            // RHS
            // Subscript Expression
            {
                // LHS
                stack.push_back (reinterpret_cast<long>(__main__B_serial));
                // OFFSET
                stack.push_back (*reinterpret_cast<long*>(&__main__for__6__i));
                __offset = stack.back ();
                stack.pop_back ();
                __pointer = stack.back ();
                stack.pop_back ();
                long __res = (*reinterpret_cast<long**>(&__pointer))[*reinterpret_cast<long*>(&__offset)];
                stack.push_back (*reinterpret_cast<long*>(&__res));
            }
            __rhs = stack.back ();
            stack.pop_back ();
            __lhs = stack.back ();
            stack.pop_back ();
            long __res = *reinterpret_cast<long*>(&__lhs) != *reinterpret_cast<long*>(&__rhs);
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        long __if__8__cond = stack.back ();
        stack.pop_back ();
        // get condition from stack
        if (__if__8__cond)
        {
            // Body
            //-------------------------------------------------------------
            // Code Block
            // Statement
            // Assignment - '='
            // RHS
            // Int Literal
            stack.push_back (0);
            __rhs = stack.back ();
            stack.pop_back ();
            __main__do_arrays_match = *reinterpret_cast<long*>(&__rhs);
            // Result of assignment
            stack.push_back (*reinterpret_cast<long*>(&__main__do_arrays_match));
            // Statement results can be ignored
            stack.pop_back ();
            // End Statement

            // Statement
            // Function Call - println(char[]) -> void
            {
                // Arguments
                // String Literal
                {
                    char str_literal[] = "Does not match";
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
                // push dummy value - funcall returns void
                stack.push_back (0);
            }
            // Statement results can be ignored
            stack.pop_back ();
            // End Statement

            // Statement
            // Function Call - print(char[]) -> void
            {
                // Arguments
                // String Literal
                {
                    char str_literal[] = "i:            ";
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
                // push dummy value - funcall returns void
                stack.push_back (0);
            }
            // Statement results can be ignored
            stack.pop_back ();
            // End Statement

            // Statement
            // Function Call - println(int) -> void
            {
                // Arguments
                stack.push_back (*reinterpret_cast<long*>(&__main__for__6__i));
                
                __stackval = stack.back ();
                stack.pop_back ();
                // Reinterpret from general register
                long __arg0 = *reinterpret_cast<long*>(&__stackval);
                // println
                __builtin__println__int (__arg0);
                // push dummy value - funcall returns void
                stack.push_back (0);
            }
            // Statement results can be ignored
            stack.pop_back ();
            // End Statement

            // Statement
            // Function Call - print(char[]) -> void
            {
                // Arguments
                // String Literal
                {
                    char str_literal[] = "B_parallel[i]:";
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
                // push dummy value - funcall returns void
                stack.push_back (0);
            }
            // Statement results can be ignored
            stack.pop_back ();
            // End Statement

            // Statement
            // Function Call - println(int) -> void
            {
                // Arguments
                // Subscript Expression
                {
                    // LHS
                    stack.push_back (reinterpret_cast<long>(__main__B_parallel));
                    // OFFSET
                    stack.push_back (*reinterpret_cast<long*>(&__main__for__6__i));
                    __offset = stack.back ();
                    stack.pop_back ();
                    __pointer = stack.back ();
                    stack.pop_back ();
                    long __res = (*reinterpret_cast<long**>(&__pointer))[*reinterpret_cast<long*>(&__offset)];
                    stack.push_back (*reinterpret_cast<long*>(&__res));
                }
                
                __stackval = stack.back ();
                stack.pop_back ();
                // Reinterpret from general register
                long __arg0 = *reinterpret_cast<long*>(&__stackval);
                // println
                __builtin__println__int (__arg0);
                // push dummy value - funcall returns void
                stack.push_back (0);
            }
            // Statement results can be ignored
            stack.pop_back ();
            // End Statement

            // Statement
            // Function Call - print(char[]) -> void
            {
                // Arguments
                // String Literal
                {
                    char str_literal[] = "B_serial[i]:  ";
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
                // push dummy value - funcall returns void
                stack.push_back (0);
            }
            // Statement results can be ignored
            stack.pop_back ();
            // End Statement

            // Statement
            // Function Call - println(int) -> void
            {
                // Arguments
                // Subscript Expression
                {
                    // LHS
                    stack.push_back (reinterpret_cast<long>(__main__B_serial));
                    // OFFSET
                    stack.push_back (*reinterpret_cast<long*>(&__main__for__6__i));
                    __offset = stack.back ();
                    stack.pop_back ();
                    __pointer = stack.back ();
                    stack.pop_back ();
                    long __res = (*reinterpret_cast<long**>(&__pointer))[*reinterpret_cast<long*>(&__offset)];
                    stack.push_back (*reinterpret_cast<long*>(&__res));
                }
                
                __stackval = stack.back ();
                stack.pop_back ();
                // Reinterpret from general register
                long __arg0 = *reinterpret_cast<long*>(&__stackval);
                // println
                __builtin__println__int (__arg0);
                // push dummy value - funcall returns void
                stack.push_back (0);
            }
            // Statement results can be ignored
            stack.pop_back ();
            // End Statement

            // Statement
            // Function Call - print(char[]) -> void
            {
                // Arguments
                // String Literal
                {
                    char str_literal[] = "A[i]:         ";
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
                // push dummy value - funcall returns void
                stack.push_back (0);
            }
            // Statement results can be ignored
            stack.pop_back ();
            // End Statement

            // Statement
            // Function Call - println(int) -> void
            {
                // Arguments
                // Subscript Expression
                {
                    // LHS
                    stack.push_back (reinterpret_cast<long>(__main__A));
                    // OFFSET
                    stack.push_back (*reinterpret_cast<long*>(&__main__for__6__i));
                    __offset = stack.back ();
                    stack.pop_back ();
                    __pointer = stack.back ();
                    stack.pop_back ();
                    long __res = (*reinterpret_cast<long**>(&__pointer))[*reinterpret_cast<long*>(&__offset)];
                    stack.push_back (*reinterpret_cast<long*>(&__res));
                }
                
                __stackval = stack.back ();
                stack.pop_back ();
                // Reinterpret from general register
                long __arg0 = *reinterpret_cast<long*>(&__stackval);
                // println
                __builtin__println__int (__arg0);
                // push dummy value - funcall returns void
                stack.push_back (0);
            }
            // Statement results can be ignored
            stack.pop_back ();
            // End Statement

            // Break out of __for__6
            break;
            //-------------------------------------------------------------
        }
        // End of if
        //-----------------------------------------------------------------
        //-----------------------------------------------------------------
        // Update
        // Pre-Increment
        {
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__for__6__i));
            __rhs = stack.back ();
            stack.pop_back ();
            __main__for__6__i = __main__for__6__i + 1;
            __res = __main__for__6__i;
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        // We can ignore the update result
        stack.pop_back ();
    }
    //---------------------------------------------------------------------
    //---------------------------------------------------------------------
    // If-Statement
    // Precomputing all if/elif conditions and give unique names
    // bc we can't have code between if and elif
    // Condition
    stack.push_back (*reinterpret_cast<long*>(&__main__do_arrays_match));
    long __if__10__cond = stack.back ();
    stack.pop_back ();
    // get condition from stack
    if (__if__10__cond)
    {
        // Body
        // Statement
        // Function Call - println(char[]) -> void
        {
            // Arguments
            // String Literal
            {
                char str_literal[] = "Verification: PASS";
                // convert to a heap string
                char* str = new char[19];
                // copy string to heap allocation
                std::memcpy (str, &str_literal, 19);
                stack.push_back (reinterpret_cast<long> (str));
            }
            
            __stackval = stack.back ();
            stack.pop_back ();
            // Reinterpret from general register
            char* __arg0 = *reinterpret_cast<char**>(&__stackval);
            // println
            __builtin__println__char__1 (__arg0);
            // push dummy value - funcall returns void
            stack.push_back (0);
        }
        // Statement results can be ignored
        stack.pop_back ();
        // End Statement

    }
    //---------------------------------------------------------------------
    // Else-Statement
    else
    {
        // Statement
        // Function Call - println(char[]) -> void
        {
            // Arguments
            // String Literal
            {
                char str_literal[] = "Verification: FAIL";
                // convert to a heap string
                char* str = new char[19];
                // copy string to heap allocation
                std::memcpy (str, &str_literal, 19);
                stack.push_back (reinterpret_cast<long> (str));
            }
            
            __stackval = stack.back ();
            stack.pop_back ();
            // Reinterpret from general register
            char* __arg0 = *reinterpret_cast<char**>(&__stackval);
            // println
            __builtin__println__char__1 (__arg0);
            // push dummy value - funcall returns void
            stack.push_back (0);
        }
        // Statement results can be ignored
        stack.pop_back ();
        // End Statement

    }
    //---------------------------------------------------------------------
    // End of if
    //---------------------------------------------------------------------
}
//=========================================================================
//### END OF MAIN ########################################################
//=========================================================================

