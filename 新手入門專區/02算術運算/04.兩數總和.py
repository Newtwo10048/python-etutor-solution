#4.兩數總和
n = input()
for i in range(int(n)):
    num = input()
    parts = num.split()
    ints = [int(x) for x in parts]
    print(sum(ints))
#sum(數字容器,起始值)，sum(ints)將ints裡的所有數字加起來
