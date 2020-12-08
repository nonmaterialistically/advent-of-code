file = open('input.txt', 'r')
Lines = file.readlines()

foundDay1 = False
foundDay2 = False

for i in Lines:
    if not foundDay1:
        for o in Lines:
            if int(i)+int(o) == 2020:
                print("Day one:", int(i)*int(o))
                foundDay1 = True
                break
            if not foundDay2:
                for p in Lines:
                    if int(i)+int(o)+int(p) == 2020:
                        print("Day two", int(i)*int(o)*int(p))
                        foundDay2 = True
                        break