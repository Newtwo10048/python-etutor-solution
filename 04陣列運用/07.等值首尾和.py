#7.等值首尾和
n = int(input())
ints = [int(x) for x in input().split()]
count = 0
pre = 0
suf = 0
for i in range(n):
    pre = pre + ints[i]
    suf = suf + ints[n-1-i]
    if pre == suf:
        count = count + 1
    
print(count)
#前面的語法