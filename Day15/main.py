'''
https://adventofcode.com/2020/day/15
Given your starting numbers, what will be the 2020th number spoken?
'''

d = {0:1, 3:2, 4:3}
lastD = 6


for i in range(4,11,1):
    if lastD in d:
        d[i-d[lastD]] = i
        print(i-d[lastD])
        lastD = i-d[lastD]
    else:
        d[0] = i
        lastD = 0
        print(i, 0)
    


