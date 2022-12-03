
need to install nasm 

nasm -felf64 hello.asm && ld hello.o && ./a.out

nasm -felf64 helloworld.asm && ld helloworld.o -o helloworld && ./helloworld


make && nasm -f elf64 helloworld.asm && ld helloworld.o -o helloworld -lc --dynamic-linker /lib/x86_64-linux-gnu/ld-linux-x86-64.so.2 && ./helloworld

make && nasm -f elf64 helloworld.asm && ld helloworld.o -o helloworld -lc --dynamic-linker /lib/x86_64-linux-gnu/ld-linux-x86-64.so.2 && echo "=> Running program" && ./helloworld

make && echo "Assembling..." && nasm -f elf64 helloworld.asm && echo "Linking..." && ld helloworld.o -o helloworld -lc --dynamic-linker /lib/x86_64-linux-gnu/ld-linux-x86-64.so.2 && echo "=> Running program" && ./helloworld && echo "exit success"


python3 ../amyScriptCompiler.py helloworld.amy -o helloworld.amy.assembly && python3 ../../amyasmi/amyAssemblyInterpreter.py helloworld.amy.assembly




https://stackoverflow.com/questions/6721041/how-can-you-code-the-c-operator-in-x86

when x then y else z

10+ hours - Saturday, Mar 26, 2022

Friday, Dec 2, 2022 - stayed up til 4:22am writing backend for python :)

- [ ] backend to python
- [ ] backend to c++

- [ ] exponent operator **
- [ ] pointer syntax - I really dislike using * for pointers
    - maybe use & 
    int& arr = ???
    - or address type?

- [ ] semantic - 

- [ ] type creation system
    - typedef Number = int | float ???
    https://docs.julialang.org/en/v1/manual/types/

- [ ] stack vs heap - we really need this
    - arrays are static size so we can just allocate stack space for the array
    - this is really rooted in amyasm garbage

- [ ] operator overloading

- [ ] function capturing 
- [ ] add log level (debug already exists)
    amyc -l {info, debug, trace} ...
    amyc --log-level {info, debug, trace} ...
- [ ] cleaner way to load built-in functions

- [ ] prefix amy functions with _amyfunction_
    and builtin with _builtin_

- [ ] input(char[]) that prompts for a input

- [ ] change input() to getline or something

- [ ] named parameters 
    - print(float, precision=5) 

- [ ] negative mod is diff for python vs x86


- [ ] massive update to documention!
    - revamp codeblocks
    - admonitions
    - the works
    - syntax highlighting
    - amyasm docs
    - compiler docs - talk about targets (amyasm, x86, python)


- [ ] change amyscript to amy++
    - we need to make a higher level language than this


- [ ] build my own unittest framework
    - python script that creates amyscript files
    - then compiles them 
    - ensures that it compiles
    - then runs it on x86 
    - ensure the stdout value is correct
    - then runs it on amyasm 
    - ensure the stdout value is correct


- [ ] 0xff, 0b0101

ECX - Used as a loop counter. "this" pointer in C++.


- [ ] keep eyes out for stack alignment 
and rsp, -16 ; ensure stack is 16-byte aligned



instead of pointers
- address ptr = null;