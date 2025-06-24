#4.前綴和
n = int(input())
ints = [int(x) for x in input().split()]
ints2 = [ints[0]] * n
print(ints2[0],end="")
for i in range(1,n):
    ints2[i] = ints2[i-1] + ints[i]
    print(f" {ints2[i]}",end="")
print()
#建立陣列：ints = [0]*n ，n個元素，值為0
#建立一個新陣列，並用陣列的第一個元素產生後續的元素