'''
https://adventofcode.com/2020/day/6
For each group, count the number of questions to which everyone answered "yes". 
What is the sum of those counts?
'''
sum=0
with open(file='Day06/input.txt', mode='r') as file:
    lines = file.read().split('\n\n')
    print(len(lines))
    for line in lines:
        line = line.replace('\n',' ')
        data = line.split(' ')
        #print(data)

        qu=0
        for char in data[0]:
            c=0
            for i in range(1,len(data)):
                if char in data[i]:
                    c+=1
            if c == (len(data)-1):
                qu+=1
                
        print(data,qu)
        

        sum+=qu
print(sum)
