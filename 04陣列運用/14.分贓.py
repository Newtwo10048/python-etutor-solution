#14.分贓
n = int(input())
ints = [int(x) for x in input().split()]
total = sum(ints)
m = [1000]
def dfs(d,value):
    if d == n:
        if abs(total-value*2)<abs(total - 2 * m[0]):
            m[0] = value
        return
    dfs(d+1,value + ints[d])
    dfs(d+1,value)

dfs(0,0)
print(abs(m[0]*2 - total))
#前面的語法
#dfs，遞迴的兩個是放進一組或另一組(但計算時只看一組，所以放入另一組相當於不放進)