'''
https://adventofcode.com/2020/day/3
Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?
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

tree = 0
x=0
y=0
hit = 0
while y<treeLines:
    if (x, y) in treePos:
        hit += 1
    x+=3
    y+=1
    if x>30:
        x = x - 31

print('hits: ', hit)