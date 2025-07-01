#10.投販賣機
n = int(input())
ints = [int(x) for x in input().split()]
value = int(input())
num = [0]*n
re = []
def dfs(depth,combo,total):
    if depth == n:#搜索到最後一種硬幣
        if total == value:#確定組合正確
            re.append(combo)
        return
    for i in range(value//ints[depth] + 1):#最多的硬幣數
        if total + i * ints[depth] <= value:#避免超過目標金額，雖然後面也會被篩掉，但這裡可以減少一些無用節點
            dfs(depth+1,combo + [i],total + i * ints[depth])
dfs(0,[],0)

for r in re:
    print(f"({r[0]}",end="")
    for i in range(1,n):
        print(f",{r[i]}",end = "")
    print(")")
#這裡運用了dfs深度優先搜索，花多一點篇幅紀錄
#dfs就是先從子節點開始遍歷：
#dfs用遞迴，depth是硬幣值的索引值
#combo是硬幣組合，也就是節點
#total是當前硬幣組合的金額總和