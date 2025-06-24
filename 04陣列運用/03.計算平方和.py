#3.計算平方和
ints = [int(x) for x in input().split()]
re = 0
for i in range(6):
    re = re + ints[i]**2
print(re)
#前面的語法