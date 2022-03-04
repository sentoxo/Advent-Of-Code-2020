'''
https://adventofcode.com/2020/day/5
What is the highest seat ID on a boarding pass?
'''

file = open(file='Day05/input.txt', mode='r')
highest = 0
for line in file.readlines():
    low = 0
    for i in range(7):
        if line[i] == 'B':
            low += 64 / 2**i
    low2 = 0
    for i in range(8,10):
        if line[i] == 'R':
            low2 += 4 / 2**(i-8)
    id = low*8+low2
    if id > highest:
        highest = id
print(highest)