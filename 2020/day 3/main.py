import numpy

file = open('input.txt', 'r')
Lines = file.readlines()

count = 0
column = 0
row = 0
right = 0
down = 0

ans = list()
m = list() #m as in map
slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

linelenght = len(Lines[0].strip()) #get the number of columns from the first line

for line in Lines:
    m.append(list(line.strip()))

for (right, down) in slopes:
    count = 0
    row = 0
    column = 0
    while row+1 < len(m):
        column += right
        row += down
        if m[row][column % linelenght] == '#':
            count += 1
    #print("Result with right:",right, "and down:", down, "-->", count)
    ans.append(count)

print("Part one:", ans[1])
print("Part two:", numpy.prod(ans))