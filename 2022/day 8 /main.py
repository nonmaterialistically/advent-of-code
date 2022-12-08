file = open('input.txt', 'r')
Lines = [list(line.strip()) for line in file.readlines()]

columns = [line for line in zip(*Lines)]

visible = 0
visible += (len(Lines[0])*2)+(len(columns[0])*2)-4

visibility = 0

def count_visible_trees(tree_list, tree):
    countvis = 0
    if len(tree_list) != 0:
        for h in tree_list:
            if int(h) < tree:
                countvis += 1
            elif int(h) >= tree:
                countvis += 1
                break
        return countvis
    else:
        return 0

def visible_from(tree_list, tree):
    if len(tree_list) != 0 and all(int(h) < tree for h in tree_list):
        return True
    else:
        False

for r, line in enumerate(Lines):
    if r == 0 or r == len(Lines[0])-1:
        next
    else:
        for c, column in enumerate(columns):
            if c == 0 or c == len(columns[0])-1:
                next
            else:
                tree = int(line[c])
                #Part 1
                if visible_from(line[0:c], tree) or visible_from(line[c+1:], tree) or visible_from(column[0:r], tree) or visible_from(column[r+1:], tree):
                    visible += 1
                #Part 2
                left = right = top = bottom = 0
                left = count_visible_trees(list(reversed(line[0:c])), tree)
                right = count_visible_trees(line[c+1:], tree)
                top = count_visible_trees(list(reversed(column[0:r])), tree)
                bottom = count_visible_trees(column[r+1:], tree)
                visibility = max(visibility, left*right*top*bottom)
print(visible)
print(visibility)