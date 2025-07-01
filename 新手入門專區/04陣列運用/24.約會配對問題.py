#24.約會配對問題
n = int(input())
dic = {}
boy = [True] * n
girl = [True] * n
for i in range(n):
    ints = [int(x) for x in input().split()]
    for j in range(n):
        dic[ints[j]] = (i,j)
for  i in range(n):
    m = 0
    for num in dic:
        if m < num and boy[dic[num][0]] and girl[dic[num][1]]:
            m = num
    print(f"boy {dic[m][0]+1} pair with girl {dic[m][1]+1}")
    boy[dic[m][0]] =False
    girl[dic[m][1]] =False
#for num in dic:，num是健值，會按照插入鍵值的順序執行迴圈