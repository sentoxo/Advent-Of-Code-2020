'''
https://adventofcode.com/2020/day/11
How many seats end up occupied?
'''

layout = []
layoutCopy = []

with open(file='Day11/input.txt', mode='r') as file:
    y = 0
    while foo := file.readline():
        layout.append([])
        layoutCopy.append([])
        for a in foo:
            if a == '#':
                layout[y].append('#')
                layoutCopy[y].append('#')
            elif a == 'L':
                layout[y].append('L')
                layoutCopy[y].append('L')
            elif a == '.':
                layout[y].append('.')
                layoutCopy[y].append('.')
        y += 1

#print(layout)
def debug(mes):
    if isinstance(mes, list):
        for a in mes:
            for b in a:
                print(b, end='')
            print('')
    print('-------------')


def copy3D(arr1, arr2):
    #Copy from arr2 to arr1
    for y in range(len(arr2)):
        for x in range(len(arr2[0])):
            arr1[y][x] = arr2[y][x]


def check(y, x, b):
    c = 0
    
    try:
        for i in range(100):
            if layout[y][x+1+i] == 'L':
                break
            if layout[y][x+1+i] == '#':
                c+=1
                break
    except IndexError:
        pass

    for i in range(100):
        if x-1-i < 0:
            break
        if layout[y][x-1-i] == 'L':
                break
        if layout[y][x-1-i] == '#' and x>0: 
            c+=1
            break

    try:
        for i in range(100):
            if layout[y+1+i][x] == 'L':
                break
            if layout[y+1+i][x] == '#':
                c+=1
                break
    except IndexError:
        pass

    for i in range(100):
        if y-1-i < 0:
            break
        if layout[y-1-i][x] == 'L':
                break
        if layout[y-1-i][x]  == '#' and y>0:
            c+=1
            break

    try:
        for i in range(150):
            if layout[y+1+i][x+1+i] == 'L':
                break
            if layout[y+1+i][x+1+i] == '#':
                c+=1
                break
    except IndexError:
        pass

    try:
        for i in range(150):
            if x-1-i < 0:
                break
            if layout[y+1+i][x-1-i] == 'L':
                break
            if layout[y+1+i][x-1-i] == '#' and x>0:
               c+=1
               break
    except IndexError:
        pass

    try:
        for i in range(150):
            if y-1-i < 0:
                break
            if layout[y-1-i][x+1+i] == 'L':
                break
            if layout[y-1-i][x+1+i] == '#' and y>0:
                c+=1
                break
    except IndexError:
        pass

    for i in range(150):
        if y-1-i < 0 or x-1-i < 0:
            break
        if layout[y-1-i][x-1-i] == 'L':
                break
        if layout[y-1-i][x-1-i] == '#' and x>0 and y>0:
            c+=1
            break
    
    if c >= b:
        return True
    else:
        return False
    

ocu=0
for y in range(len(layout)):
        for x in range(len(layout[0])):
            if layout[y][x] == '#':
                ocu+=1


for ite in range(1000):

    for y in range(len(layout)):
        for x in range(len(layout[0])):

            if ite == 3 and y==0 and x==3:
                breakpoint

            if layout[y][x] == 'L':
                if not check(y, x, 1):
                    layoutCopy[y][x] = '#'

            elif layout[y][x] == '#':
                if check(y, x, 5):
                    layoutCopy[y][x] = 'L'

    debug(layoutCopy)
    copy3D(layout, layoutCopy)

    newocu = 0
    for y in range(len(layout)):
        for x in range(len(layout[0])):
            if layout[y][x] == '#':
                newocu+=1

    if newocu == ocu:
        debug(layout)
        print(ite, newocu)
        break
    else:
        ocu = newocu