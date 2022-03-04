'''
https://adventofcode.com/2020/day/5
What is the ID of your seat?
'''

file = open(file='Day05/input.txt', mode='r')
highest = 0
arr = [False] * 128
for i in range(128):
    arr[i] = [False] * 8
t = ['BFFFBBFRRR','FFFBBBFRRR','BBFFBBFRLL']

for line in file.readlines():
    row = 0
    for i in range(7):
        if line[i] == 'B':
            row += int(64 / 2**i)
    
    column = 0
    for i in range(7, 10):
        if line[i] == 'R':
            column += int(4 / 2**(i-7))

    arr[row][column] = True

#print(arr)
print('-----')
for i,bo in enumerate(arr):
    for j,boo in enumerate(bo):
        if not boo:
            print(i,j)
