
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


- [ ] function capturing 
- [ ] add log level (debug already exists)
    amyc -l {info, debug, trace} ...
    amyc --log-level {info, debug, trace} ...
- [ ] cleaner way to load built-in functions

- [ ] prefix amy functions with _amyfunction_
    and builtin with _builtin_

- [ ] input(char[]) that prompts for a input


- [ ] named parameters 
    - print(float, precision=5) 

- [ ] negative mod is diff for python vs x86