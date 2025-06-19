#24.計算階乘
for i in range(int(input())):
    n = int(input())
    re = 1
    for i in range(n):
        re = re * (i+1)
    print(re)
#前面的語法