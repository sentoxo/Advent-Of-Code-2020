'''
https://adventofcode.com/2020/day/12
What is the Manhattan distance between that location and the ship's starting position?
'''

x = 0
y = 0
facing = 90

file = open(file='Day12/input.txt', mode='r')

for command in file.readlines():
    print(command, y, x)
    number = int(command[1:])
    if command[0] == 'N':
        y += number
    elif command[0] == 'S':
        y += -number
    elif command[0] == 'E':
        x += number
    elif command[0] == 'W':
        x += -number
    elif command[0] == 'L':
        facing += -number
        if facing < 0:
            facing += 360
    elif command[0] == 'R':
        facing += number
        if facing >= 360:
            facing += -360
    elif command[0] == 'F':
        if facing == 0:
           y += number
        elif facing == 90:
            x += number
        elif facing == 180:
            y += -number
        elif facing == 270:
            x += -number

print(x,y,abs(x)+abs(y))