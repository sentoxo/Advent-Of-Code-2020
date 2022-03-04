'''
https://adventofcode.com/2020/day/4
In your batch file, how many passports are valid?
'''
valided = 0
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
with open(file='Day04/input.txt', mode='r') as file:
    lines = file.read().split('\n\n')
    print(len(lines))
    for line in lines:
        line = line.replace('\n',' ')
        data = line.split(' ')
        N = 0
        for field in data:
            if field[0:3] in fields:
                N += 1
        if N >= 7:
            valided += 1
    print(valided)