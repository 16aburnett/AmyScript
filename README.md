AmyScript
===========

AmyScript is a middle-to-high-level programming language. It is still currently in development and the compiler exists in code/highlevel. The expectation is that AmyScript is compiled to AmyAssembly which will then be interpreted. 

Check out the documentation at https://16aburnett.github.io/AmyScript/website

AmyAssembly is a low-level command-based programming language. 
The language is similar to assembly with some differences like variable amounts of registers. 

Compiling AmyScript to AmyAssembly
==================================
to compile an AmyScript file, navigate to the highlevel directory which is where the compiler (and built-in library code) is located. 

Run the following command to compile a file 
```
$ python3 driver.py yourFile.amy
```
If your code successfully compiles, you will get a .assembly file including the compiled AmyAssembly. Check out the AmyAssembly if you want! It's pretty cool!

Running An AmyAssembly Program
==============================
AmyAssembly is an interpreted language. You can write your code in a file and use the below command to execute it (or use the AmyAssembly generated from the AmyScript compiler). 
This implementation is written in python 3.8 so make sure you use python 3.8 or higher to run the interpreter.
Documentation coming soon. 
```
$ python3 amy_lang.py yourFile.amy.assembly
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
