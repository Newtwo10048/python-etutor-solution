#1.一維陣列反轉
n = int(input())
ints = [int(x) for x in input().split()]
print(ints[n-1])
for i in range(n-1):
    print(f" {ints[n-i-2]}",end="")
print()
#前面的語法