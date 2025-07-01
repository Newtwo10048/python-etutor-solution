#15.串珠子
ints = [int(x) for x in input().split()]
dp = [0]*101
for i in ints:
    dp[i] = dp[i] + 1
for i in range(101):
    if dp[i] == 2:
        print(i)
#dp，以空間換取時間