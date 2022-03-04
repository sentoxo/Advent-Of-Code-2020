'''
https://adventofcode.com/2020/day/13
What is the ID of the earliest bus you can take to the airport multiplied by 
the number of minutes you'll need to wait for that bus?
'''
import math
file = open(file='Day13/input.txt', mode='r')

timestamp = int(file.readline())
busData = file.readline().split(',') 

smallest = 999999999999
winBus = 0
timeWait = 0

for bus in busData:
    if bus == 'x':
        continue
    bus = int(bus)
    a = math.floor(timestamp / bus)
    if (a*bus) == bus:
        print(a)
        break
    foo = a * bus + bus

    if foo < smallest:
        smallest = foo
        winBus = bus
        timeWait = foo - timestamp

print(winBus, timeWait*winBus)