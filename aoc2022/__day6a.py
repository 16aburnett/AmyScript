

line = input ()

for i in range(len(line)-3):
    # check if sequence is unique
    if line[i] == line[i+1] or \
        line[i] == line[i+2] or \
        line[i] == line[i+3] or \
        line[i+1] == line[i+2] or \
        line[i+1] == line[i+3] or \
        line[i+2] == line[i+3]:
        continue
    print (i+4)
    break