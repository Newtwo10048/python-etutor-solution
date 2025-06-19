#7.找出最大值
M =0
for i in range(int(input())):
    num = int(input())
    if M<num:
        M = num
print(M)
#這裡優化了一下range(int(input()))，range(n)直接用int(input())輸入 