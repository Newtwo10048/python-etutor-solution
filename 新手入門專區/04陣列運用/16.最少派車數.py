#16.最少派車數
n = int(input())
dp = [0] * 25
for i in range(n):
    ints = [int(x) for x in input().split()]
    for j in range(ints[0]+1,ints[1]+1):
        dp[j] = dp[j] + 1
m = 0
for k in range(25):
    if m<dp[k]:
        m = dp[k]
print(m)
#前面的語法