#5.差分
n = int(input())
ints = [int(x) for x in input().split()]
ints2 = [ints[0]]*n
print(ints2[0],end="")
for i in range(1,n):
    ints2[i] = ints[i]-ints[i-1]
    print(f" {ints2[i]}",end="")
print()
#前面的語法