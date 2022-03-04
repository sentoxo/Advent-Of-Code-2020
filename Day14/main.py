'''
https://adventofcode.com/2020/day/14
What is the sum of all values left in memory after it completes?
'''

file = open(file='Day14/input.txt', mode='r')

memory = {}
actualBitmask = ''
sum = 0

def printBits(number: int, numberOfBits = 32):
    for i in range(numberOfBits, 0, -1):
        if number & (1 << i-1):
            print(1,end='')
        else:
            print(0, end='')
    print('  ', number)

while line := file.readline():
    if not line.find('mask'):
        a, bitmask = line.split('=')
        actualBitmask = bitmask.strip()
    else:
        where, value = line.split('=')
        where = where.split('[')[1][0:-2]   # mem[256]  =>  mem,256]  =>  256]  =>  256   
        value = int(value)
        where = int(where)
        #print(where, value)

        n = 0
        actualBitmask = actualBitmask[::-1]
        for i in range(0, 36, 1):
            if actualBitmask[i] == 'X':
                n |= value & (1 << i)
            elif actualBitmask[i] == '1':
                n |= (1 << i)
            elif actualBitmask[i] == '0':
                pass
        actualBitmask = actualBitmask[::-1]
        printBits(value,36)
        print(actualBitmask)
        printBits(n, 36)
        print('')

        memory[where] = n
        
for a in memory.values():
    sum+=a
print(sum)
