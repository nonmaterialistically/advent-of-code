file = open('input.txt', 'r')
Lines = file.readlines()

D = list()

for line in Lines:
    D.append(int(line.strip()))

D.sort()
count1 = 0
count3 = 0
D.insert(0,0)
D.append(D[-1]+3)

for i in range(0, len(D)-1):
    if D[i+1]-D[i] == 1:
        count1 += 1
    elif D[i+1]-D[i] == 3:
        count3 += 1

counted = dict()

def count(i):
    if i in counted:
        return counted[i]
    if i == len(D)-1:
        return 1
    o = 0
    for j in range(i+1, len(D)):
        if D[j] - D[i] <= 3:
            o += count(j)
    counted[i] = o
    return o
        
print("Part one:", count1*count3)
print("Part two:", count(0))