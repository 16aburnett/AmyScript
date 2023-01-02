
need to install nasm 

nasm -felf64 hello.asm && ld hello.o && ./a.out

nasm -felf64 helloworld.asm && ld helloworld.o -o helloworld && ./helloworld


make && nasm -f elf64 helloworld.asm && ld helloworld.o -o helloworld -lc --dynamic-linker /lib/x86_64-linux-gnu/ld-linux-x86-64.so.2 && ./helloworld

make && nasm -f elf64 helloworld.asm && ld helloworld.o -o helloworld -lc --dynamic-linker /lib/x86_64-linux-gnu/ld-linux-x86-64.so.2 && echo "=> Running program" && ./helloworld

make && echo "Assembling..." && nasm -f elf64 helloworld.asm && echo "Linking..." && ld helloworld.o -o helloworld -lc --dynamic-linker /lib/x86_64-linux-gnu/ld-linux-x86-64.so.2 && echo "=> Running program" && ./helloworld && echo "exit success"


python3 ../amyScriptCompiler.py helloworld.amy -o helloworld.amy.assembly && python3 ../../amyasmi/amyAssemblyInterpreter.py helloworld.amy.assembly

python3 ../amyScriptCompiler.py testcpp.amy --target cpp -o testcpp.cpp && g++ testcpp.cpp -o testcpp && ./testcpp



https://stackoverflow.com/questions/6721041/how-can-you-code-the-c-operator-in-x86

when x then y else z

10+ hours - Saturday, Mar 26, 2022

Friday, Dec 2, 2022 - stayed up til 4:22am writing backend for python :)
Saturday, Dec 3, 2022 - stayed up til 3:00am implementing classes for python backend (and tweeks for x86)
Sunday Dec 4, 2022 - stayed up til 5:21am reimplementing a lot of the python backend to break up expressions into multiple lines so we can support pre/post incr/decr
Monday Dec 5, 2022 - stayed up til 3:44am (mon)- solved new aoc prob and made aoc runner and bug fixes - x86 is the only target that isnt working so I need to work on that
Tues Dec 6, 2022 - stayed up til 4:42am - working on bug fixes and stability - also added ability to check for eof and made strings null terminated so we can weed out sizeof to deprecate it

Sun Jan 1 2023  - stayed up til 6:26am jan 1
    been working most of the night/day
    separated aoc into new repo
    implemented functions and classes for cpp
    lot of stuff done today :)
    i need to sleep but dont want to :'(

- [ ] sizeof for x86
    - create a builtin array class 
    that stores pointer and array size?
    - maybe it should be user's responsibility?


- [ ] arr[:] syntax

- [ ] remove all unnecessary files

- [ ] separate amyasm to a separate repo
- [ ] targets should have default output file names

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

- [ ] extra keywords
    - and, or, not
    - c++ has support for this and so should i

- [ ] function capturing 
    function void setx [x] (int a)
    {
        x = a;
    }
    - adds reference to x

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
    - stdin for testing input


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


- [ ] 0xff (not yet), 0b0101 (not yet), 1e-3 (already supported)

ECX - Used as a loop counter. "this" pointer in C++.


- [ ] keep eyes out for stack alignment 
and rsp, -16 ; ensure stack is 16-byte aligned



instead of pointers
- address ptr = null;