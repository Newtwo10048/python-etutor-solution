#6.計算兩數和的平方值
n = input()
for i in range(int(n)):
    num = input()
    parts = num.split()
    ints = [int(x) for x in parts]
    print((ints[0]+ints[1])*(ints[0]+ints[1]))
#前面用過得語法
