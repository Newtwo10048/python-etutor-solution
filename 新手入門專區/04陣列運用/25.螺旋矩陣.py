#25.螺旋矩陣
ints = [int(x) for x in input().split(",")]
dic={
    (0,0):1
}
i=0
j=0
n = 1
p = ints[0]
if ints[1]==1:#右下左上
    for k in range(p-1):
        n = n + 1
        j = j + 1
        dic[(i,j)] = n
    while p !=0:
        if p != 0:
            for l in range(p-1):
                n = n + 1
                i = i + 1
                dic[(i,j)] = n
            for l in range(p-1):
                n = n + 1
                j = j - 1
                dic[(i,j)] = n
            p = p - 1
        if p !=0:
            for l in range(p-1):
                n = n + 1
                i = i - 1
                dic[(i,j)] = n
            for l in range(p-1):
                n = n + 1
                j = j + 1
                dic[(i,j)] = n
            p = p - 1
else:#下右上左
    for k in range(p-1):
        n = n + 1
        i = i + 1
        dic[(i,j)] = n
    while p !=0:
        if p != 0:
            for l in range(p-1):
                n = n + 1
                j = j + 1
                dic[(i,j)] = n
            for l in range(p-1):
                n = n + 1
                i = i - 1
                dic[(i,j)] = n
            p = p - 1
        if p !=0:
            for l in range(p-1):
                n = n + 1
                j = j - 1
                dic[(i,j)] = n
            for l in range(p-1):
                n = n + 1
                i = i + 1
                dic[(i,j)] = n
            p = p - 1
for a in range(ints[0]):
    for b in range(ints[0]):
        if b == ints[0]-1:
            print(f"{dic[(a,b)]:03}",end="")
        else:
            print(f"{dic[(a,b)]:03} ",end="")
    print()
#題目有問題