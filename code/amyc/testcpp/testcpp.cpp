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

long __main__block__0____sum__int__int (long __main__block__0__sum__a, long __main__block__0__sum__b);
double __main__block__0____sum__float__float (double __main__block__0__sum__a, double __main__block__0__sum__b);
long __main__block__0____sum__int__int__int (long __main__block__0__sum__a, long __main__block__0__sum__b, long __main__block__0__sum__c);
long __main__block__0__sum__block__3____sum__int__int (long __main__block__0__sum__block__3__sum__a, long __main__block__0__sum__block__3__sum__b);
void __main__block__0____print__int__char__float (long __main__block__0__print__x, char __main__block__0__print__c, double __main__block__0__print__f);
long __main__block__8____max__int__int (long __main__block__8__max__a, long __main__block__8__max__b);
long __main__block__48____add__int____int__int (long __main__block__48__add__a, long __main__block__48__add__b);
double __main__block__48____add__float____float__float (double __main__block__48__add__a, double __main__block__48__add__b);
long __main__block__48____default_value__int__ ();
double __main__block__48____default_value__float__ ();
char __main__block__48____default_value__char__ ();
// Class Declaration - __main__block__54____A inherits __builtin____main__Object
void* __dtable____main__block__54____A[2];
class __main__block__54____A : public __builtin____main__Object
{
    public:
    // Field - int A::x
    long __field____main__block__54____A____x;
    __main__block__54____A ();
};
// Class Declaration - __main__block__54____B inherits __main__block__54____A
void* __dtable____main__block__54____B[2];
class __main__block__54____B : public __main__block__54____A
{
    public:
    // Field - int B::x
    // __field____main__block__54____A____x Inherited from A
    // Field - int B::y
    long __field____main__block__54____B____y;
    __main__block__54____B ();
};
// Class Declaration - __main__block__54____C inherits __main__block__54____A
void* __dtable____main__block__54____C[2];
class __main__block__54____C : public __main__block__54____A
{
    public:
    // Field - int C::x
    // __field____main__block__54____A____x Inherited from A
    // Field - float C::z
    double __field____main__block__54____C____z;
    __main__block__54____C ();
};
void __main__block__54____print__A (__main__block__54____A* __main__block__54__print__a);
// Class Declaration - __main__block__63____A inherits __builtin____main__Object
void* __dtable____main__block__63____A[0];
class __main__block__63____A : public __builtin____main__Object
{
    public:
    // Field - int A::x
    long __field____main__block__63____A____x;
    // Field - float A::y
    double __field____main__block__63____A____y;
    __main__block__63____A ();
};
// Class Declaration - __main__block__70____Vec__char inherits __builtin____main__Object
void* __dtable____main__block__70____Vec__char[1];
class __main__block__70____Vec__char : public __builtin____main__Object
{
    public:
    // Field - char[] Vec<:char:>::data
    char* __field____main__block__70____Vec__char____data;
    // Field - int Vec<:char:>::size
    long __field____main__block__70____Vec__char____size;
    __main__block__70____Vec__char ();
};
class __main__block__70____Vec__char; // Vec<:char:>
// Class Declaration - __main__block__70____Vec__Vec inherits __builtin____main__Object
void* __dtable____main__block__70____Vec__Vec[1];
class __main__block__70____Vec__Vec : public __builtin____main__Object
{
    public:
    // Field - Vec<:char:>[] Vec<:Vec<:char:>:>::data
    __main__block__70____Vec__char** __field____main__block__70____Vec__Vec____data;
    // Field - int Vec<:Vec<:char:>:>::size
    long __field____main__block__70____Vec__Vec____size;
    __main__block__70____Vec__Vec ();
};
class __main__block__70____Point; // Point
// Class Declaration - __main__block__70____Vec__Point inherits __builtin____main__Object
void* __dtable____main__block__70____Vec__Point[1];
class __main__block__70____Vec__Point : public __builtin____main__Object
{
    public:
    // Field - Point[] Vec<:Point:>::data
    __main__block__70____Point** __field____main__block__70____Vec__Point____data;
    // Field - int Vec<:Point:>::size
    long __field____main__block__70____Vec__Point____size;
    __main__block__70____Vec__Point ();
};
// Class Declaration - __main__block__70____Point inherits __builtin____main__Object
void* __dtable____main__block__70____Point[0];
class __main__block__70____Point : public __builtin____main__Object
{
    public:
    // Field - int Point::x
    long __field____main__block__70____Point____x;
    // Field - int Point::y
    long __field____main__block__70____Point____y;
    __main__block__70____Point (long __main__block__70____Point__x, long __main__block__70____Point__y);
};
class __main__block__87____B; // B
// Class Declaration - __main__block__87____A__B inherits __builtin____main__Object
void* __dtable____main__block__87____A__B[0];
class __main__block__87____A__B : public __builtin____main__Object
{
    public:
    // Field - B A<:B:>::x
    __main__block__87____B* __field____main__block__87____A__B____x;
    __main__block__87____A__B ();
};
// Class Declaration - __main__block__87____B inherits __builtin____main__Object
void* __dtable____main__block__87____B[0];
class __main__block__87____B : public __builtin____main__Object
{
    public:
    // Field - int B::w
    long __field____main__block__87____B____w;
    __main__block__87____B ();
};
void __main__block__87____print__B (__main__block__87____B* __main__block__87__print__b);
//=========================================================================
//### Functions section ##################################################
//=========================================================================

//=========================================================================
// Function Declaration - sum(int, int) -> int
long __main__block__0____sum__int__int (long __main__block__0__sum__a, long __main__block__0__sum__b)
{
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
    // Body
    //---------------------------------------------------------------------
    // Code Block
    // Return
    // Addition
    {
        // LHS
        stack.push_back (*reinterpret_cast<long*>(&__main__block__0__sum__a));
        // RHS
        stack.push_back (*reinterpret_cast<long*>(&__main__block__0__sum__b));
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
    //---------------------------------------------------------------------
};
// End Function Declaration - __main__block__0____sum__int__int
//=========================================================================

//=========================================================================
// Function Declaration - sum(float, float) -> float
double __main__block__0____sum__float__float (double __main__block__0__sum__a, double __main__block__0__sum__b)
{
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
    // Body
    //---------------------------------------------------------------------
    // Code Block
    // Return
    // Addition
    {
        // LHS
        stack.push_back (*reinterpret_cast<long*>(&__main__block__0__sum__a));
        // RHS
        stack.push_back (*reinterpret_cast<long*>(&__main__block__0__sum__b));
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
    //---------------------------------------------------------------------
};
// End Function Declaration - __main__block__0____sum__float__float
//=========================================================================

//=========================================================================
// Function Declaration - sum(int, int) -> int
long __main__block__0__sum__block__3____sum__int__int (long __main__block__0__sum__block__3__sum__a, long __main__block__0__sum__block__3__sum__b)
{
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
    // Body
    //---------------------------------------------------------------------
    // Code Block
    // Return
    // Addition
    {
        // LHS
        stack.push_back (*reinterpret_cast<long*>(&__main__block__0__sum__block__3__sum__a));
        // RHS
        stack.push_back (*reinterpret_cast<long*>(&__main__block__0__sum__block__3__sum__b));
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
    //---------------------------------------------------------------------
};
// End Function Declaration - __main__block__0__sum__block__3____sum__int__int
//=========================================================================

//=========================================================================
// Function Declaration - sum(int, int, int) -> int
long __main__block__0____sum__int__int__int (long __main__block__0__sum__a, long __main__block__0__sum__b, long __main__block__0__sum__c)
{
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
    // Body
    //---------------------------------------------------------------------
    // Code Block
    // Function Declaration - sum(int, int) -> int
    // *see this func def before this parent function

    // Return
    // Function Call - sum(int, int) -> int
    {
        // Arguments
        // Function Call - sum(int, int) -> int
        {
            // Arguments
            stack.push_back (*reinterpret_cast<long*>(&__main__block__0__sum__a));
            stack.push_back (*reinterpret_cast<long*>(&__main__block__0__sum__b));
            
            __stackval = stack.back ();
            stack.pop_back ();
            // Reinterpret from general register
            long __arg1 = *reinterpret_cast<long*>(&__stackval);
            
            __stackval = stack.back ();
            stack.pop_back ();
            // Reinterpret from general register
            long __arg0 = *reinterpret_cast<long*>(&__stackval);
            // sum
            long __res = __main__block__0__sum__block__3____sum__int__int (__arg0, __arg1);
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        stack.push_back (*reinterpret_cast<long*>(&__main__block__0__sum__c));
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        long __arg1 = *reinterpret_cast<long*>(&__stackval);
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        long __arg0 = *reinterpret_cast<long*>(&__stackval);
        // sum
        long __res = __main__block__0__sum__block__3____sum__int__int (__arg0, __arg1);
        stack.push_back (*reinterpret_cast<long*>(&__res));
    }
    __res = stack.back ();
    stack.pop_back ();
    return *reinterpret_cast<long*>(&__res);
    //---------------------------------------------------------------------
};
// End Function Declaration - __main__block__0____sum__int__int__int
//=========================================================================

//=========================================================================
// Function Declaration - print(int, char, float) -> void
void __main__block__0____print__int__char__float (long __main__block__0__print__x, char __main__block__0__print__c, double __main__block__0__print__f)
{
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
    // Body
    //---------------------------------------------------------------------
    // Code Block
    // Statement
    // Function Call - println(int) -> void
    {
        // Arguments
        stack.push_back (*reinterpret_cast<long*>(&__main__block__0__print__x));
        
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
    // Function Call - println(char) -> void
    {
        // Arguments
        stack.push_back (static_cast<long>(static_cast<unsigned char>(__main__block__0__print__c)));
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        char __arg0 = static_cast<char>(static_cast<unsigned char>(__stackval));
        // println
        __builtin__println__char (__arg0);
        // push dummy value - funcall returns void
        stack.push_back (0);
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(float) -> void
    {
        // Arguments
        stack.push_back (*reinterpret_cast<long*>(&__main__block__0__print__f));
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        double __arg0 = *reinterpret_cast<double*>(&__stackval);
        // println
        __builtin__println__float (__arg0);
        // push dummy value - funcall returns void
        stack.push_back (0);
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    //---------------------------------------------------------------------
};
// End Function Declaration - __main__block__0____print__int__char__float
//=========================================================================

//=========================================================================
// Function Declaration - max(int, int) -> int
long __main__block__8____max__int__int (long __main__block__8__max__a, long __main__block__8__max__b)
{
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
    // Body
    //---------------------------------------------------------------------
    // Code Block
    //---------------------------------------------------------------------
    // If-Statement
    // Precomputing all if/elif conditions and give unique names
    // bc we can't have code between if and elif
    // Condition
    // Greater Than or Equal to
    {
        // LHS
        stack.push_back (*reinterpret_cast<long*>(&__main__block__8__max__a));
        // RHS
        stack.push_back (*reinterpret_cast<long*>(&__main__block__8__max__b));
        __rhs = stack.back ();
        stack.pop_back ();
        __lhs = stack.back ();
        stack.pop_back ();
        long __res = *reinterpret_cast<long*>(&__lhs) >= *reinterpret_cast<long*>(&__rhs);
        stack.push_back (*reinterpret_cast<long*>(&__res));
    }
    long __if__14__cond = stack.back ();
    stack.pop_back ();
    // get condition from stack
    if (__if__14__cond)
    {
        // Body
        // Return
        stack.push_back (*reinterpret_cast<long*>(&__main__block__8__max__a));
        __res = stack.back ();
        stack.pop_back ();
        return *reinterpret_cast<long*>(&__res);
    }
    // End of if
    //---------------------------------------------------------------------
    // Return
    stack.push_back (*reinterpret_cast<long*>(&__main__block__8__max__b));
    __res = stack.back ();
    stack.pop_back ();
    return *reinterpret_cast<long*>(&__res);
    //---------------------------------------------------------------------
};
// End Function Declaration - __main__block__8____max__int__int
//=========================================================================

//=========================================================================
// Function Declaration - add<:int:>(int, int) -> int
long __main__block__48____add__int____int__int (long __main__block__48__add__a, long __main__block__48__add__b)
{
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
    // Body
    //---------------------------------------------------------------------
    // Code Block
    // Return
    // Addition
    {
        // LHS
        stack.push_back (*reinterpret_cast<long*>(&__main__block__48__add__a));
        // RHS
        stack.push_back (*reinterpret_cast<long*>(&__main__block__48__add__b));
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
    //---------------------------------------------------------------------
};
// End Function Declaration - __main__block__48____add__int____int__int
//=========================================================================

//=========================================================================
// Function Declaration - add<:float:>(float, float) -> float
double __main__block__48____add__float____float__float (double __main__block__48__add__a, double __main__block__48__add__b)
{
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
    // Body
    //---------------------------------------------------------------------
    // Code Block
    // Return
    // Addition
    {
        // LHS
        stack.push_back (*reinterpret_cast<long*>(&__main__block__48__add__a));
        // RHS
        stack.push_back (*reinterpret_cast<long*>(&__main__block__48__add__b));
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
    //---------------------------------------------------------------------
};
// End Function Declaration - __main__block__48____add__float____float__float
//=========================================================================

//=========================================================================
// Function Declaration - default_value<:int:>() -> int
long __main__block__48____default_value__int__ ()
{
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
    // Body
    //---------------------------------------------------------------------
    // Code Block
    // Return
    // Function Call - int() -> int
    {
        // Arguments
        // int
        long __res = __builtin__int ();
        stack.push_back (*reinterpret_cast<long*>(&__res));
    }
    __res = stack.back ();
    stack.pop_back ();
    return *reinterpret_cast<long*>(&__res);
    //---------------------------------------------------------------------
};
// End Function Declaration - __main__block__48____default_value__int__
//=========================================================================

//=========================================================================
// Function Declaration - default_value<:float:>() -> float
double __main__block__48____default_value__float__ ()
{
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
    // Body
    //---------------------------------------------------------------------
    // Code Block
    // Return
    // Function Call - float() -> float
    {
        // Arguments
        // float
        double __res = __builtin__float ();
        stack.push_back (*reinterpret_cast<long*>(&__res));
    }
    __res = stack.back ();
    stack.pop_back ();
    return *reinterpret_cast<double*>(&__res);
    //---------------------------------------------------------------------
};
// End Function Declaration - __main__block__48____default_value__float__
//=========================================================================

//=========================================================================
// Function Declaration - default_value<:char:>() -> char
char __main__block__48____default_value__char__ ()
{
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
    // Body
    //---------------------------------------------------------------------
    // Code Block
    // Return
    // Function Call - char() -> char
    {
        // Arguments
        // char
        char __res = __builtin__char ();
        stack.push_back (static_cast<long>(static_cast<unsigned char>(__res)));
    }
    __res = stack.back ();
    stack.pop_back ();
    return static_cast<char>(static_cast<unsigned char>(__res));
    //---------------------------------------------------------------------
};
// End Function Declaration - __main__block__48____default_value__char__
//=========================================================================

//-------------------------------------------------------------------------
// Constructor Declaration - A::A() -> A
__main__block__54____A::__main__block__54____A ()
{
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
    // Add dispatch table to instance
    dtable = __dtable____main__block__54____A;
    __main__block__54____A* __this = this;
    // Body
    //---------------------------------------------------------------------
    // Code Block
    // Statement
    // Assignment - '='
    // RHS
    // Int Literal
    stack.push_back (10);
    // LHS
    // Member Accessor Assignment
    // LHS
    stack.push_back (reinterpret_cast<long>(__this));
    // RHS
    __parent = stack.back ();
    stack.pop_back ();
    __rhs = stack.back ();
    stack.pop_back ();
    (reinterpret_cast<__main__block__54____A*>(__parent))->__field____main__block__54____A____x = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&(reinterpret_cast<__main__block__54____A*>(__parent))->__field____main__block__54____A____x));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    //---------------------------------------------------------------------
}
// End Constructor Declaration - __ctor____main__block__54____A____A
//-------------------------------------------------------------------------

//-------------------------------------------------------------------------
// Method Declaration - A::print() -> void
void __method____main__block__54____A____print (__main__block__54____A* __this)
{
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
    // Body
    //---------------------------------------------------------------------
    // Code Block
    // Statement
    // Function Call - print(char[]) -> void
    {
        // Arguments
        // String Literal
        {
            char str_literal[] = "   is A with values ";
            // convert to a heap string
            char* str = new char[21];
            // copy string to heap allocation
            std::memcpy (str, &str_literal, 21);
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
        // Member Accessor obj.x
        {
            // LHS
            stack.push_back (reinterpret_cast<long>(__this));
            // RHS
            __parent = stack.back ();
            stack.pop_back ();
            long __res = (reinterpret_cast<__main__block__54____A*>(__parent))->__field____main__block__54____A____x;
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

    //---------------------------------------------------------------------
}
// End Method Declaration - __method____main__block__54____A____print
//-------------------------------------------------------------------------

//-------------------------------------------------------------------------
// Method Declaration - A::add(int) -> int
long __method____main__block__54____A____add__int (__main__block__54____A* __this, long __main__block__54____A__add__v)
{
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
    // Body
    //---------------------------------------------------------------------
    // Code Block
    // Statement
    // Assignment - '+='
    // RHS
    stack.push_back (*reinterpret_cast<long*>(&__main__block__54____A__add__v));
    // LHS
    // Member Accessor Assignment
    // LHS
    stack.push_back (reinterpret_cast<long>(__this));
    // RHS
    __parent = stack.back ();
    stack.pop_back ();
    __rhs = stack.back ();
    stack.pop_back ();
    (reinterpret_cast<__main__block__54____A*>(__parent))->__field____main__block__54____A____x = (reinterpret_cast<__main__block__54____A*>(__parent))->__field____main__block__54____A____x + *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&(reinterpret_cast<__main__block__54____A*>(__parent))->__field____main__block__54____A____x));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Return
    // Member Accessor obj.x
    {
        // LHS
        stack.push_back (reinterpret_cast<long>(__this));
        // RHS
        __parent = stack.back ();
        stack.pop_back ();
        long __res = (reinterpret_cast<__main__block__54____A*>(__parent))->__field____main__block__54____A____x;
        stack.push_back (*reinterpret_cast<long*>(&__res));
    }
    __res = stack.back ();
    stack.pop_back ();
    return *reinterpret_cast<long*>(&__res);
    //---------------------------------------------------------------------
}
// End Method Declaration - __method____main__block__54____A____add__int
//-------------------------------------------------------------------------

//-------------------------------------------------------------------------
// Constructor Declaration - B::B() -> B
__main__block__54____B::__main__block__54____B ()
{
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
    // Add dispatch table to instance
    dtable = __dtable____main__block__54____B;
    __main__block__54____B* __this = this;
    // Body
    //---------------------------------------------------------------------
    // Code Block
    // Statement
    // Assignment - '='
    // RHS
    // Int Literal
    stack.push_back (42);
    // LHS
    // Member Accessor Assignment
    // LHS
    stack.push_back (reinterpret_cast<long>(__this));
    // RHS
    __parent = stack.back ();
    stack.pop_back ();
    __rhs = stack.back ();
    stack.pop_back ();
    (reinterpret_cast<__main__block__54____B*>(__parent))->__field____main__block__54____A____x = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&(reinterpret_cast<__main__block__54____B*>(__parent))->__field____main__block__54____A____x));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Assignment - '='
    // RHS
    // Int Literal
    stack.push_back (14);
    // LHS
    // Member Accessor Assignment
    // LHS
    stack.push_back (reinterpret_cast<long>(__this));
    // RHS
    __parent = stack.back ();
    stack.pop_back ();
    __rhs = stack.back ();
    stack.pop_back ();
    (reinterpret_cast<__main__block__54____B*>(__parent))->__field____main__block__54____B____y = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&(reinterpret_cast<__main__block__54____B*>(__parent))->__field____main__block__54____B____y));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    //---------------------------------------------------------------------
}
// End Constructor Declaration - __ctor____main__block__54____B____B
//-------------------------------------------------------------------------

//-------------------------------------------------------------------------
// Method Declaration - B::add(int) -> int
// Inherited from A
long __method____main__block__54____B____add__int (__main__block__54____B* __this, long __main__block__54____B__add__v)
{
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
    // Jump to A's version
    long __inheritedres = __method____main__block__54____A____add__int (__this, __main__block__54____B__add__v);
    return __inheritedres;
}
// End Method Declaration - __method____main__block__54____B____add__int
//-------------------------------------------------------------------------

//-------------------------------------------------------------------------
// Method Declaration - B::print() -> void
void __method____main__block__54____B____print (__main__block__54____B* __this)
{
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
    // Body
    //---------------------------------------------------------------------
    // Code Block
    // Statement
    // Function Call - print(char[]) -> void
    {
        // Arguments
        // String Literal
        {
            char str_literal[] = "   is B with values ";
            // convert to a heap string
            char* str = new char[21];
            // copy string to heap allocation
            std::memcpy (str, &str_literal, 21);
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
        // Member Accessor obj.x
        {
            // LHS
            stack.push_back (reinterpret_cast<long>(__this));
            // RHS
            __parent = stack.back ();
            stack.pop_back ();
            long __res = (reinterpret_cast<__main__block__54____B*>(__parent))->__field____main__block__54____A____x;
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        
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
    // Function Call - print(char) -> void
    {
        // Arguments
        // Char Literal
        stack.push_back (static_cast<long>(static_cast<unsigned char>(',')));
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        char __arg0 = static_cast<char>(static_cast<unsigned char>(__stackval));
        // print
        __builtin__print__char (__arg0);
        // push dummy value - funcall returns void
        stack.push_back (0);
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

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
        // Member Accessor obj.y
        {
            // LHS
            stack.push_back (reinterpret_cast<long>(__this));
            // RHS
            __parent = stack.back ();
            stack.pop_back ();
            long __res = (reinterpret_cast<__main__block__54____B*>(__parent))->__field____main__block__54____B____y;
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

    //---------------------------------------------------------------------
}
// End Method Declaration - __method____main__block__54____B____print
//-------------------------------------------------------------------------

//-------------------------------------------------------------------------
// Constructor Declaration - C::C() -> C
__main__block__54____C::__main__block__54____C ()
{
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
    // Add dispatch table to instance
    dtable = __dtable____main__block__54____C;
    __main__block__54____C* __this = this;
    // Body
    //---------------------------------------------------------------------
    // Code Block
    // Statement
    // Assignment - '='
    // RHS
    // Int Literal
    stack.push_back (24);
    // LHS
    // Member Accessor Assignment
    // LHS
    stack.push_back (reinterpret_cast<long>(__this));
    // RHS
    __parent = stack.back ();
    stack.pop_back ();
    __rhs = stack.back ();
    stack.pop_back ();
    (reinterpret_cast<__main__block__54____C*>(__parent))->__field____main__block__54____A____x = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&(reinterpret_cast<__main__block__54____C*>(__parent))->__field____main__block__54____A____x));
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
    // Member Accessor Assignment
    // LHS
    stack.push_back (reinterpret_cast<long>(__this));
    // RHS
    __parent = stack.back ();
    stack.pop_back ();
    __rhs = stack.back ();
    stack.pop_back ();
    (reinterpret_cast<__main__block__54____C*>(__parent))->__field____main__block__54____C____z = *reinterpret_cast<double*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&(reinterpret_cast<__main__block__54____C*>(__parent))->__field____main__block__54____C____z));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    //---------------------------------------------------------------------
}
// End Constructor Declaration - __ctor____main__block__54____C____C
//-------------------------------------------------------------------------

//-------------------------------------------------------------------------
// Method Declaration - C::print() -> void
// Inherited from A
void __method____main__block__54____C____print (__main__block__54____C* __this)
{
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
    // Jump to A's version
    __method____main__block__54____A____print (__this);
}
// End Method Declaration - __method____main__block__54____C____print
//-------------------------------------------------------------------------

//-------------------------------------------------------------------------
// Method Declaration - C::add(int) -> int
// Inherited from A
long __method____main__block__54____C____add__int (__main__block__54____C* __this, long __main__block__54____C__add__v)
{
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
    // Jump to A's version
    long __inheritedres = __method____main__block__54____A____add__int (__this, __main__block__54____C__add__v);
    return __inheritedres;
}
// End Method Declaration - __method____main__block__54____C____add__int
//-------------------------------------------------------------------------

//=========================================================================
// Function Declaration - print(A) -> void
void __main__block__54____print__A (__main__block__54____A* __main__block__54__print__a)
{
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
    // Body
    //---------------------------------------------------------------------
    // Code Block
    // Statement
    // Function Call - print(char[]) -> void
    {
        // Arguments
        // String Literal
        {
            char str_literal[] = "is a A with value ";
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
        // Member Accessor obj.x
        {
            // LHS
            stack.push_back (reinterpret_cast<long>(__main__block__54__print__a));
            // RHS
            __parent = stack.back ();
            stack.pop_back ();
            long __res = (reinterpret_cast<__main__block__54____A*>(__parent))->__field____main__block__54____A____x;
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
    // Virtual Method Call - print() -> void
    // LHS
    stack.push_back (reinterpret_cast<long>(__main__block__54__print__a));
    // RHS
    {
        // Arguments
        __obj = stack.back ();
        stack.pop_back ();
        // Virtual Function Dispatch
        ((void(*)(__main__block__54____A*))(reinterpret_cast<__main__block__54____A*>(__obj)->dtable[0])) (reinterpret_cast<__main__block__54____A*>(__obj));
        // push dummy value - method rtype is void
        stack.push_back (0);
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    //---------------------------------------------------------------------
};
// End Function Declaration - __main__block__54____print__A
//=========================================================================

//-------------------------------------------------------------------------
// Constructor Declaration - A::A() -> A
__main__block__63____A::__main__block__63____A ()
{
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
    // Add dispatch table to instance
    dtable = __dtable____main__block__63____A;
    __main__block__63____A* __this = this;
    // Body
    //---------------------------------------------------------------------
    // Code Block
    // Statement
    // Assignment - '='
    // RHS
    // Int Literal
    stack.push_back (10);
    // LHS
    // Member Accessor Assignment
    // LHS
    stack.push_back (reinterpret_cast<long>(__this));
    // RHS
    __parent = stack.back ();
    stack.pop_back ();
    __rhs = stack.back ();
    stack.pop_back ();
    (reinterpret_cast<__main__block__63____A*>(__parent))->__field____main__block__63____A____x = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&(reinterpret_cast<__main__block__63____A*>(__parent))->__field____main__block__63____A____x));
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
    // Member Accessor Assignment
    // LHS
    stack.push_back (reinterpret_cast<long>(__this));
    // RHS
    __parent = stack.back ();
    stack.pop_back ();
    __rhs = stack.back ();
    stack.pop_back ();
    (reinterpret_cast<__main__block__63____A*>(__parent))->__field____main__block__63____A____y = *reinterpret_cast<double*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&(reinterpret_cast<__main__block__63____A*>(__parent))->__field____main__block__63____A____y));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    //---------------------------------------------------------------------
}
// End Constructor Declaration - __ctor____main__block__63____A____A
//-------------------------------------------------------------------------

//-------------------------------------------------------------------------
// Constructor Declaration - Vec<:char:>::Vec() -> Vec<:char:>
__main__block__70____Vec__char::__main__block__70____Vec__char ()
{
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
    // Add dispatch table to instance
    dtable = __dtable____main__block__70____Vec__char;
    __main__block__70____Vec__char* __this = this;
    // Body
    //---------------------------------------------------------------------
    // Code Block
    // Statement
    // Assignment - '='
    // RHS
    // Array Allocator
    {
        // Int Literal
        stack.push_back (10);
        __stackval = stack.back ();
        stack.pop_back ();
        char* __res = new char[__stackval];
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // LHS
    // Member Accessor Assignment
    // LHS
    stack.push_back (reinterpret_cast<long>(__this));
    // RHS
    __parent = stack.back ();
    stack.pop_back ();
    __rhs = stack.back ();
    stack.pop_back ();
    (reinterpret_cast<__main__block__70____Vec__char*>(__parent))->__field____main__block__70____Vec__char____data = *reinterpret_cast<char**>(&__rhs);
    // Result of assignment
    stack.push_back (reinterpret_cast<long>((reinterpret_cast<__main__block__70____Vec__char*>(__parent))->__field____main__block__70____Vec__char____data));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Assignment - '='
    // RHS
    // Int Literal
    stack.push_back (0);
    // LHS
    // Member Accessor Assignment
    // LHS
    stack.push_back (reinterpret_cast<long>(__this));
    // RHS
    __parent = stack.back ();
    stack.pop_back ();
    __rhs = stack.back ();
    stack.pop_back ();
    (reinterpret_cast<__main__block__70____Vec__char*>(__parent))->__field____main__block__70____Vec__char____size = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&(reinterpret_cast<__main__block__70____Vec__char*>(__parent))->__field____main__block__70____Vec__char____size));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    //---------------------------------------------------------------------
}
// End Constructor Declaration - __ctor____main__block__70____Vec__char____Vec
//-------------------------------------------------------------------------

//-------------------------------------------------------------------------
// Method Declaration - Vec<:char:>::push_back(char) -> void
void __method____main__block__70____Vec__char____push_back__char (__main__block__70____Vec__char* __this, char __main__block__70____Vec__char__push_back__v)
{
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
    // Body
    //---------------------------------------------------------------------
    // Code Block
    // Statement
    // Assignment - '='
    // RHS
    stack.push_back (static_cast<long>(static_cast<unsigned char>(__main__block__70____Vec__char__push_back__v)));
    // LHS
    // Subscript assignment
    // LHS
    // Member Accessor obj.data
    {
        // LHS
        stack.push_back (reinterpret_cast<long>(__this));
        // RHS
        __parent = stack.back ();
        stack.pop_back ();
        char* __res = (reinterpret_cast<__main__block__70____Vec__char*>(__parent))->__field____main__block__70____Vec__char____data;
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // OFFSET
    // Post-Increment
    {
        // LHS
        // Member Accessor Assignment
        // LHS
        stack.push_back (reinterpret_cast<long>(__this));
        // RHS
        __parent = stack.back ();
        stack.pop_back ();
        long __res = (reinterpret_cast<__main__block__70____Vec__char*>(__parent))->__field____main__block__70____Vec__char____size;
        (reinterpret_cast<__main__block__70____Vec__char*>(__parent))->__field____main__block__70____Vec__char____size = (reinterpret_cast<__main__block__70____Vec__char*>(__parent))->__field____main__block__70____Vec__char____size + 1;
        stack.push_back (*reinterpret_cast<long*>(&__res));
    }
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

    //---------------------------------------------------------------------
}
// End Method Declaration - __method____main__block__70____Vec__char____push_back__char
//-------------------------------------------------------------------------

//-------------------------------------------------------------------------
// Constructor Declaration - Vec<:Vec<:char:>:>::Vec() -> Vec<:Vec<:char:>:>
__main__block__70____Vec__Vec::__main__block__70____Vec__Vec ()
{
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
    // Add dispatch table to instance
    dtable = __dtable____main__block__70____Vec__Vec;
    __main__block__70____Vec__Vec* __this = this;
    // Body
    //---------------------------------------------------------------------
    // Code Block
    // Statement
    // Assignment - '='
    // RHS
    // Array Allocator
    {
        // Int Literal
        stack.push_back (10);
        __stackval = stack.back ();
        stack.pop_back ();
        __main__block__70____Vec__char** __res = new __main__block__70____Vec__char*[__stackval];
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // LHS
    // Member Accessor Assignment
    // LHS
    stack.push_back (reinterpret_cast<long>(__this));
    // RHS
    __parent = stack.back ();
    stack.pop_back ();
    __rhs = stack.back ();
    stack.pop_back ();
    (reinterpret_cast<__main__block__70____Vec__Vec*>(__parent))->__field____main__block__70____Vec__Vec____data = reinterpret_cast<__main__block__70____Vec__char**>(__rhs);
    // Result of assignment
    stack.push_back (reinterpret_cast<long>((reinterpret_cast<__main__block__70____Vec__Vec*>(__parent))->__field____main__block__70____Vec__Vec____data));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Assignment - '='
    // RHS
    // Int Literal
    stack.push_back (0);
    // LHS
    // Member Accessor Assignment
    // LHS
    stack.push_back (reinterpret_cast<long>(__this));
    // RHS
    __parent = stack.back ();
    stack.pop_back ();
    __rhs = stack.back ();
    stack.pop_back ();
    (reinterpret_cast<__main__block__70____Vec__Vec*>(__parent))->__field____main__block__70____Vec__Vec____size = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&(reinterpret_cast<__main__block__70____Vec__Vec*>(__parent))->__field____main__block__70____Vec__Vec____size));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    //---------------------------------------------------------------------
}
// End Constructor Declaration - __ctor____main__block__70____Vec__Vec____Vec
//-------------------------------------------------------------------------

//-------------------------------------------------------------------------
// Method Declaration - Vec<:Vec<:char:>:>::push_back(Vec<:char:>) -> void
void __method____main__block__70____Vec__Vec____push_back__Vec (__main__block__70____Vec__Vec* __this, __main__block__70____Vec__char* __main__block__70____Vec__Vec__push_back__v)
{
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
    // Body
    //---------------------------------------------------------------------
    // Code Block
    // Statement
    // Assignment - '='
    // RHS
    stack.push_back (reinterpret_cast<long>(__main__block__70____Vec__Vec__push_back__v));
    // LHS
    // Subscript assignment
    // LHS
    // Member Accessor obj.data
    {
        // LHS
        stack.push_back (reinterpret_cast<long>(__this));
        // RHS
        __parent = stack.back ();
        stack.pop_back ();
        __main__block__70____Vec__char** __res = (reinterpret_cast<__main__block__70____Vec__Vec*>(__parent))->__field____main__block__70____Vec__Vec____data;
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // OFFSET
    // Post-Increment
    {
        // LHS
        // Member Accessor Assignment
        // LHS
        stack.push_back (reinterpret_cast<long>(__this));
        // RHS
        __parent = stack.back ();
        stack.pop_back ();
        long __res = (reinterpret_cast<__main__block__70____Vec__Vec*>(__parent))->__field____main__block__70____Vec__Vec____size;
        (reinterpret_cast<__main__block__70____Vec__Vec*>(__parent))->__field____main__block__70____Vec__Vec____size = (reinterpret_cast<__main__block__70____Vec__Vec*>(__parent))->__field____main__block__70____Vec__Vec____size + 1;
        stack.push_back (*reinterpret_cast<long*>(&__res));
    }
    __offset = stack.back ();
    stack.pop_back ();
    __pointer = stack.back ();
    stack.pop_back ();
    __rhs = stack.back ();
    stack.pop_back ();
    (reinterpret_cast<__main__block__70____Vec__char**>(__pointer))[__offset] = reinterpret_cast<__main__block__70____Vec__char*>(__rhs);
    // Result of assignment
    stack.push_back (reinterpret_cast<long>((reinterpret_cast<__main__block__70____Vec__char**>(__pointer))[__offset]));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    //---------------------------------------------------------------------
}
// End Method Declaration - __method____main__block__70____Vec__Vec____push_back__Vec
//-------------------------------------------------------------------------

//-------------------------------------------------------------------------
// Constructor Declaration - Vec<:Point:>::Vec() -> Vec<:Point:>
__main__block__70____Vec__Point::__main__block__70____Vec__Point ()
{
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
    // Add dispatch table to instance
    dtable = __dtable____main__block__70____Vec__Point;
    __main__block__70____Vec__Point* __this = this;
    // Body
    //---------------------------------------------------------------------
    // Code Block
    // Statement
    // Assignment - '='
    // RHS
    // Array Allocator
    {
        // Int Literal
        stack.push_back (10);
        __stackval = stack.back ();
        stack.pop_back ();
        __main__block__70____Point** __res = new __main__block__70____Point*[__stackval];
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // LHS
    // Member Accessor Assignment
    // LHS
    stack.push_back (reinterpret_cast<long>(__this));
    // RHS
    __parent = stack.back ();
    stack.pop_back ();
    __rhs = stack.back ();
    stack.pop_back ();
    (reinterpret_cast<__main__block__70____Vec__Point*>(__parent))->__field____main__block__70____Vec__Point____data = reinterpret_cast<__main__block__70____Point**>(__rhs);
    // Result of assignment
    stack.push_back (reinterpret_cast<long>((reinterpret_cast<__main__block__70____Vec__Point*>(__parent))->__field____main__block__70____Vec__Point____data));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Assignment - '='
    // RHS
    // Int Literal
    stack.push_back (0);
    // LHS
    // Member Accessor Assignment
    // LHS
    stack.push_back (reinterpret_cast<long>(__this));
    // RHS
    __parent = stack.back ();
    stack.pop_back ();
    __rhs = stack.back ();
    stack.pop_back ();
    (reinterpret_cast<__main__block__70____Vec__Point*>(__parent))->__field____main__block__70____Vec__Point____size = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&(reinterpret_cast<__main__block__70____Vec__Point*>(__parent))->__field____main__block__70____Vec__Point____size));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    //---------------------------------------------------------------------
}
// End Constructor Declaration - __ctor____main__block__70____Vec__Point____Vec
//-------------------------------------------------------------------------

//-------------------------------------------------------------------------
// Method Declaration - Vec<:Point:>::push_back(Point) -> void
void __method____main__block__70____Vec__Point____push_back__Point (__main__block__70____Vec__Point* __this, __main__block__70____Point* __main__block__70____Vec__Point__push_back__v)
{
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
    // Body
    //---------------------------------------------------------------------
    // Code Block
    // Statement
    // Assignment - '='
    // RHS
    stack.push_back (reinterpret_cast<long>(__main__block__70____Vec__Point__push_back__v));
    // LHS
    // Subscript assignment
    // LHS
    // Member Accessor obj.data
    {
        // LHS
        stack.push_back (reinterpret_cast<long>(__this));
        // RHS
        __parent = stack.back ();
        stack.pop_back ();
        __main__block__70____Point** __res = (reinterpret_cast<__main__block__70____Vec__Point*>(__parent))->__field____main__block__70____Vec__Point____data;
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // OFFSET
    // Post-Increment
    {
        // LHS
        // Member Accessor Assignment
        // LHS
        stack.push_back (reinterpret_cast<long>(__this));
        // RHS
        __parent = stack.back ();
        stack.pop_back ();
        long __res = (reinterpret_cast<__main__block__70____Vec__Point*>(__parent))->__field____main__block__70____Vec__Point____size;
        (reinterpret_cast<__main__block__70____Vec__Point*>(__parent))->__field____main__block__70____Vec__Point____size = (reinterpret_cast<__main__block__70____Vec__Point*>(__parent))->__field____main__block__70____Vec__Point____size + 1;
        stack.push_back (*reinterpret_cast<long*>(&__res));
    }
    __offset = stack.back ();
    stack.pop_back ();
    __pointer = stack.back ();
    stack.pop_back ();
    __rhs = stack.back ();
    stack.pop_back ();
    (reinterpret_cast<__main__block__70____Point**>(__pointer))[__offset] = reinterpret_cast<__main__block__70____Point*>(__rhs);
    // Result of assignment
    stack.push_back (reinterpret_cast<long>((reinterpret_cast<__main__block__70____Point**>(__pointer))[__offset]));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    //---------------------------------------------------------------------
}
// End Method Declaration - __method____main__block__70____Vec__Point____push_back__Point
//-------------------------------------------------------------------------

//-------------------------------------------------------------------------
// Constructor Declaration - Point::Point(int, int) -> Point
__main__block__70____Point::__main__block__70____Point (long __main__block__70____Point__Point__x, long __main__block__70____Point__Point__y)
{
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
    // Add dispatch table to instance
    dtable = __dtable____main__block__70____Point;
    __main__block__70____Point* __this = this;
    // Body
    //---------------------------------------------------------------------
    // Code Block
    // Statement
    // Assignment - '='
    // RHS
    stack.push_back (*reinterpret_cast<long*>(&__main__block__70____Point__Point__x));
    // LHS
    // Member Accessor Assignment
    // LHS
    stack.push_back (reinterpret_cast<long>(__this));
    // RHS
    __parent = stack.back ();
    stack.pop_back ();
    __rhs = stack.back ();
    stack.pop_back ();
    (reinterpret_cast<__main__block__70____Point*>(__parent))->__field____main__block__70____Point____x = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&(reinterpret_cast<__main__block__70____Point*>(__parent))->__field____main__block__70____Point____x));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Assignment - '='
    // RHS
    stack.push_back (*reinterpret_cast<long*>(&__main__block__70____Point__Point__y));
    // LHS
    // Member Accessor Assignment
    // LHS
    stack.push_back (reinterpret_cast<long>(__this));
    // RHS
    __parent = stack.back ();
    stack.pop_back ();
    __rhs = stack.back ();
    stack.pop_back ();
    (reinterpret_cast<__main__block__70____Point*>(__parent))->__field____main__block__70____Point____y = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&(reinterpret_cast<__main__block__70____Point*>(__parent))->__field____main__block__70____Point____y));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    //---------------------------------------------------------------------
}
// End Constructor Declaration - __ctor____main__block__70____Point____Point__int__int
//-------------------------------------------------------------------------

//-------------------------------------------------------------------------
// Constructor Declaration - A<:B:>::A() -> A<:B:>
__main__block__87____A__B::__main__block__87____A__B ()
{
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
    // Add dispatch table to instance
    dtable = __dtable____main__block__87____A__B;
    __main__block__87____A__B* __this = this;
    // Body
    //---------------------------------------------------------------------
    // Code Block
    // Statement
    // Assignment - '='
    // RHS
    // Function Call - B::B() -> B
    {
        // Arguments
        // B::B
        __main__block__87____B* __res = new __main__block__87____B ();
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // LHS
    // Member Accessor Assignment
    // LHS
    stack.push_back (reinterpret_cast<long>(__this));
    // RHS
    __parent = stack.back ();
    stack.pop_back ();
    __rhs = stack.back ();
    stack.pop_back ();
    (reinterpret_cast<__main__block__87____A__B*>(__parent))->__field____main__block__87____A__B____x = reinterpret_cast<__main__block__87____B*>(__rhs);
    // Result of assignment
    stack.push_back (reinterpret_cast<long>((reinterpret_cast<__main__block__87____A__B*>(__parent))->__field____main__block__87____A__B____x));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    //---------------------------------------------------------------------
}
// End Constructor Declaration - __ctor____main__block__87____A__B____A
//-------------------------------------------------------------------------

//-------------------------------------------------------------------------
// Constructor Declaration - B::B() -> B
__main__block__87____B::__main__block__87____B ()
{
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
    // Add dispatch table to instance
    dtable = __dtable____main__block__87____B;
    __main__block__87____B* __this = this;
    // Body
    //---------------------------------------------------------------------
    // Code Block
    // Statement
    // Assignment - '='
    // RHS
    // Int Literal
    stack.push_back (23);
    // LHS
    // Member Accessor Assignment
    // LHS
    stack.push_back (reinterpret_cast<long>(__this));
    // RHS
    __parent = stack.back ();
    stack.pop_back ();
    __rhs = stack.back ();
    stack.pop_back ();
    (reinterpret_cast<__main__block__87____B*>(__parent))->__field____main__block__87____B____w = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&(reinterpret_cast<__main__block__87____B*>(__parent))->__field____main__block__87____B____w));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    //---------------------------------------------------------------------
}
// End Constructor Declaration - __ctor____main__block__87____B____B
//-------------------------------------------------------------------------

//=========================================================================
// Function Declaration - print(B) -> void
void __main__block__87____print__B (__main__block__87____B* __main__block__87__print__b)
{
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
    // Body
    //---------------------------------------------------------------------
    // Code Block
    //---------------------------------------------------------------------
    // If-Statement
    // Precomputing all if/elif conditions and give unique names
    // bc we can't have code between if and elif
    // Condition
    // Equal
    {
        // LHS
        stack.push_back (reinterpret_cast<long>(__main__block__87__print__b));
        // RHS
        // Null Literal
        stack.push_back ((long)nullptr);
        __rhs = stack.back ();
        stack.pop_back ();
        __lhs = stack.back ();
        stack.pop_back ();
        long __res = reinterpret_cast<__main__block__87____B*>(__lhs) == nullptr;
        stack.push_back (*reinterpret_cast<long*>(&__res));
    }
    long __if__91__cond = stack.back ();
    stack.pop_back ();
    // get condition from stack
    if (__if__91__cond)
    {
        // Body
        // Statement
        // Function Call - println(char[]) -> void
        {
            // Arguments
            // String Literal
            {
                char str_literal[] = "null";
                // convert to a heap string
                char* str = new char[5];
                // copy string to heap allocation
                std::memcpy (str, &str_literal, 5);
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
        // Function Call - println(int) -> void
        {
            // Arguments
            // Member Accessor obj.w
            {
                // LHS
                stack.push_back (reinterpret_cast<long>(__main__block__87__print__b));
                // RHS
                __parent = stack.back ();
                stack.pop_back ();
                long __res = (reinterpret_cast<__main__block__87____B*>(__parent))->__field____main__block__87____B____w;
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

    }
    //---------------------------------------------------------------------
    // End of if
    //---------------------------------------------------------------------
    //---------------------------------------------------------------------
};
// End Function Declaration - __main__block__87____print__B
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
        // push dummy value - funcall returns void
        stack.push_back (0);
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
        // push dummy value - funcall returns void
        stack.push_back (0);
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
        // push dummy value - funcall returns void
        stack.push_back (0);
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    //---------------------------------------------------------------------
    // Code Block
    // Statement
    // Function Call - println(char[]) -> void
    {
        // Arguments
        // String Literal
        {
            char str_literal[] = "=== function";
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

    // Function Declaration - sum(int, int) -> int
    // *see this func def before this parent function

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
            long __res = __main__block__0____sum__int__int (__arg0, __arg1);
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

    // Function Declaration - sum(float, float) -> float
    // *see this func def before this parent function

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
            double __res = __main__block__0____sum__float__float (__arg0, __arg1);
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        double __arg0 = *reinterpret_cast<double*>(&__stackval);
        // println
        __builtin__println__float (__arg0);
        // push dummy value - funcall returns void
        stack.push_back (0);
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Function Declaration - sum(int, int, int) -> int
    // *see this func def before this parent function

    // Statement
    // Function Call - println(int) -> void
    {
        // Arguments
        // Function Call - sum(int, int, int) -> int
        {
            // Arguments
            // Int Literal
            stack.push_back (34);
            // Int Literal
            stack.push_back (26);
            // Int Literal
            stack.push_back (40);
            
            __stackval = stack.back ();
            stack.pop_back ();
            // Reinterpret from general register
            long __arg2 = *reinterpret_cast<long*>(&__stackval);
            
            __stackval = stack.back ();
            stack.pop_back ();
            // Reinterpret from general register
            long __arg1 = *reinterpret_cast<long*>(&__stackval);
            
            __stackval = stack.back ();
            stack.pop_back ();
            // Reinterpret from general register
            long __arg0 = *reinterpret_cast<long*>(&__stackval);
            // sum
            long __res = __main__block__0____sum__int__int__int (__arg0, __arg1, __arg2);
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

    // Function Declaration - print(int, char, float) -> void
    // *see this func def before this parent function

    // Statement
    // Function Call - print(int, char, float) -> void
    {
        // Arguments
        // Int Literal
        stack.push_back (24);
        // Char Literal
        stack.push_back (static_cast<long>(static_cast<unsigned char>('A')));
        // Float Literal
        {
            double float_literal = 0.25;
            stack.push_back (*reinterpret_cast<long*>(&float_literal));
        }
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        double __arg2 = *reinterpret_cast<double*>(&__stackval);
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        char __arg1 = static_cast<char>(static_cast<unsigned char>(__stackval));
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        long __arg0 = *reinterpret_cast<long*>(&__stackval);
        // print
        __main__block__0____print__int__char__float (__arg0, __arg1, __arg2);
        // push dummy value - funcall returns void
        stack.push_back (0);
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
    char* __main__block__6__str;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__6__str = *reinterpret_cast<char**>(&__rhs);
    // Result of assignment
    stack.push_back (reinterpret_cast<long>(__main__block__6__str));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(char[]) -> void
    {
        // Arguments
        stack.push_back (reinterpret_cast<long>(__main__block__6__str));
        
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
    stack.push_back (reinterpret_cast<long>(__main__block__6__str));
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
        stack.push_back (reinterpret_cast<long>(__main__block__6__str));
        
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
        // push dummy value - funcall returns void
        stack.push_back (0);
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
    char* __main__block__7__name;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__7__name = *reinterpret_cast<char**>(&__rhs);
    // Result of assignment
    stack.push_back (reinterpret_cast<long>(__main__block__7__name));
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
        stack.push_back (reinterpret_cast<long>(__main__block__7__name));
        
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
        // push dummy value - funcall returns void
        stack.push_back (0);
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
    double __main__block__8__x;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__8__x = *reinterpret_cast<double*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__8__x));
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
        stack.push_back (*reinterpret_cast<long*>(&__main__block__8__x));
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
    long __if__9__cond = stack.back ();
    stack.pop_back ();
    // Condition for elif #0
    // Greater Than
    {
        // LHS
        stack.push_back (*reinterpret_cast<long*>(&__main__block__8__x));
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
    long __elif__9x0__cond = stack.back ();
    stack.pop_back ();
    // get condition from stack
    if (__if__9__cond)
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
            // push dummy value - funcall returns void
            stack.push_back (0);
        }
        // Statement results can be ignored
        stack.pop_back ();
        // End Statement

        //-----------------------------------------------------------------
    }
    //---------------------------------------------------------------------
    // Elif-Statement
    // Condition
    else if (__elif__9x0__cond)
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
            // push dummy value - funcall returns void
            stack.push_back (0);
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
            // push dummy value - funcall returns void
            stack.push_back (0);
        }
        // Statement results can be ignored
        stack.pop_back ();
        // End Statement

        //-----------------------------------------------------------------
    }
    //---------------------------------------------------------------------
    // End of if
    //---------------------------------------------------------------------
    // Function Declaration - max(int, int) -> int
    // *see this func def before this parent function

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
            long __res = __main__block__8____max__int__int (__arg0, __arg1);
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
            long __res = __main__block__8____max__int__int (__arg0, __arg1);
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
            long __res = __main__block__8____max__int__int (__arg0, __arg1);
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
            long __res = __main__block__8____max__int__int (__arg0, __arg1);
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
    long __main__block__15__for__16__i;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__15__for__16__i = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__15__for__16__i));
    // We can ignore the init result
    stack.pop_back ();
    // Using an infinite loop so we can write a separate multi-line condition
    while (1)
    {
        // Condition
        // Less Than
        {
            // LHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__15__for__16__i));
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
            stack.push_back (*reinterpret_cast<long*>(&__main__block__15__for__16__i));
            
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

        //-----------------------------------------------------------------
        // Update
        // Pre-Increment
        {
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__15__for__16__i));
            __rhs = stack.back ();
            stack.pop_back ();
            __main__block__15__for__16__i = __main__block__15__for__16__i + 1;
            __res = __main__block__15__for__16__i;
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        // We can ignore the update result
        stack.pop_back ();
    }
    //---------------------------------------------------------------------
    // Statement
    // Function Call - println() -> void
    {
        // Arguments
        // println
        __builtin__println ();
        // push dummy value - funcall returns void
        stack.push_back (0);
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
    stack.push_back (0);
    // LHS
    // Variable declaration
    long __main__block__18__i;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__18__i = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__18__i));
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
            stack.push_back (*reinterpret_cast<long*>(&__main__block__18__i));
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
            stack.push_back (*reinterpret_cast<long*>(&__main__block__18__i));
            
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
        // Pre-Increment
        {
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__18__i));
            __rhs = stack.back ();
            stack.pop_back ();
            __main__block__18__i = __main__block__18__i + 1;
            __res = __main__block__18__i;
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
        // push dummy value - funcall returns void
        stack.push_back (0);
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
    stack.push_back (10);
    // LHS
    // Variable declaration
    long __main__block__21__size;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__21__size = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__21__size));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Assignment - '='
    // RHS
    // Array Allocator
    {
        stack.push_back (*reinterpret_cast<long*>(&__main__block__21__size));
        __stackval = stack.back ();
        stack.pop_back ();
        long* __res = new long[__stackval];
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // LHS
    // Variable declaration
    long* __main__block__21__arr;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__21__arr = *reinterpret_cast<long**>(&__rhs);
    // Result of assignment
    stack.push_back (reinterpret_cast<long>(__main__block__21__arr));
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
    long __main__block__21__for__22__i;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__21__for__22__i = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__21__for__22__i));
    // We can ignore the init result
    stack.pop_back ();
    // Using an infinite loop so we can write a separate multi-line condition
    while (1)
    {
        // Condition
        // Less Than
        {
            // LHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__21__for__22__i));
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__21__size));
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
            stack.push_back (*reinterpret_cast<long*>(&__main__block__21__for__22__i));
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__21__for__22__i));
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
        stack.push_back (reinterpret_cast<long>(__main__block__21__arr));
        // OFFSET
        stack.push_back (*reinterpret_cast<long*>(&__main__block__21__for__22__i));
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
            stack.push_back (*reinterpret_cast<long*>(&__main__block__21__for__22__i));
            __rhs = stack.back ();
            stack.pop_back ();
            __main__block__21__for__22__i = __main__block__21__for__22__i + 1;
            __res = __main__block__21__for__22__i;
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        // We can ignore the update result
        stack.pop_back ();
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
    long __main__block__21__for__24__i;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__21__for__24__i = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__21__for__24__i));
    // We can ignore the init result
    stack.pop_back ();
    // Using an infinite loop so we can write a separate multi-line condition
    while (1)
    {
        // Condition
        // Less Than
        {
            // LHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__21__for__24__i));
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__21__size));
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
            // Subscript Expression
            {
                // LHS
                stack.push_back (reinterpret_cast<long>(__main__block__21__arr));
                // OFFSET
                stack.push_back (*reinterpret_cast<long*>(&__main__block__21__for__24__i));
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
            // print
            __builtin__print__int (__arg0);
            // push dummy value - funcall returns void
            stack.push_back (0);
        }
        // Statement results can be ignored
        stack.pop_back ();
        // End Statement

        //-----------------------------------------------------------------
        // Update
        // Pre-Increment
        {
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__21__for__24__i));
            __rhs = stack.back ();
            stack.pop_back ();
            __main__block__21__for__24__i = __main__block__21__for__24__i + 1;
            __res = __main__block__21__for__24__i;
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        // We can ignore the update result
        stack.pop_back ();
    }
    //---------------------------------------------------------------------
    // Statement
    // Function Call - println() -> void
    {
        // Arguments
        // println
        __builtin__println ();
        // push dummy value - funcall returns void
        stack.push_back (0);
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
    double* __main__block__26__arr;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__26__arr = *reinterpret_cast<double**>(&__rhs);
    // Result of assignment
    stack.push_back (reinterpret_cast<long>(__main__block__26__arr));
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
    long __main__block__26__for__27__i;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__26__for__27__i = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__26__for__27__i));
    // We can ignore the init result
    stack.pop_back ();
    // Using an infinite loop so we can write a separate multi-line condition
    while (1)
    {
        // Condition
        // Less Than
        {
            // LHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__26__for__27__i));
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
            // push dummy value - funcall returns void
            stack.push_back (0);
        }
        // Statement results can be ignored
        stack.pop_back ();
        // End Statement

        // Statement
        // Function Call - print(float) -> void
        {
            // Arguments
            // Subscript Expression
            {
                // LHS
                stack.push_back (reinterpret_cast<long>(__main__block__26__arr));
                // OFFSET
                stack.push_back (*reinterpret_cast<long*>(&__main__block__26__for__27__i));
                __offset = stack.back ();
                stack.pop_back ();
                __pointer = stack.back ();
                stack.pop_back ();
                double __res = (*reinterpret_cast<double**>(&__pointer))[*reinterpret_cast<long*>(&__offset)];
                stack.push_back (*reinterpret_cast<long*>(&__res));
            }
            
            __stackval = stack.back ();
            stack.pop_back ();
            // Reinterpret from general register
            double __arg0 = *reinterpret_cast<double*>(&__stackval);
            // print
            __builtin__print__float (__arg0);
            // push dummy value - funcall returns void
            stack.push_back (0);
        }
        // Statement results can be ignored
        stack.pop_back ();
        // End Statement

        //-----------------------------------------------------------------
        // Update
        // Pre-Increment
        {
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__26__for__27__i));
            __rhs = stack.back ();
            stack.pop_back ();
            __main__block__26__for__27__i = __main__block__26__for__27__i + 1;
            __res = __main__block__26__for__27__i;
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        // We can ignore the update result
        stack.pop_back ();
    }
    //---------------------------------------------------------------------
    // Statement
    // Function Call - println() -> void
    {
        // Arguments
        // println
        __builtin__println ();
        // push dummy value - funcall returns void
        stack.push_back (0);
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
    char* __main__block__29__line;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__29__line = *reinterpret_cast<char**>(&__rhs);
    // Result of assignment
    stack.push_back (reinterpret_cast<long>(__main__block__29__line));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(char[]) -> void
    {
        // Arguments
        stack.push_back (reinterpret_cast<long>(__main__block__29__line));
        
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
    // Char Literal
    stack.push_back (static_cast<long>(static_cast<unsigned char>('m')));
    // LHS
    // Subscript assignment
    // LHS
    stack.push_back (reinterpret_cast<long>(__main__block__29__line));
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
        stack.push_back (reinterpret_cast<long>(__main__block__29__line));
        
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
    // Char Literal
    stack.push_back (static_cast<long>(static_cast<unsigned char>('y')));
    // LHS
    // Subscript assignment
    // LHS
    stack.push_back (reinterpret_cast<long>(__main__block__29__line));
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
        stack.push_back (reinterpret_cast<long>(__main__block__29__line));
        
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
    stack.push_back (5);
    // LHS
    // Variable declaration
    long __main__block__30__rows;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__30__rows = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__30__rows));
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
    long __main__block__30__cols;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__30__cols = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__30__cols));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Assignment - '='
    // RHS
    // Array Allocator
    {
        stack.push_back (*reinterpret_cast<long*>(&__main__block__30__rows));
        __stackval = stack.back ();
        stack.pop_back ();
        char** __res = new char*[__stackval];
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // LHS
    // Variable declaration
    char** __main__block__30__board;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__30__board = *reinterpret_cast<char***>(&__rhs);
    // Result of assignment
    stack.push_back (reinterpret_cast<long>(__main__block__30__board));
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
    long __main__block__30__for__31__i;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__30__for__31__i = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__30__for__31__i));
    // We can ignore the init result
    stack.pop_back ();
    // Using an infinite loop so we can write a separate multi-line condition
    while (1)
    {
        // Condition
        // Less Than
        {
            // LHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__30__for__31__i));
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__30__rows));
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
            stack.push_back (*reinterpret_cast<long*>(&__main__block__30__cols));
            __stackval = stack.back ();
            stack.pop_back ();
            char* __res = new char[__stackval];
            stack.push_back (reinterpret_cast<long>(__res));
        }
        // LHS
        // Subscript assignment
        // LHS
        stack.push_back (reinterpret_cast<long>(__main__block__30__board));
        // OFFSET
        stack.push_back (*reinterpret_cast<long*>(&__main__block__30__for__31__i));
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
        long __main__block__30__for__31__block__32__for__33__j;
        __rhs = stack.back ();
        stack.pop_back ();
        __main__block__30__for__31__block__32__for__33__j = *reinterpret_cast<long*>(&__rhs);
        // Result of assignment
        stack.push_back (*reinterpret_cast<long*>(&__main__block__30__for__31__block__32__for__33__j));
        // We can ignore the init result
        stack.pop_back ();
        // Using an infinite loop so we can write a separate multi-line condition
        while (1)
        {
            // Condition
            // Less Than
            {
                // LHS
                stack.push_back (*reinterpret_cast<long*>(&__main__block__30__for__31__block__32__for__33__j));
                // RHS
                stack.push_back (*reinterpret_cast<long*>(&__main__block__30__cols));
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
            // Subscript Expression
            {
                // LHS
                stack.push_back (reinterpret_cast<long>(__main__block__30__board));
                // OFFSET
                stack.push_back (*reinterpret_cast<long*>(&__main__block__30__for__31__i));
                __offset = stack.back ();
                stack.pop_back ();
                __pointer = stack.back ();
                stack.pop_back ();
                char* __res = (*reinterpret_cast<char***>(&__pointer))[*reinterpret_cast<long*>(&__offset)];
                stack.push_back (reinterpret_cast<long>(__res));
            }
            // OFFSET
            stack.push_back (*reinterpret_cast<long*>(&__main__block__30__for__31__block__32__for__33__j));
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
                stack.push_back (*reinterpret_cast<long*>(&__main__block__30__for__31__block__32__for__33__j));
                __rhs = stack.back ();
                stack.pop_back ();
                __main__block__30__for__31__block__32__for__33__j = __main__block__30__for__31__block__32__for__33__j + 1;
                __res = __main__block__30__for__31__block__32__for__33__j;
                stack.push_back (*reinterpret_cast<long*>(&__res));
            }
            // We can ignore the update result
            stack.pop_back ();
        }
        //-----------------------------------------------------------------
        //-----------------------------------------------------------------
        // Update
        // Pre-Increment
        {
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__30__for__31__i));
            __rhs = stack.back ();
            stack.pop_back ();
            __main__block__30__for__31__i = __main__block__30__for__31__i + 1;
            __res = __main__block__30__for__31__i;
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        // We can ignore the update result
        stack.pop_back ();
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
    long __main__block__30__for__35__i;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__30__for__35__i = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__30__for__35__i));
    // We can ignore the init result
    stack.pop_back ();
    // Using an infinite loop so we can write a separate multi-line condition
    while (1)
    {
        // Condition
        // Less Than
        {
            // LHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__30__for__35__i));
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__30__rows));
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
        long __main__block__30__for__35__block__36__for__37__j;
        __rhs = stack.back ();
        stack.pop_back ();
        __main__block__30__for__35__block__36__for__37__j = *reinterpret_cast<long*>(&__rhs);
        // Result of assignment
        stack.push_back (*reinterpret_cast<long*>(&__main__block__30__for__35__block__36__for__37__j));
        // We can ignore the init result
        stack.pop_back ();
        // Using an infinite loop so we can write a separate multi-line condition
        while (1)
        {
            // Condition
            // Less Than
            {
                // LHS
                stack.push_back (*reinterpret_cast<long*>(&__main__block__30__for__35__block__36__for__37__j));
                // RHS
                stack.push_back (*reinterpret_cast<long*>(&__main__block__30__cols));
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
                // Subscript Expression
                {
                    // LHS
                    // Subscript Expression
                    {
                        // LHS
                        stack.push_back (reinterpret_cast<long>(__main__block__30__board));
                        // OFFSET
                        stack.push_back (*reinterpret_cast<long*>(&__main__block__30__for__35__i));
                        __offset = stack.back ();
                        stack.pop_back ();
                        __pointer = stack.back ();
                        stack.pop_back ();
                        char* __res = (*reinterpret_cast<char***>(&__pointer))[*reinterpret_cast<long*>(&__offset)];
                        stack.push_back (reinterpret_cast<long>(__res));
                    }
                    // OFFSET
                    stack.push_back (*reinterpret_cast<long*>(&__main__block__30__for__35__block__36__for__37__j));
                    __offset = stack.back ();
                    stack.pop_back ();
                    __pointer = stack.back ();
                    stack.pop_back ();
                    char __res = (*reinterpret_cast<char**>(&__pointer))[*reinterpret_cast<long*>(&__offset)];
                    stack.push_back (static_cast<long>(static_cast<unsigned char>(__res)));
                }
                
                __stackval = stack.back ();
                stack.pop_back ();
                // Reinterpret from general register
                char __arg0 = static_cast<char>(static_cast<unsigned char>(__stackval));
                // print
                __builtin__print__char (__arg0);
                // push dummy value - funcall returns void
                stack.push_back (0);
            }
            // Statement results can be ignored
            stack.pop_back ();
            // End Statement

            //-------------------------------------------------------------
            // Update
            // Pre-Increment
            {
                // RHS
                stack.push_back (*reinterpret_cast<long*>(&__main__block__30__for__35__block__36__for__37__j));
                __rhs = stack.back ();
                stack.pop_back ();
                __main__block__30__for__35__block__36__for__37__j = __main__block__30__for__35__block__36__for__37__j + 1;
                __res = __main__block__30__for__35__block__36__for__37__j;
                stack.push_back (*reinterpret_cast<long*>(&__res));
            }
            // We can ignore the update result
            stack.pop_back ();
        }
        //-----------------------------------------------------------------
        // Statement
        // Function Call - println() -> void
        {
            // Arguments
            // println
            __builtin__println ();
            // push dummy value - funcall returns void
            stack.push_back (0);
        }
        // Statement results can be ignored
        stack.pop_back ();
        // End Statement

        //-----------------------------------------------------------------
        // Update
        // Pre-Increment
        {
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__30__for__35__i));
            __rhs = stack.back ();
            stack.pop_back ();
            __main__block__30__for__35__i = __main__block__30__for__35__i + 1;
            __res = __main__block__30__for__35__i;
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        // We can ignore the update result
        stack.pop_back ();
    }
    //---------------------------------------------------------------------
    // Statement
    // Function Call - println() -> void
    {
        // Arguments
        // println
        __builtin__println ();
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
    long __main__block__30__for__39__i;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__30__for__39__i = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__30__for__39__i));
    // We can ignore the init result
    stack.pop_back ();
    // Using an infinite loop so we can write a separate multi-line condition
    while (1)
    {
        // Condition
        // Less Than
        {
            // LHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__30__for__39__i));
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__30__rows));
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
        long __main__block__30__for__39__block__40__for__41__j;
        __rhs = stack.back ();
        stack.pop_back ();
        __main__block__30__for__39__block__40__for__41__j = *reinterpret_cast<long*>(&__rhs);
        // Result of assignment
        stack.push_back (*reinterpret_cast<long*>(&__main__block__30__for__39__block__40__for__41__j));
        // We can ignore the init result
        stack.pop_back ();
        // Using an infinite loop so we can write a separate multi-line condition
        while (1)
        {
            // Condition
            // Less Than
            {
                // LHS
                stack.push_back (*reinterpret_cast<long*>(&__main__block__30__for__39__block__40__for__41__j));
                // RHS
                stack.push_back (*reinterpret_cast<long*>(&__main__block__30__cols));
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
                        stack.push_back (*reinterpret_cast<long*>(&__main__block__30__for__39__i));
                        // RHS
                        stack.push_back (*reinterpret_cast<long*>(&__main__block__30__for__39__block__40__for__41__j));
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
            long __if__43__cond = stack.back ();
            stack.pop_back ();
            // get condition from stack
            if (__if__43__cond)
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
                // Subscript Expression
                {
                    // LHS
                    stack.push_back (reinterpret_cast<long>(__main__block__30__board));
                    // OFFSET
                    stack.push_back (*reinterpret_cast<long*>(&__main__block__30__for__39__i));
                    __offset = stack.back ();
                    stack.pop_back ();
                    __pointer = stack.back ();
                    stack.pop_back ();
                    char* __res = (*reinterpret_cast<char***>(&__pointer))[*reinterpret_cast<long*>(&__offset)];
                    stack.push_back (reinterpret_cast<long>(__res));
                }
                // OFFSET
                stack.push_back (*reinterpret_cast<long*>(&__main__block__30__for__39__block__40__for__41__j));
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
                stack.push_back (*reinterpret_cast<long*>(&__main__block__30__for__39__block__40__for__41__j));
                __rhs = stack.back ();
                stack.pop_back ();
                __main__block__30__for__39__block__40__for__41__j = __main__block__30__for__39__block__40__for__41__j + 1;
                __res = __main__block__30__for__39__block__40__for__41__j;
                stack.push_back (*reinterpret_cast<long*>(&__res));
            }
            // We can ignore the update result
            stack.pop_back ();
        }
        //-----------------------------------------------------------------
        //-----------------------------------------------------------------
        // Update
        // Pre-Increment
        {
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__30__for__39__i));
            __rhs = stack.back ();
            stack.pop_back ();
            __main__block__30__for__39__i = __main__block__30__for__39__i + 1;
            __res = __main__block__30__for__39__i;
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        // We can ignore the update result
        stack.pop_back ();
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
    long __main__block__30__for__44__i;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__30__for__44__i = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__30__for__44__i));
    // We can ignore the init result
    stack.pop_back ();
    // Using an infinite loop so we can write a separate multi-line condition
    while (1)
    {
        // Condition
        // Less Than
        {
            // LHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__30__for__44__i));
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__30__rows));
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
        long __main__block__30__for__44__block__45__for__46__j;
        __rhs = stack.back ();
        stack.pop_back ();
        __main__block__30__for__44__block__45__for__46__j = *reinterpret_cast<long*>(&__rhs);
        // Result of assignment
        stack.push_back (*reinterpret_cast<long*>(&__main__block__30__for__44__block__45__for__46__j));
        // We can ignore the init result
        stack.pop_back ();
        // Using an infinite loop so we can write a separate multi-line condition
        while (1)
        {
            // Condition
            // Less Than
            {
                // LHS
                stack.push_back (*reinterpret_cast<long*>(&__main__block__30__for__44__block__45__for__46__j));
                // RHS
                stack.push_back (*reinterpret_cast<long*>(&__main__block__30__cols));
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
                // Subscript Expression
                {
                    // LHS
                    // Subscript Expression
                    {
                        // LHS
                        stack.push_back (reinterpret_cast<long>(__main__block__30__board));
                        // OFFSET
                        stack.push_back (*reinterpret_cast<long*>(&__main__block__30__for__44__i));
                        __offset = stack.back ();
                        stack.pop_back ();
                        __pointer = stack.back ();
                        stack.pop_back ();
                        char* __res = (*reinterpret_cast<char***>(&__pointer))[*reinterpret_cast<long*>(&__offset)];
                        stack.push_back (reinterpret_cast<long>(__res));
                    }
                    // OFFSET
                    stack.push_back (*reinterpret_cast<long*>(&__main__block__30__for__44__block__45__for__46__j));
                    __offset = stack.back ();
                    stack.pop_back ();
                    __pointer = stack.back ();
                    stack.pop_back ();
                    char __res = (*reinterpret_cast<char**>(&__pointer))[*reinterpret_cast<long*>(&__offset)];
                    stack.push_back (static_cast<long>(static_cast<unsigned char>(__res)));
                }
                
                __stackval = stack.back ();
                stack.pop_back ();
                // Reinterpret from general register
                char __arg0 = static_cast<char>(static_cast<unsigned char>(__stackval));
                // print
                __builtin__print__char (__arg0);
                // push dummy value - funcall returns void
                stack.push_back (0);
            }
            // Statement results can be ignored
            stack.pop_back ();
            // End Statement

            //-------------------------------------------------------------
            // Update
            // Pre-Increment
            {
                // RHS
                stack.push_back (*reinterpret_cast<long*>(&__main__block__30__for__44__block__45__for__46__j));
                __rhs = stack.back ();
                stack.pop_back ();
                __main__block__30__for__44__block__45__for__46__j = __main__block__30__for__44__block__45__for__46__j + 1;
                __res = __main__block__30__for__44__block__45__for__46__j;
                stack.push_back (*reinterpret_cast<long*>(&__res));
            }
            // We can ignore the update result
            stack.pop_back ();
        }
        //-----------------------------------------------------------------
        // Statement
        // Function Call - println() -> void
        {
            // Arguments
            // println
            __builtin__println ();
            // push dummy value - funcall returns void
            stack.push_back (0);
        }
        // Statement results can be ignored
        stack.pop_back ();
        // End Statement

        //-----------------------------------------------------------------
        // Update
        // Pre-Increment
        {
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__30__for__44__i));
            __rhs = stack.back ();
            stack.pop_back ();
            __main__block__30__for__44__i = __main__block__30__for__44__i + 1;
            __res = __main__block__30__for__44__i;
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        // We can ignore the update result
        stack.pop_back ();
    }
    //---------------------------------------------------------------------
    //---------------------------------------------------------------------
    //---------------------------------------------------------------------
    // Code Block
    // Statement
    // Function Call - println(char[]) -> void
    {
        // Arguments
        // String Literal
        {
            char str_literal[] = "=== function template";
            // convert to a heap string
            char* str = new char[22];
            // copy string to heap allocation
            std::memcpy (str, &str_literal, 22);
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

    //=====================================================================
    // Function Template - 
    // Function Declaration - add<:int:>(int, int) -> int
    // *see this func def before this parent function

    // Function Declaration - add<:float:>(float, float) -> float
    // *see this func def before this parent function

    // End Function Template - 
    //=====================================================================

    // Statement
    // Function Call - println(int) -> void
    {
        // Arguments
        // Function Call - add<:int:>(int, int) -> int
        {
            // Arguments
            // Int Literal
            stack.push_back (6);
            // Int Literal
            stack.push_back (3);
            
            __stackval = stack.back ();
            stack.pop_back ();
            // Reinterpret from general register
            long __arg1 = *reinterpret_cast<long*>(&__stackval);
            
            __stackval = stack.back ();
            stack.pop_back ();
            // Reinterpret from general register
            long __arg0 = *reinterpret_cast<long*>(&__stackval);
            // add
            long __res = __main__block__48____add__int____int__int (__arg0, __arg1);
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
    // Function Call - println(float) -> void
    {
        // Arguments
        // Function Call - add<:float:>(float, float) -> float
        {
            // Arguments
            // Float Literal
            {
                double float_literal = 0.12;
                stack.push_back (*reinterpret_cast<long*>(&float_literal));
            }
            // Float Literal
            {
                double float_literal = 12.22;
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
            // add
            double __res = __main__block__48____add__float____float__float (__arg0, __arg1);
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        double __arg0 = *reinterpret_cast<double*>(&__stackval);
        // println
        __builtin__println__float (__arg0);
        // push dummy value - funcall returns void
        stack.push_back (0);
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    //=====================================================================
    // Function Template - 
    // Function Declaration - default_value<:int:>() -> int
    // *see this func def before this parent function

    // Function Declaration - default_value<:float:>() -> float
    // *see this func def before this parent function

    // Function Declaration - default_value<:char:>() -> char
    // *see this func def before this parent function

    // End Function Template - 
    //=====================================================================

    // Statement
    // Function Call - println(int) -> void
    {
        // Arguments
        // Equal
        {
            // LHS
            // Function Call - default_value<:int:>() -> int
            {
                // Arguments
                // default_value
                long __res = __main__block__48____default_value__int__ ();
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
    // Function Call - println(int) -> void
    {
        // Arguments
        // Equal
        {
            // LHS
            // Function Call - default_value<:float:>() -> float
            {
                // Arguments
                // default_value
                double __res = __main__block__48____default_value__float__ ();
                stack.push_back (*reinterpret_cast<long*>(&__res));
            }
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
    // Function Call - println(int) -> void
    {
        // Arguments
        // Equal
        {
            // LHS
            // Function Call - default_value<:char:>() -> char
            {
                // Arguments
                // default_value
                char __res = __main__block__48____default_value__char__ ();
                stack.push_back (static_cast<long>(static_cast<unsigned char>(__res)));
            }
            // RHS
            // Char Literal
            stack.push_back (static_cast<long>(static_cast<unsigned char>('\0')));
            __rhs = stack.back ();
            stack.pop_back ();
            __lhs = stack.back ();
            stack.pop_back ();
            long __res = static_cast<char>(static_cast<unsigned char>(__lhs)) == static_cast<char>(static_cast<unsigned char>(__rhs));
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

    //---------------------------------------------------------------------
    //---------------------------------------------------------------------
    // Code Block
    // Statement
    // Function Call - println(char[]) -> void
    {
        // Arguments
        // String Literal
        {
            char str_literal[] = "=== classes";
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
        // println
        __builtin__println__char__1 (__arg0);
        // push dummy value - funcall returns void
        stack.push_back (0);
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Class Declaration - __main__block__54____A inherits __builtin____main__Object
    // *see this class def before this parent function

    // Populate Dispatch Table
    __dtable____main__block__54____A[0] = (void*)__method____main__block__54____A____print;
    __dtable____main__block__54____A[1] = (void*)__method____main__block__54____A____add__int;
    // Class Declaration - __main__block__54____B inherits __main__block__54____A
    // *see this class def before this parent function

    // Populate Dispatch Table
    __dtable____main__block__54____B[0] = (void*)__method____main__block__54____B____print;
    __dtable____main__block__54____B[1] = (void*)__method____main__block__54____A____add__int;
    // Class Declaration - __main__block__54____C inherits __main__block__54____A
    // *see this class def before this parent function

    // Populate Dispatch Table
    __dtable____main__block__54____C[0] = (void*)__method____main__block__54____A____print;
    __dtable____main__block__54____C[1] = (void*)__method____main__block__54____A____add__int;
    // Function Declaration - print(A) -> void
    // *see this func def before this parent function

    // Statement
    // Assignment - '='
    // RHS
    // Constructor Call - A::A() -> A
    {
        // Arguments
        stack.push_back (reinterpret_cast<long>(new __main__block__54____A ()));
    }
    // LHS
    // Variable declaration
    __main__block__54____A* __main__block__54__a;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__54__a = reinterpret_cast<__main__block__54____A*>(__rhs);
    // Result of assignment
    stack.push_back (reinterpret_cast<long>(__main__block__54__a));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Assignment - '='
    // RHS
    // Constructor Call - B::B() -> B
    {
        // Arguments
        stack.push_back (reinterpret_cast<long>(new __main__block__54____B ()));
    }
    // LHS
    // Variable declaration
    __main__block__54____B* __main__block__54__b;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__54__b = reinterpret_cast<__main__block__54____B*>(__rhs);
    // Result of assignment
    stack.push_back (reinterpret_cast<long>(__main__block__54__b));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Assignment - '='
    // RHS
    // Constructor Call - C::C() -> C
    {
        // Arguments
        stack.push_back (reinterpret_cast<long>(new __main__block__54____C ()));
    }
    // LHS
    // Variable declaration
    __main__block__54____C* __main__block__54__c;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__54__c = reinterpret_cast<__main__block__54____C*>(__rhs);
    // Result of assignment
    stack.push_back (reinterpret_cast<long>(__main__block__54__c));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - print(A) -> void
    {
        // Arguments
        stack.push_back (reinterpret_cast<long>(__main__block__54__a));
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        __main__block__54____A* __arg0 = reinterpret_cast<__main__block__54____A*>(__stackval);
        // print
        __main__block__54____print__A (__arg0);
        // push dummy value - funcall returns void
        stack.push_back (0);
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - print(A) -> void
    {
        // Arguments
        stack.push_back (reinterpret_cast<long>(__main__block__54__b));
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        __main__block__54____B* __arg0 = reinterpret_cast<__main__block__54____B*>(__stackval);
        // print
        __main__block__54____print__A (__arg0);
        // push dummy value - funcall returns void
        stack.push_back (0);
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - print(A) -> void
    {
        // Arguments
        stack.push_back (reinterpret_cast<long>(__main__block__54__c));
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        __main__block__54____C* __arg0 = reinterpret_cast<__main__block__54____C*>(__stackval);
        // print
        __main__block__54____print__A (__arg0);
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
        // Virtual Method Call - add(int) -> int
        // LHS
        stack.push_back (reinterpret_cast<long>(__main__block__54__a));
        // RHS
        {
            // Arguments
            // Int Literal
            stack.push_back (5);
            __stackval = stack.back ();
            stack.pop_back ();
            // Reinterpret from general register
            long __arg0 = *reinterpret_cast<long*>(&__stackval);
            __obj = stack.back ();
            stack.pop_back ();
            // Virtual Function Dispatch
            long __res = ((int(*)(__main__block__54____A*, long))(reinterpret_cast<__main__block__54____A*>(__obj)->dtable[1])) (reinterpret_cast<__main__block__54____A*>(__obj), __arg0);
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
    // Function Call - println(int) -> void
    {
        // Arguments
        // Virtual Method Call - add(int) -> int
        // LHS
        stack.push_back (reinterpret_cast<long>(__main__block__54__b));
        // RHS
        {
            // Arguments
            // Int Literal
            stack.push_back (5);
            __stackval = stack.back ();
            stack.pop_back ();
            // Reinterpret from general register
            long __arg0 = *reinterpret_cast<long*>(&__stackval);
            __obj = stack.back ();
            stack.pop_back ();
            // Virtual Function Dispatch
            long __res = ((int(*)(__main__block__54____B*, long))(reinterpret_cast<__main__block__54____B*>(__obj)->dtable[1])) (reinterpret_cast<__main__block__54____B*>(__obj), __arg0);
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
    // Function Call - println(int) -> void
    {
        // Arguments
        // Virtual Method Call - add(int) -> int
        // LHS
        stack.push_back (reinterpret_cast<long>(__main__block__54__c));
        // RHS
        {
            // Arguments
            // Int Literal
            stack.push_back (5);
            __stackval = stack.back ();
            stack.pop_back ();
            // Reinterpret from general register
            long __arg0 = *reinterpret_cast<long*>(&__stackval);
            __obj = stack.back ();
            stack.pop_back ();
            // Virtual Function Dispatch
            long __res = ((int(*)(__main__block__54____C*, long))(reinterpret_cast<__main__block__54____C*>(__obj)->dtable[1])) (reinterpret_cast<__main__block__54____C*>(__obj), __arg0);
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
    // Function Call - print(A) -> void
    {
        // Arguments
        stack.push_back (reinterpret_cast<long>(__main__block__54__a));
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        __main__block__54____A* __arg0 = reinterpret_cast<__main__block__54____A*>(__stackval);
        // print
        __main__block__54____print__A (__arg0);
        // push dummy value - funcall returns void
        stack.push_back (0);
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - print(A) -> void
    {
        // Arguments
        stack.push_back (reinterpret_cast<long>(__main__block__54__b));
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        __main__block__54____B* __arg0 = reinterpret_cast<__main__block__54____B*>(__stackval);
        // print
        __main__block__54____print__A (__arg0);
        // push dummy value - funcall returns void
        stack.push_back (0);
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - print(A) -> void
    {
        // Arguments
        stack.push_back (reinterpret_cast<long>(__main__block__54__c));
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        __main__block__54____C* __arg0 = reinterpret_cast<__main__block__54____C*>(__stackval);
        // print
        __main__block__54____print__A (__arg0);
        // push dummy value - funcall returns void
        stack.push_back (0);
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
            char str_literal[] = "=== conversions";
            // convert to a heap string
            char* str = new char[16];
            // copy string to heap allocation
            std::memcpy (str, &str_literal, 16);
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
    stack.push_back (10);
    // LHS
    // Variable declaration
    long __main__block__62__x;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__62__x = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__62__x));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(int) -> void
    {
        // Arguments
        stack.push_back (*reinterpret_cast<long*>(&__main__block__62__x));
        
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
    // Assignment - '='
    // RHS
    // Addition
    {
        // LHS
        // Function Call - intToFloat(int) -> float
        {
            // Arguments
            stack.push_back (*reinterpret_cast<long*>(&__main__block__62__x));
            
            __stackval = stack.back ();
            stack.pop_back ();
            // Reinterpret from general register
            long __arg0 = *reinterpret_cast<long*>(&__stackval);
            // intToFloat
            double __res = __builtin__intToFloat__int (__arg0);
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        // RHS
        // Float Literal
        {
            double float_literal = 0.25;
            stack.push_back (*reinterpret_cast<long*>(&float_literal));
        }
        __rhs = stack.back ();
        stack.pop_back ();
        __lhs = stack.back ();
        stack.pop_back ();
        double __res = *reinterpret_cast<double*>(&__lhs) + *reinterpret_cast<double*>(&__rhs);
        stack.push_back (*reinterpret_cast<long*>(&__res));
    }
    // LHS
    // Variable declaration
    double __main__block__62__y;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__62__y = *reinterpret_cast<double*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__62__y));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(float) -> void
    {
        // Arguments
        stack.push_back (*reinterpret_cast<long*>(&__main__block__62__y));
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        double __arg0 = *reinterpret_cast<double*>(&__stackval);
        // println
        __builtin__println__float (__arg0);
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
        // Function Call - floatToInt(float) -> int
        {
            // Arguments
            stack.push_back (*reinterpret_cast<long*>(&__main__block__62__y));
            
            __stackval = stack.back ();
            stack.pop_back ();
            // Reinterpret from general register
            double __arg0 = *reinterpret_cast<double*>(&__stackval);
            // floatToInt
            long __res = __builtin__floatToInt__float (__arg0);
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
    // Assignment - '='
    // RHS
    // String Literal
    {
        char str_literal[] = "3.1415e2";
        // convert to a heap string
        char* str = new char[9];
        // copy string to heap allocation
        std::memcpy (str, &str_literal, 9);
        stack.push_back (reinterpret_cast<long> (str));
    }
    // LHS
    // Variable declaration
    char* __main__block__62__str;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__62__str = *reinterpret_cast<char**>(&__rhs);
    // Result of assignment
    stack.push_back (reinterpret_cast<long>(__main__block__62__str));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(float) -> void
    {
        // Arguments
        // Multiplication
        {
            // LHS
            // Function Call - stringToFloat(char[]) -> float
            {
                // Arguments
                stack.push_back (reinterpret_cast<long>(__main__block__62__str));
                
                __stackval = stack.back ();
                stack.pop_back ();
                // Reinterpret from general register
                char* __arg0 = *reinterpret_cast<char**>(&__stackval);
                // stringToFloat
                double __res = __builtin__stringToFloat__char__1 (__arg0);
                stack.push_back (*reinterpret_cast<long*>(&__res));
            }
            // RHS
            // Float Literal
            {
                double float_literal = 2.0;
                stack.push_back (*reinterpret_cast<long*>(&float_literal));
            }
            __rhs = stack.back ();
            stack.pop_back ();
            __lhs = stack.back ();
            stack.pop_back ();
            double __res = *reinterpret_cast<double*>(&__lhs) * *reinterpret_cast<double*>(&__rhs);
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        double __arg0 = *reinterpret_cast<double*>(&__stackval);
        // println
        __builtin__println__float (__arg0);
        // push dummy value - funcall returns void
        stack.push_back (0);
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Assignment - '='
    // RHS
    // String Literal
    {
        char str_literal[] = "12";
        // convert to a heap string
        char* str = new char[3];
        // copy string to heap allocation
        std::memcpy (str, &str_literal, 3);
        stack.push_back (reinterpret_cast<long> (str));
    }
    // LHS
    // Variable declaration
    char* __main__block__62__str2;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__62__str2 = *reinterpret_cast<char**>(&__rhs);
    // Result of assignment
    stack.push_back (reinterpret_cast<long>(__main__block__62__str2));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(int) -> void
    {
        // Arguments
        // Multiplication
        {
            // LHS
            // Function Call - stringToInt(char[]) -> int
            {
                // Arguments
                stack.push_back (reinterpret_cast<long>(__main__block__62__str2));
                
                __stackval = stack.back ();
                stack.pop_back ();
                // Reinterpret from general register
                char* __arg0 = *reinterpret_cast<char**>(&__stackval);
                // stringToInt
                long __res = __builtin__stringToInt__char__1 (__arg0);
                stack.push_back (*reinterpret_cast<long*>(&__res));
            }
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
    // Assignment - '='
    // RHS
    // Char Literal
    stack.push_back (static_cast<long>(static_cast<unsigned char>('7')));
    // LHS
    // Variable declaration
    char __main__block__62__c;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__62__c = static_cast<char>(static_cast<unsigned char>(__rhs));
    // Result of assignment
    stack.push_back (static_cast<long>(static_cast<unsigned char>(__main__block__62__c)));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(int) -> void
    {
        // Arguments
        // Function Call - charToInt(char) -> int
        {
            // Arguments
            stack.push_back (static_cast<long>(static_cast<unsigned char>(__main__block__62__c)));
            
            __stackval = stack.back ();
            stack.pop_back ();
            // Reinterpret from general register
            char __arg0 = static_cast<char>(static_cast<unsigned char>(__stackval));
            // charToInt
            long __res = __builtin__charToInt__char (__arg0);
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

    //---------------------------------------------------------------------
    //---------------------------------------------------------------------
    // Code Block
    // Statement
    // Function Call - println(char[]) -> void
    {
        // Arguments
        // String Literal
        {
            char str_literal[] = "=== more class tests";
            // convert to a heap string
            char* str = new char[21];
            // copy string to heap allocation
            std::memcpy (str, &str_literal, 21);
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

    // Class Declaration - __main__block__63____A inherits __builtin____main__Object
    // *see this class def before this parent function

    // Populate Dispatch Table
    // Statement
    // Assignment - '='
    // RHS
    // Constructor Call - A::A() -> A
    {
        // Arguments
        stack.push_back (reinterpret_cast<long>(new __main__block__63____A ()));
    }
    // LHS
    // Variable declaration
    __main__block__63____A* __main__block__63__a;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__63__a = reinterpret_cast<__main__block__63____A*>(__rhs);
    // Result of assignment
    stack.push_back (reinterpret_cast<long>(__main__block__63__a));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(int) -> void
    {
        // Arguments
        // Member Accessor obj.x
        {
            // LHS
            stack.push_back (reinterpret_cast<long>(__main__block__63__a));
            // RHS
            __parent = stack.back ();
            stack.pop_back ();
            long __res = (reinterpret_cast<__main__block__63____A*>(__parent))->__field____main__block__63____A____x;
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
    // Assignment - '='
    // RHS
    // Int Literal
    stack.push_back (42);
    // LHS
    // Member Accessor Assignment
    // LHS
    stack.push_back (reinterpret_cast<long>(__main__block__63__a));
    // RHS
    __parent = stack.back ();
    stack.pop_back ();
    __rhs = stack.back ();
    stack.pop_back ();
    (reinterpret_cast<__main__block__63____A*>(__parent))->__field____main__block__63____A____x = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&(reinterpret_cast<__main__block__63____A*>(__parent))->__field____main__block__63____A____x));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(int) -> void
    {
        // Arguments
        // Member Accessor obj.x
        {
            // LHS
            stack.push_back (reinterpret_cast<long>(__main__block__63__a));
            // RHS
            __parent = stack.back ();
            stack.pop_back ();
            long __res = (reinterpret_cast<__main__block__63____A*>(__parent))->__field____main__block__63____A____x;
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
    // Assignment - '+='
    // RHS
    // Int Literal
    stack.push_back (20);
    // LHS
    // Member Accessor Assignment
    // LHS
    stack.push_back (reinterpret_cast<long>(__main__block__63__a));
    // RHS
    __parent = stack.back ();
    stack.pop_back ();
    __rhs = stack.back ();
    stack.pop_back ();
    (reinterpret_cast<__main__block__63____A*>(__parent))->__field____main__block__63____A____x = (reinterpret_cast<__main__block__63____A*>(__parent))->__field____main__block__63____A____x + *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&(reinterpret_cast<__main__block__63____A*>(__parent))->__field____main__block__63____A____x));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(int) -> void
    {
        // Arguments
        // Member Accessor obj.x
        {
            // LHS
            stack.push_back (reinterpret_cast<long>(__main__block__63__a));
            // RHS
            __parent = stack.back ();
            stack.pop_back ();
            long __res = (reinterpret_cast<__main__block__63____A*>(__parent))->__field____main__block__63____A____x;
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
    // Assignment - '-='
    // RHS
    // Int Literal
    stack.push_back (13);
    // LHS
    // Member Accessor Assignment
    // LHS
    stack.push_back (reinterpret_cast<long>(__main__block__63__a));
    // RHS
    __parent = stack.back ();
    stack.pop_back ();
    __rhs = stack.back ();
    stack.pop_back ();
    (reinterpret_cast<__main__block__63____A*>(__parent))->__field____main__block__63____A____x = (reinterpret_cast<__main__block__63____A*>(__parent))->__field____main__block__63____A____x - *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&(reinterpret_cast<__main__block__63____A*>(__parent))->__field____main__block__63____A____x));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(int) -> void
    {
        // Arguments
        // Member Accessor obj.x
        {
            // LHS
            stack.push_back (reinterpret_cast<long>(__main__block__63__a));
            // RHS
            __parent = stack.back ();
            stack.pop_back ();
            long __res = (reinterpret_cast<__main__block__63____A*>(__parent))->__field____main__block__63____A____x;
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
    // Assignment - '*='
    // RHS
    // Int Literal
    stack.push_back (2);
    // LHS
    // Member Accessor Assignment
    // LHS
    stack.push_back (reinterpret_cast<long>(__main__block__63__a));
    // RHS
    __parent = stack.back ();
    stack.pop_back ();
    __rhs = stack.back ();
    stack.pop_back ();
    (reinterpret_cast<__main__block__63____A*>(__parent))->__field____main__block__63____A____x = (reinterpret_cast<__main__block__63____A*>(__parent))->__field____main__block__63____A____x * *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&(reinterpret_cast<__main__block__63____A*>(__parent))->__field____main__block__63____A____x));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(int) -> void
    {
        // Arguments
        // Member Accessor obj.x
        {
            // LHS
            stack.push_back (reinterpret_cast<long>(__main__block__63__a));
            // RHS
            __parent = stack.back ();
            stack.pop_back ();
            long __res = (reinterpret_cast<__main__block__63____A*>(__parent))->__field____main__block__63____A____x;
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
    // Assignment - '/='
    // RHS
    // Int Literal
    stack.push_back (3);
    // LHS
    // Member Accessor Assignment
    // LHS
    stack.push_back (reinterpret_cast<long>(__main__block__63__a));
    // RHS
    __parent = stack.back ();
    stack.pop_back ();
    __rhs = stack.back ();
    stack.pop_back ();
    (reinterpret_cast<__main__block__63____A*>(__parent))->__field____main__block__63____A____x = (reinterpret_cast<__main__block__63____A*>(__parent))->__field____main__block__63____A____x / *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&(reinterpret_cast<__main__block__63____A*>(__parent))->__field____main__block__63____A____x));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(int) -> void
    {
        // Arguments
        // Member Accessor obj.x
        {
            // LHS
            stack.push_back (reinterpret_cast<long>(__main__block__63__a));
            // RHS
            __parent = stack.back ();
            stack.pop_back ();
            long __res = (reinterpret_cast<__main__block__63____A*>(__parent))->__field____main__block__63____A____x;
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
    // Function Call - println(int) -> void
    {
        // Arguments
        // Pre-Increment
        {
            // RHS
            // Member Accessor obj.x
            {
                // LHS
                stack.push_back (reinterpret_cast<long>(__main__block__63__a));
                // RHS
                __parent = stack.back ();
                stack.pop_back ();
                long __res = (reinterpret_cast<__main__block__63____A*>(__parent))->__field____main__block__63____A____x;
                stack.push_back (*reinterpret_cast<long*>(&__res));
            }
            __rhs = stack.back ();
            stack.pop_back ();
            // LHS
            // Member Accessor Assignment
            // LHS
            stack.push_back (reinterpret_cast<long>(__main__block__63__a));
            // RHS
            __parent = stack.back ();
            stack.pop_back ();
            (reinterpret_cast<__main__block__63____A*>(__parent))->__field____main__block__63____A____x = (reinterpret_cast<__main__block__63____A*>(__parent))->__field____main__block__63____A____x + 1;
            __res = (reinterpret_cast<__main__block__63____A*>(__parent))->__field____main__block__63____A____x;
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
    // Function Call - println(int) -> void
    {
        // Arguments
        // Pre-Decrement
        {
            // RHS
            // Member Accessor obj.x
            {
                // LHS
                stack.push_back (reinterpret_cast<long>(__main__block__63__a));
                // RHS
                __parent = stack.back ();
                stack.pop_back ();
                long __res = (reinterpret_cast<__main__block__63____A*>(__parent))->__field____main__block__63____A____x;
                stack.push_back (*reinterpret_cast<long*>(&__res));
            }
            __rhs = stack.back ();
            stack.pop_back ();
            // LHS
            // Member Accessor Assignment
            // LHS
            stack.push_back (reinterpret_cast<long>(__main__block__63__a));
            // RHS
            __parent = stack.back ();
            stack.pop_back ();
            (reinterpret_cast<__main__block__63____A*>(__parent))->__field____main__block__63____A____x = (reinterpret_cast<__main__block__63____A*>(__parent))->__field____main__block__63____A____x - 1;
            __res = (reinterpret_cast<__main__block__63____A*>(__parent))->__field____main__block__63____A____x;
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
    // Function Call - println(int) -> void
    {
        // Arguments
        // Negative
        {
            // RHS
            // Member Accessor obj.x
            {
                // LHS
                stack.push_back (reinterpret_cast<long>(__main__block__63__a));
                // RHS
                __parent = stack.back ();
                stack.pop_back ();
                long __res = (reinterpret_cast<__main__block__63____A*>(__parent))->__field____main__block__63____A____x;
                stack.push_back (*reinterpret_cast<long*>(&__res));
            }
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
        // Positive
        {
            // RHS
            // Member Accessor obj.x
            {
                // LHS
                stack.push_back (reinterpret_cast<long>(__main__block__63__a));
                // RHS
                __parent = stack.back ();
                stack.pop_back ();
                long __res = (reinterpret_cast<__main__block__63____A*>(__parent))->__field____main__block__63____A____x;
                stack.push_back (*reinterpret_cast<long*>(&__res));
            }
            __rhs = stack.back ();
            stack.pop_back ();
            long __res = *reinterpret_cast<long*>(&__rhs);
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
    // Function Call - println(int) -> void
    {
        // Arguments
        // Negate
        {
            // RHS
            // Member Accessor obj.x
            {
                // LHS
                stack.push_back (reinterpret_cast<long>(__main__block__63__a));
                // RHS
                __parent = stack.back ();
                stack.pop_back ();
                long __res = (reinterpret_cast<__main__block__63____A*>(__parent))->__field____main__block__63____A____x;
                stack.push_back (*reinterpret_cast<long*>(&__res));
            }
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
        // Bitwise Negation
        {
            // RHS
            // Member Accessor obj.x
            {
                // LHS
                stack.push_back (reinterpret_cast<long>(__main__block__63__a));
                // RHS
                __parent = stack.back ();
                stack.pop_back ();
                long __res = (reinterpret_cast<__main__block__63____A*>(__parent))->__field____main__block__63____A____x;
                stack.push_back (*reinterpret_cast<long*>(&__res));
            }
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
        // Post-Increment
        {
            // LHS
            // Member Accessor Assignment
            // LHS
            stack.push_back (reinterpret_cast<long>(__main__block__63__a));
            // RHS
            __parent = stack.back ();
            stack.pop_back ();
            long __res = (reinterpret_cast<__main__block__63____A*>(__parent))->__field____main__block__63____A____x;
            (reinterpret_cast<__main__block__63____A*>(__parent))->__field____main__block__63____A____x = (reinterpret_cast<__main__block__63____A*>(__parent))->__field____main__block__63____A____x + 1;
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
    // Function Call - println(int) -> void
    {
        // Arguments
        // Member Accessor obj.x
        {
            // LHS
            stack.push_back (reinterpret_cast<long>(__main__block__63__a));
            // RHS
            __parent = stack.back ();
            stack.pop_back ();
            long __res = (reinterpret_cast<__main__block__63____A*>(__parent))->__field____main__block__63____A____x;
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
    // Function Call - println(int) -> void
    {
        // Arguments
        // Post-Decrement
        {
            // LHS
            // Member Accessor Assignment
            // LHS
            stack.push_back (reinterpret_cast<long>(__main__block__63__a));
            // RHS
            __parent = stack.back ();
            stack.pop_back ();
            long __res = (reinterpret_cast<__main__block__63____A*>(__parent))->__field____main__block__63____A____x;
            (reinterpret_cast<__main__block__63____A*>(__parent))->__field____main__block__63____A____x = (reinterpret_cast<__main__block__63____A*>(__parent))->__field____main__block__63____A____x - 1;
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
    // Function Call - println(int) -> void
    {
        // Arguments
        // Member Accessor obj.x
        {
            // LHS
            stack.push_back (reinterpret_cast<long>(__main__block__63__a));
            // RHS
            __parent = stack.back ();
            stack.pop_back ();
            long __res = (reinterpret_cast<__main__block__63____A*>(__parent))->__field____main__block__63____A____x;
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

    //---------------------------------------------------------------------
    //---------------------------------------------------------------------
    // Code Block
    // Statement
    // Function Call - println(char[]) -> void
    {
        // Arguments
        // String Literal
        {
            char str_literal[] = "=== test logical and";
            // convert to a heap string
            char* str = new char[21];
            // copy string to heap allocation
            std::memcpy (str, &str_literal, 21);
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
        // Int Literal
        stack.push_back (2);
        __stackval = stack.back ();
        stack.pop_back ();
        long** __res = new long*[__stackval];
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // LHS
    // Variable declaration
    long** __main__block__65__a;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__65__a = *reinterpret_cast<long***>(&__rhs);
    // Result of assignment
    stack.push_back (reinterpret_cast<long>(__main__block__65__a));
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
    long __main__block__65__x;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__65__x = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__65__x));
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
    long __main__block__65__y;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__65__y = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__65__y));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Assignment - '='
    // RHS
    // AND
    // LHS
    // AND
    // LHS
    stack.push_back (*reinterpret_cast<long*>(&__main__block__65__x));
    __lhs = stack.back ();
    // Short circuit eval - only check rhs if lhs was true
    if (__lhs)
    {
        // RHS
        stack.push_back (*reinterpret_cast<long*>(&__main__block__65__y));
        __rhs = stack.back ();
        stack.pop_back ();
    }
    __lhs = stack.back ();
    stack.pop_back ();
    __res = __lhs && __rhs;
    stack.push_back (__res);
    __lhs = stack.back ();
    // Short circuit eval - only check rhs if lhs was true
    if (__lhs)
    {
        // RHS
        // Subscript Expression
        {
            // LHS
            // Subscript Expression
            {
                // LHS
                stack.push_back (reinterpret_cast<long>(__main__block__65__a));
                // OFFSET
                // Int Literal
                stack.push_back (512);
                __offset = stack.back ();
                stack.pop_back ();
                __pointer = stack.back ();
                stack.pop_back ();
                long* __res = (*reinterpret_cast<long***>(&__pointer))[*reinterpret_cast<long*>(&__offset)];
                stack.push_back (reinterpret_cast<long>(__res));
            }
            // OFFSET
            // Int Literal
            stack.push_back (0);
            __offset = stack.back ();
            stack.pop_back ();
            __pointer = stack.back ();
            stack.pop_back ();
            long __res = (*reinterpret_cast<long**>(&__pointer))[*reinterpret_cast<long*>(&__offset)];
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        __rhs = stack.back ();
        stack.pop_back ();
    }
    __lhs = stack.back ();
    stack.pop_back ();
    __res = __lhs && __rhs;
    stack.push_back (__res);
    // LHS
    // Variable declaration
    long __main__block__65__r;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__65__r = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__65__r));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(int) -> void
    {
        // Arguments
        stack.push_back (*reinterpret_cast<long*>(&__main__block__65__r));
        
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

    //---------------------------------------------------------------------
    //---------------------------------------------------------------------
    // Code Block
    // Statement
    // Function Call - println(char[]) -> void
    {
        // Arguments
        // String Literal
        {
            char str_literal[] = "=== test logical or";
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

    // Statement
    // Assignment - '='
    // RHS
    // Array Allocator
    {
        // Int Literal
        stack.push_back (2);
        __stackval = stack.back ();
        stack.pop_back ();
        long** __res = new long*[__stackval];
        stack.push_back (reinterpret_cast<long>(__res));
    }
    // LHS
    // Variable declaration
    long** __main__block__66__a;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__66__a = *reinterpret_cast<long***>(&__rhs);
    // Result of assignment
    stack.push_back (reinterpret_cast<long>(__main__block__66__a));
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
    long __main__block__66__x;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__66__x = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__66__x));
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
    long __main__block__66__y;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__66__y = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__66__y));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Assignment - '='
    // RHS
    // OR
    // LHS
    // OR
    // LHS
    stack.push_back (*reinterpret_cast<long*>(&__main__block__66__x));
    __lhs = stack.back ();
    // Short circuit eval - only check rhs if lhs was false
    if (!__lhs)
    {
        // RHS
        stack.push_back (*reinterpret_cast<long*>(&__main__block__66__y));
        __rhs = stack.back ();
        stack.pop_back ();
    }
    __lhs = stack.back ();
    stack.pop_back ();
    __res = __lhs || __rhs;
    stack.push_back (__res);
    __lhs = stack.back ();
    // Short circuit eval - only check rhs if lhs was false
    if (!__lhs)
    {
        // RHS
        // Subscript Expression
        {
            // LHS
            // Subscript Expression
            {
                // LHS
                stack.push_back (reinterpret_cast<long>(__main__block__66__a));
                // OFFSET
                // Int Literal
                stack.push_back (512);
                __offset = stack.back ();
                stack.pop_back ();
                __pointer = stack.back ();
                stack.pop_back ();
                long* __res = (*reinterpret_cast<long***>(&__pointer))[*reinterpret_cast<long*>(&__offset)];
                stack.push_back (reinterpret_cast<long>(__res));
            }
            // OFFSET
            // Int Literal
            stack.push_back (0);
            __offset = stack.back ();
            stack.pop_back ();
            __pointer = stack.back ();
            stack.pop_back ();
            long __res = (*reinterpret_cast<long**>(&__pointer))[*reinterpret_cast<long*>(&__offset)];
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        __rhs = stack.back ();
        stack.pop_back ();
    }
    __lhs = stack.back ();
    stack.pop_back ();
    __res = __lhs || __rhs;
    stack.push_back (__res);
    // LHS
    // Variable declaration
    long __main__block__66__r;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__66__r = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__66__r));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(int) -> void
    {
        // Arguments
        stack.push_back (*reinterpret_cast<long*>(&__main__block__66__r));
        
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

    //---------------------------------------------------------------------
    //---------------------------------------------------------------------
    // Code Block
    // Statement
    // Assignment - '='
    // RHS
    // Null Literal
    stack.push_back ((long)nullptr);
    // LHS
    // Variable declaration
    char* __main__block__67__arr;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__67__arr = *reinterpret_cast<char**>(&__rhs);
    // Result of assignment
    stack.push_back (reinterpret_cast<long>(__main__block__67__arr));
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
        stack.push_back (reinterpret_cast<long>(__main__block__67__arr));
        // RHS
        // Null Literal
        stack.push_back ((long)nullptr);
        __rhs = stack.back ();
        stack.pop_back ();
        __lhs = stack.back ();
        stack.pop_back ();
        long __res = *reinterpret_cast<char**>(&__lhs) == nullptr;
        stack.push_back (*reinterpret_cast<long*>(&__res));
    }
    long __if__68__cond = stack.back ();
    stack.pop_back ();
    // get condition from stack
    if (__if__68__cond)
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
                char str_literal[] = "it null";
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
            // push dummy value - funcall returns void
            stack.push_back (0);
        }
        // Statement results can be ignored
        stack.pop_back ();
        // End Statement

        //-----------------------------------------------------------------
    }
    // End of if
    //---------------------------------------------------------------------
    //---------------------------------------------------------------------
    //---------------------------------------------------------------------
    // Code Block
    // Statement
    // Function Call - println(char[]) -> void
    {
        // Arguments
        // String Literal
        {
            char str_literal[] = "=== test vector of vector";
            // convert to a heap string
            char* str = new char[26];
            // copy string to heap allocation
            std::memcpy (str, &str_literal, 26);
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

    //=====================================================================
    // Class Template - 
    // Class Declaration - __main__block__70____Vec__char inherits __builtin____main__Object
    // *see this class def before this parent function

    // Populate Dispatch Table
    __dtable____main__block__70____Vec__char[0] = (void*)__method____main__block__70____Vec__char____push_back__char;
    // Class Declaration - __main__block__70____Vec__Vec inherits __builtin____main__Object
    // *see this class def before this parent function

    // Populate Dispatch Table
    __dtable____main__block__70____Vec__Vec[0] = (void*)__method____main__block__70____Vec__Vec____push_back__Vec;
    // Class Declaration - __main__block__70____Vec__Point inherits __builtin____main__Object
    // *see this class def before this parent function

    // Populate Dispatch Table
    __dtable____main__block__70____Vec__Point[0] = (void*)__method____main__block__70____Vec__Point____push_back__Point;
    // End Class Template - 
    //=====================================================================

    // Statement
    // Assignment - '='
    // RHS
    // Constructor Call - Vec<:Vec<:char:>:>::Vec() -> Vec<:Vec<:char:>:>
    {
        // Arguments
        stack.push_back (reinterpret_cast<long>(new __main__block__70____Vec__Vec ()));
    }
    // LHS
    // Variable declaration
    __main__block__70____Vec__Vec* __main__block__70__v;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__70__v = reinterpret_cast<__main__block__70____Vec__Vec*>(__rhs);
    // Result of assignment
    stack.push_back (reinterpret_cast<long>(__main__block__70__v));
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
    long __main__block__70__for__77__i;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__70__for__77__i = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__70__for__77__i));
    // We can ignore the init result
    stack.pop_back ();
    // Using an infinite loop so we can write a separate multi-line condition
    while (1)
    {
        // Condition
        // Less Than
        {
            // LHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__70__for__77__i));
            // RHS
            // Int Literal
            stack.push_back (5);
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
        // Method Call - Vec<:Vec<:char:>:>::push_back(Vec<:char:>) -> void
        // LHS
        stack.push_back (reinterpret_cast<long>(__main__block__70__v));
        // RHS
        {
            // Arguments
            // Constructor Call - Vec<:char:>::Vec() -> Vec<:char:>
            {
                // Arguments
                stack.push_back (reinterpret_cast<long>(new __main__block__70____Vec__char ()));
            }
            __stackval = stack.back ();
            stack.pop_back ();
            // Reinterpret from general register
            __main__block__70____Vec__char* __arg0 = reinterpret_cast<__main__block__70____Vec__char*>(__stackval);
            __obj = stack.back ();
            stack.pop_back ();
            __method____main__block__70____Vec__Vec____push_back__Vec (reinterpret_cast<__main__block__70____Vec__Vec*>(__obj), __arg0);
            // push dummy value - method rtype is void
            stack.push_back (0);
        }
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
        long __main__block__70__for__77__block__78__for__79__j;
        __rhs = stack.back ();
        stack.pop_back ();
        __main__block__70__for__77__block__78__for__79__j = *reinterpret_cast<long*>(&__rhs);
        // Result of assignment
        stack.push_back (*reinterpret_cast<long*>(&__main__block__70__for__77__block__78__for__79__j));
        // We can ignore the init result
        stack.pop_back ();
        // Using an infinite loop so we can write a separate multi-line condition
        while (1)
        {
            // Condition
            // Less Than
            {
                // LHS
                stack.push_back (*reinterpret_cast<long*>(&__main__block__70__for__77__block__78__for__79__j));
                // RHS
                // Int Literal
                stack.push_back (5);
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
                        stack.push_back (*reinterpret_cast<long*>(&__main__block__70__for__77__i));
                        // RHS
                        stack.push_back (*reinterpret_cast<long*>(&__main__block__70__for__77__block__78__for__79__j));
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
            long __if__81__cond = stack.back ();
            stack.pop_back ();
            // get condition from stack
            if (__if__81__cond)
            {
                // Body
                // Statement
                // Method Call - Vec<:char:>::push_back(char) -> void
                // LHS
                // Subscript Expression
                {
                    // LHS
                    // Member Accessor obj.data
                    {
                        // LHS
                        stack.push_back (reinterpret_cast<long>(__main__block__70__v));
                        // RHS
                        __parent = stack.back ();
                        stack.pop_back ();
                        __main__block__70____Vec__char** __res = (reinterpret_cast<__main__block__70____Vec__Vec*>(__parent))->__field____main__block__70____Vec__Vec____data;
                        stack.push_back (reinterpret_cast<long>(__res));
                    }
                    // OFFSET
                    stack.push_back (*reinterpret_cast<long*>(&__main__block__70__for__77__i));
                    __offset = stack.back ();
                    stack.pop_back ();
                    __pointer = stack.back ();
                    stack.pop_back ();
                    __main__block__70____Vec__char* __res = (reinterpret_cast<__main__block__70____Vec__char**>(__pointer))[*reinterpret_cast<long*>(&__offset)];
                    stack.push_back (reinterpret_cast<long>(__res));
                }
                // RHS
                {
                    // Arguments
                    // Char Literal
                    stack.push_back (static_cast<long>(static_cast<unsigned char>('x')));
                    __stackval = stack.back ();
                    stack.pop_back ();
                    // Reinterpret from general register
                    char __arg0 = static_cast<char>(static_cast<unsigned char>(__stackval));
                    __obj = stack.back ();
                    stack.pop_back ();
                    __method____main__block__70____Vec__char____push_back__char (reinterpret_cast<__main__block__70____Vec__char*>(__obj), __arg0);
                    // push dummy value - method rtype is void
                    stack.push_back (0);
                }
                // Statement results can be ignored
                stack.pop_back ();
                // End Statement

            }
            //-------------------------------------------------------------
            // Else-Statement
            else
            {
                // Statement
                // Method Call - Vec<:char:>::push_back(char) -> void
                // LHS
                // Subscript Expression
                {
                    // LHS
                    // Member Accessor obj.data
                    {
                        // LHS
                        stack.push_back (reinterpret_cast<long>(__main__block__70__v));
                        // RHS
                        __parent = stack.back ();
                        stack.pop_back ();
                        __main__block__70____Vec__char** __res = (reinterpret_cast<__main__block__70____Vec__Vec*>(__parent))->__field____main__block__70____Vec__Vec____data;
                        stack.push_back (reinterpret_cast<long>(__res));
                    }
                    // OFFSET
                    stack.push_back (*reinterpret_cast<long*>(&__main__block__70__for__77__i));
                    __offset = stack.back ();
                    stack.pop_back ();
                    __pointer = stack.back ();
                    stack.pop_back ();
                    __main__block__70____Vec__char* __res = (reinterpret_cast<__main__block__70____Vec__char**>(__pointer))[*reinterpret_cast<long*>(&__offset)];
                    stack.push_back (reinterpret_cast<long>(__res));
                }
                // RHS
                {
                    // Arguments
                    // Char Literal
                    stack.push_back (static_cast<long>(static_cast<unsigned char>('.')));
                    __stackval = stack.back ();
                    stack.pop_back ();
                    // Reinterpret from general register
                    char __arg0 = static_cast<char>(static_cast<unsigned char>(__stackval));
                    __obj = stack.back ();
                    stack.pop_back ();
                    __method____main__block__70____Vec__char____push_back__char (reinterpret_cast<__main__block__70____Vec__char*>(__obj), __arg0);
                    // push dummy value - method rtype is void
                    stack.push_back (0);
                }
                // Statement results can be ignored
                stack.pop_back ();
                // End Statement

            }
            //-------------------------------------------------------------
            // End of if
            //-------------------------------------------------------------
            //-------------------------------------------------------------
            // Update
            // Pre-Increment
            {
                // RHS
                stack.push_back (*reinterpret_cast<long*>(&__main__block__70__for__77__block__78__for__79__j));
                __rhs = stack.back ();
                stack.pop_back ();
                __main__block__70__for__77__block__78__for__79__j = __main__block__70__for__77__block__78__for__79__j + 1;
                __res = __main__block__70__for__77__block__78__for__79__j;
                stack.push_back (*reinterpret_cast<long*>(&__res));
            }
            // We can ignore the update result
            stack.pop_back ();
        }
        //-----------------------------------------------------------------
        //-----------------------------------------------------------------
        // Update
        // Pre-Increment
        {
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__70__for__77__i));
            __rhs = stack.back ();
            stack.pop_back ();
            __main__block__70__for__77__i = __main__block__70__for__77__i + 1;
            __res = __main__block__70__for__77__i;
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        // We can ignore the update result
        stack.pop_back ();
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
    long __main__block__70__for__82__i;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__70__for__82__i = *reinterpret_cast<long*>(&__rhs);
    // Result of assignment
    stack.push_back (*reinterpret_cast<long*>(&__main__block__70__for__82__i));
    // We can ignore the init result
    stack.pop_back ();
    // Using an infinite loop so we can write a separate multi-line condition
    while (1)
    {
        // Condition
        // Less Than
        {
            // LHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__70__for__82__i));
            // RHS
            // Member Accessor obj.size
            {
                // LHS
                stack.push_back (reinterpret_cast<long>(__main__block__70__v));
                // RHS
                __parent = stack.back ();
                stack.pop_back ();
                long __res = (reinterpret_cast<__main__block__70____Vec__Vec*>(__parent))->__field____main__block__70____Vec__Vec____size;
                stack.push_back (*reinterpret_cast<long*>(&__res));
            }
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
        long __main__block__70__for__82__block__83__for__84__j;
        __rhs = stack.back ();
        stack.pop_back ();
        __main__block__70__for__82__block__83__for__84__j = *reinterpret_cast<long*>(&__rhs);
        // Result of assignment
        stack.push_back (*reinterpret_cast<long*>(&__main__block__70__for__82__block__83__for__84__j));
        // We can ignore the init result
        stack.pop_back ();
        // Using an infinite loop so we can write a separate multi-line condition
        while (1)
        {
            // Condition
            // Less Than
            {
                // LHS
                stack.push_back (*reinterpret_cast<long*>(&__main__block__70__for__82__block__83__for__84__j));
                // RHS
                // Member Accessor obj.size
                {
                    // LHS
                    // Subscript Expression
                    {
                        // LHS
                        // Member Accessor obj.data
                        {
                            // LHS
                            stack.push_back (reinterpret_cast<long>(__main__block__70__v));
                            // RHS
                            __parent = stack.back ();
                            stack.pop_back ();
                            __main__block__70____Vec__char** __res = (reinterpret_cast<__main__block__70____Vec__Vec*>(__parent))->__field____main__block__70____Vec__Vec____data;
                            stack.push_back (reinterpret_cast<long>(__res));
                        }
                        // OFFSET
                        stack.push_back (*reinterpret_cast<long*>(&__main__block__70__for__82__i));
                        __offset = stack.back ();
                        stack.pop_back ();
                        __pointer = stack.back ();
                        stack.pop_back ();
                        __main__block__70____Vec__char* __res = (reinterpret_cast<__main__block__70____Vec__char**>(__pointer))[*reinterpret_cast<long*>(&__offset)];
                        stack.push_back (reinterpret_cast<long>(__res));
                    }
                    // RHS
                    __parent = stack.back ();
                    stack.pop_back ();
                    long __res = (reinterpret_cast<__main__block__70____Vec__char*>(__parent))->__field____main__block__70____Vec__char____size;
                    stack.push_back (*reinterpret_cast<long*>(&__res));
                }
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
                // Subscript Expression
                {
                    // LHS
                    // Member Accessor obj.data
                    {
                        // LHS
                        // Subscript Expression
                        {
                            // LHS
                            // Member Accessor obj.data
                            {
                                // LHS
                                stack.push_back (reinterpret_cast<long>(__main__block__70__v));
                                // RHS
                                __parent = stack.back ();
                                stack.pop_back ();
                                __main__block__70____Vec__char** __res = (reinterpret_cast<__main__block__70____Vec__Vec*>(__parent))->__field____main__block__70____Vec__Vec____data;
                                stack.push_back (reinterpret_cast<long>(__res));
                            }
                            // OFFSET
                            stack.push_back (*reinterpret_cast<long*>(&__main__block__70__for__82__i));
                            __offset = stack.back ();
                            stack.pop_back ();
                            __pointer = stack.back ();
                            stack.pop_back ();
                            __main__block__70____Vec__char* __res = (reinterpret_cast<__main__block__70____Vec__char**>(__pointer))[*reinterpret_cast<long*>(&__offset)];
                            stack.push_back (reinterpret_cast<long>(__res));
                        }
                        // RHS
                        __parent = stack.back ();
                        stack.pop_back ();
                        char* __res = (reinterpret_cast<__main__block__70____Vec__char*>(__parent))->__field____main__block__70____Vec__char____data;
                        stack.push_back (reinterpret_cast<long>(__res));
                    }
                    // OFFSET
                    stack.push_back (*reinterpret_cast<long*>(&__main__block__70__for__82__block__83__for__84__j));
                    __offset = stack.back ();
                    stack.pop_back ();
                    __pointer = stack.back ();
                    stack.pop_back ();
                    char __res = (*reinterpret_cast<char**>(&__pointer))[*reinterpret_cast<long*>(&__offset)];
                    stack.push_back (static_cast<long>(static_cast<unsigned char>(__res)));
                }
                
                __stackval = stack.back ();
                stack.pop_back ();
                // Reinterpret from general register
                char __arg0 = static_cast<char>(static_cast<unsigned char>(__stackval));
                // print
                __builtin__print__char (__arg0);
                // push dummy value - funcall returns void
                stack.push_back (0);
            }
            // Statement results can be ignored
            stack.pop_back ();
            // End Statement

            //-------------------------------------------------------------
            // Update
            // Pre-Increment
            {
                // RHS
                stack.push_back (*reinterpret_cast<long*>(&__main__block__70__for__82__block__83__for__84__j));
                __rhs = stack.back ();
                stack.pop_back ();
                __main__block__70__for__82__block__83__for__84__j = __main__block__70__for__82__block__83__for__84__j + 1;
                __res = __main__block__70__for__82__block__83__for__84__j;
                stack.push_back (*reinterpret_cast<long*>(&__res));
            }
            // We can ignore the update result
            stack.pop_back ();
        }
        //-----------------------------------------------------------------
        // Statement
        // Function Call - println() -> void
        {
            // Arguments
            // println
            __builtin__println ();
            // push dummy value - funcall returns void
            stack.push_back (0);
        }
        // Statement results can be ignored
        stack.pop_back ();
        // End Statement

        //-----------------------------------------------------------------
        // Update
        // Pre-Increment
        {
            // RHS
            stack.push_back (*reinterpret_cast<long*>(&__main__block__70__for__82__i));
            __rhs = stack.back ();
            stack.pop_back ();
            __main__block__70__for__82__i = __main__block__70__for__82__i + 1;
            __res = __main__block__70__for__82__i;
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
            char str_literal[] = "=== test class decl after template decl";
            // convert to a heap string
            char* str = new char[40];
            // copy string to heap allocation
            std::memcpy (str, &str_literal, 40);
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

    // Class Declaration - __main__block__70____Point inherits __builtin____main__Object
    // *see this class def before this parent function

    // Populate Dispatch Table
    // Statement
    // Assignment - '='
    // RHS
    // Constructor Call - Vec<:Point:>::Vec() -> Vec<:Point:>
    {
        // Arguments
        stack.push_back (reinterpret_cast<long>(new __main__block__70____Vec__Point ()));
    }
    // LHS
    // Variable declaration
    __main__block__70____Vec__Point* __main__block__70__points;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__70__points = reinterpret_cast<__main__block__70____Vec__Point*>(__rhs);
    // Result of assignment
    stack.push_back (reinterpret_cast<long>(__main__block__70__points));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Method Call - Vec<:Point:>::push_back(Point) -> void
    // LHS
    stack.push_back (reinterpret_cast<long>(__main__block__70__points));
    // RHS
    {
        // Arguments
        // Constructor Call - Point::Point(int, int) -> Point
        {
            // Arguments
            // Int Literal
            stack.push_back (7);
            // Int Literal
            stack.push_back (6);
            __stackval = stack.back ();
            stack.pop_back ();
            // Reinterpret from general register
            long __arg1 = *reinterpret_cast<long*>(&__stackval);
            __stackval = stack.back ();
            stack.pop_back ();
            // Reinterpret from general register
            long __arg0 = *reinterpret_cast<long*>(&__stackval);
            stack.push_back (reinterpret_cast<long>(new __main__block__70____Point (__arg0, __arg1)));
        }
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        __main__block__70____Point* __arg0 = reinterpret_cast<__main__block__70____Point*>(__stackval);
        __obj = stack.back ();
        stack.pop_back ();
        __method____main__block__70____Vec__Point____push_back__Point (reinterpret_cast<__main__block__70____Vec__Point*>(__obj), __arg0);
        // push dummy value - method rtype is void
        stack.push_back (0);
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - print(int) -> void
    {
        // Arguments
        // Member Accessor obj.x
        {
            // LHS
            // Subscript Expression
            {
                // LHS
                // Member Accessor obj.data
                {
                    // LHS
                    stack.push_back (reinterpret_cast<long>(__main__block__70__points));
                    // RHS
                    __parent = stack.back ();
                    stack.pop_back ();
                    __main__block__70____Point** __res = (reinterpret_cast<__main__block__70____Vec__Point*>(__parent))->__field____main__block__70____Vec__Point____data;
                    stack.push_back (reinterpret_cast<long>(__res));
                }
                // OFFSET
                // Int Literal
                stack.push_back (0);
                __offset = stack.back ();
                stack.pop_back ();
                __pointer = stack.back ();
                stack.pop_back ();
                __main__block__70____Point* __res = (reinterpret_cast<__main__block__70____Point**>(__pointer))[*reinterpret_cast<long*>(&__offset)];
                stack.push_back (reinterpret_cast<long>(__res));
            }
            // RHS
            __parent = stack.back ();
            stack.pop_back ();
            long __res = (reinterpret_cast<__main__block__70____Point*>(__parent))->__field____main__block__70____Point____x;
            stack.push_back (*reinterpret_cast<long*>(&__res));
        }
        
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
        // Member Accessor obj.y
        {
            // LHS
            // Subscript Expression
            {
                // LHS
                // Member Accessor obj.data
                {
                    // LHS
                    stack.push_back (reinterpret_cast<long>(__main__block__70__points));
                    // RHS
                    __parent = stack.back ();
                    stack.pop_back ();
                    __main__block__70____Point** __res = (reinterpret_cast<__main__block__70____Vec__Point*>(__parent))->__field____main__block__70____Vec__Point____data;
                    stack.push_back (reinterpret_cast<long>(__res));
                }
                // OFFSET
                // Int Literal
                stack.push_back (0);
                __offset = stack.back ();
                stack.pop_back ();
                __pointer = stack.back ();
                stack.pop_back ();
                __main__block__70____Point* __res = (reinterpret_cast<__main__block__70____Point**>(__pointer))[*reinterpret_cast<long*>(&__offset)];
                stack.push_back (reinterpret_cast<long>(__res));
            }
            // RHS
            __parent = stack.back ();
            stack.pop_back ();
            long __res = (reinterpret_cast<__main__block__70____Point*>(__parent))->__field____main__block__70____Point____y;
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

    //---------------------------------------------------------------------
    //---------------------------------------------------------------------
    // Code Block
    // Statement
    // Function Call - println(char[]) -> void
    {
        // Arguments
        // String Literal
        {
            char str_literal[] = "=== test template defaults";
            // convert to a heap string
            char* str = new char[27];
            // copy string to heap allocation
            std::memcpy (str, &str_literal, 27);
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

    //=====================================================================
    // Class Template - 
    // Class Declaration - __main__block__87____A__B inherits __builtin____main__Object
    // *see this class def before this parent function

    // Populate Dispatch Table
    // End Class Template - 
    //=====================================================================

    // Class Declaration - __main__block__87____B inherits __builtin____main__Object
    // *see this class def before this parent function

    // Populate Dispatch Table
    // Statement
    // Assignment - '='
    // RHS
    // Constructor Call - A<:B:>::A() -> A<:B:>
    {
        // Arguments
        stack.push_back (reinterpret_cast<long>(new __main__block__87____A__B ()));
    }
    // LHS
    // Variable declaration
    __main__block__87____A__B* __main__block__87__a;
    __rhs = stack.back ();
    stack.pop_back ();
    __main__block__87__a = reinterpret_cast<__main__block__87____A__B*>(__rhs);
    // Result of assignment
    stack.push_back (reinterpret_cast<long>(__main__block__87__a));
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    // Statement
    // Function Call - println(int) -> void
    {
        // Arguments
        // Member Accessor obj.w
        {
            // LHS
            // Member Accessor obj.x
            {
                // LHS
                stack.push_back (reinterpret_cast<long>(__main__block__87__a));
                // RHS
                __parent = stack.back ();
                stack.pop_back ();
                __main__block__87____B* __res = (reinterpret_cast<__main__block__87____A__B*>(__parent))->__field____main__block__87____A__B____x;
                stack.push_back (reinterpret_cast<long>(__res));
            }
            // RHS
            __parent = stack.back ();
            stack.pop_back ();
            long __res = (reinterpret_cast<__main__block__87____B*>(__parent))->__field____main__block__87____B____w;
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

    // Function Declaration - print(B) -> void
    // *see this func def before this parent function

    // Statement
    // Function Call - print(B) -> void
    {
        // Arguments
        // Null Literal
        stack.push_back ((long)nullptr);
        
        __stackval = stack.back ();
        stack.pop_back ();
        // Reinterpret from general register
        std::nullptr_t __arg0 = nullptr;
        // print
        __main__block__87____print__B (__arg0);
        // push dummy value - funcall returns void
        stack.push_back (0);
    }
    // Statement results can be ignored
    stack.pop_back ();
    // End Statement

    //---------------------------------------------------------------------
}
//=========================================================================
//### END OF MAIN ########################################################
//=========================================================================

