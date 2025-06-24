#27.平面魔方
ints = input().split()
n = int(ints[0])
ma = [[0 for i in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        ma[i][j] = i * n + j + 1
if ints[1]=="L":
    for i in range(n):
        for j in range(n):
            if j != n -1: 
                print(ma[j][n-1-i],end=" ")
            else:
                print(ma[j][n-1-i],end="")
        print()
elif ints[1]=="R":
    for i in range(n):
        for j in range(n):
            if j != n -1:
                print(ma[n-1-j][i],end=" ")
            else:
                print(ma[n-1-j][i],end="")
        print()
else:
    for i in range(n):
        for j in range(n):
            if j != n -1:
                print(ma[n-i-1][j],end=" ")
            else:
                print(ma[n-i-1][j],end="")
        print()
#前面的語法