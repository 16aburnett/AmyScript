
import os
import subprocess
import time
import argparse

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
RUN_INPUT_MODE = SAMPLE

RUN_TIMEOUT = 3600

libraries = ["Vector.amy", "algorithms.amy", "LinkedList.amy"]

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

def run (days, parts, targets, inputset, hide_answers):
    runs = []

    for day in days:
        for part in parts:
            for target in targets:
                runs.append (Run (day, part, target))

    # execute runs
    for run in runs:
        code_filename = f"day{run.day}{run.part}.amy"
        sample_filename = f"day{run.day}.sample"
        input_filename = f"day{run.day}.input"
        if inputset == "input":
            acting_input_filename = input_filename
        elif inputset == "sample":
            acting_input_filename = sample_filename
        sample_answer_filename = f"day{run.day}{run.part}.sample.answer"
        input_answer_filename = f"day{run.day}{run.part}.input.answer"
        if inputset == "input":
            acting_answer_filename = input_answer_filename
        elif inputset == "sample":
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

        # print (code_filename, run.target, input_filename, dest_filename)

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
        # print (run.is_compiled)

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
        try:
            rstart = time.perf_counter()
            if (run.target == "amyasm"):
                run_output = subprocess.run ([f'python3', AMYASM_PATH, dest_filename], input=input_data, capture_output=True, text=True, timeout=RUN_TIMEOUT)
            elif (run.target == "x86"):
                # x86 needs to be assembled and linked
                assembled_filename = f"generated_code/day{day}{part}.o"
                os.system (f'nasm -f elf64 {dest_filename} -o {assembled_filename}')
                bin_filename = f"generated_code/day{day}{part}.out"
                os.system (f'ld {assembled_filename} -o {bin_filename} -lc --dynamic-linker /lib/x86_64-linux-gnu/ld-linux-x86-64.so.2')
                # we're finally ready to run the code
                run_output = subprocess.run ([f"./{bin_filename}"], input=input_data, capture_output=True, text=True, timeout=RUN_TIMEOUT)
            elif (run.target == "python"):
                run_output = subprocess.run ([f'python3', dest_filename], input=input_data, capture_output=True, text=True, timeout=RUN_TIMEOUT)
            else: 
                print ("Error: invalid target:", run.target)
                exit (1)
            rend = time.perf_counter ()
            run.runtime = rend - rstart
        except subprocess.TimeoutExpired:
                # catch timeout errors
                print (f"Error: timeout of {RUN_TIMEOUT} seconds exceeded")
                print (f"   Maybe there is a hang or the timeout needs to be increased or the process is waiting on input or your implementation is too slow")
                continue

        # Ensure code ran successfully
        run.ran_successfully = run_output.returncode == 0
        if not run.ran_successfully:
            print (run_output.stdout)
            print (run_output.stderr)
            exit(1)

        # Grab result
        # print ("result =>", run_output.stdout)
        run.result = run_output.stdout.strip()
        
        # Check if it is correct
        run.is_correct = run.result == expected_answer


    # day, part, target, compiled?, compiletime, result, time

    # if inputset == "input":
    #     print ("results are from 'input' datasets")
    # elif inputset == "sample":
    #     print ("results are from 'sample' datasets")

    print     (f"+-{  '---':>3}-+-{  '----':>4}-+-{  '------':>6}-+-{               '-'*9}-+-{                   '-'*10}-+-{                    '-'*8}-+-{        '-'*12}-+-{              '-'*8}-+-{               '-'*9}-+")
    print     (f"| {  'day':^3} | {  'part':^4} | {  'target':^6} | {             'is':^9} | {            'compile':^10} | {                'exit':^8} | {  'result':^12} | {            'is':^8} | {        'runtime':^9} |")
    print     (f"| {     '':^3} | {      '':^4} | {    'lang':^6} | {      'compiled?':^9} | {         'time (sec)':^10} | {            'success?':^8} | {        '':^12} | {      'correct?':^8} | {          '(sec)':^9} |")
    print     (f"+-{  '---':>3}-+-{  '----':>4}-+-{  '------':>6}-+-{               '-'*9}-+-{                   '-'*10}-+-{                    '-'*8}-+-{        '-'*12}-+-{              '-'*8}-+-{               '-'*9}-+")
    total_compile_time = 0
    total_run_time = 0
    for run in runs:
        if run.target == "amyasm":
            print (style.GREEN, end="")
        elif run.target == "x86":
            print (style.RED, end="")
        elif run.target == "python":
            print (style.CYAN, end="")
        if hide_answers:
            result = f"{'-'*10}"
        else:
            result = run.result
        print (f"| {run.day:>3} | {run.part:>4} | {run.target:>6} | {run.is_compiled!s:>9} | {  run.compile_time:>10.4f} | {run.ran_successfully!s:>8} | {    result:>12} | {run.is_correct!s:>8} | {   run.runtime:>9.4f} |")
        print(style.RESET, end="")
        total_compile_time += run.compile_time
        total_run_time += run.runtime
    print     (f"+-{  '---':>3}-+-{  '----':>4}-+-{  '------':>6}-+-{               '-'*9}-+-{                   '-'*10}-+-{                    '-'*8}-+-{        '-'*12}-+-{              '-'*8}-+-{               '-'*9}-+")
    print     (f"| {               'total':^10} | {  '      ':>6} | {               ' '*9} | {total_compile_time:>10.4f} | {                    ' '*8} | {        ' '*12} | {              ' '*8} | {total_run_time:>9.4f} |")
    print     (f"+-{  '---':>3}-+-{  '----':>4}-+-{  '------':>6}-+-{               '-'*9}-+-{                   '-'*10}-+-{                    '-'*8}-+-{        '-'*12}-+-{              '-'*8}-+-{               '-'*9}-+")

    print ()


if __name__ == "__main__":
    argparser = argparse.ArgumentParser (description="Arguments")

    argparser.add_argument("-d", "--days", nargs="+", default=["all"], help="days to run [default all] (1, 2, ..., 24 | all)")
    argparser.add_argument("-p", "--parts", choices=["a", "b", "both"], default="both", help="parts to run per day [default both] (a | b | both)")
    argparser.add_argument("-t", "--targets", nargs="+", default=["all"], help="targets to compile to for each run [default all] (amyasm, x86, python, all)")
    argparser.add_argument("-i", "--input", choices=["sample", "input"], default="input", help="specifies the input dataset [default input] (sample, input)")
    argparser.add_argument("--hide_answers", action="store_true", help="hides the outputted answers")

    args = argparser.parse_args ()

    # print (args)

    valid_days = [str(i) for i in range(1, 15)]
    days = args.days
    if "all" in args.days:
        days = valid_days
    # ensure valid targets 
    for day in days:
        if day not in valid_days:
            print (f"Error: '{day}' is not a valid day")
            exit (1)

    # print (days)

    if args.parts == "both":
        parts = ["a", "b"]
    else:
        parts = [args.parts]

    # print (parts)

    valid_targets = ["amyasm", "x86", "python"]

    targets = args.targets
    if "all" in args.targets:
        targets = valid_targets
    # ensure valid targets 
    for target in targets:
        if target not in valid_targets:
            print (f"Error: '{target}' is not a valid target")
            exit (1)

    # print (targets)

    run (days, parts, targets, args.input, args.hide_answers)
    
