#27.九九乘法表
ints = [int(x) for x in input().split()]
for i in range(ints[0]):
    for j in range(ints[1]):
        print(f"{i+1}x{j+1}={(i+1)*(j+1)}")
#前面的語法