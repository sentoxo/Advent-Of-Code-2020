'''
https://adventofcode.com/2020/day/9
What is the encryption weakness in your XMAS-encrypted list of numbers?
'''

xmas = 15690279
data = []

file = open(file='Day09/input.txt', mode='r')
for line in file.readlines():
    data.append(int(line))

biggest = 0
lowest = 99999999999

for i in range(len(data)):
    biggest = 0
    n1 = data[i]
    sum = n1
    for n2 in data[i:]:
        if n1 == n2:
            continue
        if n2>biggest:
            biggest = n2
        if n2<lowest:
            lowest = n2
        sum+=n2
        if sum == xmas:
            print(i,n1,n2)

