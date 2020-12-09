file = open('input.txt', 'r')
Lines = file.readlines()

lowerLimit = 0
upperLimit = 127
lowerSeat = 0
upperSeat = 7
uid=0
uidList = list()

for line in Lines:
    lowerLimit = 0
    upperLimit = 127
    lowerSeat = 0
    upperSeat = 7
    uid=0
    for index in range(0, len(line)):
        if line[index] == 'F': #lower half
            upperLimit = (((upperLimit-lowerLimit+1)/2)+lowerLimit)-1
        if line[index] == 'B': #upper half
            lowerLimit = (((upperLimit-lowerLimit+1)/2)+lowerLimit)
        if lowerLimit == upperLimit:
            if line[index] == 'L': #lower half
                upperSeat = (((upperSeat-lowerSeat+1)/2)+lowerSeat)-1
            if line[index] == 'R': #upper half
                lowerSeat = (((upperSeat-lowerSeat+1)/2)+lowerSeat)
    if lowerSeat == upperSeat:
        uid = (lowerLimit * 8) + lowerSeat
        uidList.append(int(uid))

uidList.sort() #Sort the list now, I'm gonna need it later anyway

print("Part one:", uidList[-1])

for i in range(uidList[0], uidList[-1]):
    if i not in uidList:
        print("Part two:", i)