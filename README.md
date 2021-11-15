AmyScript
===========

AmyScript is a middle-to-high-level programming language. It is still currently in development and the compiler exists in `code/amyc`. The expectation is that AmyScript is compiled to AmyAssembly which will then be interpreted. 

Check out the documentation at https://16aburnett.github.io/AmyScript/website

AmyAssembly is a low-level command-based programming language. 
The language is similar to assembly with some differences like variables instead of registers. 
The interpreter exists in `code/amyasmi`

Dependencies
============

- Python3.8 - Both the interpreter and compiler are written in Python3.8.
- pyinstaller - used to build the compiler and interpreter 
- Bash terminal - for running the bash build scripts 

Building Tools
==============

Requires pyinstaller. This is still a work in progress. 
```
source install.sh
```
this will build the compiler and interpreter and add them to the PATH. Note, when you quit out of the terminal, you will need to source the install again to add the compiler and interpreter to the PATH. 

Compiling AmyScript to AmyAssembly
==================================

Run the following command to compile a file 
```
$ amyc yourFile.amy
```
If your code successfully compiles, you will get a .assembly file including the compiled AmyAssembly. Check out the AmyAssembly if you want! It's pretty cool!

AmyScript Example Program
=========================

AmyScript code:
```
function void printSubstring (char[] str, int start, int end)
{
    for (int i = start; i < end; ++i)
    {
        printChar (str[i]);
    }
}

char[] msg = "Hello, World!";

printSubstring (msg, 0, 5);
printSubstring (msg, 5, 13);

println ("");
```
Output:
```
Hello, World!
```


Running An AmyAssembly Program
==============================
AmyAssembly can be executed using the AmyAssembly Interpreter (amyasmi).

Documentation coming soon. 
```
$ amyasmi yourFile.amy.assembly
```

Sample AmyAssembly Program
==========================
Below is a sample hello world program 
```
// 'Simple' AmyAssembly hello world program 
// By Amy Burnett
//========================================================================

// start at main
    jump main

//========================================================================
// Returns a customary phrase stored on the heap
getCustomaryPhraseFromHeap:
    malloc phrase 13
    assign phrase[0] 'H' 
    assign phrase[1] 'e'
    assign phrase[2] 'l'
    assign phrase[3] 'l'
    assign phrase[4] 'o'
    assign phrase[5] ','
    assign phrase[6] ' '
    assign phrase[7] 'W'
    assign phrase[8] 'o'
    assign phrase[9] 'r'
    assign phrase[10] 'l'
    assign phrase[11] 'd'
    assign phrase[12] '!'
    return phrase

//========================================================================

main:
    call getCustomaryPhraseFromHeap
    // grab the return value of the previous call
    response msg 
    // loop through phrase and print out 
    assign i 0
while:
    // condition
    cmp i 13
    jge endwhile
    // body 
    print msg[i]
    // update
    add i i 1
    // repeat
    jump while
endwhile:
    println 
    free msg 
    halt
```
Which outputs
```
Hello, World!
```
