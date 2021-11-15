// The Amy Assembly Programming Language memory manager
// Author: Amy Burnett
// October 29 2021
//========================================================================

#ifndef MEMORY_H
#define MEMORY_H

//========================================================================
// Includes 

#include <vector>
#include <unordered_map>

#include "util.hpp"

//========================================================================

const int INITIAL_CAPACITY = 100000000;
const int MEMORY_NULL = 0;

//========================================================================

class BlockHeader
{
public:
    BlockHeader* prevBlock;
    int payloadSize;
    bool isAlloc;
    int address; 

    BlockHeader ();

    BlockHeader (BlockHeader* _prevBlock, int _payloadSize, bool _isAlloc, int address);

};

//========================================================================

class Heap
{
public:
    std::unordered_map<int, BlockHeader> blockHeaders; 
    std::vector<Data> memory;

    Heap ();

    int 
    malloc (int size);

    int 
    free (int address);

    int 
    coalesce (int address);

    int 
    sizeOf (int address);

};

//========================================================================

void
printheap (Heap heap);

//========================================================================

void
sampleRun ();

//========================================================================

#endif