#28.刪除數字
s,k= input().split(",")
k = int(k)
stack = []
for d in s:
    while k>0 and stack and stack[-1] > d:
        stack.pop()
        k = k - 1
    stack.append(d)
while k > 0:
    stack.pop()
    k = k - 1
re = "".join(stack).lstrip("0") or "0"
print(re)
#用stack來將比較大的數字刪去pop()，將小的數append()
#如果有多的就繼續pop()
#"".join(stack) 以""的字串將stack裡的元素串成字串
#.lstrip("0")是字串裡的""裡的元素刪除
#or "0" 當"".join(stack).lstrip("0") 就輸出"0"
#---錯誤的
s,k= input().split(",")
k = int(k)
ind = 1
bo = -1
while k > 0 and bo < 1:
    bo = -1
    n = 10
    ind = -1
    for i in range(k+1):
        if n > int(s[i]) and int(s[i]) >0:
            n = int(s[i])
            ind = i
            bo = bo + 1
    print(s[ind],end="")
    s = s[ind+1:]
    k = k - ind

for _ in range(k):
    m = 0
    index = 0
    for i in range(len(s)):
        if m < int(s[i]):
            m = int(s[i])
            index = i
    s = s[:index] + s[index+1:]
print(s)
#---