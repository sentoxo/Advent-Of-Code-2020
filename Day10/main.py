'''
https://adventofcode.com/2020/day/10
What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?
'''

# I did this in spreadsheet...

file = open(file='Day10/input.txt', mode='r')

arr=[]
for line in file.readlines():
    arr.append(int(line))
arr.append(0)

arr.sort()

DP= {}

def dp(i):
    if i==len(arr)-1:
        return 1
    if i in DP:
        return DP[i]
    ans = 0
    for j in range(i+1, len(arr)):
        if arr[j]-arr[i] <= 3:
            ans += dp(j)
    DP[i] = ans
    return ans

print(dp(0))