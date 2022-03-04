'''
https://adventofcode.com/2020/day/2
How many passwords are valid according to their policies?
'''
valided = 0

with open(file='Day02/input.txt', mode='r') as file:
    for line in file:
        foo = line.split(' ')

        lowN, highN = foo[0].split('-')
        char = foo[1][0]
        password = foo[2]

        c = 0
        p = password.find(char)
        while p>=0:
            c += 1
            p = password.find(char, p+1)
        print(lowN, highN, c, char, password)

        if c <= int(highN) and c >= int(lowN):
            valided += 1
        
    print(valided)