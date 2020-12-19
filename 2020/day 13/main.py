import math

file = open('input.txt', 'r')
Lines = file.readlines()

timestamp = int(Lines[0].strip())
t = timestamp
busses = Lines[1].strip().split(',')
found = False

while found == False:
    for bus in busses:
        if bus == 'x':
            continue
        else:
            if t%int(bus) == 0:
                found = True
                print("Part one:", int(bus)*(t-timestamp))
                break
    t += 1

t = int(busses[0])
period = t
testedbusses = list()
testedbusses.append(t)

for bus in busses:
    if bus == 'x':
        continue
    else:
        while True:
            if (t+busses.index(bus))%int(bus) == 0:
                testedbusses.append(int(bus))
                period = math.lcm(*testedbusses)
                break
            else:
                t += period
print("Part two:", t)