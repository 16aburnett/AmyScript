

import os
import subprocess
from enum import Enum 

# GIVEN 
# WHEN 
# THEN



class TestTarget (Enum):
    AMYASM = 0
    X86 = 1
    PYTHON = 2
    CPP = 3
    ALL = 4 # tests all targets

# expectedOutputX86 - this is the expected output to match with the stdout 
#   from running with target X86.
#   if this is None, then the default expectedOutput is used for X86 tests
# expectedOutputAMYASM - this is the expected output to match with the stdout 
#   from running with target AMYASM.
#   if this is None, then the default expectedOutput is used for AMYASM tests
# expectedOutput - the default expected output. 
# expectedCompilerOutput - this will be matched against the compiler output,
#   if this string is not found in the compiler output, then the test will fail.
#   this is helpful for testing cases that should fail to compile. See the shouldCompile test option.
# shouldCompile - if set to true, then the following test will fail if the 
#   code fails to compile. if set to false, then the following test will fail
#   if the code compiles without error. 
# 
#   
class Test:
    def __init__(self, 
        name:str, 
        code:str="", 
        expectedOutput:str="", 
        expectedOutputAMYASM:str=None, 
        expectedOutputX86:str=None, 
        expectedOutputPython:str=None,
        expectedOutputCPP:str=None,
        expectedCompilerOutput:str=None,
        shouldCompile:bool=True
    ):
        self.name = name
        self.code = code
        self.expectedOutput = expectedOutput
        self.expectedOutputAMYASM = expectedOutputAMYASM if expectedOutputAMYASM != None else expectedOutput
        self.expectedOutputX86    = expectedOutputX86    if expectedOutputX86    != None else expectedOutput
        self.expectedOutputPython = expectedOutputPython if expectedOutputPython != None else expectedOutput
        self.expectedOutputCPP    = expectedOutputCPP    if expectedOutputCPP    != None else expectedOutput
        self.expectedCompilerOutput = expectedCompilerOutput
        self.shouldCompile = shouldCompile

class MultiFileTest (Test):
    def __init__(self, 
        name: str, 
        code: str = "", 
        expectedOutput: str = "", 
        expectedOutputAMYASM: str = None, 
        expectedOutputX86: str = None, 
        expectedOutputPython: str = None, 
        expectedOutputCPP:str=None,
        expectedCompilerOutput: str = None, 
        shouldCompile: bool = True
    ):
        super().__init__(name, code, expectedOutput, expectedOutputAMYASM, expectedOutputX86, expectedOutputPython, expectedOutputCPP, expectedCompilerOutput, shouldCompile)

class TestGroup:
    def __init__(self, name:str, sharedCode:str="", tests:list=[]):
        self.name = name
        self.sharedCode = sharedCode
        self.tests = tests

# returns true if test passes, false otherwise
# if test fails, it also prints the error information
# def runAndCheck (test, code:str, testTarget:TestTarget, level:int, groupChain:str=""):
#     # combine shared code with this test's code
#     fullCode = code + test.code

#     if testTarget == TestTarget.AMYASM:
#         # compile the code
#         os.system (f'cat > test_data/test.amy <<EOF \n{fullCode}\nEOF')
#         compilerOutput = subprocess.run ([f'python3', '../amyc/amyScriptCompiler.py', 'test_data/test.amy', '--target', 'amyasm', '-o', 'test_data/test.amy.assembly'], capture_output=True, text=True)
#         print (compilerOutput)

#         # 1. Failed to Compile when expecting fail

#         # 2. Failed to Compile when expecting success

#         # 2. Compiled when expecting fail

#         # 3. Compiled when expecting success

#         # 3a. Run program 

#         # 3b. correct result

#         # 3c. incorrect result


#         # ensure it compiled
#         if compilerOutput.returncode != 0:
#             # check if 
#             pass
#         # code compiles
#         else:
#             # run the code
#             result = subprocess.run (['python3', '../amyasmi/amyAssemblyInterpreter.py', 'test_data/test.amy.assembly'], capture_output=True, text=True)
#             # ensure it was successful
#             wasTestSuccessful = result.stdout == test.expectedOutputAMYASM
#             if not wasTestSuccessful:
#                 print (f"=== FAILED =====================")
#                 print (f"Test Group: {groupChain}")
#                 print (f"Test: {test.name}")
#                 print (f"Target: {TestTarget.AMYASM}")
#                 print ("Code:")
#                 print (fullCode)
#                 print ("Expected Output:")
#                 print (test.expectedOutputAMYASM)
#                 print ("Actual Output:")
#                 print (result.stdout)
#                 print (f"================================")
#             else:
#                 numSuccessfulTests += 1
#         numTests += 1

# returns [numSuccessfulTests, numTests]
def runTest_helper (test, code:str, testTarget:TestTarget, level:int, groupChain:str="", shouldBreakOnFail=False):
    if isinstance(test, TestGroup):

        for i in range(level):
            print ('| ', end='')
        print ('v ', end='')
        print (test.name)

        numSuccessful = 0
        numTests = 0
        for subtest in test.tests:
            [numSuccessfulSubtests, numSubtests] = runTest_helper (subtest, code + test.sharedCode, testTarget, level+1, f"{groupChain} > {test.name}", shouldBreakOnFail=shouldBreakOnFail)
            numSuccessful += numSuccessfulSubtests
            numTests += numSubtests

        for i in range(level):
            print ('| ', end='')
        print ('^ ', end='')
        print (test.name, numSuccessful, '/', numTests, "passed")

        return [numSuccessful, numTests]
    elif isinstance(test, Test):

        fullCode = code + test.code

        numTests = 0
        numSuccessfulTests = 0

        # run the code
        if testTarget == TestTarget.AMYASM or testTarget == TestTarget.ALL:
            # compile the code
            os.system (f'cat > test_data/test.amy <<EOF \n{fullCode}\nEOF')
            compilerOutput = subprocess.run ([f'python3', '../amyc/amyScriptCompiler.py', 'test_data/test.amy', '--target', 'amyasm', '-o', 'test_data/test.amy.assembly'], capture_output=True, text=True)

            isCompiled = (compilerOutput.returncode == 0)

            # 1. Failed to Compile when expecting fail
            if not isCompiled and not test.shouldCompile:
                # ensure expectedCompilerOutput exists
                if test.expectedCompilerOutput not in compilerOutput.stdout:
                    print (f"=== FAILED =====================")
                    print (f"Test Group: {groupChain}")
                    print (f"Test: {test.name}")
                    print (f"Target: {TestTarget.AMYASM}")
                    print ("Code:")
                    print (fullCode)
                    print (f"Compiled? {isCompiled}")
                    print ("Expected Compiler Output:")
                    print (test.expectedCompilerOutput)
                    print ("Actual Compiler Output:")
                    print (compilerOutput.stdout)
                    print (f"--- STDERR ---------------------")
                    print (compilerOutput.stderr)
                    print (f"--------------------------------")
                    print (f"================================")
                else:
                    numSuccessfulTests += 1
            
            # 2. Failed to Compile when expecting success
            elif not isCompiled and test.shouldCompile:
                print (f"=== FAILED =====================")
                print (f"Test Group: {groupChain}")
                print (f"Test: {test.name}")
                print (f"Target: {TestTarget.AMYASM}")
                print ("Code:")
                print (fullCode)
                print (f"Compiled? {isCompiled}")
                print ("Compiler Output:")
                print (compilerOutput.stdout)
                print (f"--- STDERR ---------------------")
                print (compilerOutput.stderr)
                print (f"--------------------------------")
                print (f"================================")
            
            # 3. Compiles when expecting fail
            elif isCompiled and not test.shouldCompile:
                print (f"=== FAILED =====================")
                print (f"Reason: Should have failed to compile")
                print (f"Test Group: {groupChain}")
                print (f"Test: {test.name}")
                print (f"Target: {TestTarget.AMYASM}")
                print ("Code:")
                print (fullCode)
                print (f"Compiled? {isCompiled}")
                print ("Expected Compiler Output:")
                print (test.expectedCompilerOutput)
                print ("Compiler Output:")
                print (compilerOutput.stdout)
                print (f"================================")

            # 4. Compiles when expecting success
            else:
                # run the code
                result = subprocess.run (['python3', '../amyasmi/amyAssemblyInterpreter.py', 'test_data/test.amy.assembly'], capture_output=True, text=True)
                # ensure it was successful
                wasTestSuccessful = result.stdout == test.expectedOutputAMYASM
                if not wasTestSuccessful:
                    print (f"=== FAILED =====================")
                    print (f"Test Group: {groupChain}")
                    print (f"Test: {test.name}")
                    print (f"Target: {TestTarget.AMYASM}")
                    print ("Code:")
                    print (fullCode)
                    print (f"Compiled? {isCompiled}")
                    print ("Expected Output:")
                    print (test.expectedOutputAMYASM)
                    print ("Actual Output:")
                    print (result.stdout)
                    print (f"================================")
                else:
                    numSuccessfulTests += 1
            numTests += 1
        if testTarget == TestTarget.X86 or testTarget == TestTarget.ALL:
            # compile the code
            os.system (f'cat > test_data/test.amy <<EOF \n{fullCode}\nEOF')
            compilerOutput = subprocess.run ([f'python3', '../amyc/amyScriptCompiler.py', 'test_data/test.amy', '--target', 'x86', '-o', 'test_data/test.asm'], capture_output=True, text=True)

            isCompiled = (compilerOutput.returncode == 0)

            # 1. Failed to Compile when expecting fail
            if not isCompiled and not test.shouldCompile:
                # ensure expectedCompilerOutput exists
                if test.expectedCompilerOutput not in compilerOutput.stdout:
                    print (f"=== FAILED =====================")
                    print (f"Test Group: {groupChain}")
                    print (f"Test: {test.name}")
                    print (f"Target: {TestTarget.X86}")
                    print ("Code:")
                    print (fullCode)
                    print (f"Compiled? {isCompiled}")
                    print ("Expected Compiler Output:")
                    print (test.expectedCompilerOutput)
                    print ("Actual Compiler Output:")
                    print (compilerOutput.stdout)
                    print (f"--- STDERR ---------------------")
                    print (compilerOutput.stderr)
                    print (f"--------------------------------")
                    print (f"================================")
                else:
                    numSuccessfulTests += 1
            
            # 2. Failed to Compile when expecting success
            elif not isCompiled and test.shouldCompile:
                print (f"=== FAILED =====================")
                print (f"Test Group: {groupChain}")
                print (f"Test: {test.name}")
                print (f"Target: {TestTarget.X86}")
                print ("Code:")
                print (fullCode)
                print (f"Compiled? {isCompiled}")
                print ("Compiler Output:")
                print (compilerOutput.stdout)
                print (f"--- STDERR ---------------------")
                print (compilerOutput.stderr)
                print (f"--------------------------------")
                print (f"================================")
            
            # 3. Compiles when expecting fail
            elif isCompiled and not test.shouldCompile:
                print (f"=== FAILED =====================")
                print (f"Reason: Should have failed to compile")
                print (f"Test Group: {groupChain}")
                print (f"Test: {test.name}")
                print (f"Target: {TestTarget.X86}")
                print ("Code:")
                print (fullCode)
                print (f"Compiled? {isCompiled}")
                print ("Expected Compiler Output:")
                print (test.expectedCompilerOutput)
                print ("Compiler Output:")
                print (compilerOutput.stdout)
                print (f"================================")

            # 4. Compiles when expecting success
            else:
                # run the code
                os.system (f'nasm -f elf64 test_data/test.asm')
                os.system (f'ld test_data/test.o -o test -lc --dynamic-linker /lib/x86_64-linux-gnu/ld-linux-x86-64.so.2')
                result = subprocess.run (['./test'], capture_output=True, text=True)
                # ensure it was successful
                wasTestSuccessful = result.stdout == test.expectedOutputX86
                if not wasTestSuccessful:
                    print (f"=== FAILED =====================")
                    print (f"Test Group: {groupChain}")
                    print (f"Test: {test.name}")
                    print (f"Target: {TestTarget.X86}")
                    print ("Code:")
                    print (fullCode)
                    print (f"Compiled? {isCompiled}")
                    print ("Expected Output:")
                    print (test.expectedOutputX86)
                    print ("Actual Output:")
                    print (result.stdout)
                    print (f"================================")
                else:
                    numSuccessfulTests += 1
            numTests += 1
        if testTarget == TestTarget.PYTHON or testTarget == TestTarget.ALL:
            # compile the code
            os.system (f'cat > test_data/test.amy <<EOF \n{fullCode}\nEOF')
            compilerOutput = subprocess.run ([f'python3', '../amyc/amyScriptCompiler.py', 'test_data/test.amy', '--target', 'python', '-o', 'test_data/test.py'], capture_output=True, text=True)

            isCompiled = (compilerOutput.returncode == 0)

            # 1. Failed to Compile when expecting fail
            if not isCompiled and not test.shouldCompile:
                # ensure expectedCompilerOutput exists
                if test.expectedCompilerOutput not in compilerOutput.stdout:
                    print (f"=== FAILED =====================")
                    print (f"Test Group: {groupChain}")
                    print (f"Test: {test.name}")
                    print (f"Target: {TestTarget.PYTHON}")
                    print ("Code:")
                    print (fullCode)
                    print (f"Compiled? {isCompiled}")
                    print ("Expected Compiler Output:")
                    print (test.expectedCompilerOutput)
                    print ("Actual Compiler Output:")
                    print (compilerOutput.stdout)
                    print (compilerOutput.stderr)
                    print (f"================================")
                else:
                    numSuccessfulTests += 1
            
            # 2. Failed to Compile when expecting success
            elif not isCompiled and test.shouldCompile:
                print (f"=== FAILED =====================")
                print (f"Test Group: {groupChain}")
                print (f"Test: {test.name}")
                print (f"Target: {TestTarget.PYTHON}")
                print ("Code:")
                print (fullCode)
                print (f"Compiled? {isCompiled}")
                print ("Compiler Output:")
                print (compilerOutput.stdout)
                print (f"--- STDERR ---------------------")
                print (compilerOutput.stderr)
                print (f"--------------------------------")
                print (f"================================")
            
            # 3. Compiles when expecting fail
            elif isCompiled and not test.shouldCompile:
                print (f"=== FAILED =====================")
                print (f"Reason: Should have failed to compile")
                print (f"Test Group: {groupChain}")
                print (f"Test: {test.name}")
                print (f"Target: {TestTarget.PYTHON}")
                print ("Code:")
                print (fullCode)
                print (f"Compiled? {isCompiled}")
                print ("Expected Compiler Output:")
                print (test.expectedCompilerOutput)
                print ("Compiler Output:")
                print (compilerOutput.stdout)
                print (f"================================")

            # 4. Compiles when expecting success
            else:
                # run the code
                result = subprocess.run (["python3", "test_data/test.py"], capture_output=True, text=True)
                # ensure it was successful
                wasTestSuccessful = result.stdout == test.expectedOutputPython
                if not wasTestSuccessful:
                    print (f"=== FAILED =====================")
                    print (f"Test Group: {groupChain}")
                    print (f"Test: {test.name}")
                    print (f"Target: {TestTarget.PYTHON}")
                    print ("Code:")
                    print (fullCode)
                    print (f"Compiled? {isCompiled}")
                    print ("Expected Output:")
                    print (test.expectedOutputPython)
                    print ("Actual Output:")
                    print (result.stdout)
                    print (f"================================")
                elif result.returncode != 0:
                    print (f"=== FAILED =====================")
                    print (f"Test Group: {groupChain}")
                    print (f"Test: {test.name}")
                    print (f"Target: {TestTarget.PYTHON}")
                    print ("Code:")
                    print (fullCode)
                    print (f"Compiled? {isCompiled}")
                    print ("Failed due to non-zero return code")
                    print ("Returncode:", result.returncode)
                    print (f"--- STDERR ---------------------")
                    print (result.stderr)
                    print (f"--------------------------------")
                    print (f"================================")
                else:
                    numSuccessfulTests += 1
            numTests += 1

        if testTarget == TestTarget.CPP or testTarget == TestTarget.ALL:
            # compile the code
            os.system (f'cat > test_data/test.amy <<EOF \n{fullCode}\nEOF')
            compilerOutput = subprocess.run ([f'python3', '../amyc/amyScriptCompiler.py', 'test_data/test.amy', '--target', 'cpp', '-o', 'test_data/test.cpp'], capture_output=True, text=True)

            isCompiled = (compilerOutput.returncode == 0)

            # 1. Failed to Compile when expecting fail
            if not isCompiled and not test.shouldCompile:
                # ensure expectedCompilerOutput exists
                if test.expectedCompilerOutput not in compilerOutput.stdout:
                    print (f"=== FAILED =====================")
                    print (f"Test Group: {groupChain}")
                    print (f"Test: {test.name}")
                    print (f"Target: {TestTarget.CPP}")
                    print ("Code:")
                    print (fullCode)
                    print (f"Compiled? {isCompiled}")
                    print ("Expected Compiler Output:")
                    print (test.expectedCompilerOutput)
                    print ("Actual Compiler Output:")
                    print (compilerOutput.stdout)
                    print (compilerOutput.stderr)
                    print (f"================================")
                else:
                    numSuccessfulTests += 1
            
            # 2. Failed to Compile when expecting success
            elif not isCompiled and test.shouldCompile:
                print (f"=== FAILED =====================")
                print (f"Test Group: {groupChain}")
                print (f"Test: {test.name}")
                print (f"Target: {TestTarget.CPP}")
                print ("Code:")
                print (fullCode)
                print (f"Compiled? {isCompiled}")
                print ("Compiler Output:")
                print (compilerOutput.stdout)
                print (f"--- STDERR ---------------------")
                print (compilerOutput.stderr)
                print (f"--------------------------------")
                print (f"================================")
            
            # 3. Compiles when expecting fail
            elif isCompiled and not test.shouldCompile:
                print (f"=== FAILED =====================")
                print (f"Reason: Should have failed to compile")
                print (f"Test Group: {groupChain}")
                print (f"Test: {test.name}")
                print (f"Target: {TestTarget.CPP}")
                print ("Code:")
                print (fullCode)
                print (f"Compiled? {isCompiled}")
                print ("Expected Compiler Output:")
                print (test.expectedCompilerOutput)
                print ("Compiler Output:")
                print (compilerOutput.stdout)
                print (f"================================")

            # 4. Compiles when expecting success
            else:
                # build code with gcc
                gcc_result = subprocess.run (['g++','test_data/test.cpp','-o', 'testcpp'], capture_output=True, text=True)
                # ensure code builds with g++
                if gcc_result.returncode != 0:
                    print (f"=== FAILED =====================")
                    print (f"Test Group: {groupChain}")
                    print (f"Test: {test.name}")
                    print (f"Target: {TestTarget.CPP}")
                    print ("Code:")
                    print (fullCode)
                    print (f"Compiled? {isCompiled}")
                    print ("Reason: g++ failed to compile code")
                    print ("Returncode:", gcc_result.returncode)
                    print (f"--- STDERR ---------------------")
                    print (gcc_result.stderr)
                    print (f"--------------------------------")
                    print (f"================================")
                    
                # run the code
                result = subprocess.run (["./testcpp"], capture_output=True, text=True)
                # ensure it was successful
                wasTestSuccessful = result.stdout == test.expectedOutputCPP
                if not wasTestSuccessful:
                    print (f"=== FAILED =====================")
                    print (f"Test Group: {groupChain}")
                    print (f"Test: {test.name}")
                    print (f"Target: {TestTarget.CPP}")
                    print ("Code:")
                    print (fullCode)
                    print (f"Compiled? {isCompiled}")
                    print ("Expected Output:")
                    print (test.expectedOutputCPP)
                    print ("Actual Output:")
                    print (result.stdout)
                    print (f"================================")
                elif result.returncode != 0:
                    print (f"=== FAILED =====================")
                    print (f"Test Group: {groupChain}")
                    print (f"Test: {test.name}")
                    print (f"Target: {TestTarget.CPP}")
                    print ("Code:")
                    print (fullCode)
                    print (f"Compiled? {isCompiled}")
                    print ("Failed due to non-zero return code")
                    print ("Returncode:", result.returncode)
                    print (f"--- STDERR ---------------------")
                    print (result.stderr)
                    print (f"--------------------------------")
                    print (f"================================")
                else:
                    numSuccessfulTests += 1
            numTests += 1

        for i in range(level):
            print ('| ', end='')
        print ('> ', end='')
        print (f"{test.name} {numSuccessfulTests} / {numTests} passed")

        if numSuccessfulTests != numTests and shouldBreakOnFail:
            print ("Error: Exiting due to failed test")
            exit (1)

        return [numSuccessfulTests, numTests]

def runTest (test, testTarget:TestTarget=TestTarget.AMYASM, shouldBreakOnFail=False):

    runTest_helper (test, "", testTarget, 0, shouldBreakOnFail=shouldBreakOnFail)


# ** new code
# code = {"filename": "test.amy", "code": "int x = 0;\nprintln (x);"}

allTests = TestGroup ("All Tests", "", [
    Test ("Empty file", "", ""),
    TestGroup ("Printing", "", [
        Test ("print int", code="print (7);", expectedOutput="7"),
        Test ("print float", code="print (3.14);", expectedOutput="3.14"),
        Test ("print char", code='print (\'A\');', expectedOutput="A"),
        Test ("print char[]", code='print (\"Amy\");', expectedOutput="Amy"),
        Test ("print with no arg should fail", code='print ();', expectedCompilerOutput="Semantic Error: No function matching signature print()", shouldCompile=False)
    ]),
    TestGroup ("Arithmetic", "", [
        TestGroup ("Integer Arithmetic", "", [
            TestGroup ("Addition", "", [
                Test ("Test0", code="print (21 + 23);", expectedOutput="44"),
                Test ("Test1", code="print (21 + -23);", expectedOutput="-2"),
                Test ("Test2", code="print (-21 + 23);", expectedOutput="2"),
                Test ("Test3", code="print (-21 + -23);", expectedOutput="-44"),
                Test ("Test4", code="print (2000000000 + 1000000000);", expectedOutput="3000000000", expectedOutputAMYASM="3000000000")
            ]),
            TestGroup ("Subtraction", "", [
                Test ("Test0", code="print (21 - 23);", expectedOutput="-2"),
                Test ("Test1", code="print (21 - -23);", expectedOutput="44"),
                Test ("Test2", code="print (-21 - 23);", expectedOutput="-44"),
                Test ("Test3", code="print (-21 - -23);", expectedOutput="2"),
                Test ("Test4", code="print (-2000000000 - 1000000000);", expectedOutput="-3000000000", expectedOutputAMYASM="-3000000000")
            ]),
            TestGroup ("Multiplication", "", [
                Test ("Test0", code="print (3 * 31);", expectedOutput="93"),
                Test ("Test1", code="print (7 * -7);", expectedOutput="-49"),
                Test ("Test2", code="print (-9 * 4);", expectedOutput="-36"),
                Test ("Test3", code="print (-5 * -20);", expectedOutput="100"),
                Test ("Test4", code="print (-1000000000 * 1000000000);", expectedOutput="-1000000000000000000", expectedOutputAMYASM="-1000000000000000000")
            ]),
            TestGroup ("Division", "", [
                Test ("Test0", code="print (45 / 9);", expectedOutput="5"),
                Test ("Test1", code="print (45 / -5);", expectedOutput="-9"),
                Test ("Test2", code="print (-5 / 2);", expectedOutput="-2", expectedOutputAMYASM="-3", expectedOutputPython="-3"),
                Test ("Test3", code="print (-5 / -20);", expectedOutput="0")
            ]),
            TestGroup ("Mod", "", [
                Test ("Test0", code="print (45 % 9);", expectedOutput="0"),
                Test ("Test1", code="print (45 % 2);", expectedOutput="1"),
                Test ("Test2", code="print (-5 % 2);", expectedOutput="-1", expectedOutputAMYASM="1", expectedOutputPython="1"),
                Test ("Test3", code="print (-5 % -20);", expectedOutput="-5")
            ]),
            TestGroup ("Combining Operators", "", [
                Test (
                    "Test0", 
                    code="""
int x = (-17 + 42 * (2 + 2) + 1) * -1;
int y = x * 23;
print (y);""", 
                    expectedOutput="-3496"
                ),
            ])
        ])
    ]),
    TestGroup ("Variables", "", [
        Test ("Declaration", code="int x; int y = 10;", expectedOutput=""),
        Test ("Assignment", code="int x = 10;", expectedOutput=""),
        Test ("Variable value", code="float x = 3.14;print(x);", expectedOutput="3.14"),
        Test ("Arithmetic With Variables", code="int x = 30; int y = 42; print ((x + y) / 8);", expectedOutput="9"),
        Test ("Reassign Variables", code="int x = 10; x = 42; print(x);", expectedOutput="42"),
        Test ("Ensure reference before assignment fails", code="int x; print (x);", shouldCompile=False, expectedCompilerOutput=""),
    ]),
    TestGroup ("Misc", "int x = 10;", [
        Test ("Test0", code="print (x);", expectedOutput="10"),
        Test ("Test1", code="print (x+2);", expectedOutput="12"),
        Test ("Test2", code="print (x*2);", expectedOutput="20"),
    ]),
    TestGroup ("Functions", "", [
        Test ("Super Simple Function Declaration", code=
"""
function void print10 ()
{
    print (10);
}
print10 ();
""", expectedOutput="10"),
        Test ("Test Parameters", code=
"""
function void printint (int a)
{
    print (a);
}
printint (42);
""", expectedOutput="42"),
        Test ("Test Return", code=
"""
function float getPI ()
{
    return 3.14;
}
print (getPI());
""", expectedOutput="3.14"),
        Test ("Test Return no value", code=
            """
            function void printsomething ()
            {
                print ("this");
                return;
                print ("not this");
            }
            printsomething();
            """, expectedOutput="this"),
        TestGroup (
            "Max function", 
            """
            function int max (int a, int b)
            {
                if (a >= b)
                    return a;
                return b;
            }
            """, 
            [
                Test ("a < b", "print (max(-3, 7));", expectedOutput="7"),
                Test ("a == b", "print (max(7, 7));", expectedOutput="7"),
                Test ("a > b", "print (max(42, 3));", expectedOutput="42"),
            ]),
    ]),
    TestGroup ("Classes", "", [
        TestGroup (
            "Templated Vector Class testing", 
            """
template <:T:>
class Vector
{
    public field T[]   data;
    public field int   size;
    public field int   capacity;  

    constructor ()
    {
        this.capacity = 10;
        this.size = 0; 
        this.data = new T[this.capacity];
    }

    public method void pushBack (T val)
    {
        // ensure there is space 
        if (this.size + 1 >= this.capacity)
        {
            this.capacity = this.capacity * 2; 
            T[] nData = new T[this.capacity];
            // move old data over
            for (int i = 0; i < this.size; ++i)
            {
                nData[i] = this.data[i];
            }
            free (this.data);
            this.data = nData; 
        }

        // add new num
        this.data[this.size] = val; 
        ++this.size; 
    }

    public method T popBack ()
    {
        this.size -= 1;
        return this.data[this.size];
    }

    public method T get (int index)
    {
        return this.data[index];
    }

    public method void set (int index, T value)
    {
        this.data[index] = value;
    }

}

template <:T:>
function void print (Vector<:T:> v)
{
    print ('[');
    if (v.size != 0)
        print (v.data[0]);
    for (int i = 1; i < v.size; ++i)
    {
        print (',');
        print (' ');
        print (v.data[i]);
    }
    print (']');
}

template <:T:>
function void println (Vector<:T:> v)
{
    print<:T:> (v);
    println ();
}
            """, 
            [
                TestGroup (
                    "Vector<:int:>", 
                    "Vector<:int:> v = new Vector<:int:> ();", 
                    [
                        Test ("Constructing Vector", code="println<:int:> (v);", expectedOutput="[]\n"),
                        Test ("Push back", code="v.pushBack (42); println<:int:> (v);", expectedOutput="[42]\n"),
                        Test ("Push back multiple", code="v.pushBack (42); v.pushBack (7); v.pushBack (-3); println<:int:> (v);", expectedOutput="[42, 7, -3]\n"),
                    ]
                ),
                TestGroup (
                    "Vector<:float:>", 
                    "Vector<:float:> v = new Vector<:float:> ();", 
                    [
                        Test ("Constructing Vector", code="println<:float:> (v);", expectedOutput="[]\n"),
                        Test ("Push back", code="v.pushBack (3.14); println<:float:> (v);", expectedOutput="[3.14]\n"),
                        Test ("Push back multiple", code="v.pushBack (3.14); v.pushBack (-2.145e2); v.pushBack (1.0e-4); println<:float:> (v);", expectedOutput="[3.14, -214.5, 0.0001]\n"),
                    ]
                ),
            ]
        ),
    ])
])



runTest (allTests, TestTarget.CPP, shouldBreakOnFail=True)

# runTest (, TestTarget.ALL, shouldBreakOnFail=False)