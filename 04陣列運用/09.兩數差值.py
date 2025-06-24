#9.兩數差值
ints = [int(x) for x in input().split(",")]
M = sorted(ints,reverse=True)
N = sorted(ints)
Max = 0
Min = 0
for i in range(len(M)):
    Max = Max + M[i]*(10**(len(M)-i-1))
    Min = Min + N[i]*(10**(len(M)-i-1))
print(Max-Min)
#sorted(陣列容器)，回傳一個陣列