file = open('input.txt', 'r')
Lines = file.readlines()

byr, iyr, eyr, hgt, hcl, ecl, pid, cid = [0, 0, 0, 0, 0, 0, 0, 0]
keylist = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
ans1 = 0
ans2 = 0
blanklines = 0

def checkhgt(hgt):
    hgt = list(hgt)
    unit = ''.join(hgt[-2:])
    if unit == "cm" or unit == "in":
        number = int(''.join(hgt[:-2]))
        if unit == "cm":
            return number >= 150 and number <= 193
        elif unit == "in":
            return number >= 59 and number <= 76
        else:
            return False
    else:
        return False

def checkhcl(hcl):
    hcl = list(hcl)
    return hcl[0] == "#" and len(hcl[1:]) == 6

def checkecl(ecl):
    return ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def checkpid(pid):
    return len(list(pid)) == 9 and all(x.isdigit() for x in list(pid))

for line in Lines:
    if line[0] == "\n":
        blanklines += 1
        if 0 not in (byr, iyr, eyr, hgt, hcl, ecl, pid):
            checkbyr = (byr>=1920 and byr<=2002)
            checkiyr = (iyr>=2010 and iyr<=2020)
            checkeyr = (eyr>=2020 and eyr<=2030)
            if checkbyr and checkiyr and checkeyr and checkhgt(hgt) and checkhcl(hcl) and checkecl(ecl) and checkpid(pid):
                ans1 += 1
                ans2 += 1
            else: 
                ans1 += 1
        byr, iyr, eyr, hgt, hcl, ecl, pid, cid = [0, 0, 0, 0, 0, 0, 0, 0]
    else:
        passport = line.split()
        for pair in passport:
            key = pair.split(':')[0]
            value = pair.split(':')[1]
            if key == "byr":
                byr = int(value)
            if key == "iyr":
                iyr = int(value)
            if key == "eyr":
                eyr = int(value)
            if key == "hgt":
                hgt = value
            if key == "hcl":
                hcl = value
            if key == "ecl":
                ecl = value
            if key == "pid":
                pid = value
            if key == "cid":
                cid = value
#Check the last passport
if 0 not in (byr, iyr, eyr, hgt, hcl, ecl, pid):
    checkbyr = (byr>=1920 and byr<=2002)
    checkiyr = (iyr>=2010 and iyr<=2020)
    checkeyr = (eyr>=2020 and eyr<=2030)
    if checkbyr and checkiyr and checkeyr and checkhgt(hgt) and checkhcl(hcl) and checkecl(ecl) and checkpid(pid):
        ans1 += 1
        ans2 += 1
    else: 
        ans1 += 1

print("Part one:", ans1)
print("Part two:", ans2)