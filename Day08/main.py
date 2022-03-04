'''
https://adventofcode.com/2020/day/8
what value is in the accumulator?
'''

acc = 0

code = []
codeExec = []
codeLen = 0

file = open(file='Day08/input.txt', mode='r')
for line in file.readlines():
    code.append(line)
    codeLen += 1



IP = 0
while True:
    #print('pass')
    try:
        line = code[IP]
    except:
        print("Out of instructions")

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

print(IP, acc)