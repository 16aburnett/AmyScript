// The Amy Assembly Programming Language Util Functions 
// Author: Amy Burnett
// October 29 2021
//========================================================================

#ifndef UTIL_H
#define UTIL_H

//========================================================================
//includes 

#include <sstream>
#include <vector>
#include <string>

//========================================================================

const int WORD = 0;
const int INT = 1;
const int FLOAT = 2;
const int ERROR = 5;
const int MEMORY = 7;
const int CHAR = 8;
const int JUMPPOINT = 9;

//========================================================================

class Data
{
public:
    int type; 
    int i;
    float f;
    char c; 
    std::string s; 
    Data ()
    {
        i = 0; 
        type = INT;
    }
    Data (int val)
    {
        i = val; 
        type = INT;
    }
    Data (float val)
    {
        f = val; 
        type = FLOAT;
    }
    Data (char val)
    {
        c = val; 
        type = CHAR;
    }
    Data (std::string val)
    {
        s = val; 
        type = WORD;
    }
    std::string
    toString ();

};

//========================================================================

#endif