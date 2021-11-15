// The Amy Assembly Programming Language Lexer
// Author: Amy Burnett
// October 29 2021
//========================================================================

#ifndef LEXER_H
#define LEXER_H

//========================================================================
// Includes 

#include <sstream>
#include <vector>
#include <string>
#include <tuple>

#include "util.hpp"

//========================================================================

const std::string DELIMITERS = " \t\n";

//========================================================================

class Lexer
{
public:
    std::string source; 
    int index = 0; 

    Lexer (std::string source);

    std::vector<Data>
    getNumber (); 

    std::vector<Data> 
    getWord (); 

    std::vector<Data>
    getToken ();
     
    bool 
    hasToken ();
    
}; 


//========================================================================

#endif 