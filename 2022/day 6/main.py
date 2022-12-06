file = open('input.txt', 'r')
Lines = file.readlines()

code = list(Lines[0].strip())
check1 = []
check2 = []
part1 = False
part2 = False

for n,current in enumerate(code):
    if not(part1):
        check1.append(current)
        if n >= 3:
            if len(set(check1)) == 4:
                print(n+1)
                part1 = True
            check1.pop(0)
    if not(part2):
        check2.append(current)
        if n >= 13:
            if len(set(check2)) == 14:
                print(n+1)
                part2 = True
            check2.pop(0)