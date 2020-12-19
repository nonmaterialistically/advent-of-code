numbers = [0,8,15,2,12,1,4]
last = numbers[-1]
d = dict()
turn = 1

for number in numbers:
    d.setdefault(number, []).append(turn)
    turn+=1

while turn <= 30000000:
    if len(d[last]) == 1:
        last = 0
    else:
        last = d[last][-1] - d[last][-2]
    if turn == 2020:
        print("Part one:", last)
    if turn == 30000000:
        print("Part two:", last)
        break
    d.setdefault(last, []).append(turn)
    turn += 1