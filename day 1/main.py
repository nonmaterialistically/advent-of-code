file = open('input.txt', 'r')
Lines = file.readlines()

foundPart1 = False
foundPart2 = False

for i in Lines:
    if not foundPart1:
        for o in Lines:
            if int(i)+int(o) == 2020:
                print("Part one:", int(i)*int(o))
                foundPart1 = True
                break
            if not foundPart2:
                for p in Lines:
                    if int(i)+int(o)+int(p) == 2020:
                        print("Part two", int(i)*int(o)*int(p))
                        foundPart2 = True
                        break