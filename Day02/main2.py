'''
https://adventofcode.com/2020/day/2
How many passwords are valid according to the new interpretation of the policies?
'''
valided = 0

with open(file='Day02/input.txt', mode='r') as file:
    for line in file:
        foo = line.split(' ')

        lowN, highN = foo[0].split('-')
        char = foo[1][0]
        password = foo[2]

        
        if password[int(lowN)-1] == char or password[int(highN)-1] == char:
            if not (password[int(lowN)-1] == char and password[int(highN)-1] == char):
                valided += 1
                print(lowN, highN, char, password)

        
    print(valided)