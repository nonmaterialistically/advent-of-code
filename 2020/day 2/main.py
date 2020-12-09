file = open('input.txt', 'r')
Lines = file.readlines()

countPart1 = 0
countPart2 = 0

for line in Lines:
    firstNum = int(line.split()[0].split('-')[0]) 
    secondNum = int(line.split()[0].split('-')[1])
    letter = line.split()[1].split(':')[0]
    password = line.split()[2]
    letterpositions = ([pos for pos, char in enumerate(password, start=1) if char == letter])
    if firstNum <= password.count(letter) <= secondNum:
        countPart1 += 1
    if bool(firstNum in letterpositions) != bool(secondNum in letterpositions):
        countPart2 += 1

print("Part 1:", countPart1)
print("Part 2:", countPart2)