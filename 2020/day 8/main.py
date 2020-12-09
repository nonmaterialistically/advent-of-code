file = open('input.txt', 'r')
oldLines = file.readlines()

Lines = list(oldLines)
parsedinstructions = list()
accumulator = 0
i=0

while 0 <= i <= len(Lines):
    instruction = Lines[i].split()
    operation = instruction[0]
    argument = instruction[1]
    if i in parsedinstructions:
        print("Day 1:", accumulator)
        break
    else:
        parsedinstructions.append(i)
        if operation == "nop":
            i += 1
            continue
        if operation == "acc":
            if argument[0] == "+":
                accumulator += int(argument[1:])
            if argument[0] == "-":
                accumulator -= int(argument[1:])
            i += 1
            continue
        if operation == "jmp":
            if argument[0] == "+":
                i += int(argument[1:])
            if argument[0] == "-":
                i -= int(argument[1:])
            continue

Lines = list(oldLines)
parsedinstructions = list()
accumulator = 0
i=0
t=0

for change in range(len(oldLines)):
    Lines = list(oldLines)
    operation = Lines[change].split()[0]
    if operation == 'nop':
        Lines[change] = 'jmp '+Lines[change].split()[1]
    elif operation == 'jmp':
        Lines[change] = 'nop '+Lines[change].split()[1]
    else:
        continue
    parsedinstructions = list()
    accumulator = 0
    i=0
    t=0
    while 0 <= i <= len(Lines):
        if i == len(Lines):
            print("Day 2:", accumulator)
            break 
        if i in parsedinstructions:
            break
        else:
            parsedinstructions.append(i)
            instruction = Lines[i].split()
            operation = instruction[0]
            argument = instruction[1]
            if operation == "nop":
                i += 1
                continue
            if operation == "acc":
                if argument[0] == "+":
                    accumulator += int(argument[1:])
                if argument[0] == "-":
                    accumulator -= int(argument[1:])
                i += 1
                continue
            if operation == "jmp":
                #print(Lines[i], "Index", i)
                if argument[0] == "+":
                    i += int(argument[1:])
                if argument[0] == "-":
                    i -= int(argument[1:])
                continue
    if i == len(Lines):
        break 