AmyScript
===========

AmyScript is a middle-to-high-level programming language which looks somewhat similar to C, C++, or Java. It is still currently in development and the compiler exists in `code/amyc`. This is just a fun personal project and is not a serious language. The compiler is currently built just to be functional and does not have any optimizations.

Check out the documentation at https://16aburnett.github.io/AmyScript/website

Dependencies
============

- Python3.8 - The compiler is written in Python3.8.
- pyinstaller - used to build the compiler and interpreter 
- Bash terminal - for running the bash build scripts 

Building
========

Requires pyinstaller. This is still a work in progress. 
```
cd code/amyc
./build.sh
```
This will build the compiler and add a symlink to the executable in `$HOME/bin` so you should add `$HOME/bin` to your PATH if it isn't already. You can do that by adding the following to your `~/.bashrc`
```bash
export PATH="$HOME/bin:$PATH
```

Uninstalling
============
AmyScript does not install anything outside of the cloned repo other than the symlink in `$HOME/bin`. To uninstall, you can remove that symlink.
```bash
rm $HOME/bin/amyc
```

Compiling an AmyScript Program
==============================

Run the following command to compile a file 
```
amyc yourFile.amy
```
By default, the compiler compiles to a custom language called [AmyAssembly](https://github.com/16aburnett/AmyAssembly). If your code successfully compiles, you will get a .amyasm file including the compiled AmyAssembly. Check out the generated AmyAssembly code if you want! It's pretty cool!

Also, fun fact, this is a multi-target compiler meaning that you can compile the code to AmyAssembly, x86, python3, or C++.

There are multiple flags and arguments that you can give to the compiler. You can see a list of them by using the `--help` argument:
```bash
amyc --help
```

AmyScript Example Program
=========================

AmyScript code, 'helloworld.amy':
```cpp
function void printSubstring (char[] str, int start, int end)
{
    for (int i = start; i < end; ++i)
    {
        print (str[i]);
    }
}

char[] msg = "Hello, World!";

printSubstring (msg, 0, 5);
printSubstring (msg, 5, 13);

println ("");
```

Compile with:
```bash
amyc helloworld.amy --target amyasm -o helloworld.amyasm
```

Since we compiled to AmyAssembly, we can run the program with the following (as long as AmyAssembly is installed):
```bash
amyasmi helloworld.amyasm
```

Output:
```
Hello, World!
```
