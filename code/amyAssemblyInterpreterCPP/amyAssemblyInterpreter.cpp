// Amy Assembly Interpreter CPP Version
// Author: Amy Burnett
//========================================================================
// Includes 

#include <iostream>       // std::cout, std::cin 
#include <string> 
#include <cstring>        // strlen()
#include <fstream>
#include <sstream> 
#include <vector>
#include <list>
#include <unordered_map>
#include <algorithm>      // std::remove

#include "util.hpp"
#include "lexer.hpp"
#include "memory.hpp"

//========================================================================
// // Globals/Constants

// // OPCODES
const int OPCODE_ASSIGN      = 0;
const int OPCODE_MALLOC      = 1;
const int OPCODE_FREE        = 2;
const int OPCODE_ADD         = 3;
const int OPCODE_SUBTRACT    = 4;
const int OPCODE_MULTIPLY    = 5;
const int OPCODE_DIVIDE      = 6;
const int OPCODE_MOD         = 7;
const int OPCODE_PRINT       = 8;
const int OPCODE_PRINTLN     = 9;
const int OPCODE_INPUT       = 10;
const int OPCODE_HALT        = 11;
const int OPCODE_CALL        = 12;
const int OPCODE_RETURN      = 13;
const int OPCODE_RESPONSE    = 14;
const int OPCODE_JUMP        = 15;
const int OPCODE_JUMPLT      = 16;
const int OPCODE_JUMPLE      = 17;
const int OPCODE_JUMPEQ      = 18;
const int OPCODE_JUMPNEQ     = 19;
const int OPCODE_JUMPGE      = 20;
const int OPCODE_JUMPGT      = 21;
const int OPCODE_EQUAL       = 22;
const int OPCODE_NEQUAL      = 23;
const int OPCODE_LT          = 24;
const int OPCODE_LE          = 25;
const int OPCODE_GT          = 26;
const int OPCODE_GE          = 27;
const int OPCODE_COMPARE     = 28;
const int OPCODE_AND         = 29;
const int OPCODE_OR          = 30;
const int OPCODE_NOT         = 31;
const int OPCODE_SIZEOF      = 32;
const int OPCODE_PUSH        = 33;
const int OPCODE_POP         = 34;
const int OPCODE_STACKGET    = 35;
const int OPCODE_FtoI        = 36; // float to int
const int OPCODE_ItoF        = 37; // int to float
const int OPCODE_STRING      = 38; // int/float to string
const int OPCODE_StoF        = 39; // string to float
const int OPCODE_StoI        = 40; // string to int 
std::unordered_map<std::string, int> toOpCode = { 
   {"assign"      , OPCODE_ASSIGN},
   {"malloc"      , OPCODE_MALLOC},
   {"free"        , OPCODE_FREE},
   {"add"         , OPCODE_ADD},
   {"subtract"    , OPCODE_SUBTRACT},
   {"multiply"    , OPCODE_MULTIPLY},
   {"divide"      , OPCODE_DIVIDE},
   {"mod"         , OPCODE_MOD},
   {"print"       , OPCODE_PRINT},
   {"input"       , OPCODE_INPUT},
   {"halt"        , OPCODE_HALT},
   {"call"        , OPCODE_CALL},
   {"return"      , OPCODE_RETURN},
   {"response"    , OPCODE_RESPONSE},
   {"jump"        , OPCODE_JUMP},
   {"jlt"         , OPCODE_JUMPLT},
   {"jle"         , OPCODE_JUMPLE},
   {"jeq"         , OPCODE_JUMPEQ},
   {"jneq"        , OPCODE_JUMPNEQ},
   {"jge"         , OPCODE_JUMPGE},
   {"jgt"         , OPCODE_JUMPGT},
   {"equal"       , OPCODE_EQUAL},
   {"nequal"      , OPCODE_NEQUAL},
   {"lt"          , OPCODE_LT},
   {"le"          , OPCODE_LE},
   {"gt"          , OPCODE_GT},
   {"ge"          , OPCODE_GE},
   {"cmp"         , OPCODE_COMPARE},
   {"println"     , OPCODE_PRINTLN},
   {"sizeof"      , OPCODE_SIZEOF},
   {"and"         , OPCODE_AND},
   {"or"          , OPCODE_OR},
   {"not"         , OPCODE_NOT},
   {"push"        , OPCODE_PUSH},
   {"pop"         , OPCODE_POP},
   {"stackget"    , OPCODE_STACKGET},
   {"ftoi"        , OPCODE_FtoI},
   {"itof"        , OPCODE_ItoF},
   {"string"      , OPCODE_STRING},
   {"stof"        , OPCODE_StoF},
   {"stoi"        , OPCODE_StoI}
};


// // PARAM MODES
const int MODE_IMMEDIATE = 0; // value represent data
const int MODE_STACK     = 1; // value is a stack address (aka a variable/function)
const int MODE_MEMORY    = 2; // value is a heap address 
const int MODE_JUMPPOINT = -1;

//========================================================================
// Util functions 

//    def padzeros(i, maxdigits):
//             stri = str(i)
//             while len(stri) < maxdigits:
//                 stri = "".join(["0",stri])
//             return stri

std::vector<std::string> 
splitlines (const std::string & str)
{
    std::vector<std::string> lines; 
    std::stringstream ss (str); 

    std::string line; 
    while (std::getline (ss, line, '\n'))
        lines.push_back (line);
    return lines; 
}

const std::string WHITESPACE = " \n\r\t\f\v";

std::string ltrim(const std::string &s)
{
    size_t start = s.find_first_not_of(WHITESPACE);
    return (start == std::string::npos) ? "" : s.substr(start);
}
 
std::string rtrim(const std::string &s)
{
    size_t end = s.find_last_not_of(WHITESPACE);
    return (end == std::string::npos) ? "" : s.substr(0, end + 1);
}
 
std::string trim(const std::string &s) {
    return rtrim(ltrim(s));
}

Data
getVariableValue (std::vector<Data> & stack, std::unordered_map<int, std::unordered_map<int, Data>> & scopes, Heap & heap, int base_pointer, std::unordered_map<int, std::string> intToWord, Data var)
{
    // Ensure variable exists in the current scope or parent scopes
    int bptr = base_pointer;
    // top scope will have prev base pointer of -1
    while (bptr != -1)
    {
        // found variable in bptr's scope
        if (scopes[bptr].find (var.i) != scopes[bptr].end())
        {
            // if (scopes[bptr][var].type == CHAR && scopes[bptr][var].c == '\\')
            //     return scopes[bptr][var].replace ("\\n", "\n").replace ("\\t", "\t").replace ("\\r", "\r").replace ("\\b", "\b")
            return scopes[bptr][var.i];
        }
        bptr = stack[bptr-1].i;
    }
    
    std::cout << "Error: variable referenced before assignment - '" << intToWord[var.i] << "'" << std::endl;
    exit(1);
}


// Gets the absolute memory address including any offset
int 
getMemAddress (std::vector<Data> & stack, std::unordered_map<int, std::unordered_map<int, Data>> & scopes, Heap & heap, int base_pointer, std::unordered_map<int, std::string> intToWord, Data pmode, Data pointer, Data omode, Data offset)  
{
    // Ensure pointer mode is stack variable
    if (pmode.i != MODE_STACK)
    {
        std::cout << "Error: ptr mode must be stack variable" << std::endl;
        exit(1);
    }

    // grab pointer value
    int address = getVariableValue(stack, scopes, heap, base_pointer, intToWord, pointer).i;

    // make sure pointer is not null 
    if (address == MEMORY_NULL)
    {
        std::cout << "Error: Cannot read from null address" << std::endl;
        exit (1);
    }

    // add offset
    if (omode.i == MODE_STACK)
        offset = getVariableValue(stack, scopes, heap, base_pointer, intToWord, offset).i;

    // make sure offset isn't outside of address' block
    if (offset.i >= heap.sizeOf (address))
    {
        std::cout << "Error: Index out of bounds." << std::endl;
        exit (1);
    }
    
    return address+offset.i;
}

// Returns the next parameter value whether the parameter mode
//   is MODE_MEMORY, MODE_STACK, MODE_IMMEDIATE, or MODE_STRING
// Params:
// - heap - the heap for getting memory values
// - stack - the stack for getting variable values
// - params - a list of code parameters to parse the next value out of
// - reject - a list of modes to reject if they are found next 

std::pair<Data, int>
getNextValue (std::vector<Data> & stack, std::unordered_map<int, std::unordered_map<int, Data>> & scopes, Heap & heap, int base_pointer, std::unordered_map<int, std::string> intToWord, std::vector<Data> & params, int i, std::vector<int> reject)
{
    // Case 1: Memory
    if (params[i].i == MODE_MEMORY && std::find (reject.begin(), reject.end(), MODE_MEMORY) == reject.end())
    {
        // next 4 nums make up the pointer and offset
        Data pmode, pointer, omode, offset;
        pmode = params[i+1];
        pointer = params[i+2];
        omode = params[i+3];
        offset = params[i+4];

        Data address = getVariableValue(stack, scopes, heap, base_pointer, intToWord, pointer.i);
        if (omode.i == MODE_STACK)
            offset = getVariableValue(stack, scopes, heap, base_pointer, intToWord, offset.i);

        // make sure offset isn't outside of address' block
        if (offset.i >= heap.sizeOf (address.i))
        {
            std::cout << "Error: Index out of bounds." << std::endl;
            exit (1);
        }

        // heap address must be int
        if (address.type == INT)
            // make sure pointer is not null 
            if (address.i == MEMORY_NULL)
            {
                std::cout << "Error: Cannot read from null address" << std::endl;
                exit (1);
            }
            return {heap.memory[address.i+offset.i], i+5};
        // float is invalid
        if (address.type == FLOAT)
        {
            std::cout << "Error: float is not an address" << std::endl;
            exit(1);
        }
        // strings and lists
        else
            return {heap.memory[address.i+offset.i], i+5};
    }
    
    // Case 2: Stack variable
    else if (params[i].i == MODE_STACK && std::find (reject.begin(), reject.end(), MODE_STACK) == reject.end())
        return {getVariableValue(stack, scopes, heap, base_pointer, intToWord, params[i+1].i), i+2};
    
    // Case 3: Immediate Variable
    else if (params[i].i == MODE_IMMEDIATE && std::find (reject.begin(), reject.end(), MODE_IMMEDIATE) == reject.end())
    {
        // convert special characters for output
        // if isinstance(params[i+1], str) and params[i+1][0] == '\\':
        //     return params[i+1].replace ("\\n", "\n").replace ("\\t", "\t").replace ("\\r", "\r").replace ("\\b", "\b"), i+2
        return {params[i+1], i+2};
    }

    // Case 5: Unknown mode
    std::cout << "Error: Bad Parameter Mode" << std::endl;
    exit(1);
}

//========================================================================
// The Interpreter for AmyAssembly 

class AmyAssemblyInterpreter
{
public: 
    std::string file_name; 
    bool output_combined; 
    bool output_intcode; 
    bool debug; 
    int argc; 
    char** argv;

    //--------------------------------------------------------------------

    AmyAssemblyInterpreter (std::string _file_name, int _argc, char* _argv[])
    {
        file_name = _file_name; 
        output_combined = false; 
        output_intcode = false; 
        debug = false; 
        argc = _argc;
        argv = _argv; 
    }

    //--------------------------------------------------------------------

    void execute (const std::string & sourceCode)
    {
        // Break up code into separate lines 
        std::vector<std::string> lines = splitlines (sourceCode);

        // remove any comments and empty lines
        for (int i = lines.size()-1; i > -1; --i)
        {
            // remove trailing whitespace 
            lines[i] = trim(lines[i]);
            if (lines[i][0] == '/' && lines[i][1] == '/')
                lines.erase (std::next (lines.begin(), i)); 
            else if (lines[i] == "")
                lines.erase (std::next (lines.begin(), i));
        }

        // for (auto line : lines)
        //     std::cout << line << std::endl; 


        //=== CONVERT TO INTCODE =========================================

        // this translates each line into a list of integers
        // to more easily execute each line 

        // Variable name to Int mapping
        // This does not care about scope 
        std::unordered_map<std::string, int> wordToInt; 
        // this holds the reverse mapping 
        // for outputting the variable's string name in error messages 
        std::unordered_map<int, std::string> intToWord;
        int wordId = 0;
        // stores all the jump points (label, instruction)
        // this populates the initial stack frame 
        // and treats the labels as variables that store their instruction pointer
        std::unordered_map<int, int> jumpPoints;
        std::vector<std::vector<Data>> instructions; 
        int lineNo = -1;
        for (auto line : lines)
        {
            // std::cout << line << std::endl;

            // advance lineNo
            lineNo++; 

            // tokenize line
            Lexer lexer (line);
            std::vector<Data> code_line; 

            std::vector<Data> token = lexer.getToken();
            int type = token[0].i; 
            std::string msg = token[1].s;
            Data value = token[2];

            // save jump points before executing code 
            // allows for jumps to labels that weren't executed yet 
            if (type == JUMPPOINT)
            {
                // var DNE
                if (wordToInt.find (value.s) == wordToInt.end())
                {
                    wordToInt[value.s] = wordId;
                    intToWord[wordId] = value.s; 
                    ++wordId;
                }
                // jump point already exists 
                else if (jumpPoints.find (wordToInt[value.s]) != jumpPoints.end())
                {
                    std::cout << "Error: Duplicate jump point '" << value.s << std::endl; 
                    exit (1);
                }
                jumpPoints[wordToInt[value.s]] = instructions.size();
                instructions.push_back({Data(MODE_JUMPPOINT), Data(wordToInt[value.s]), Data((int)instructions.size())});
                continue;

            }
            // ensure first component is a word for a instruction name 
            else if (type != WORD)
            {
                std::cout << "lines should start with a word or jump point label \n " << line << std::endl;
                exit(1);
            }
            std::string command = value.s;
            // convert to lowercase 
            std::transform (command.begin(), command.end(), command.begin(), ::tolower);
            // ensure it is a valid command
            if (toOpCode.find (command) == toOpCode.end())
            {
                std::cout << command << " is not a command" << std::endl;
                exit(1);
            }
            code_line.push_back (Data(toOpCode[command]));

            // convert the arguments to integers
            while (lexer.hasToken())
            {
                std::vector<Data> token = lexer.getToken();

                // for (Data d : token)
                //     std::cout << d.toString() << " ";
                // std::cout << std::endl;

                int type = token[0].i; 
                std::string msg = token[1].s;
                Data value = token[2];

                // report errors in parsing
                if (type == ERROR)
                {
                    std::cout << "error" << std::endl;
                    exit(1);
                }
                // immediate
                if (type == INT || type == FLOAT || type == CHAR)
                {
                    code_line.push_back (Data(MODE_IMMEDIATE));
                    code_line.push_back (value);
                }
                // var/func
                else if (type == WORD)
                {
                    // var DNE
                    if (wordToInt.find (value.s) == wordToInt.end())
                    {
                        wordToInt[value.s] = wordId;
                        intToWord[wordId] = value.s;
                        ++wordId;
                    }
                    code_line.push_back(Data(MODE_STACK));
                    code_line.push_back(Data(wordToInt[value.s])); 
                }
                // memory 
                else if (type == MEMORY)
                {
                    code_line.push_back (Data(MODE_MEMORY));
                    // pointer is immediate
                    if (token[2].i == INT or token[2].i == FLOAT)
                    {
                        // push pointer 
                        code_line.push_back (Data(MODE_IMMEDIATE)); 
                        code_line.push_back (token[3]);
                        // offset is immediate
                        // **should only be INT
                        if (token[4].i == INT or token[4].i == FLOAT)
                        {
                            code_line.push_back (Data(MODE_IMMEDIATE));
                            code_line.push_back (token[5]);
                        }
                        // offset is stack
                        // should only be WORD
                        else
                        {
                            // var DNE
                            if (wordToInt.find (token[5].s) == wordToInt.end())
                            {
                                wordToInt[token[5].s] = wordId;
                                intToWord[wordId] = token[5].s;
                                ++wordId;
                            }
                            code_line.push_back (Data(MODE_STACK));
                            code_line.push_back (Data(wordToInt[token[5].s]));
                        }
                    }
                    // pointer is a var
                    else
                    {
                        // var DNE
                        if (wordToInt.find(token[3].s) == wordToInt.end())
                        {
                            wordToInt[token[3].s] = wordId;
                            intToWord[wordId] = token[3].s;
                            ++wordId;
                        }
                        code_line.push_back (Data(MODE_STACK));
                        code_line.push_back (Data(wordToInt[token[3].s]));
                        // offset is immediate
                        // **should only be INT
                        if (token[4].i == INT or token[4].i == FLOAT)
                        {
                            code_line.push_back (Data(MODE_IMMEDIATE));
                            code_line.push_back (Data(token[5].i));
                        }
                        // offset is var 
                        else
                        {
                            // var DNE
                            if (wordToInt.find(token[5].s) == wordToInt.end())
                            {
                                wordToInt[token[5].s] = wordId;
                                intToWord[wordId] = token[5].s;
                                ++wordId;
                            }
                            code_line.push_back (Data(MODE_STACK));
                            code_line.push_back (Data(wordToInt[token[5].s]));
                        }
                    }
                }
            }
            // add line to code list
            instructions.push_back (code_line); 
        }

    
        //=== Print Code =================================================

        // for (int i = 0; i < instructions.size(); ++i)
        // {
        //     std::cout << lines[i] << " | ";
        //     for (Data d : instructions[i])
        //     {
        //         std::cout << d.toString() << " "; 
        //     }
        //     std::cout << std::endl;
        // }
        // std::cout << std::endl;
    
        //=== Write Combined to File =====================================

        if (output_combined)
        {
            std::ofstream file (file_name + ("c"));
            int maxdigits = std::to_string(instructions.size()).size(); 
            for (int i = 0; i < instructions.size(); ++i)
            {
                file << "[";
                if (instructions[i].size() > 0)
                    file << instructions[i][0].toString();
                for (int j = 1; j < instructions[i].size(); ++j)
                    if (instructions[i][j].type == CHAR)
                        file << ", '" << instructions[i][j].toString() << "'";
                    else
                        file << ", " << instructions[i][j].toString();
                file << "] " << lines[i] << "\n"; 
            }
            file.close();

        }

        //=== Write IntCode to File ======================================

        if (output_intcode)
        {
            std::ofstream file (file_name + ("i"));
            for (int i = 0; i < instructions.size(); ++i)
            {
                if (instructions[i].size() > 0)
                    file << instructions[i][0].toString();
                for (int j = 1; j < instructions[i].size(); ++j)
                    if (instructions[i][j].type == CHAR)
                        file << ", '" << instructions[i][j].toString() << "'";
                    else
                        file << ", " << instructions[i][j].toString();
                file << "\n"; 
            }
            file.close();

        }

        //=== Setup stack and heap =======================================

        Heap heap; 

        // create the stack 
        // starts with the program arguments
        // and variable scope for main 
        // for each stack frame, the base_pointer should point
        // to the variable dictionary 
        std::vector<Data> stack;
        std::unordered_map<int, std::unordered_map<int, Data>> scopes;
        
        // push program args in reverse order
        for (int i = argc-1; i >= 0; --i)
        {
            // allocate string on heap
            int size = std::strlen(argv[i]);
            int ptr = heap.malloc(size);
            // copy string to heap 
            for (int j = 0; j < size; ++j)
                heap.memory[ptr+j] = argv[i][j];
            // put ptr on stack 
            stack.push_back (ptr);
        }
        // add the first stack frame 
        stack.push_back (argc);
        stack.push_back (-1);
        stack.push_back (-1);
        stack.push_back (0);// place holder for stack's scope
        // keep track of the base of the stack
        // this is the same address as the stack's current scope 
        int base_pointer = stack.size()-1;
        // add stack scope 
        scopes[base_pointer] = std::unordered_map<int,Data>();
        // populate stack scope with jump points 
        for (auto& iter : jumpPoints)
        {
            scopes[base_pointer][iter.first] = iter.second; 
        }
        // setup rest of the state variables
        int instruction_pointer = 0;
        Data return_value = 0;
        // flag states 
        int lessThanFlag = 0;
        int equalFlag = 0;
        int greaterThanFlag = 0;

        // std::cout << "=== Stack ===================" << std::endl;
        // for (int i = 0; i < stack.size(); ++i)
        // {
        //     if (scopes.find (i) != scopes.end())
        //     {
        //         std::cout << i << " -> [ "; 
        //         for (auto& iter : scopes[i])
        //         {
        //             std::cout << "{" << iter.first << " : " << iter.second.toString() << "} ";
        //         }
        //         std::cout << "]" << std::endl;
        //     }
        //     else 
        //         std::cout << i << " " << stack[i].toString() << std::endl;
        // }
        // std::cout << "=============================" << std::endl;


        // std::cout << "=== Heap ====================" << std::endl;
        // printheap (heap);
        // std::cout << "=============================" << std::endl;

        //=== Execute The Code ===========================================

        // evaluate lines
        while (instruction_pointer < instructions.size())
        {

            std::vector<Data> instruction = instructions[instruction_pointer];
            int cmd = instruction[0].i;
            std::vector<Data> params (++instruction.begin(), instruction.end());
            
            // print debug output 
            if (debug)
            {
                std::cout << "====================================================" << std::endl;
                // print ("[heap]", heap.memory, end="\n\n\n");
                // printheap (heap);
                // print ("[stack]", stack, end="\n\n\n");
                // std::cout << "[base-pointer] " << base_pointer << std::endl;
                // std::cout << "[less-than-flag] " << lessThanFlag << std::endl;
                // std::cout << "[equal-to-flag] " << equalFlag << std::endl;
                // std::cout << "[greater-than-flag] " << greaterThanFlag << std::endl;
                std::cout << "[current-instruction] [" << instruction_pointer << "] " << cmd << " ";
                for (int i = 0; i < params.size(); ++i)
                    std::cout << params[i].toString() << " ";
                std::cout << " | " << lines[instruction_pointer] << std::endl;
                std::cout << "====================================================" << std::endl;
            }

            switch (cmd)
            {
            case OPCODE_ASSIGN:
                // ASSIGN dest src
                // Case 1: Dest is Memory
                if (params[0].i == MODE_MEMORY)
                {
                    // next 4 nums make up the pointer and offset
                    Data pmode = params[1];
                    Data pointer = params[2];
                    Data omode = params[3];
                    Data offset = params[4];
                    int address = getMemAddress(stack, scopes, heap, base_pointer, intToWord, pmode, pointer, omode, offset);
                    // Assign dest to src
                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 5, std::vector<int>{});
                    heap.memory[address] = p.first;
                    int i = p.second; 
                }
                // Case 2: Dest is Stack variable
                else if (params[0].i == MODE_STACK)
                {
                    // Assign dest to src 
                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 2, std::vector<int>{});
                    scopes[base_pointer][params[1].i] = p.first; 
                    int i = p.second;
                }
                // Case 3: Dest is Invalid param type
                else
                {
                    std::cout << "Error: Can only assign a value to a stack variable or memory address" << std::endl;
                    exit(1);
                }
            break;
            case OPCODE_ADD:
            {
                // ADD dest src1 src2
                // Case 1: Dest is Memory
                if (params[0].i == MODE_MEMORY)
                {
                    // next 4 nums make up the pointer and offset
                    Data pmode = params[1];
                    Data pointer = params[2];
                    Data omode = params[3];
                    Data offset = params[4];
                    int address = getMemAddress(stack, scopes, heap, base_pointer, intToWord, pmode, pointer, omode, offset);

                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 5, std::vector<int>{});
                    Data src1 = p.first;
                    int i = p.second; 
                    p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, i, std::vector<int>{});
                    Data src2 = p.first;
                    i = p.second; 
                    
                    // perform addition based on types 
                    if (src1.type == INT)
                    {
                        if (src2.type == INT)
                            heap.memory[address] = src1.i + src2.i;
                        else if (src2.type == FLOAT)
                            heap.memory[address] = src1.i + src2.f;
                    }
                    else if (src1.type == FLOAT)
                    {
                        if (src2.type == INT)
                            heap.memory[address] = src1.f + src2.i;
                        else if (src2.type == FLOAT)
                            heap.memory[address] = src1.f + src2.f;
                    }
                    else
                    {
                        std::cout << "Error: Invalid type" << std::endl;
                        exit (1);
                    }
                }
                // Case 2: Dest is Stack variable
                else if (params[0].i == MODE_STACK)
                {
                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 2, std::vector<int>{});
                    Data src1 = p.first;
                    int i = p.second; 
                    p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, i, std::vector<int>{});
                    Data src2 = p.first;
                    i = p.second; 
                    
                    // perform addition based on types 
                    if (src1.type == INT)
                    {
                        if (src2.type == INT)
                            scopes[base_pointer][params[1].i] = src1.i + src2.i;
                        else if (src2.type == FLOAT)
                            scopes[base_pointer][params[1].i] = src1.i + src2.f;
                    }
                    else if (src1.type == FLOAT)
                    {
                        if (src2.type == INT)
                            scopes[base_pointer][params[1].i] = src1.f + src2.i;
                        else if (src2.type == FLOAT)
                            scopes[base_pointer][params[1].i] = src1.f + src2.f;
                    }
                    else
                    {
                        std::cout << "Error: Invalid type" << std::endl;
                        exit (1);
                    }
                }
                // Case 3: Dest is Invalid param type
                else
                {
                    std::cout << "Error: Dest should be memory or stack" << std::endl;
                    exit (1);
                }
            }
            break;
            case OPCODE_SUBTRACT:
            {
                // SUBTRACT dest src1 src2
                // Case 1: Dest is Memory
                if (params[0].i == MODE_MEMORY)
                {
                    // next 4 nums make up the pointer and offset
                    Data pmode = params[1];
                    Data pointer = params[2];
                    Data omode = params[3];
                    Data offset = params[4];
                    int address = getMemAddress(stack, scopes, heap, base_pointer, intToWord, pmode, pointer, omode, offset);

                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 5, std::vector<int>{});
                    Data src1 = p.first;
                    int i = p.second; 
                    p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, i, std::vector<int>{});
                    Data src2 = p.first;
                    i = p.second; 
                    
                    // perform op based on types 
                    if (src1.type == INT)
                    {
                        if (src2.type == INT)
                            heap.memory[address] = src1.i - src2.i;
                        else if (src2.type == FLOAT)
                            heap.memory[address] = src1.i - src2.f;
                    }
                    else if (src1.type == FLOAT)
                    {
                        if (src2.type == INT)
                            heap.memory[address] = src1.f - src2.i;
                        else if (src2.type == FLOAT)
                            heap.memory[address] = src1.f - src2.f;
                    }
                    else
                    {
                        std::cout << "Error: Invalid type" << std::endl;
                        exit (1);
                    }
                }
                // Case 2: Dest is Stack variable
                else if (params[0].i == MODE_STACK)
                {
                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 2, std::vector<int>{});
                    Data src1 = p.first;
                    int i = p.second; 
                    p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, i, std::vector<int>{});
                    Data src2 = p.first;
                    i = p.second; 
                    
                    // perform op based on types 
                    if (src1.type == INT)
                    {
                        if (src2.type == INT)
                            scopes[base_pointer][params[1].i] = src1.i - src2.i;
                        else if (src2.type == FLOAT)
                            scopes[base_pointer][params[1].i] = src1.i - src2.f;
                    }
                    else if (src1.type == FLOAT)
                    {
                        if (src2.type == INT)
                            scopes[base_pointer][params[1].i] = src1.f - src2.i;
                        else if (src2.type == FLOAT)
                            scopes[base_pointer][params[1].i] = src1.f - src2.f;
                    }
                    else
                    {
                        std::cout << "Error: Invalid type" << std::endl;
                        exit (1);
                    }
                }
                // Case 3: Dest is Invalid param type
                else
                {
                    std::cout << "Error: Dest should be memory or stack" << std::endl;
                    exit (1);
                }
            }
            break;
            case OPCODE_MULTIPLY:
            {
                // MULTIPLY dest src1 src2
                // Case 1: Dest is Memory
                if (params[0].i == MODE_MEMORY)
                {
                    // next 4 nums make up the pointer and offset
                    Data pmode = params[1];
                    Data pointer = params[2];
                    Data omode = params[3];
                    Data offset = params[4];
                    int address = getMemAddress(stack, scopes, heap, base_pointer, intToWord, pmode, pointer, omode, offset);

                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 5, std::vector<int>{});
                    Data src1 = p.first;
                    int i = p.second; 
                    p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, i, std::vector<int>{});
                    Data src2 = p.first;
                    i = p.second; 
                    
                    // perform op based on types 
                    if (src1.type == INT)
                    {
                        if (src2.type == INT)
                            heap.memory[address] = src1.i * src2.i;
                        else if (src2.type == FLOAT)
                            heap.memory[address] = src1.i * src2.f;
                    }
                    else if (src1.type == FLOAT)
                    {
                        if (src2.type == INT)
                            heap.memory[address] = src1.f * src2.i;
                        else if (src2.type == FLOAT)
                            heap.memory[address] = src1.f * src2.f;
                    }
                    else
                    {
                        std::cout << "Error: Invalid type" << std::endl;
                        exit (1);
                    }
                }
                // Case 2: Dest is Stack variable
                else if (params[0].i == MODE_STACK)
                {
                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 2, std::vector<int>{});
                    Data src1 = p.first;
                    int i = p.second; 
                    p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, i, std::vector<int>{});
                    Data src2 = p.first;
                    i = p.second; 
                    
                    // perform op based on types 
                    if (src1.type == INT)
                    {
                        if (src2.type == INT)
                            scopes[base_pointer][params[1].i] = src1.i * src2.i;
                        else if (src2.type == FLOAT)
                            scopes[base_pointer][params[1].i] = src1.i * src2.f;
                    }
                    else if (src1.type == FLOAT)
                    {
                        if (src2.type == INT)
                            scopes[base_pointer][params[1].i] = src1.f * src2.i;
                        else if (src2.type == FLOAT)
                            scopes[base_pointer][params[1].i] = src1.f * src2.f;
                    }
                    else
                    {
                        std::cout << "Error: Invalid type" << std::endl;
                        exit (1);
                    }
                }
                // Case 3: Dest is Invalid param type
                else
                {
                    std::cout << "Error: Dest should be memory or stack" << std::endl;
                    exit (1);
                }
            }
            break;
            case OPCODE_DIVIDE:
            {
                // DIVIDE dest src1 src2
                // Case 1: Dest is Memory
                if (params[0].i == MODE_MEMORY)
                {
                    // next 4 nums make up the pointer and offset
                    Data pmode = params[1];
                    Data pointer = params[2];
                    Data omode = params[3];
                    Data offset = params[4];
                    int address = getMemAddress(stack, scopes, heap, base_pointer, intToWord, pmode, pointer, omode, offset);

                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 5, std::vector<int>{});
                    Data src1 = p.first;
                    int i = p.second; 
                    p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, i, std::vector<int>{});
                    Data src2 = p.first;
                    i = p.second; 
                    
                    // perform op based on types 
                    if (src1.type == INT)
                    {
                        if (src2.type == INT)
                            heap.memory[address] = src1.i / src2.i;
                        else if (src2.type == FLOAT)
                            heap.memory[address] = src1.i / src2.f;
                    }
                    else if (src1.type == FLOAT)
                    {
                        if (src2.type == INT)
                            heap.memory[address] = src1.f / src2.i;
                        else if (src2.type == FLOAT)
                            heap.memory[address] = src1.f / src2.f;
                    }
                    else
                    {
                        std::cout << "Error: Invalid type" << std::endl;
                        exit (1);
                    }
                }
                // Case 2: Dest is Stack variable
                else if (params[0].i == MODE_STACK)
                {
                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 2, std::vector<int>{});
                    Data src1 = p.first;
                    int i = p.second; 
                    p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, i, std::vector<int>{});
                    Data src2 = p.first;
                    i = p.second; 
                    
                    // perform op based on types 
                    if (src1.type == INT)
                    {
                        if (src2.type == INT)
                            scopes[base_pointer][params[1].i] = src1.i / src2.i;
                        else if (src2.type == FLOAT)
                            scopes[base_pointer][params[1].i] = src1.i / src2.f;
                    }
                    else if (src1.type == FLOAT)
                    {
                        if (src2.type == INT)
                            scopes[base_pointer][params[1].i] = src1.f / src2.i;
                        else if (src2.type == FLOAT)
                            scopes[base_pointer][params[1].i] = src1.f / src2.f;
                    }
                    else
                    {
                        std::cout << "Error: Invalid type" << std::endl;
                        exit (1);
                    }
                }
                // Case 3: Dest is Invalid param type
                else
                {
                    std::cout << "Error: Dest should be memory or stack" << std::endl;
                    exit (1);
                }
            }
            break;
            case OPCODE_MOD:
            {
                // MOD dest src1 src2
                // Case 1: Dest is Memory
                if (params[0].i == MODE_MEMORY)
                {
                    // next 4 nums make up the pointer and offset
                    Data pmode = params[1];
                    Data pointer = params[2];
                    Data omode = params[3];
                    Data offset = params[4];
                    int address = getMemAddress(stack, scopes, heap, base_pointer, intToWord, pmode, pointer, omode, offset);

                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 5, std::vector<int>{});
                    Data src1 = p.first;
                    int i = p.second; 
                    p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, i, std::vector<int>{});
                    Data src2 = p.first;
                    i = p.second; 
                    
                    // perform op based on types 
                    if (src1.type == INT && src2.type == INT)
                            heap.memory[address] = src1.i % src2.i;
                    else
                    {
                        std::cout << "Error: Invalid type" << std::endl;
                        std::cout << "Can only MOD an INT by an INT" << std::endl;
                        exit (1);
                    }
                }
                // Case 2: Dest is Stack variable
                else if (params[0].i == MODE_STACK)
                {
                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 2, std::vector<int>{});
                    Data src1 = p.first;
                    int i = p.second; 
                    p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, i, std::vector<int>{});
                    Data src2 = p.first;
                    i = p.second; 

                    // perform op based on types 
                    if (src1.type == INT && src2.type == INT)
                            scopes[base_pointer][params[1].i] = src1.i % src2.i;
                    else
                    {
                        std::cout << "Error: Invalid type" << std::endl;
                        std::cout << "Can only MOD an INT by an INT" << std::endl;
                        exit (1);
                    }
                }
                // Case 3: Dest is Invalid param type
                else
                {
                    std::cout << "Error: Dest should be memory or stack" << std::endl;
                    exit (1);
                }
            }
            break;
            case OPCODE_PRINT:
            {
                // PRINT src
                // Only One Parameter
                auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 0, std::vector<int>{});
                Data src1 = p.first;
                int i = p.second; 
                // print
                std::cout << src1.toString();
            }
            break;
            case OPCODE_PRINTLN:
            {
                // PRINTLN 
                // PRINTLN value
                if (params.size() == 0)
                    std::cout << std::endl;
                else
                {
                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 0, std::vector<int>{});
                    Data src1 = p.first;
                    int i = p.second; 
                    // print
                    std::cout << src1.toString() << std::endl;
                }
            }
            break;
            case OPCODE_INPUT:
            {
                // INPUT dest 

                // Read in line 
                std::string line; 
                std::getline(std::cin, line);

                // put in memory 
                int lineAddress = heap.malloc(line.size());
                for (int i = 0; i < line.size(); ++i)
                    heap.memory[lineAddress+i] = Data(line[i]);

                // Case 1: Memory
                if (params[0].i == MODE_MEMORY)
                {
                    // next 4 nums make up the pointer and offset
                    Data pmode = params[1];
                    Data pointer = params[2];
                    Data omode = params[3];
                    Data offset = params[4];
                    int address = getMemAddress(stack, scopes, heap, base_pointer, intToWord, pmode, pointer, omode, offset);
                    heap.memory[address] = Data(lineAddress);
                }
                // Case 2: Stack variable
                else if (params[0].i == MODE_STACK)
                    scopes[base_pointer][params[1].i] = lineAddress;
                // Case 3: Invalid param type
                else
                {
                    std::cout << "Error: Dest should be memory or stack" << std::endl;
                    exit(1);
                }
            // calling functions
            }
            break;
            case OPCODE_CALL:
            {
                // CALL funcPtr
                // print (f"[interpreter] Function call {lines[instruction_pointer]}")

                auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 0, std::vector<int>{});
                Data funcPtr = p.first;
                int i = p.second; 

                // push return address 
                stack.push_back(instruction_pointer);

                // push previous base pointer
                stack.push_back(base_pointer);

                // move stack base pointer to after return address 
                base_pointer = stack.size();

                // add new variable scope 
                stack.push_back(0);
                scopes[base_pointer] = std::unordered_map<int, Data>();

                // jump to function start
                instruction_pointer = funcPtr.i;

            // returning from functions
            }
            break;
            case OPCODE_RETURN:
            {
                // RETURN value
                auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 0, std::vector<int>{});
                return_value = p.first;
                int i = p.second; 
                
                // restore instruction pointer
                instruction_pointer = stack[base_pointer-2].i;
                // pop off function's scope 
                // this does not work if there are extra values on the stack
                // stack.pop()

                // new pop off function's scope 
                scopes.erase (base_pointer);
                stack.resize (base_pointer);

                // restore base_pointer
                base_pointer = stack[base_pointer-1].i;
                // pop off base_pointer
                stack.pop_back();
                // pop off return address
                stack.pop_back();
                // top of stack should be at the params now 
            }
            break;
            case OPCODE_RESPONSE:
            {
                // RESPONSE dest
                // Case 1 : Stack variable
                if (params[0].i == MODE_STACK)
                    scopes[base_pointer][params[1].i] = return_value;
                // Case 2 : Memory address
                else if (params[0].i == MODE_MEMORY)
                {
                    // next 4 nums make up the pointer and offset
                    Data pmode = params[1];
                    Data pointer = params[2];
                    Data omode = params[3];
                    Data offset = params[4];
                    int address = getMemAddress(stack, scopes, heap, base_pointer, intToWord, pmode, pointer, omode, offset);
                    heap.memory[address] = return_value;
                }
                // Case 3 : Bad token
                else
                {
                    std::cout << "Error: RESPONSE requires a stack variable or a memory address" << std::endl;
                    exit(1);
                }
            // allocating data on heap
            }
            break;
            case OPCODE_MALLOC:
            {
                // MALLOC ptrDest size 
                // Pointer Case1 : variable
                if (params[0].i == MODE_STACK)
                {
                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 2, std::vector<int>{});
                    Data size = p.first;
                    int i = p.second; 
                    scopes[base_pointer][params[1].i] = heap.malloc (size.i);
                }
                // Pointer Case2 : memory
                else if (params[0].i == MODE_MEMORY)
                {
                    // next 4 nums make up the pointer and offset
                    Data pmode = params[1];
                    Data pointer = params[2];
                    Data omode = params[3];
                    Data offset = params[4];
                    int address = getMemAddress(stack, scopes, heap, base_pointer, intToWord, pmode, pointer, omode, offset);

                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 5, std::vector<int>{});
                    Data size = p.first;
                    int i = p.second;

                    heap.memory[address] = heap.malloc(size.i);
                }
                // Case 3: Invalid param type
                else
                {
                    std::cout << "Error: Dest should be Memory or Stack var" << std::endl;
                    exit(1);
                }
                // printheap(heap)
            // deallocating data on heap
            }
            break;
            case OPCODE_FREE:
            {
                // FREE pointer
                auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 0, std::vector<int>{});
                Data pointer = p.first;
                int i = p.second;
                // allocate space on heap 
                heap.free(pointer.i);
            }
            break;
            case OPCODE_SIZEOF:
            {
                // SIZEOF dest pointer
                // Case1 : variable
                if (params[0].i == MODE_STACK)
                {
                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 2, std::vector<int>{});
                    Data pointer = p.first;
                    int i = p.second; 
                    scopes[base_pointer][params[1].i] = heap.sizeOf (pointer.i);
                }
                // Case2 : memory
                else if (params[0].i == MODE_MEMORY)
                {
                    // next 4 nums make up the pointer and offset
                    Data pmode = params[1];
                    Data pointer = params[2];
                    Data omode = params[3];
                    Data offset = params[4];
                    int address = getMemAddress(stack, scopes, heap, base_pointer, intToWord, pmode, pointer, omode, offset);

                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 5, std::vector<int>{});
                    Data ptr = p.first;
                    int i = p.second;

                    heap.memory[address] = heap.sizeOf (ptr.i);
                }
                // Case 3: Invalid param type
                else
                {
                    std::cout << "Error: Dest should be Memory or Stack var" << std::endl;
                    exit(1);
                }
            }
            break;
            case OPCODE_COMPARE:
            {
                // COMPARE src1 src2
                // sets the appropriate comparision flag 
                auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 0, std::vector<int>{});
                Data src1 = p.first;
                int i = p.second;
                p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, i, std::vector<int>{});
                Data src2 = p.first;
                i = p.second;

                // set flags 
                if (src1.type == INT)
                {
                    if (src2.type == INT)
                    {
                        lessThanFlag = src1.i < src2.i;
                        equalFlag = src1.i == src2.i;
                        greaterThanFlag = src1.i > src2.i; 
                    }
                    else if (src2.type == FLOAT)
                    {
                        lessThanFlag = src1.i < src2.f;
                        equalFlag = src1.i == src2.f;
                        greaterThanFlag = src1.i > src2.f; 
                    }
                    else if (src2.type == CHAR)
                    {
                        lessThanFlag = src1.i < src2.c;
                        equalFlag = src1.i == src2.c;
                        greaterThanFlag = src1.i > src2.c; 
                    }
                }
                else if (src1.type == FLOAT)
                {
                    if (src2.type == INT)
                    {
                        lessThanFlag = src1.f < src2.i;
                        equalFlag = src1.f == src2.i;
                        greaterThanFlag = src1.f > src2.i; 
                    }
                    else if (src2.type == FLOAT)
                    {
                        lessThanFlag = src1.f < src2.f;
                        equalFlag = src1.f == src2.f;
                        greaterThanFlag = src1.f > src2.f; 
                    }
                    else if (src2.type == CHAR)
                    {
                        lessThanFlag = src1.f < src2.c;
                        equalFlag = src1.f == src2.c;
                        greaterThanFlag = src1.f > src2.c; 
                    }
                }
                else if (src1.type == CHAR)
                {
                    if (src2.type == INT)
                    {
                        lessThanFlag = src1.c < src2.i;
                        equalFlag = src1.c == src2.i;
                        greaterThanFlag = src1.c > src2.i; 
                    }
                    else if (src2.type == FLOAT)
                    {
                        lessThanFlag = src1.c < src2.f;
                        equalFlag = src1.c == src2.f;
                        greaterThanFlag = src1.c > src2.f; 
                    }
                    else if (src2.type == CHAR)
                    {
                        lessThanFlag = src1.c < src2.c;
                        equalFlag = src1.c == src2.c;
                        greaterThanFlag = src1.c > src2.c; 
                    }
                }
            }
            break;
            case OPCODE_JUMP:
            {
                // JUMP dest
                // unconditional jump 
                // move to jump point
                auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 0, std::vector<int>{});
                Data pointer = p.first;
                int i = p.second;

                instruction_pointer = pointer.i; 
            }
            break;
            case OPCODE_JUMPLT:
            {
                // JUMPLT dest
                // jump if less than flag is true
                if (lessThanFlag)
                {
                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 0, std::vector<int>{});
                    Data pointer = p.first;
                    int i = p.second;
                    
                    instruction_pointer = pointer.i; 
                }
            }
            break;
            case OPCODE_JUMPLE:
            {
                // JUMPLE dest
                // jump if less than or equal to flags are true 
                if (lessThanFlag || equalFlag)
                {
                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 0, std::vector<int>{});
                    Data pointer = p.first;
                    int i = p.second;
                    
                    instruction_pointer = pointer.i; 
                }
            }
            break;
            case OPCODE_JUMPEQ:
            {
                // JUMPEQ dest
                // jump if equal to flag is true 
                if (equalFlag)
                {
                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 0, std::vector<int>{});
                    Data pointer = p.first;
                    int i = p.second;
                    
                    instruction_pointer = pointer.i; 
                }
            }
            break;
            case OPCODE_JUMPNEQ:
            {
                // JUMPNEQ dest
                // jump if equal to flag is false 
                if (!equalFlag)
                {
                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 0, std::vector<int>{});
                    Data pointer = p.first;
                    int i = p.second;
                    
                    instruction_pointer = pointer.i; 
                }
            }
            break;
            case OPCODE_JUMPGE:
            {
                // JUMPGE dest
                // jump if greater than or equal to flags are true
                if (greaterThanFlag || equalFlag)
                {
                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 0, std::vector<int>{});
                    Data pointer = p.first;
                    int i = p.second;
                    
                    instruction_pointer = pointer.i; 
                }
            }
            break;
            case OPCODE_JUMPGT:
            {
                // JUMPGT dest
                // jump if greater than flag is true 
                if (greaterThanFlag)
                {
                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 0, std::vector<int>{});
                    Data pointer = p.first;
                    int i = p.second;
                    
                    instruction_pointer = pointer.i; 
                }
            }
            break;
            case OPCODE_EQUAL:
            {
                // EQUAL dest src1 src2 
                // Case 1: Dest is Memory
                if (params[0].i == MODE_MEMORY)
                {
                    // next 4 nums make up the pointer and offset
                    Data pmode = params[1];
                    Data pointer = params[2];
                    Data omode = params[3];
                    Data offset = params[4];
                    int address = getMemAddress(stack, scopes, heap, base_pointer, intToWord, pmode, pointer, omode, offset);

                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 5, std::vector<int>{});
                    Data src1 = p.first;
                    int i = p.second; 
                    p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, i, std::vector<int>{});
                    Data src2 = p.first;
                    i = p.second; 
                    
                    // perform op based on types 
                    if (src1.type == INT)
                    {
                        if (src2.type == INT)
                            heap.memory[address] = Data(src1.i == src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            heap.memory[address] = Data(src1.i == src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            heap.memory[address] = Data(src1.i == src2.c ? 1 : 0);
                    }
                    else if (src1.type == FLOAT)
                    {
                        if (src2.type == INT)
                            heap.memory[address] = Data(src1.f == src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            heap.memory[address] = Data(src1.f == src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            heap.memory[address] = Data(src1.f == src2.c ? 1 : 0);
                    }
                    else if (src1.type == CHAR)
                    {
                        if (src2.type == INT)
                            heap.memory[address] = Data(src1.c == src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            heap.memory[address] = Data(src1.c == src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            heap.memory[address] = Data(src1.c == src2.c ? 1 : 0);
                    }
                    else
                    {
                        std::cout << "Error: Invalid type" << std::endl;
                        exit (1);
                    }
                }
                // Case 2: Dest is Stack variable
                else if (params[0].i == MODE_STACK)
                {
                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 2, std::vector<int>{});
                    Data src1 = p.first;
                    int i = p.second; 
                    p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, i, std::vector<int>{});
                    Data src2 = p.first;
                    i = p.second; 
                    
                    // perform op based on types 
                    if (src1.type == INT)
                    {
                        if (src2.type == INT)
                            scopes[base_pointer][params[1].i] = Data(src1.i == src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            scopes[base_pointer][params[1].i] = Data(src1.i == src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            scopes[base_pointer][params[1].i] = Data(src1.i == src2.c ? 1 : 0);
                    }
                    else if (src1.type == FLOAT)
                    {
                        if (src2.type == INT)
                            scopes[base_pointer][params[1].i] = Data(src1.f == src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            scopes[base_pointer][params[1].i] = Data(src1.f == src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            scopes[base_pointer][params[1].i] = Data(src1.f == src2.c ? 1 : 0);
                    }
                    else if (src1.type == CHAR)
                    {
                        if (src2.type == INT)
                            scopes[base_pointer][params[1].i] = Data(src1.c == src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            scopes[base_pointer][params[1].i] = Data(src1.c == src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            scopes[base_pointer][params[1].i] = Data(src1.c == src2.c ? 1 : 0);
                    }
                    else
                    {
                        std::cout << "Error: Invalid type" << std::endl;
                        exit (1);
                    }
                }
                // Case 3: Dest is Invalid param type
                else
                {
                    std::cout << "Error: Dest should be memory or stack" << std::endl;
                    exit (1);
                }
            }
            break;
            case OPCODE_NEQUAL:
            {
                // NEQUAL dest src1 src2 
                // Case 1: Dest is Memory
                if (params[0].i == MODE_MEMORY)
                {
                    // next 4 nums make up the pointer and offset
                    Data pmode = params[1];
                    Data pointer = params[2];
                    Data omode = params[3];
                    Data offset = params[4];
                    int address = getMemAddress(stack, scopes, heap, base_pointer, intToWord, pmode, pointer, omode, offset);

                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 5, std::vector<int>{});
                    Data src1 = p.first;
                    int i = p.second; 
                    p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, i, std::vector<int>{});
                    Data src2 = p.first;
                    i = p.second; 
                    
                    // perform op based on types 
                    if (src1.type == INT)
                    {
                        if (src2.type == INT)
                            heap.memory[address] = Data(src1.i != src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            heap.memory[address] = Data(src1.i != src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            heap.memory[address] = Data(src1.i != src2.c ? 1 : 0);
                    }
                    else if (src1.type == FLOAT)
                    {
                        if (src2.type == INT)
                            heap.memory[address] = Data(src1.f != src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            heap.memory[address] = Data(src1.f != src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            heap.memory[address] = Data(src1.f != src2.c ? 1 : 0);
                    }
                    else if (src1.type == CHAR)
                    {
                        if (src2.type == INT)
                            heap.memory[address] = Data(src1.c != src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            heap.memory[address] = Data(src1.c != src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            heap.memory[address] = Data(src1.c != src2.c ? 1 : 0);
                    }
                    else
                    {
                        std::cout << "Error: Invalid type" << std::endl;
                        exit (1);
                    }
                }
                // Case 2: Dest is Stack variable
                else if (params[0].i == MODE_STACK)
                {
                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 2, std::vector<int>{});
                    Data src1 = p.first;
                    int i = p.second; 
                    p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, i, std::vector<int>{});
                    Data src2 = p.first;
                    i = p.second; 
                    
                    // perform op based on types 
                    if (src1.type == INT)
                    {
                        if (src2.type == INT)
                            scopes[base_pointer][params[1].i] = Data(src1.i != src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            scopes[base_pointer][params[1].i] = Data(src1.i != src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            scopes[base_pointer][params[1].i] = Data(src1.i != src2.c ? 1 : 0);
                    }
                    else if (src1.type == FLOAT)
                    {
                        if (src2.type == INT)
                            scopes[base_pointer][params[1].i] = Data(src1.f != src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            scopes[base_pointer][params[1].i] = Data(src1.f != src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            scopes[base_pointer][params[1].i] = Data(src1.f != src2.c ? 1 : 0);
                    }
                    else if (src1.type == CHAR)
                    {
                        if (src2.type == INT)
                            scopes[base_pointer][params[1].i] = Data(src1.c != src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            scopes[base_pointer][params[1].i] = Data(src1.c != src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            scopes[base_pointer][params[1].i] = Data(src1.c != src2.c ? 1 : 0);
                    }
                    else
                    {
                        std::cout << "Error: Invalid type" << std::endl;
                        exit (1);
                    }
                }
                // Case 3: Dest is Invalid param type
                else
                {
                    std::cout << "Error: Dest should be memory or stack" << std::endl;
                    exit (1);
                }
            }
            break;
            case OPCODE_LT:
            {
                // LT dest src1 src2 
                // dest = src1 < src2
                // Case 1: Dest is Memory
                if (params[0].i == MODE_MEMORY)
                {
                    // next 4 nums make up the pointer and offset
                    Data pmode = params[1];
                    Data pointer = params[2];
                    Data omode = params[3];
                    Data offset = params[4];
                    int address = getMemAddress(stack, scopes, heap, base_pointer, intToWord, pmode, pointer, omode, offset);

                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 5, std::vector<int>{});
                    Data src1 = p.first;
                    int i = p.second; 
                    p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, i, std::vector<int>{});
                    Data src2 = p.first;
                    i = p.second; 
                    
                    // perform op based on types 
                    if (src1.type == INT)
                    {
                        if (src2.type == INT)
                            heap.memory[address] = Data(src1.i < src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            heap.memory[address] = Data(src1.i < src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            heap.memory[address] = Data(src1.i < src2.c ? 1 : 0);
                    }
                    else if (src1.type == FLOAT)
                    {
                        if (src2.type == INT)
                            heap.memory[address] = Data(src1.f < src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            heap.memory[address] = Data(src1.f < src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            heap.memory[address] = Data(src1.f < src2.c ? 1 : 0);
                    }
                    else if (src1.type == CHAR)
                    {
                        if (src2.type == INT)
                            heap.memory[address] = Data(src1.c < src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            heap.memory[address] = Data(src1.c < src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            heap.memory[address] = Data(src1.c < src2.c ? 1 : 0);
                    }
                    else
                    {
                        std::cout << "Error: Invalid type" << std::endl;
                        exit (1);
                    }
                }
                // Case 2: Dest is Stack variable
                else if (params[0].i == MODE_STACK)
                {
                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 2, std::vector<int>{});
                    Data src1 = p.first;
                    int i = p.second; 
                    p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, i, std::vector<int>{});
                    Data src2 = p.first;
                    i = p.second; 
                    
                    // perform op based on types 
                    if (src1.type == INT)
                    {
                        if (src2.type == INT)
                            scopes[base_pointer][params[1].i] = Data(src1.i < src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            scopes[base_pointer][params[1].i] = Data(src1.i < src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            scopes[base_pointer][params[1].i] = Data(src1.i < src2.c ? 1 : 0);
                    }
                    else if (src1.type == FLOAT)
                    {
                        if (src2.type == INT)
                            scopes[base_pointer][params[1].i] = Data(src1.f < src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            scopes[base_pointer][params[1].i] = Data(src1.f < src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            scopes[base_pointer][params[1].i] = Data(src1.f < src2.c ? 1 : 0);
                    }
                    else if (src1.type == CHAR)
                    {
                        if (src2.type == INT)
                            scopes[base_pointer][params[1].i] = Data(src1.c < src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            scopes[base_pointer][params[1].i] = Data(src1.c < src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            scopes[base_pointer][params[1].i] = Data(src1.c < src2.c ? 1 : 0);
                    }
                    else
                    {
                        std::cout << "Error: Invalid type" << std::endl;
                        exit (1);
                    }
                }
                // Case 3: Dest is Invalid param type
                else
                {
                    std::cout << "Error: Dest should be memory or stack" << std::endl;
                    exit (1);
                }
            }
            break;
            case OPCODE_LE:
            {
                // LE dest src1 src2 
                // dest = src1 <= src2
                // Case 1: Dest is Memory
                if (params[0].i == MODE_MEMORY)
                {
                    // next 4 nums make up the pointer and offset
                    Data pmode = params[1];
                    Data pointer = params[2];
                    Data omode = params[3];
                    Data offset = params[4];
                    int address = getMemAddress(stack, scopes, heap, base_pointer, intToWord, pmode, pointer, omode, offset);

                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 5, std::vector<int>{});
                    Data src1 = p.first;
                    int i = p.second; 
                    p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, i, std::vector<int>{});
                    Data src2 = p.first;
                    i = p.second; 
                    
                    // perform op based on types 
                    if (src1.type == INT)
                    {
                        if (src2.type == INT)
                            heap.memory[address] = Data(src1.i <= src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            heap.memory[address] = Data(src1.i <= src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            heap.memory[address] = Data(src1.i <= src2.c ? 1 : 0);
                    }
                    else if (src1.type == FLOAT)
                    {
                        if (src2.type == INT)
                            heap.memory[address] = Data(src1.f <= src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            heap.memory[address] = Data(src1.f <= src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            heap.memory[address] = Data(src1.f <= src2.c ? 1 : 0);
                    }
                    else if (src1.type == CHAR)
                    {
                        if (src2.type == INT)
                            heap.memory[address] = Data(src1.c <= src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            heap.memory[address] = Data(src1.c <= src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            heap.memory[address] = Data(src1.c <= src2.c ? 1 : 0);
                    }
                    else
                    {
                        std::cout << "Error: Invalid type" << std::endl;
                        exit (1);
                    }
                }
                // Case 2: Dest is Stack variable
                else if (params[0].i == MODE_STACK)
                {
                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 2, std::vector<int>{});
                    Data src1 = p.first;
                    int i = p.second; 
                    p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, i, std::vector<int>{});
                    Data src2 = p.first;
                    i = p.second; 
                    
                    // perform op based on types 
                    if (src1.type == INT)
                    {
                        if (src2.type == INT)
                            scopes[base_pointer][params[1].i] = Data(src1.i <= src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            scopes[base_pointer][params[1].i] = Data(src1.i <= src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            scopes[base_pointer][params[1].i] = Data(src1.i <= src2.c ? 1 : 0);
                    }
                    else if (src1.type == FLOAT)
                    {
                        if (src2.type == INT)
                            scopes[base_pointer][params[1].i] = Data(src1.f <= src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            scopes[base_pointer][params[1].i] = Data(src1.f <= src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            scopes[base_pointer][params[1].i] = Data(src1.f <= src2.c ? 1 : 0);
                    }
                    else if (src1.type == CHAR)
                    {
                        if (src2.type == INT)
                            scopes[base_pointer][params[1].i] = Data(src1.c <= src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            scopes[base_pointer][params[1].i] = Data(src1.c <= src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            scopes[base_pointer][params[1].i] = Data(src1.c <= src2.c ? 1 : 0);
                    }
                    else
                    {
                        std::cout << "Error: Invalid type" << std::endl;
                        exit (1);
                    }
                }
                // Case 3: Dest is Invalid param type
                else
                {
                    std::cout << "Error: Dest should be memory or stack" << std::endl;
                    exit (1);
                }
            }
            break;
            case OPCODE_GT:
            {
                // GT dest src1 src2 
                // dest = src1 > src2
                // Case 1: Dest is Memory
                if (params[0].i == MODE_MEMORY)
                {
                    // next 4 nums make up the pointer and offset
                    Data pmode = params[1];
                    Data pointer = params[2];
                    Data omode = params[3];
                    Data offset = params[4];
                    int address = getMemAddress(stack, scopes, heap, base_pointer, intToWord, pmode, pointer, omode, offset);

                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 5, std::vector<int>{});
                    Data src1 = p.first;
                    int i = p.second; 
                    p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, i, std::vector<int>{});
                    Data src2 = p.first;
                    i = p.second; 
                    
                    // perform op based on types 
                    if (src1.type == INT)
                    {
                        if (src2.type == INT)
                            heap.memory[address] = Data(src1.i > src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            heap.memory[address] = Data(src1.i > src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            heap.memory[address] = Data(src1.i > src2.c ? 1 : 0);
                    }
                    else if (src1.type == FLOAT)
                    {
                        if (src2.type == INT)
                            heap.memory[address] = Data(src1.f > src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            heap.memory[address] = Data(src1.f > src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            heap.memory[address] = Data(src1.f > src2.c ? 1 : 0);
                    }
                    else if (src1.type == CHAR)
                    {
                        if (src2.type == INT)
                            heap.memory[address] = Data(src1.c > src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            heap.memory[address] = Data(src1.c > src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            heap.memory[address] = Data(src1.c > src2.c ? 1 : 0);
                    }
                    else
                    {
                        std::cout << "Error: Invalid type" << std::endl;
                        exit (1);
                    }
                }
                // Case 2: Dest is Stack variable
                else if (params[0].i == MODE_STACK)
                {
                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 2, std::vector<int>{});
                    Data src1 = p.first;
                    int i = p.second; 
                    p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, i, std::vector<int>{});
                    Data src2 = p.first;
                    i = p.second; 
                    
                    // perform op based on types 
                    if (src1.type == INT)
                    {
                        if (src2.type == INT)
                            scopes[base_pointer][params[1].i] = Data(src1.i > src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            scopes[base_pointer][params[1].i] = Data(src1.i > src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            scopes[base_pointer][params[1].i] = Data(src1.i > src2.c ? 1 : 0);
                    }
                    else if (src1.type == FLOAT)
                    {
                        if (src2.type == INT)
                            scopes[base_pointer][params[1].i] = Data(src1.f > src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            scopes[base_pointer][params[1].i] = Data(src1.f > src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            scopes[base_pointer][params[1].i] = Data(src1.f > src2.c ? 1 : 0);
                    }
                    else if (src1.type == CHAR)
                    {
                        if (src2.type == INT)
                            scopes[base_pointer][params[1].i] = Data(src1.c > src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            scopes[base_pointer][params[1].i] = Data(src1.c > src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            scopes[base_pointer][params[1].i] = Data(src1.c > src2.c ? 1 : 0);
                    }
                    else
                    {
                        std::cout << "Error: Invalid type" << std::endl;
                        exit (1);
                    }
                }
                // Case 3: Dest is Invalid param type
                else
                {
                    std::cout << "Error: Dest should be memory or stack" << std::endl;
                    exit (1);
                }
            }
            break;
            case OPCODE_GE:
            {
                // GE dest src1 src2 
                // dest = src1 >= src2
                // Case 1: Dest is Memory
                if (params[0].i == MODE_MEMORY)
                {
                    // next 4 nums make up the pointer and offset
                    Data pmode = params[1];
                    Data pointer = params[2];
                    Data omode = params[3];
                    Data offset = params[4];
                    int address = getMemAddress(stack, scopes, heap, base_pointer, intToWord, pmode, pointer, omode, offset);

                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 5, std::vector<int>{});
                    Data src1 = p.first;
                    int i = p.second; 
                    p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, i, std::vector<int>{});
                    Data src2 = p.first;
                    i = p.second; 
                    
                    // perform op based on types 
                    if (src1.type == INT)
                    {
                        if (src2.type == INT)
                            heap.memory[address] = Data(src1.i >= src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            heap.memory[address] = Data(src1.i >= src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            heap.memory[address] = Data(src1.i >= src2.c ? 1 : 0);
                    }
                    else if (src1.type == FLOAT)
                    {
                        if (src2.type == INT)
                            heap.memory[address] = Data(src1.f >= src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            heap.memory[address] = Data(src1.f >= src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            heap.memory[address] = Data(src1.f >= src2.c ? 1 : 0);
                    }
                    else if (src1.type == CHAR)
                    {
                        if (src2.type == INT)
                            heap.memory[address] = Data(src1.c >= src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            heap.memory[address] = Data(src1.c >= src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            heap.memory[address] = Data(src1.c >= src2.c ? 1 : 0);
                    }
                    else
                    {
                        std::cout << "Error: Invalid type" << std::endl;
                        exit (1);
                    }
                }
                // Case 2: Dest is Stack variable
                else if (params[0].i == MODE_STACK)
                {
                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 2, std::vector<int>{});
                    Data src1 = p.first;
                    int i = p.second; 
                    p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, i, std::vector<int>{});
                    Data src2 = p.first;
                    i = p.second; 
                    
                    // perform op based on types 
                    if (src1.type == INT)
                    {
                        if (src2.type == INT)
                            scopes[base_pointer][params[1].i] = Data(src1.i >= src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            scopes[base_pointer][params[1].i] = Data(src1.i >= src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            scopes[base_pointer][params[1].i] = Data(src1.i >= src2.c ? 1 : 0);
                    }
                    else if (src1.type == FLOAT)
                    {
                        if (src2.type == INT)
                            scopes[base_pointer][params[1].i] = Data(src1.f >= src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            scopes[base_pointer][params[1].i] = Data(src1.f >= src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            scopes[base_pointer][params[1].i] = Data(src1.f >= src2.c ? 1 : 0);
                    }
                    else if (src1.type == CHAR)
                    {
                        if (src2.type == INT)
                            scopes[base_pointer][params[1].i] = Data(src1.c >= src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            scopes[base_pointer][params[1].i] = Data(src1.c >= src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            scopes[base_pointer][params[1].i] = Data(src1.c >= src2.c ? 1 : 0);
                    }
                    else
                    {
                        std::cout << "Error: Invalid type" << std::endl;
                        exit (1);
                    }
                }
                // Case 3: Dest is Invalid param type
                else
                {
                    std::cout << "Error: Dest should be memory or stack" << std::endl;
                    exit (1);
                }
            }
            break;
            case OPCODE_AND:
            {
                // AND dest src1 src2 
                // dest = src1 && src2
                // Case 1: Dest is Memory
                if (params[0].i == MODE_MEMORY)
                {
                    // next 4 nums make up the pointer and offset
                    Data pmode = params[1];
                    Data pointer = params[2];
                    Data omode = params[3];
                    Data offset = params[4];
                    int address = getMemAddress(stack, scopes, heap, base_pointer, intToWord, pmode, pointer, omode, offset);

                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 5, std::vector<int>{});
                    Data src1 = p.first;
                    int i = p.second; 
                    p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, i, std::vector<int>{});
                    Data src2 = p.first;
                    i = p.second; 
                    
                    // perform op based on types 
                    if (src1.type == INT)
                    {
                        if (src2.type == INT)
                            heap.memory[address] = Data(src1.i && src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            heap.memory[address] = Data(src1.i && src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            heap.memory[address] = Data(src1.i && src2.c ? 1 : 0);
                    }
                    else if (src1.type == FLOAT)
                    {
                        if (src2.type == INT)
                            heap.memory[address] = Data(src1.f && src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            heap.memory[address] = Data(src1.f && src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            heap.memory[address] = Data(src1.f && src2.c ? 1 : 0);
                    }
                    else if (src1.type == CHAR)
                    {
                        if (src2.type == INT)
                            heap.memory[address] = Data(src1.c && src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            heap.memory[address] = Data(src1.c && src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            heap.memory[address] = Data(src1.c && src2.c ? 1 : 0);
                    }
                    else
                    {
                        std::cout << "Error: Invalid type" << std::endl;
                        exit (1);
                    }
                }
                // Case 2: Dest is Stack variable
                else if (params[0].i == MODE_STACK)
                {
                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 2, std::vector<int>{});
                    Data src1 = p.first;
                    int i = p.second; 
                    p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, i, std::vector<int>{});
                    Data src2 = p.first;
                    i = p.second; 
                    
                    // perform op based on types 
                    if (src1.type == INT)
                    {
                        if (src2.type == INT)
                            scopes[base_pointer][params[1].i] = Data(src1.i && src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            scopes[base_pointer][params[1].i] = Data(src1.i && src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            scopes[base_pointer][params[1].i] = Data(src1.i && src2.c ? 1 : 0);
                    }
                    else if (src1.type == FLOAT)
                    {
                        if (src2.type == INT)
                            scopes[base_pointer][params[1].i] = Data(src1.f && src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            scopes[base_pointer][params[1].i] = Data(src1.f && src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            scopes[base_pointer][params[1].i] = Data(src1.f && src2.c ? 1 : 0);
                    }
                    else if (src1.type == CHAR)
                    {
                        if (src2.type == INT)
                            scopes[base_pointer][params[1].i] = Data(src1.c && src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            scopes[base_pointer][params[1].i] = Data(src1.c && src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            scopes[base_pointer][params[1].i] = Data(src1.c && src2.c ? 1 : 0);
                    }
                    else
                    {
                        std::cout << "Error: Invalid type" << std::endl;
                        exit (1);
                    }
                }
                // Case 3: Dest is Invalid param type
                else
                {
                    std::cout << "Error: Dest should be memory or stack" << std::endl;
                    exit (1);
                }
            }
            break;
            case OPCODE_OR:
            {
                // OR dest src1 src2 
                // dest = src1 || src2
                // Case 1: Dest is Memory
                if (params[0].i == MODE_MEMORY)
                {
                    // next 4 nums make up the pointer and offset
                    Data pmode = params[1];
                    Data pointer = params[2];
                    Data omode = params[3];
                    Data offset = params[4];
                    int address = getMemAddress(stack, scopes, heap, base_pointer, intToWord, pmode, pointer, omode, offset);

                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 5, std::vector<int>{});
                    Data src1 = p.first;
                    int i = p.second; 
                    p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, i, std::vector<int>{});
                    Data src2 = p.first;
                    i = p.second; 
                    
                    // perform op based on types 
                    if (src1.type == INT)
                    {
                        if (src2.type == INT)
                            heap.memory[address] = Data(src1.i || src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            heap.memory[address] = Data(src1.i || src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            heap.memory[address] = Data(src1.i || src2.c ? 1 : 0);
                    }
                    else if (src1.type == FLOAT)
                    {
                        if (src2.type == INT)
                            heap.memory[address] = Data(src1.f || src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            heap.memory[address] = Data(src1.f || src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            heap.memory[address] = Data(src1.f || src2.c ? 1 : 0);
                    }
                    else if (src1.type == CHAR)
                    {
                        if (src2.type == INT)
                            heap.memory[address] = Data(src1.c || src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            heap.memory[address] = Data(src1.c || src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            heap.memory[address] = Data(src1.c || src2.c ? 1 : 0);
                    }
                    else
                    {
                        std::cout << "Error: Invalid type" << std::endl;
                        exit (1);
                    }
                }
                // Case 2: Dest is Stack variable
                else if (params[0].i == MODE_STACK)
                {
                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 2, std::vector<int>{});
                    Data src1 = p.first;
                    int i = p.second; 
                    p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, i, std::vector<int>{});
                    Data src2 = p.first;
                    i = p.second; 
                    
                    // perform op based on types 
                    if (src1.type == INT)
                    {
                        if (src2.type == INT)
                            scopes[base_pointer][params[1].i] = Data(src1.i || src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            scopes[base_pointer][params[1].i] = Data(src1.i || src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            scopes[base_pointer][params[1].i] = Data(src1.i || src2.c ? 1 : 0);
                    }
                    else if (src1.type == FLOAT)
                    {
                        if (src2.type == INT)
                            scopes[base_pointer][params[1].i] = Data(src1.f || src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            scopes[base_pointer][params[1].i] = Data(src1.f || src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            scopes[base_pointer][params[1].i] = Data(src1.f || src2.c ? 1 : 0);
                    }
                    else if (src1.type == CHAR)
                    {
                        if (src2.type == INT)
                            scopes[base_pointer][params[1].i] = Data(src1.c || src2.i ? 1 : 0);
                        else if (src2.type == FLOAT)
                            scopes[base_pointer][params[1].i] = Data(src1.c || src2.f ? 1 : 0);
                        else if (src2.type == CHAR)
                            scopes[base_pointer][params[1].i] = Data(src1.c || src2.c ? 1 : 0);
                    }
                    else
                    {
                        std::cout << "Error: Invalid type" << std::endl;
                        exit (1);
                    }
                }
                // Case 3: Dest is Invalid param type
                else
                {
                    std::cout << "Error: Dest should be memory or stack" << std::endl;
                    exit (1);
                }
            }
            break;
            case OPCODE_NOT:
            {
                // NOT dest src
                // dest = ~src
                // Case 1: Dest is Memory
                if (params[0].i == MODE_MEMORY)
                {
                    // next 4 nums make up the pointer and offset
                    Data pmode = params[1];
                    Data pointer = params[2];
                    Data omode = params[3];
                    Data offset = params[4];
                    int address = getMemAddress(stack, scopes, heap, base_pointer, intToWord, pmode, pointer, omode, offset);

                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 5, std::vector<int>{});
                    Data src1 = p.first;
                    int i = p.second; 
                    
                    // perform op based on types 
                    if (src1.type == INT)
                        heap.memory[address] = Data(src1.i == 0 ? 1 : 0);
                    else if (src1.type == FLOAT)
                        heap.memory[address] = Data(src1.f == 0 ? 1 : 0);
                    else if (src1.type == CHAR)
                        heap.memory[address] = Data(src1.c == 0 ? 1 : 0);
                    else
                    {
                        std::cout << "Error: Invalid type" << std::endl;
                        exit (1);
                    }
                }
                // Case 2: Dest is Stack variable
                else if (params[0].i == MODE_STACK)
                {
                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 2, std::vector<int>{});
                    Data src1 = p.first;
                    int i = p.second; 
                    
                    // perform op based on types 
                    if (src1.type == INT)
                        scopes[base_pointer][params[1].i] = Data(src1.i == 0 ? 1 : 0);
                    else if (src1.type == FLOAT)
                        scopes[base_pointer][params[1].i] = Data(src1.f == 0 ? 1 : 0);
                    else if (src1.type == CHAR)
                        scopes[base_pointer][params[1].i] = Data(src1.c == 0 ? 1 : 0);
                    else
                    {
                        std::cout << "Error: Invalid type" << std::endl;
                        exit (1);
                    }
                }
                // Case 3: Dest is Invalid param type
                else
                {
                    std::cout << "Error: Dest should be memory or stack" << std::endl;
                    exit (1);
                }
            }
            break;
            case OPCODE_PUSH:
            {
                // PUSH src 
                auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 0, std::vector<int>{});
                Data src1 = p.first;
                int i = p.second; 

                stack.push_back (src1);
            }
            break;
            case OPCODE_POP:
            {
                // POP dest 
                // ensure there is something to pop
                if (stack.size()-1 == base_pointer)
                {
                    std::cout << "Error: nothing to pop off of stack" << std::endl;
                    exit(1);
                }
                // Case 1: Dest is Memory
                if (params[0].i == MODE_MEMORY)
                {
                    // next 4 nums make up the pointer and offset
                    Data pmode = params[1];
                    Data pointer = params[2];
                    Data omode = params[3];
                    Data offset = params[4];
                    int address = getMemAddress(stack, scopes, heap, base_pointer, intToWord, pmode, pointer, omode, offset);

                    heap.memory[address] = stack.back ();
                    stack.pop_back ();
                }
                // Case 2: Dest is Stack variable
                else if (params[0].i == MODE_STACK)
                {
                    scopes[base_pointer][params[1].i] = stack.back ();
                    stack.pop_back ();   
                    
                }
                // Case 3: Dest is Invalid param type
                else
                {
                    std::cout << "Error: Dest should be memory or stack" << std::endl;
                    exit (1);
                }
            }
            break;
            case OPCODE_STACKGET:
            {
                // STACKGET dest offset 
                // Case1 : variable
                if (params[0].i == MODE_STACK)
                {
                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 2, std::vector<int>{});
                    Data offset = p.first;
                    int i = p.second; 
                    // -3 initially because
                    // first argument <--- base pointer - 3
                    // return address <--- base pointer - 2
                    // old base pointer <- base pointer - 1
                    // variables <-------- base pointer
                    scopes[base_pointer][params[1].i] = stack[base_pointer-3-offset.i];
                }
                // Case2 : memory
                else if (params[0].i == MODE_MEMORY)
                {
                    Data pmode = params[1];
                    Data pointer = params[2];
                    Data omode = params[3];
                    Data offset = params[4];
                    int address = getMemAddress(stack, scopes, heap, base_pointer, intToWord, pmode, pointer, omode, offset);
                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 5, std::vector<int>{});
                    Data off = p.first;
                    int i = p.second; 
                    // -3 initially because
                    // first argument <--- base pointer - 3
                    // return address <--- base pointer - 2
                    // old base pointer <- base pointer - 1
                    // variables <-------- base pointer
                    heap.memory[address] = stack[base_pointer-3-off.i];
                }
                // Case 3: Invalid param type
                else
                {
                    std::cout << "Error: Dest should be memory or stack" << std::endl;
                    exit(1);
                }
            }
            break;
            case OPCODE_FtoI:
            {
                // FTOI dest src 
                // Case1 : variable
                if (params[0].i == MODE_STACK)
                {
                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 2, std::vector<int>{});
                    Data src = p.first;
                    int i = p.second; 

                    // if (src.type != FLOAT)
                    // {
                    //     std::cout << "[FTOI] Error - src should be FLOAT" << std::endl;
                    //     exit(1);
                    // }
                    scopes[base_pointer][params[1].i] = (int) src.f;
                }
                // Case2 : memory
                else if (params[0].i == MODE_MEMORY)
                {
                    Data pmode = params[1];
                    Data pointer = params[2];
                    Data omode = params[3];
                    Data offset = params[4];
                    int address = getMemAddress(stack, scopes, heap, base_pointer, intToWord, pmode, pointer, omode, offset);
                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 5, std::vector<int>{});
                    Data src = p.first;
                    int i = p.second; 
                    
                    if (src.type != FLOAT)
                    {
                        std::cout << "[FTOI] Error - src should be FLOAT" << std::endl;
                        exit(1);
                    }
                    heap.memory[address] = (int) src.f;
                }
                // Case 3: Invalid param type
                else
                {
                    std::cout << "Error: Dest should be memory or stack" << std::endl;
                    exit(1);
                }
            }
            break;
            case OPCODE_ItoF:
            {
                // ITOF dest src 
                // Case1 : variable
                if (params[0].i == MODE_STACK)
                {
                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 2, std::vector<int>{});
                    Data src = p.first;
                    int i = p.second; 

                    if (src.type != INT)
                    {
                        std::cout << "[ITOF] Error - src should be INT" << std::endl;
                        exit(1);
                    }
                    scopes[base_pointer][params[1].i] = (float) src.i;
                }
                // Case2 : memory
                else if (params[0].i == MODE_MEMORY)
                {
                    Data pmode = params[1];
                    Data pointer = params[2];
                    Data omode = params[3];
                    Data offset = params[4];
                    int address = getMemAddress(stack, scopes, heap, base_pointer, intToWord, pmode, pointer, omode, offset);
                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 5, std::vector<int>{});
                    Data src = p.first;
                    int i = p.second; 
                    
                    if (src.type != INT)
                    {
                        std::cout << "[ITOF] Error - src should be INT" << std::endl;
                        exit(1);
                    }
                    heap.memory[address] = (float) src.i;
                }
                // Case 3: Invalid param type
                else
                {
                    std::cout << "Error: Dest should be memory or stack" << std::endl;
                    exit(1);
                }
            }
            break;
            case OPCODE_STRING:
            {
                // STRING dest src 
                // Case1 : variable
                if (params[0].i == MODE_STACK)
                {
                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 2, std::vector<int>{});
                    Data src = p.first;
                    int i = p.second; 

                    std::string str = src.toString();

                    // create string on heap
                    int ptr = heap.malloc (str.size());
                    // add characters to heap block
                    for (int i = 0; i < str.size(); ++i)
                        heap.memory[ptr+i] = str[i]; 
                    // give ptr to user 

                    scopes[base_pointer][params[1].i] = Data(ptr);
                }
                // Case2 : memory
                else if (params[0].i == MODE_MEMORY)
                {
                    Data pmode = params[1];
                    Data pointer = params[2];
                    Data omode = params[3];
                    Data offset = params[4];
                    int address = getMemAddress(stack, scopes, heap, base_pointer, intToWord, pmode, pointer, omode, offset);
                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 5, std::vector<int>{});
                    Data src = p.first;
                    int i = p.second; 

                    std::string str = src.toString();

                    // create string on heap
                    int ptr = heap.malloc (str.size());
                    // add characters to heap block
                    for (int i = 0; i < str.size(); ++i)
                        heap.memory[ptr+i] = str[i]; 
                    // give ptr to user 
                    heap.memory[address] = Data (ptr);
                }
                // Case 3: Invalid param type
                else
                {
                    std::cout << "Error: Dest should be memory or stack" << std::endl;
                    exit(1);
                }
            }
            break;
            case OPCODE_StoF:
            {
                // STOF dest src 
                // Case1 : variable
                if (params[0].i == MODE_STACK)
                {
                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 2, std::vector<int>{});
                    Data src = p.first;
                    int i = p.second; 
                    // ensure src is address (int)
                    if (src.type != INT)
                    {
                        std::cout << "Error STOF - src should be a memory address (int)" << std::endl;
                        exit (1);
                    }

                    // accumulate characters 
                    int size = heap.sizeOf (src.i);
                    char s[size];
                    for (int i = 0; i < size; ++i)
                        s[i] = heap.memory[src.i+i].c;
                    scopes[base_pointer][params[1].i] = Data((float) atof (s));
                }
                // Case2 : memory
                else if (params[0].i == MODE_MEMORY)
                {
                    Data pmode = params[1];
                    Data pointer = params[2];
                    Data omode = params[3];
                    Data offset = params[4];
                    int address = getMemAddress(stack, scopes, heap, base_pointer, intToWord, pmode, pointer, omode, offset);
                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 5, std::vector<int>{});
                    Data src = p.first;
                    int i = p.second; 
                    // ensure src is address (int)
                    if (src.type != INT)
                    {
                        std::cout << "Error STOF - src should be a memory address (int)" << std::endl;
                        exit (1);
                    }

                    // accumulate characters 
                    int size = heap.sizeOf (src.i);
                    char s[size];
                    for (int i = 0; i < size; ++i)
                        s[i] = heap.memory[src.i+i].c;
                    // give ptr to user 
                    heap.memory[address] = Data((float) atof (s));
                }
                // Case 3: Invalid param type
                else
                {
                    std::cout << "Error: Dest should be memory or stack" << std::endl;
                    exit(1);
                }
            }
            break;
            case OPCODE_StoI:
            {
                // STOI dest src 
                // Case1 : variable
                if (params[0].i == MODE_STACK)
                {
                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 2, std::vector<int>{});
                    Data src = p.first;
                    int i = p.second; 
                    // ensure src is address (int)
                    if (src.type != INT)
                    {
                        std::cout << "Error STOF - src should be a memory address (int)" << std::endl;
                        exit (1);
                    }

                    // accumulate characters 
                    int size = heap.sizeOf (src.i);
                    char s[size];
                    for (int i = 0; i < size; ++i)
                        s[i] = heap.memory[src.i+i].c;
                    scopes[base_pointer][params[1].i] = Data((int) atoi (s));
                }
                // Case2 : memory
                else if (params[0].i == MODE_MEMORY)
                {
                    Data pmode = params[1];
                    Data pointer = params[2];
                    Data omode = params[3];
                    Data offset = params[4];
                    int address = getMemAddress(stack, scopes, heap, base_pointer, intToWord, pmode, pointer, omode, offset);
                    auto p = getNextValue(stack, scopes, heap, base_pointer, intToWord, params, 5, std::vector<int>{});
                    Data src = p.first;
                    int i = p.second; 
                    // ensure src is address (int)
                    if (src.type != INT)
                    {
                        std::cout << "Error STOF - src should be a memory address (int)" << std::endl;
                        exit (1);
                    }

                    // accumulate characters 
                    int size = heap.sizeOf (src.i);
                    char s[size];
                    for (int i = 0; i < size; ++i)
                        s[i] = heap.memory[src.i+i].c;
                    // give ptr to user 
                    heap.memory[address] = Data((int) atoi (s));
                }
                // Case 3: Invalid param type
                else
                {
                    std::cout << "Error: Dest should be memory or stack" << std::endl;
                    exit(1);
                }
            }
            break;
            case OPCODE_HALT:
            {
                return; 
            //  jump point line
            }
            break;
            case MODE_JUMPPOINT:
            {
                
            }
            break; 
            default:
            {
                std::cout << "Error: '" << lines[instruction_pointer][0] << "' is not a valid command" << std::endl;
                exit(1);
            }

            }

            ++instruction_pointer;

        }


    }

    //--------------------------------------------------------------------



};


//========================================================================

int 
main (int argc, char* argv[])
{
    // fast IO ? hopefully 
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);

    // ensure file was inputted 
    if (argc < 2)
    {
        std::cout << "Please provide a file to interpret" << std::endl; 
        std::cout << argv[0] << " <file_name>" << std::endl; 
    }

    // read in code from file 
    std::string fileName = argv[1]; 
    std::ifstream file (fileName);
    std::stringstream buffer;
    buffer << file.rdbuf ();
    std::string code = buffer.str ();
    // execute code
    AmyAssemblyInterpreter interpreter (fileName, argc, argv);
    interpreter.execute (code);


}


