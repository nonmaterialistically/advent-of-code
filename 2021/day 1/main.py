file = open('input.txt', 'r')
Lines = file.readlines()

previousLine = int(Lines[0].strip())
increasedcounter = 0

for i in Lines:
    currentLine = int(i.strip())
    if currentLine > previousLine:
        increasedcounter += 1
    previousLine = currentLine

print("Part 1: ", increasedcounter)
increasedcounter = 0
oldWindow = 0
sumWindow = 0

for i in range(0, len(Lines)):
    if i == 0 or i == len(Lines)-1:  # There's no need to calculate the sum at the first and last line -- they get calculated on the second and second-last
        continue
    else:
        sumWindow = int(Lines[i-1].strip())+int(Lines[i].strip())+int(Lines[i+1].strip())
    if oldWindow == 0:  # No need to increase the counter the first time, since that means we're at the first sum
        pass
    elif oldWindow != 0 and sumWindow > oldWindow:
        increasedcounter += 1
    oldWindow = sumWindow

print("Part 2: ", increasedcounter)