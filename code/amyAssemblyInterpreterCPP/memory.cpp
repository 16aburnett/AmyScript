// The Amy Assembly Programming Language memory manager
// Author: Amy Burnett
// October 29 2021
//========================================================================
// Includes 

#include <iostream>
#include <vector>
#include <unordered_map>

#include "memory.hpp"

//========================================================================

BlockHeader::BlockHeader ()
{
    prevBlock = nullptr;
    payloadSize = 0;
    isAlloc = false;
    address = 0;
}

//========================================================================

BlockHeader::BlockHeader (BlockHeader* _prevBlock, int _payloadSize, bool _isAlloc, int _address)
{
    prevBlock = _prevBlock;
    payloadSize = _payloadSize;
    isAlloc = _isAlloc;
    address = _address;
}

//========================================================================

Heap::Heap ()
{
    memory = std::vector<Data> (INITIAL_CAPACITY);
    // set up first free block 
    blockHeaders[1] = BlockHeader (nullptr, INITIAL_CAPACITY-2, false, 1);
    // mem[0] is reserved for NULLPTR
}

//========================================================================
// allocates space for given size and returns the pointer to 
//    the starting position

int 
Heap::malloc (int size)
{
    // Search for sufficient mem block
    int i = 1;
    BlockHeader* header = nullptr; 
    while (i < memory.size())
    {
        // get header
        header = &blockHeaders[i];
        // ensure it is free
        if (header->isAlloc)
        {
            i += header->payloadSize + 1;
            continue;
        }
        // if sufficient 
        if (header->payloadSize == size)
        {
            // allocate 
            header->isAlloc = true; 
            // return pointer to first payload pos
            return i + 1;
        }
        // if sufficient
        if (header->payloadSize > size)
        {
            // split payload
            int secondPayload = header->payloadSize - size - 1;
            int secondAddress = i+size+1;
            // modify this payload
            header->payloadSize = size;
            header->isAlloc = true; 
            // if second split has >0 payload
            // *** removed if because caused error 
            // if secondPayload > 0:
                // create new payload
            // create new payload
            blockHeaders[secondAddress] = BlockHeader(header, secondPayload, false, secondAddress);
            memory[secondAddress] = Data('x');
            // assign second split's next's prev to the second split
            if (secondAddress+secondPayload+1 < memory.size())
                blockHeaders[secondAddress+secondPayload+1].prevBlock = &blockHeaders[secondAddress];
            // coalesce 
            coalesce(secondAddress);
            // ****
            // return pointer to first payload pos
            return i + 1;
        }
        i += header->payloadSize + 1;
    }
    // Reachs here if no sufficient free blocks were found
    // Lets add one
    memory.resize (memory.size() + size+1); // plus one for header
    blockHeaders[i] = BlockHeader(header, size, true, i);
    memory[i] = Data('x');
    // return pointer to first payload pos
    return i + 1;
}

//========================================================================
// Frees the block containing the address

int 
Heap::free (int address)
{
    blockHeaders[address-1].isAlloc = false;
    coalesce (address-1);
}

//========================================================================
// Merges the free block at given address with
//   adjacent free blocks

int 
Heap::coalesce (int address)
{
    // combine with free block after
    int nextBlockAddr = address + blockHeaders[address].payloadSize + 1;
    if (nextBlockAddr < memory.size() && !blockHeaders[nextBlockAddr].isAlloc)
    {
        // clear second block
        int temp = blockHeaders[nextBlockAddr].payloadSize;
        blockHeaders.erase (nextBlockAddr);
        memory[nextBlockAddr].i = 0;
        // add space to this block
        // + 1 for the space that used to have the header
        blockHeaders[address].payloadSize += temp+1;
        // assign this to the prev of the next header
        int newNextBlockAddr = address+blockHeaders[address].payloadSize+1; // +1 for this blockheader
        if (newNextBlockAddr < memory.size())
            blockHeaders[newNextBlockAddr].prevBlock = &blockHeaders[address];
    }
    // Combine with free block before
    if (blockHeaders[address].prevBlock != nullptr && !blockHeaders[address].prevBlock->isAlloc)
    {
        // add this space to the prev block payload
        blockHeaders[address].prevBlock->payloadSize += 1 + blockHeaders[address].payloadSize;
        // assign this next to the prev
        // if there is a next
        if (address + blockHeaders[address].payloadSize + 1 < memory.size())
            blockHeaders[address+blockHeaders[address].payloadSize+1].prevBlock = blockHeaders[address].prevBlock;
        // delete header
        blockHeaders.erase (address);
        memory[address].i = 0;
    }
}

//========================================================================
// Returns the payload size for a given pointer
// Pre-condition: pointer must be allocated and not offset 
//   from the start of the block
int 
Heap::sizeOf (int address)
{
    return blockHeaders[address-1].payloadSize;
}

//========================================================================

void
printheap (Heap heap)
{
    for (int i = 0; i < heap.memory.size(); ++i)
    {
        // check if i is a block
        if (heap.blockHeaders.find(i) != heap.blockHeaders.end())
            std::cout << i << " -> " << heap.blockHeaders[i].payloadSize << " " << heap.blockHeaders[i].isAlloc << std::endl;
        else
            std::cout << i << " " << heap.memory[i].toString() << std::endl;
    }
}

//========================================================================

void
sampleRun ()
{
    Heap heap; 

    printheap(heap);
    std::cout << "======================" << std::endl;
    std::cout << "Malloc 6" << std::endl;
    int a = heap.malloc(6);
    printheap(heap);
    std::cout << "pointer -> " << a << std::endl;
    std::cout << "======================" << std::endl;
    std::cout << "Malloc 3" << std::endl;
    int b = heap.malloc(3);
    printheap(heap);
    std::cout << "pointer -> " << b << std::endl;
    std::cout << "======================" << std::endl;
    std::cout << "Malloc 5" << std::endl;
    int c = heap.malloc(5);
    printheap(heap);
    std::cout << "pointer -> " << c << std::endl;
    heap.memory[c+0] = 'h';
    heap.memory[c+1] = 'e';
    heap.memory[c+2] = 'l';
    heap.memory[c+3] = 'l';
    heap.memory[c+4] = 'o';
    std::cout << "======================" << std::endl;
    std::cout << "Free A" << std::endl;
    heap.free(a);
    printheap(heap);
    std::cout << "======================" << std::endl;
    std::cout << "Malloc 3" << std::endl;
    int d = heap.malloc(3);
    printheap(heap);
    std::cout << "pointer -> " << d << std::endl;
    std::cout << "======================" << std::endl;
    std::cout << "Free D" << std::endl;
    heap.free(d);
    printheap(heap);
    std::cout << "======================" << std::endl;
    std::cout << "Free B" << std::endl;
    heap.free(b);
    printheap(heap);
    std::cout << "======================" << std::endl;
    std::cout << "Malloc 3" << std::endl;
    a = heap.malloc(3);
    printheap(heap);
    std::cout << "pointer -> " << a << std::endl;
    std::cout << "======================" << std::endl;
    std::cout << "Malloc 6" << std::endl;
    int e = heap.malloc(6);
    printheap(heap);
    std::cout << "pointer -> " << e << std::endl;
    std::cout << "======================" << std::endl;
    std::cout << "Free A" << std::endl;
    heap.free(a);
    printheap(heap);
    std::cout << "======================" << std::endl;
    std::cout << "Free C" << std::endl;
    heap.free(c);
    printheap(heap);
    std::cout << "======================" << std::endl;
    std::cout << "Free e" << std::endl;
    heap.free(e);
    printheap(heap);
    std::cout << "======================" << std::endl;
}





   

 
   