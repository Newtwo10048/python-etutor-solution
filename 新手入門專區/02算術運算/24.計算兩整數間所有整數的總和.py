#24.計算兩整數間所有整數的總和
n = int(input())
for i in range(n):
    num =input()
    parts = num.split()
    ints = [int(x) for x in parts]
    re = 0
    if ints[0]<ints[1]:
        for j in range(ints[0],ints[1]+1,1):
            re+=j
    else:
        for j in range(ints[1],ints[0]+1,1):
            re+=j
    print(re)
#range(小的數,大的數,間距)range(10,100,1)從10加1加到99