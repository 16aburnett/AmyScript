
import sys

stacklines = []
instructionlines = []

newline = False
for line in sys.stdin:
    if line[0] == "\n":
        newline = True
    elif not newline:
        stacklines += [line]
    else:
        instructionlines += [line]


size = int(stacklines[-1].split()[-1])

print (size)

stacks = [[] for _ in range(size)]

for j in range(len(stacklines)-2, -1, -1):
    print (stacklines[j],end="")
    for i in range(size):
        if stacklines[j][i*4+1] != ' ':
            print (stacklines[j][i*4+1])
            stacks[i] += [stacklines[j][i*4+1]]
        # if i*4 < len(stacklines[j]) and stacklines[j][i*4] != ' ':

print (stacks)        

# follow instructions
for instruction in instructionlines:
    # move x from y to z
    if (instruction == '$\n') : break
    tokens = instruction.split()
    print (instruction)
    num_boxes = int(tokens[1])
    src = int(tokens[3])-1
    dest = int (tokens[5])-1

    boxes_to_move = stacks[src][len(stacks[src])-num_boxes:]
    for _ in range(num_boxes):
        stacks[src].pop()
    stacks[dest] += boxes_to_move
    
print (stacks)

for stack in stacks:
    if len(stack) != 0:
        print (stack[-1], end="")
print ()

