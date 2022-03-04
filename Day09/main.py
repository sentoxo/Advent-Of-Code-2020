'''
https://adventofcode.com/2020/day/9
What is the first number that does not have this property?
'''

PREAMBLE = 25
data = []

file = open(file='Day09/input.txt', mode='r')
for line in file.readlines():
    data.append(int(line))

for i in range(len(data)):
    if i < PREAMBLE:
        continue

    number = data[i]
    if i>=25: 
        size = (i-25)
    else: 
        size = 0
    isOk = False


    for n1 in data[size:i]:
        for n2 in data[size:i]:
            if n1 == n2: 
                continue
            if n1+n2 == number:
                #print(number,n1,n2)
                isOk = True
                break
    
    if not isOk:
        print(number)
