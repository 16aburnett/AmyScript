# The Amy Programming Language Memory Heap
# By Amy Burnett
# November 5 2020
##########################################################################
# Imports

##########################################################################

MEMORY_NULL = 0

class BlockHeader:
    def __init__(self, prevBlock, payloadSize:int, isAlloc:bool):
        self.prevBlock = prevBlock
        self.payloadSize = payloadSize
        self.isAlloc = isAlloc
    def __str__ (self):
        return (f"[{self.payloadSize}, {self.isAlloc}]")
    def __repr__ (self):
        return self.__str__ ()

class Heap:
    def __init__(self):
        initialSize = 100000
        self.memory = [0 for _ in range(initialSize)]
        # set up first free block
        # mem[0] is reserved for NULLPTR
        self.memory[1] = BlockHeader(None, initialSize-2, False)
        self.allocatedMemory = 0

    def malloc(self, size:int) -> int:
        """allocates space for given size and returns the pointer to 
        the starting position"""
        # Search for sufficient mem block
        i = 1
        header = None
        while i < len(self.memory):
            # get header
            header = self.memory[i]
            # ensure it is free
            if header.isAlloc:
                i += header.payloadSize + 1
                continue
            # if sufficient 
            if header.payloadSize == size:
                # allocate this block
                header.isAlloc = True
                self.allocatedMemory += header.payloadSize
                # return pointer to first payload pos
                return i + 1
            # if sufficient
            if header.payloadSize > size:
                # split payload
                secondPayload = header.payloadSize - size - 1
                secondAddress = i+size+1
                # modify this payload
                header.payloadSize = size
                header.isAlloc = True
                self.allocatedMemory += header.payloadSize
                # if second split has >0 payload
                # *** removed if because caused error 
                # if secondPayload > 0:
                    # create new payload
                self.memory[secondAddress] = BlockHeader(header, secondPayload, False)
                # coalesce 
                self.coallese(secondAddress)
                # assign second split's next's prev to the second split
                if secondAddress+secondPayload+1 < len(self.memory):
                    self.memory[secondAddress+secondPayload+1].prevBlock = self.memory[secondAddress]
                # ****
                # return pointer to first payload pos
                return i + 1
            i += header.payloadSize + 1
        # Reachs here if no sufficient free blocks were found
        # Lets add one
        self.memory += [BlockHeader(header, size, True)]
        self.memory += [0 for _ in range(size)]
        self.allocatedMemory += size
        # return pointer to first payload pos
        return i + 1

    def free(self, address:int):
        """Frees the block containing the address"""
        self.memory[address-1].isAlloc = False
        self.allocatedMemory -= self.memory[address-1].payloadSize
        self.coallese(address-1)
    
    def coallese(self, address:int):
        """
        Merges the free block at given address with adjacent free blocks
        - allocated blocks are left unchanged
        """
        # combine with free block after
        nextBlockAddr = address+self.memory[address].payloadSize+1
        if nextBlockAddr < len(self.memory) and not self.memory[nextBlockAddr].isAlloc:
            # clear second split
            temp = self.memory[nextBlockAddr].payloadSize
            self.memory[nextBlockAddr] = 0
            # add space to this block
            # + 1 for the space that used to have the header
            self.memory[address].payloadSize += temp+1
            # assign this to the prev of the next header
            newNextBlockAddr = address+self.memory[address].payloadSize+1
            if newNextBlockAddr < len(self.memory):
                self.memory[newNextBlockAddr].prevBlock = self.memory[address]
        # Combine with free block before
        if self.memory[address].prevBlock != None and not self.memory[address].prevBlock.isAlloc:
            # add this space to the prev block payload
            self.memory[address].prevBlock.payloadSize += 1+self.memory[address].payloadSize
            # assign this next to the prev
            # if there is a next
            if address+self.memory[address].payloadSize+1 < len(self.memory):
                self.memory[address+self.memory[address].payloadSize+1].prevBlock = self.memory[address].prevBlock
            # delete header
            self.memory[address] = 0

    def sizeof(self, address):
        """Returns the payload size for a given pointer

        Pre-condition: pointer must be allocated and not offset 
        from the start of the block
        """
        return self.memory[address-1].payloadSize




def printheap(heap):
    for i in range(len(heap.memory)):
        if isinstance(heap.memory[i], BlockHeader):
            print(f"{i} {heap.memory[i].payloadSize} {heap.memory[i].isAlloc}")
            # if heap.memory[i].prevBlock != None:
            #     print(f"\t{heap.memory[i].prevBlock.payloadSize} {heap.memory[i].prevBlock.isAlloc}")
        else:
            print(f"{i} {heap.memory[i]}")


def sampleRun():
    heap = Heap()

    printheap(heap)
    print("======================")
    print("Malloc 6")
    a = heap.malloc(6)
    printheap(heap)
    print("pointer -> ", a)
    print("======================")
    print("Malloc 3")
    b = heap.malloc(3)
    printheap(heap)
    print("pointer -> ", b)
    print("======================")
    print("Malloc 5")
    c = heap.malloc(5)
    printheap(heap)
    print("pointer -> ", c)
    print("======================")
    print("Free A")
    heap.free(a)
    printheap(heap)
    print("======================")
    print("Malloc 3")
    d = heap.malloc(3)
    printheap(heap)
    print("pointer -> ", d)
    print("======================")
    print("Free D")
    heap.free(d)
    printheap(heap)
    print("======================")
    print("Free B")
    heap.free(b)
    printheap(heap)
    print("======================")
    print("Malloc 3")
    a = heap.malloc(3)
    printheap(heap)
    print("pointer -> ", a)
    print("======================")
    print("Malloc 6")
    e = heap.malloc(6)
    printheap(heap)
    print("pointer -> ", e)
    print("======================")
    print("Free A")
    heap.free(a)
    printheap(heap)
    print("======================")
    print("Free C")
    heap.free(c)
    printheap(heap)
    print("======================")
    print("Free e")
    heap.free(e)
    printheap(heap)
    print("======================")
