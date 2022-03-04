'''
https://adventofcode.com/2020/day/13
What is the earliest timestamp such that all of the listed bus IDs 
depart at offsets matching their positions in the list?
'''
import math
file = open(file='Day13/input.txt', mode='r')

timestamp = int(file.readline())
busData = file.readline().strip().split(',')

buses = []
busesI = []
W = 0

for i, bus in enumerate(busData):
    if bus == 'x':
        continue
    buses.append(int(bus))
    busesI.append((i,int(bus)))

busesI.sort(key=lambda tup: tup[1],reverse=True)
w = busesI[0][1]*busesI[1][1]


imprtantValue = 0

for i in range(0,999999999999, busesI[0][1]):
    if  (i-(busesI[0][0] - busesI[1][0])) % busesI[1][1] == 0:
        imprtantValue = i
        break

print(imprtantValue)

#My head... pain...
#This code is bad, but works, eventually...
for i in range(imprtantValue, 1012171816131164+w, w):
    if  (i-(busesI[0][0] - busesI[2][0])) % busesI[2][1] == 0:
        if  (i-(busesI[0][0] - busesI[3][0])) % busesI[3][1] == 0:
            if  (i-(busesI[0][0] - busesI[4][0])) % busesI[4][1] == 0:
                if  (i-(busesI[0][0] - busesI[5][0])) % busesI[5][1] == 0:
                    if  (i-(busesI[0][0] - busesI[6][0])) % busesI[6][1] == 0:
                        if  (i-(busesI[0][0] - busesI[7][0])) % busesI[7][1] == 0:
                            if  (i-(busesI[0][0] - busesI[8][0])) % busesI[8][1] == 0:
                                print('end:',i - 50)
                                imprtantValue = i
                                break

print(busesI)


for i in range(imprtantValue-50, imprtantValue+50, 1):
    print(i, end='')
    for a in [19,37,599,29,17,23,761,41,13]:
        if not i%a:
            print(' D ', end='')
        else:
            print(' . ', end='')
    if i == imprtantValue:
        print('  <--', end='')
    print('')
