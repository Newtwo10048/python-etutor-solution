#29.我想要聯誼
n = int(input())
num = [x for x in input().split()]
l = input()
count =0
for i in range(n):
    fit = True
    for j in range(len(l)):
        singlefit = False
        for k in range(3):
            if l[j]==num[i][k]:
                singlefit = True
        if singlefit==False:
            fit=False
    if fit:
        count=count+1
print(count)
#注意這裡的num[i][k]是num容器地索引值i的索引值k的字符
#例num = {abc,def}
#num[0][2] = "c"