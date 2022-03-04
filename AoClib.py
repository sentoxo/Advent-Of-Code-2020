
def printMap(map: list):
    '''
    Printing two-dimensional array on screen

    :param map: two-dimensional list
    '''
    for x in map:
        for char in x:
            print(char, end='')
        print('')

def printBits(number: int, numberOfBits = 32):
    '''
    Printing integer in bits
    '''
    for i in range(numberOfBits, 0, -1):
        if number & (1 << i-1):
            print(1,end='')
        else:
            print(0, end='')
    print('  ', number)