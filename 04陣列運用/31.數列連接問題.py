#31.數列連接問題
n = int(input())
stack = []
for _ in range(n):
    i = int(input())
    stack.append(i)
stack.sort(reverse = True)
re = "".join(str(x) for x in stack)
print(re)
#前面的語法