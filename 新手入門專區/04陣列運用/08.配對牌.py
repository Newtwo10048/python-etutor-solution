#8.配對牌
n = int(input())
ints = [int(x) for x in input().split()]
count =0
for i in range(n):
    ints2 = [int(x) for x in input().split()]
    for j in range(5):
        for k in range(5):
            if ints[j] == ints2[k]:
                count = count + 1
                ints[j] =-1
print(count)
#前面的語法