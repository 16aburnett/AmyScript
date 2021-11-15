// The Amy Assembly Programming Language Lexer
// Author: Amy Burnett
// October 29 2021
//========================================================================
// Includes 

#include <iostream>

#include <sstream>
#include <vector>
#include <string>
#include <tuple>

#include "lexer.hpp"

//========================================================================


Lexer::Lexer (std::string source_)
{
    source = source_; 
    index = 0; 
}

//========================================================================

std::vector<Data>
Lexer::getNumber ()
{
    // std::cout << "[getNumber] looking for INT/FLOAT in \"" << source.substr (index) << "\"" << std::endl << std::flush;

    // ensure valid index
    if (index >= source.size())
        return std::vector<Data> {Data(ERROR), Data("No Number")};
    // ensure it starts with 0-9 or '-' minus
    if (!(isdigit (source[index]) || source[index] == '-'))
    {

        // std::cout << "doesnt start with 0-9 or '-'" << std::endl << std::flush;
    
        std::stringstream msg;
        msg << "Unexpected '" << source[index] << "' for line \n " << source << "\n";
        return std::vector<Data> {Data(ERROR), Data(msg.str())};
    }

    std::stringstream token;
    token << source[index]; 
    index++;

    // grab left of decimal 
    while (index < source.size() && isdigit (source[index]))
    {
        token << source[index];
        ++index; 
    }

    // FLOAT
    if (index < source.size() && source[index] == '.')
    {
        token << '.';
        ++index; 
        // grab right of decimal 
        while (index < source.size() && isdigit (source[index]))
        {
            token << source[index];
            ++index; 
        }
        // success return the float 
        return std::vector<Data> {Data(FLOAT), Data(""), Data(stof (token.str ()))};
    }
    // INT
    // ensure token isnt just '-'
    if (token.str() == "-")
    {
        std::stringstream msg;
        msg << "Unexpected '-' for line \n " << source << "\n";
        return std::vector<Data> {Data(ERROR), Data(msg.str())};
    }
    // success! return the int 
    return std::vector<Data> {Data(INT), Data(""), Data(stoi (token.str ()))};

}

//========================================================================

std::vector<Data> 
Lexer::getWord ()
{
    // std::cout << "[getWord] looking for word in \"" << source.substr (index) << "\"" << std::endl << std::flush;

    // ensure valid index
    if (index >= source.size())
        return std::vector<Data> {Data(ERROR), Data("No word")};
    // ensure first is alpha, or underscore 
    if (!(isalpha(source[index]) || source[index] == '_'))
    {
        std::stringstream msg;
        msg << "Unexpected '" << source[index] << "' for line \n " << source << "\n";
        return std::vector<Data> {Data(ERROR), Data(msg.str())};
    }
    std::stringstream token; 
    token << source[index];
    ++index; 
    // read alphanumerics + '_'
    while (index < source.size() && (isalnum (source[index]) or source[index] == '_'))
    {
        token << source[index];
        ++index; 
    }
    // success: matched a word 
    return std::vector<Data> {Data(WORD), Data(""), Data(token.str())};
}

//========================================================================

std::vector<Data>
Lexer::getToken ()
{
    // std::cout << "Getting token from \"" << source.substr (index) << "\"" << std::endl << std::flush;
    // grab next component 
    while (index < source.size())
    {
        // possibly a word (x __init__ x09 wq9_8qw__e9qw8e)
        if (isalpha (source[index]) || source[index] == '_')
        {
            // std::cout << "Possibly a word" << std::endl << std::flush;
            std::vector<Data> tuple = getWord ();
            // skip over whitespace
            while (index < source.size() && DELIMITERS.find(source[index]) != DELIMITERS.npos)
            {
                ++index; 
            }
            // try to match JUMPPOINT label 
            if (index < source.size() && source[index] == ':')
                return std::vector<Data> {Data(JUMPPOINT), Data(""), tuple[2]};
            // try to match subscript 
            if (tuple[0].i != ERROR && index < source.size() && source[index] == '[')
            {
                // std::cout << "Trying to match subscript" << std::endl << std::flush;
                ++index; 
                // subscript is var 
                if (index < source.size() && (isalpha(source[index]) or source[index] == '_'))
                {
                    // std::cout << "Subscript is a var" << std::endl << std::flush;
                    auto subscript = getWord ();
                    // ensure success
                    if (subscript[0].i == ERROR)
                        return subscript; 
                    // ensure subscript is closed
                    if (index >= source.size() || source[index] != ']')
                    {
                        std::stringstream msg;
                        msg << "Expected ']' at index " << index << " for line \n " << source << "\n";
                        return std::vector<Data> {Data(ERROR), Data(msg.str())};
                    }
                    // skip over RBRACKET 
                    ++index; 
                    // ensure next is space if not end of string
                    if (index < source.size() && DELIMITERS.find(source[index]) == DELIMITERS.npos)
                    {
                        // std::cout << (DELIMITERS.find(source[index]) == DELIMITERS.npos) << std::endl << std::flush;
                        std::stringstream msg;
                        msg << "Unexpected '" << source[index] << "' for line \n " << source << "\n";
                        return std::vector<Data> {Data(ERROR), Data(msg.str())};
                    }

                    // std::cout << "success" << std::endl << std::flush;
                    // success
                    ++index;
                    return std::vector<Data> {Data(MEMORY), Data(""), Data(WORD), tuple[2], Data(WORD), subscript[2]};

                }
                // subscript is immediate 
                if (index < source.size() && (isdigit(source[index]) or source[index] == '-'))
                {
                    // std::cout << "Subscript is immediate val" << std::endl << std::flush;
                    auto subscript = getNumber ();
                    // ensure success
                    if (subscript[0].i == ERROR)
                        return subscript; 
                    // ensure it is an int
                    if (subscript[0].i != INT)
                    {
                        std::stringstream msg;
                        msg << "Memory address should be an integer for line \n " << source << "\n";
                        return std::vector<Data> {Data(ERROR), Data(msg.str())};
                    }
                    // ensure subscript is closed
                    if (index >= source.size() || source[index] != ']')
                    {
                        std::stringstream msg;
                        msg << "Expected ']' at index " << index << " for line \n " << source << "\n";
                        return std::vector<Data> {Data(ERROR), Data(msg.str())};
                    }
                    // skip over RBRACKET 
                    ++index; 
                    // ensure next is space
                    if (index < source.size() && DELIMITERS.find(source[index]) == DELIMITERS.npos)
                    {
                        std::stringstream msg;
                        msg << "Unexpected '" << source[index] << "' for line \n " << source << "\n";
                        return std::vector<Data> {Data(ERROR), Data(msg.str())};
                    }
                    // success
                    ++index;
                    return std::vector<Data> {Data(MEMORY), Data(""), Data(WORD), tuple[2], Data(INT), subscript[2]};

                }
            }

            return tuple; 
        }

        // possibly a number 3 3.14 -2 102
        if (isdigit (source[index]) || source[index] == '-')
        {
            return getNumber ();
        }

        // character ('x' ' ' 't' '\n')
        if (source[index] == '\'')
        {
            std::stringstream token; 
            ++index; 
            while (index < source.size() && source[index] != '\'')
            {
                token << source[index];
                ++index; 
            }
            // ensure ending single quote
            if (index >= source.size() || source[index] != '\'')
            {
                std::stringstream msg;
                msg << "Line ended without closing double quotes for line \n " << source << "\n";
                return std::vector<Data> {Data(ERROR), Data(msg.str())};
            }
            ++index; 
            // ensure next position is whitespace or end 
            if (index < source.size() &&  DELIMITERS.find(source[index]) == DELIMITERS.npos)
            {
                std::stringstream msg;
                msg << "Unexpected '" << source[index] << "' for line \n " << source << "\n";
                return std::vector<Data> {Data(ERROR), Data(msg.str())};
            }
            // success: return char 
            Data c;
            c.c = token.str()[0];
            c.type = CHAR;
            return std::vector<Data> {Data(CHAR), Data(""), c};

        }

        ++index; 
    
    }

    std::stringstream msg;
    msg << "Unexpected '" << source[index] << "' for line \n " << source << "\n";
    return std::vector<Data> {Data(ERROR), Data(msg.str())};
}

//========================================================================

bool 
Lexer::hasToken ()
{
    return index < source.size(); 
}


//========================================================================