'''
https://adventofcode.com/2020/day/12
What is the Manhattan distance between that location and the ship's starting position?
'''


x = 0
y = 0
waypontX = 10
waypontY = 1
facing = 90

file = open(file='Day12/input.txt', mode='r')

for command in file.readlines():
    print(command, y, x)
    number = int(command[1:])
    if command[0] == 'N':
        waypontY += number
    elif command[0] == 'S':
        waypontY += -number
    elif command[0] == 'E':
        waypontX += number
    elif command[0] == 'W':
        waypontX += -number
    elif command[0] == 'R':
        for i in range(0, number,90):
            buffX = waypontX
            waypontX = waypontY
            waypontY = -buffX
    elif command[0] == 'L':
        for i in range(0, number,90):
            buffY = waypontY
            waypontY = waypontX
            waypontX = -buffY
    elif command[0] == 'F':
        x+=number*waypontX
        y+=number*waypontY

print(x,y,abs(x)+abs(y))