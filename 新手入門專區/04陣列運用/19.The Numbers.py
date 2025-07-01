#19.The Numbers
ints = [x for x in input().split()]
count = 0
for i in range(len(ints[1])-len(ints[0])+1):
    a = True
    for j in range(len(ints[0])):
        if ints[0][j] != ints[1][i+j]:
            a = False
    if a:
        count = count + 1
print(count)
#前面的語法