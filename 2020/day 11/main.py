import copy

file = open('input.txt', 'r')
Lines = file.readlines()

inputstate = list()
oldstate = list()
newstate = list()

for line in Lines:
    inputstate.append(list(line.strip()))

oldstate = copy.deepcopy(inputstate)
newstate = copy.deepcopy(inputstate)

#Since I'm not familiar with a way to compare lists of lists I don't know how to check if equilibrium was reached
#I'm just doing X iterations where X is a number I know is enough

times = 0
while times < 70:
    for row in range(len(oldstate)):
        for column in range(len(oldstate[row])):
            seat = oldstate[row][column]
            up = '.' if row == 0 else oldstate[row-1][column]
            down =  '.' if row == len(oldstate)-1 else oldstate[row+1][column]
            left = '.' if column == 0 else oldstate[row][column-1]
            right = '.' if column == len(oldstate[row])-1 else oldstate[row][column+1]
            if row != 0 and column != 0:
                diagupleft = oldstate[row-1][column-1]
            else:
                diagupleft = '.'
            if row != len(oldstate)-1 and column != len(oldstate[row])-1:
                diagdownright = oldstate[row+1][column+1]
            else:
                diagdownright = '.'
            if row != 0 and column != len(oldstate[row])-1:
                diagupright = oldstate[row-1][column+1]
            else:
                diagupright = '.'
            if row != len(oldstate)-1 and column != 0: 
                diagdownleft = oldstate[row+1][column-1]
            else:
                diagdownleft = '.'
            adiacentseats = [up, down, right, left, diagupright, diagupleft, diagdownright, diagdownleft]
            if seat == "L" and adiacentseats.count("#") == 0:
                newstate[row][column] = "#"
            if seat == "#" and adiacentseats.count("#") >= 4:
                newstate[row][column] = "L"
    times += 1
    oldstate = copy.deepcopy(newstate)

ans1 = 0
for line in newstate:
    ans1 += line.count('#')
print("Part one:", ans1)

oldstate = copy.deepcopy(inputstate)
newstate = copy.deepcopy(inputstate)

#Since I'm not familiar with a way to compare lists of lists I don't know how to check if equilibrium was reached
#I'm just doing X iterations where X is a number I know is enough

times = 0
while times < 90:
    for row in range(len(oldstate)):
        for column in range(len(oldstate[row])):
            seat = oldstate[row][column]
            if row != 0:
                for i in range(1, row+1):
                    if oldstate[row-i][column] != '.':
                        up = oldstate[row-i][column]
                        break
                    else:
                        up = '.'
            else:
                up = '.'

            if row != len(oldstate)-1:
                for i in range(1, len(oldstate)-row):
                    if oldstate[row+i][column] != '.':
                        down = oldstate[row+i][column]
                        break
                    else:
                        down = '.'
            else:
                down =  '.' 

            if column != 0: 
                for i in range(1, column+1):
                    if oldstate[row][column-i] != '.':
                        left = oldstate[row][column-i]
                        break
                    else:
                        left = '.'
            else:
                left = '.' 

            if column != len(oldstate[row])-1:
                for i in range(1, len(oldstate[row])-column):
                    if oldstate[row][column+i] != '.':
                        right = oldstate[row][column+i]
                        break
                    else: 
                        right = '.'
            else:
                right = '.'

            if row != 0 and column != 0:
                for i,j in zip(range(1, row+1),range(1, column+1)):
                    if oldstate[row-i][column-j] != '.':
                        diagupleft = oldstate[row-i][column-j]
                        break
                    else:
                        diagupleft = '.'
            else:
                diagupleft = '.'

            if row != len(oldstate)-1 and column != len(oldstate[row])-1:
                for i,j in zip(range(1, len(oldstate)-row), range(1, len(oldstate[row])-column)):
                    if oldstate[row+i][column+j] != '.':
                        diagdownright = oldstate[row+i][column+j]
                        break
                    else:
                        diagdownright = '.'
            else:
                diagdownright = '.'

            if row != 0 and column != len(oldstate[row])-1:
                for i,j in zip(range(1, row+1), range(1, len(oldstate[row])-column)):
                    if oldstate[row-i][column+j] != '.':
                        diagupright = oldstate[row-i][column+j]
                        break
                    else:
                        diagupright = '.'
            else:
                diagupright = '.'

            if row != len(oldstate)-1 and column != 0: 
                for i,j in zip(range(1, len(oldstate)-row), range(1, column+1)):
                    if oldstate[row+i][column-j] != '.':
                        diagdownleft = oldstate[row+i][column-j]
                        break
                    else:
                        diagdownleft = '.'
            else:
                diagdownleft = '.'

            adiacentseats = [up, down, right, left, diagupright, diagupleft, diagdownright, diagdownleft]

            if seat == "L" and adiacentseats.count("#") == 0:
                newstate[row][column] = "#"
            if seat == "#" and adiacentseats.count("#") >= 5:
                newstate[row][column] = "L"
    times += 1
    oldstate = copy.deepcopy(newstate)

ans2 = 0
for line in newstate:
    ans2 += line.count('#')
print("Part two:", ans2)