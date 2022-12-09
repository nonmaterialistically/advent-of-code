import re

file = open('input.txt', 'r')
Lines = [line.strip() for line in file.readlines()]

filesystem = dict()
result = dict()
part1 = 0

def insert_file(d, filepath, value):
    for key in filepath[:-1]:
        d = d.setdefault(key, {})
    d[filepath[-1]] = value

def calc_size(d):
    size = 0
    for key, value in d.items():
        if isinstance(value, dict):
            size += calc_size(value)
        else:
            size += int(value)
    return size

def dir_size_list(d, result, pos=''):
    for key, value in d.items():
        if isinstance(value, dict):
            result[pos+"/"+key] = calc_size(value)
            dir_size_list(value, result, key)

#build tree
for line in Lines:
    if line.startswith("$ cd "):
        search = re.search('\$ cd ([\w\/\.]+)', line)
        chdir = search.group(1)
        if chdir == "/":
            pwd = "/"
        elif chdir == "..":
            pwd = "/"+"/".join(pwd.split("/")[1:-2])+"/"
            if pwd == "//":
                pwd = "/"
        else:
            pwd = pwd + chdir + "/"
        p = filesystem
        for x in pwd.split("/")[1:-1]:
            p = p.setdefault(x, {})
    elif line.startswith("dir "):
        next
    elif line.startswith("$ ls"):
        next
    else:
        search = re.search('(\d+) ([\w\.]+)', line)
        size = search.group(1)
        filename = search.group(2)
        filepath = pwd.split("/")[1:-1]
        filepath.append(filename)
        insert_file(filesystem, filepath, size)

#part 1
dir_size_list(filesystem, result)
for key, value in result.items():
   if value < 100000:
        part1 += value
print(part1)

#part 2
unused_space = 70000000 - calc_size(filesystem)
needed_space = 30000000 - unused_space
marklist = sorted(result.items(), key=lambda x:x[1])
result = dict(marklist)
for n, pair in enumerate(result.items()):
    if pair[1] < needed_space:
        next
    else:
        print(pair)
        break