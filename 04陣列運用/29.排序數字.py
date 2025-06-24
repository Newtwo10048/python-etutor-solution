#29.排序數字
n = int(input())
ints = [int(x) for x in input().split()]
a = int(input())
ints.append(a)
ints.sort()
re = ",".join(str(x) for x in ints)
print(re)
#前面的語法