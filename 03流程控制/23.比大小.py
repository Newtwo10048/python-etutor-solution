#23.比大小
#---A解法
num = input()
parts = num.split()
ints = [int(x) for x in parts]
k = input()
if k == "Asc":
    for i in range(2):
        if ints[i]>ints[i+1]:
            swap = ints[i]
            ints[i] = ints[i+1]
            ints[i+1] = swap
    for i in range(2):
        if ints[i]>ints[i+1]:
            swap = ints[i]
            ints[i] = ints[i+1]
            ints[i+1] = swap
    for i in range(2):
        print(ints[i],end="<")
    print(ints[2])
elif k =="Desc":
    for i in range(2):
        if ints[i]<ints[i+1]:
            swap = ints[i]
            ints[i] = ints[i+1]
            ints[i+1] = swap
    for i in range(2):
        if ints[i]<ints[i+1]:
            swap = ints[i]
            ints[i] = ints[i+1]
            ints[i+1] = swap
    for i in range(2):
        print(ints[i],end=">")
    print(ints[2])
#---
#---B解法
num = input()
parts = num.split()
ints = [int(x) for x in parts]
k = input()
if k == "Asc":
    ints.sort()
    for i in range(2):
        print(ints[i], end="<")
    print(ints[2])
elif k == "Desc":
    ints.sort(reverse=True)
    for i in range(2):
        print(ints[i], end=">")
    print(ints[2])
#---
#使用bubble排序法，不用sort()就會變得很複雜
#int容器.sort()是升冪
#sort(revverse=True)則是降冪