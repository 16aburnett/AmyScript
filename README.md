AmyScript
===========

AmyScript is a low-level command-based programming language. 
The language has similarities with assembly while providing some higher-level features like variable names, control flow, and more to come. 
Currently, this language is a work in progress. 

Running the Program
===================
AmyScript is an interpreted language. You can write your code in a file and use the below command to execute your code. 
This implementation is written in python 3.8 so make sure you use python 3.8 or higher to run the interpreter.
```
$ python amy_lang.py yourFile.amy
```

Sample Program
==============
Below is a sample hello world program 
```
// You can delcare functions with FUNCTION
FUNCTION getPhrase
  RETURN "Hello, World!"
ENDFUNCTION getPhrase

// You can call functions with CALL
CALL getPhrase 
// When a function returns a value, 
// you can assign that value to a variable with RESPONSE
RESPONSE phrase
// PRINTLN will print the value of the variable with a newline
PRINTLN phrase
```
Which outputs
```
Hello, World!
```
