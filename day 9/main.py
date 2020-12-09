file = open('input.txt', 'r')
Lines = file.readlines()

preamble = 25
numbers = list(Lines)

contiguous = 0
ans1 = 0
ans2 = 0

for i in range(preamble, len(numbers)):
    ans1 = int(numbers[i].strip())
    valid = False
    if i < preamble:
        for o in range(0, preamble-1):
            if valid == True:
                break
            else:
                for p in range(0, preamble-1):
                    if o != p:
                        if int(numbers[o].strip())+int(numbers[p].strip()) == ans1:
                            valid = True
                            break
    else:
        for o in range(i-preamble, i):
            if valid == True:
                break
            else:
                for p in range(i-preamble, i):
                    if o != p:
                        if int(numbers[o].strip())+int(numbers[p].strip()) == ans1:
                            valid = True
                            break
    if valid == False:
        print("Part 1:", ans1)
        break

contiguousList = list()

for i in range(len(numbers)):
    if int(numbers[i].strip()) < ans1:
        contiguousList = list()
        contiguousList.append(int(numbers[i].strip()))
        for o in range(i+1, len(numbers)):
            if int(numbers[i].strip()) < ans1:
                contiguousList.append(int(numbers[o].strip()))
                contiguous = sum(contiguousList)
                if contiguous > ans1:
                    break
                elif contiguous == ans1:
                    contiguousList.sort()
                    ans2 = contiguousList[0] + contiguousList[-1]
                    print("Part 2:", ans2)
                    break