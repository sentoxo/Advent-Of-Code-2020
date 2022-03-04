'''
https://adventofcode.com/2020/day/7
How many individual bags are required inside your single shiny gold bag?
'''
dic = {}

def F(color: str):
    arr = dic[color]
    N = 0
    for foo in arr:
        N += foo[0] * F(foo[1])
    if N > 0:
        return N +1
    return 1
            

file = open(file='Day07/input.txt', mode='r')
for line in file.readlines():
    data = line.split('contain')
    color = data[0].strip().replace('bags','bag')
    contain = data[1].split(',')
    bags = []
    for con in contain:
        foo = con.strip()
        if foo[0] == 'n':
            pass
        else:
            bags.append((int(foo[0]), foo[1:].strip().replace('.','').replace('bags','bag')))
    dic[color] = bags


print(F('shiny gold bag')-1)
