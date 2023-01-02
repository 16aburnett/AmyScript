

line = input ()

for i in range(len(line)-14):
    # ensure sequence is unique
    isUnique = True
    for j in range(i, i+14):
        for k in range(j+1, i+14):
            if line[j] == line[k]:
                isUnique = False
                break
        if not isUnique:
            break
    if not isUnique:
        continue
    print (i+14)
    break