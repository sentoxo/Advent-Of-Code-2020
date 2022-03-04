'''
https://adventofcode.com/2020/day/6
What is the sum of those counts?
'''
sum=0
with open(file='Day06/input.txt', mode='r') as file:
    lines = file.read().split('\n\n')
    print(len(lines))
    for line in lines:
        line = line.replace('\n',' ')
        data = line.split(' ')
        print(data)

        q = []

        for word in data:
            for char in word:
                if not (char in q) :
                    q.append(char)
        
        sum+=len(q)
print(sum)
