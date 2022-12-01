file = open('input.txt', 'r')
Lines = file.readlines()

currentElf = 0
elfArray = []

for i in Lines:
    if i == "\n":
        elfArray.append(currentElf)
        currentElf = 0
    else:
        currentElf = currentElf + int(i.strip())
elfArray.sort(reverse=True)
print("Most elf: " + str(elfArray[0]))
print("Sum of top three elves: " + str(elfArray[0]+elfArray[1]+elfArray[2]))