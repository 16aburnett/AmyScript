

import os
import subprocess
from enum import Enum 

# GIVEN 
# WHEN 
# THEN



class TestTarget (Enum):
    AMYASM = 0
    X86 = 1
    ALL = 2 # tests all targets

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
        expectedOutputX86:str=None, 
        expectedOutputAMYASM:str=None, 
        expectedCompilerOutput:str=None,
        shouldCompile:bool=True
    ):
        self.name = name
        self.code = code
        self.expectedOutput = expectedOutput
        self.expectedOutputX86 = expectedOutputX86 if expectedOutputX86 != None else expectedOutput
        self.expectedOutputAMYASM = expectedOutputAMYASM if expectedOutputAMYASM != None else expectedOutput
        self.expectedCompilerOutput = expectedCompilerOutput
        self.shouldCompile = shouldCompile


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
                Test ("Test2", code="print (-5 / 2);", expectedOutput="-2", expectedOutputAMYASM="-3"),
                Test ("Test3", code="print (-5 / -20);", expectedOutput="0")
            ]),
            TestGroup ("Mod", "", [
                Test ("Test0", code="print (45 % 9);", expectedOutput="0"),
                Test ("Test1", code="print (45 % 2);", expectedOutput="1"),
                Test ("Test2", code="print (-5 % 2);", expectedOutput="-1", expectedOutputAMYASM="1"),
                Test ("Test3", code="print (-5 % -20);", expectedOutput="-5")
            ]),
            TestGroup ("Combining Operators", "", [
                Test (
                    "Test0", 
                    code="""
int x = (-17 + 42 * (2 + 2) + 1) * -1 % 3;
int y = x * 23;
print (y / x);""", 
                    expectedOutput="23"
                ),
            ])
        ])
    ]),
    TestGroup ("Variables", "", [
        Test ("Declaration", code="int x;", expectedOutput=""),
        Test ("Assignment", code="int x = 10;", expectedOutput=""),
        Test ("Variable value", code="int x = 10;print(x);", expectedOutput="10"),
        Test ("Arithmetic With Variables", code="int x = 30; int y = 42; print ((x + y) / 8);", expectedOutput="9"),
        Test ("Reassign Variables", code="int x = 10; x = 42; print(x);", expectedOutput="42"),
    ])
])



runTest (allTests, TestTarget.ALL, shouldBreakOnFail=False)