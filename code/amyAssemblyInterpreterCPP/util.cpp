// The Amy Assembly Programming Language Util Functions 
// Author: Amy Burnett
// October 29 2021
//========================================================================
// Includes 

#include <sstream>
#include <vector>
#include <string>

#include "util.hpp"

//========================================================================

std::string
Data::toString ()
{
    if (type == INT)
        return std::to_string (i);
    if (type == FLOAT)
        return std::to_string (f);
    if (type == CHAR)
        return std::string (1, c);
    if (type == WORD)
        return s; 
    return "ERROR";
}

//========================================================================
