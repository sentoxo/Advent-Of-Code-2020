'''
https://adventofcode.com/2020/day/1
Find the two entries that sum to 2020; 
what do you get if you multiply them together?
In your expense report, what is the product of the three entries that sum to 2020?
'''
arr = []

with open(file='Day01/input.txt', mode='r') as file:
    for line in file:
        arr.append(int(line))

for foo in arr:
    for foo2 in arr:
        for foo3 in arr:
            if foo + foo2 + foo3 == 2020:
                print(foo, foo2, foo3)
                print(foo * foo2 * foo3)