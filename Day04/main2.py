'''
https://adventofcode.com/2020/day/4
In your batch file, how many passports are valid?
'''
valided = 0
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
with open(file='Day04/input.txt', mode='r') as file:
    lines = file.read().split('\n\n')
    for line in lines:
        line = line.replace('\n',' ')
        data = line.split(' ')
        N = 0
        for field in data:
            if field[0:3] in fields:
                N += 1
        if N < 7:
            continue
        for field in data:
            word, info = field.split(':')
            print(word, info)
            if word == 'byr':
                if not (int(info)>=1920 and int(info)<=2002):
                    N = 0
                    break
            elif word == 'iyr':
                if not (int(info)>=2010 and int(info)<=2020):
                    N = 0
                    break
            elif word == 'eyr':
                if not (int(info)>=2020 and int(info)<=2030):
                    N = 0
                    break
            elif word == 'hgt':
                hgt = info.split('cm')
                if len(hgt) == 2:
                    if not (int(hgt[0])>=150 and int(hgt[0])<=193):
                        N = 0
                        break
                else:
                    hgt = info.split('in')
                    if not (int(hgt[0])>=59 and int(hgt[0])<=76):
                        N = 0
                        break
            elif word == 'hcl':
                if not info[0] is '#':
                    N = 0
                    break
                val = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
                for i in range(1,7):
                    if not info[i] in val:
                        N = 0
                        break
            elif word == 'ecl':
                if not info in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    N = 0
                    break
            elif word == 'pid':
                if not len(info)==9:
                    N = 0
                    break
                for i in range(9):
                    if not info[i] in ['0','1','2','3','4','5','6','7','8','9']:
                        N = 0
                        break
        if N > 0:
            valided+=1

            
    print(valided)