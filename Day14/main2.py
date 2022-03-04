'''
https://adventofcode.com/2020/day/14
What is the sum of all values left in memory after it completes?
'''

file = open(file='Day14/input.txt', mode='r')
import pprint

memory = {}
actualBitmask = ''
sum = 0

def printBits(number: int, numberOfBits = 32) -> str:
    R = ''
    for i in range(numberOfBits, 0, -1):
        if number & (1 << i-1):
            print(1,end='')
            R+='1'
        else:
            print(0, end='')
            R+='0'
    print('  ', number)
    return R

def setValue(value: int, adress: str):
    if adress.count('X') == 0:
        memory[adress] = value
        print('setValue: ', adress, value)
        return
    else:
        setValue(value, adress.replace('X', '0', 1))
        setValue(value, adress.replace('X', '1', 1))


while line := file.readline():
    if not line.find('mask'):
        a, bitmask = line.split('=')
        actualBitmask = bitmask.strip()
    else:
        where, value = line.split('=')
        where = where.split('[')[1][0:-2]   # mem[256]  =>  mem,256]  =>  256]  =>  256   
        value = int(value)
        #print(where, value)

        n = 0

        where = printBits(int(where), 36)

        adress=[]
        for i in range(0, 36, 1):
            if actualBitmask[i] == 'X':
                adress.append('X')
                #n |= value & (1 << i)
            elif actualBitmask[i] == '1':
                adress.append('1')
                #n |= (1 << i)
            elif actualBitmask[i] == '0':
                adress.append(where[i])

        setValue(value,''.join(adress))

        '''
        printBits(value,36)
        print(actualBitmask)
        printBits(n, 36)
        print('')
        '''

        
for a in memory.values():
    sum+=a
#print(memory.values())
print(sum)
#pprint.pprint(memory)
