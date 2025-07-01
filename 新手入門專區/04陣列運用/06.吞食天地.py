#6.吞食天地
n = int(input())
ints = [int(x) for x in input().split()]
ints2 = [int(x) for x in input().split()]
re = 0
for i in range(ints2[0],ints2[1]+1):
    re = re + ints[i-1]
print(re)
#前面的語法