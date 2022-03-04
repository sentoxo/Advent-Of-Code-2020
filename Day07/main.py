'''
https://adventofcode.com/2020/day/7
How many bag colors can eventually contain at least one shiny gold bag?
'''
dic = {}

def F(color: str):
    if color == "dark olive bag":
        breakpoint
    if color == "shiny gold bag":
        return True
    arr = dic[color]
    for foo in arr:
        if F(foo[1]):
            return True
    return False

file = open(file='Day07/test.txt', mode='r')
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

N=0
for color in dic:
    print(color, F(color))
    if F(color):
        N+=1
print(N-1)

