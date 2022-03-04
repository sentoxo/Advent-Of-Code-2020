'''
https://adventofcode.com/2020/day/3
What do you get if you multiply together the number of trees encountered on each of the listed slopes?
'''
treePos = []
treeLines = 0

with open(file='Day03/input.txt', mode='r') as file:
    y = 0
    while foo := file.readline():
        for x,a in enumerate(foo):
            if a == '#':
                treePos.append((x, y))
        y += 1
    treeLines = y

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

for slope in slopes:    
    tree = 0
    x=0
    y=0
    hit = 0
    while y<treeLines:
        if (x, y) in treePos:
            hit += 1
        x+=slope[0]
        y+=slope[1]
        if x>30:
            x = x - 31

    print(slope, 'hits: ', hit)