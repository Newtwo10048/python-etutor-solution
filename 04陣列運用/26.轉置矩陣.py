#26.轉置矩陣
ints = [int(x) for x in input().split()]
dic = {}
for i in range(ints[0]):
    ints2 = [int(x) for x in input().split()]
    for j in range(ints[1]):
        dic[(i,j)] = ints2[j]
for j in range(ints[1]):
    for i in range(ints[0]):
        if i != ints[0]-1:
            print(f"{dic[(i,j)]} ",end="")
        else:
            print(f"{dic[(i,j)]}",end="")
    print()
#我覺得雖然程式是對的，但應該使用矩陣來寫：
#matrix = [[0 for _ in range(4)] for _ in range(3)]宣告
#for row in matrix:
#    for value in row:
#        print(value, end=" ")
#    print()輸出
#matrix[i][j]索引值
#---B解法
ints = [int(x) for x in input().split()]
ma = [[0 for i in range(ints[1])] for i in range(ints[0])]

for i in range(ints[0]):
    ints2 = [int(x) for x in input().split()]
    for j in range(ints[1]):
        ma[i][j] = ints2[j]
for j in range(ints[1]):
    for i in range(ints[0]):
        if i != ints[0]-1:
            print(f"{ma[i][j]} ",end="")
        else:
            print(f"{ma[i][j]}",end="")
    print()
#---