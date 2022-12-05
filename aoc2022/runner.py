
import os
import subprocess
import time

# System call
os.system("")

# Class of different styles
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

AMYSCRIPT_COMPILER_PATH = '../code/amyc/amyScriptCompiler.py'
AMYASM_PATH = "../code/amyasmi/amyAssemblyInterpreter.py"

SAMPLE = 0
INPUT = 1
RUN_INPUT_MODE = INPUT

RUN_TIMEOUT = 30

libraries = ["Vector.amy", "algorithms.amy"]

class Run:
    def __init__ (self, day, part, target):
        self.day = day
        self.part = part
        self.target = target
        self.is_compiled = False
        self.compile_time = 0
        self.ran_successfully = False
        self.result = "N/A"
        self.is_correct = False
        self.runtime = 0

runs = []

days = [i for i in range(1, 6)]
parts = ["a", "b"]
targets = ["amyasm", "x86", "python"]
# targets = ["amyasm", "python"]

for day in days:
    for part in parts:
        for target in targets:
            runs.append (Run (day, part, target))

# execute runs
for run in runs:
    code_filename = f"day{run.day}{run.part}.amy"
    sample_filename = f"day{run.day}.sample"
    input_filename = f"day{run.day}.input"
    if RUN_INPUT_MODE == INPUT:
        acting_input_filename = input_filename
    elif RUN_INPUT_MODE == SAMPLE:
        acting_input_filename = sample_filename
    sample_answer_filename = f"day{run.day}{run.part}.sample.answer"
    input_answer_filename = f"day{run.day}{run.part}.input.answer"
    if RUN_INPUT_MODE == INPUT:
        acting_answer_filename = input_answer_filename
    elif RUN_INPUT_MODE == SAMPLE:
        acting_answer_filename = sample_answer_filename

    dest_filename = f"generated_code/day{run.day}{run.part}"
    if (run.target == "amyasm"):
        dest_filename += ".amy.assembly"
    elif (run.target == "x86"):
        dest_filename += ".asm"
    elif (run.target == "python"):
        dest_filename += ".py"
    else: 
        print ("Error: invalid target:", run.target)
        exit (1)

    print (code_filename, run.target, input_filename, dest_filename)

    # Compile
    cstart = time.perf_counter()
    if (run.target == "amyasm"):
        compiler_output = subprocess.run ([f'python3', AMYSCRIPT_COMPILER_PATH, code_filename, *libraries, '--target', run.target, '-o', dest_filename], capture_output=True, text=True)
    elif (run.target == "x86"):
        compiler_output = subprocess.run ([f'python3', AMYSCRIPT_COMPILER_PATH, code_filename, *libraries, '--target', run.target, '-o', dest_filename], capture_output=True, text=True)
    elif (run.target == "python"):
        compiler_output = subprocess.run ([f'python3', AMYSCRIPT_COMPILER_PATH, code_filename, *libraries, '--target', run.target, '-o', dest_filename], capture_output=True, text=True)
    else: 
        print ("Error: invalid target:", run.target)
        exit (1)
    cend = time.perf_counter ()
    run.compile_time = cend - cstart

    # Ensure it compiled succesfully
    run.is_compiled = compiler_output.returncode == 0
    print (run.is_compiled)

    if (not run.is_compiled):
        print (compiler_output.stdout)
        print (compiler_output.stderr)
        # move on to next run
        continue

    # get input
    with open (acting_input_filename, "r") as f:
        input_data = f.read()
    
    # get answer
    with open (acting_answer_filename, "r") as f:
        expected_answer = f.read ().strip ()

    # Run generated code
    rstart = time.perf_counter()
    if (run.target == "amyasm"):
        run_output = subprocess.run ([f'python3', AMYASM_PATH, dest_filename], input=input_data, capture_output=True, text=True)
    elif (run.target == "x86"):
        # x86 needs to be assembled and linked
        assembled_filename = f"generated_code/day{day}{part}.o"
        os.system (f'nasm -f elf64 {dest_filename} -o {assembled_filename}')
        bin_filename = f"generated_code/day{day}{part}.out"
        os.system (f'ld {assembled_filename} -o {bin_filename} -lc --dynamic-linker /lib/x86_64-linux-gnu/ld-linux-x86-64.so.2')
        # we're finally ready to run the code
        try:
            run_output = subprocess.run ([f"./{bin_filename}"], input=input_data, capture_output=True, text=True, timeout=RUN_TIMEOUT)
        except subprocess.TimeoutExpired:
            # catch timeout errors
            print (f"Error: timeout of {RUN_TIMEOUT} seconds exceeded")
            print (f"   Maybe there is a hang or the timeout needs to be increased or the process is waiing on input")
            continue
    elif (run.target == "python"):
        run_output = subprocess.run ([f'python3', dest_filename], input=input_data, capture_output=True, text=True)
    else: 
        print ("Error: invalid target:", run.target)
        exit (1)
    rend = time.perf_counter ()
    run.runtime = rend - rstart

    # Ensure code ran successfully
    run.ran_successfully = run_output.returncode == 0
    if not run.ran_successfully:
        print (run_output.stdout)
        print (run_output.stderr)

    # Grab result
    print ("result =>", run_output.stdout)
    run.result = run_output.stdout.strip()
    
    # Check if it is correct
    run.is_correct = run.result == expected_answer


# day, part, target, compiled?, compiletime, result, time

if RUN_INPUT_MODE == INPUT:
    print ("results are from 'input' datasets")
elif RUN_INPUT_MODE == SAMPLE:
    print ("results are from 'sample' datasets")

print     (f"+-{  '---':>3}-+-{  '----':>4}-+-{  '------':>6}-+-{               '-'*11}-+-{                 '-'*12}-+-{                    '-'*11}-+-{        '-'*10}-+-{              '-'*10}-+-{            '-'*7}-+")
print     (f"| {  'day':>3} | {  'part':>4} | {  'target':>6} | {    'is_compiled':>11} | {     'compile_time':>12} | {         'successful?':>11} | {  'result':>10} | {    'is_correct':>10} | {     'runtime':>7} |")
print     (f"+-{  '---':>3}-+-{  '----':>4}-+-{  '------':>6}-+-{               '-'*11}-+-{                 '-'*12}-+-{                    '-'*11}-+-{        '-'*10}-+-{              '-'*10}-+-{            '-'*7}-+")
for run in runs:
    if run.target == "amyasm":
        print (style.GREEN, end="")
    elif run.target == "x86":
        print (style.RED, end="")
    elif run.target == "python":
        print (style.CYAN, end="")
    print (f"| {run.day:>3} | {run.part:>4} | {run.target:>6} | {run.is_compiled!s:>11} | {run.compile_time:>12.4f} | {run.ran_successfully!s:>11} | {run.result:>10} | {run.is_correct!s:>10} | {run.runtime:>7.4f} |")
    print(style.RESET, end="")
print     (f"+-{  '---':>3}-+-{  '----':>4}-+-{  '------':>6}-+-{               '-'*11}-+-{                 '-'*12}-+-{                    '-'*11}-+-{        '-'*10}-+-{              '-'*10}-+-{            '-'*7}-+")

