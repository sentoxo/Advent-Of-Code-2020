'''
https://adventofcode.com/2020/day/8
what value is in the accumulator?
'''



codeS = []
codeLen = 0

file = open(file='Day08/input.txt', mode='r')
for line in file.readlines():
    codeS.append(line)
    codeLen += 1

for i in range(codeLen):
    code = codeS.copy()
    #print('.',end='')
    if code[i][0:3] == 'jmp':
        code[i] = code[i].replace('jmp', 'nop')
    elif code[i][0:3] == 'nop':
        code[i] = code[i].replace('nop', 'jmp')
    acc = 0
    IP = 0
    codeExec = []
    while True:
        #print('pass')
        try:
            line = code[IP]
        except:
            print("Out of instructions")
            print(acc)
            break
    
        if IP in codeExec:
            break
        codeExec.append(IP)
    
        instruction, value = line.split(' ')
        value = int(value)
        #print(value)
    
        if instruction == 'acc':
            acc += value
        elif instruction == 'jmp':
            IP += value - 1
        elif instruction == 'nop':
            pass
        
        IP += 1
    
    