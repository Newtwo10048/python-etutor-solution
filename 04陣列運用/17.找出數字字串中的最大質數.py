#17.找出數字字串中的最大質數
def isprime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n% i ==0:
            return False
    return True
n = input()
m = -1
for i in range(len(n)):
    for j in range(len(n)-i):
        p = int(n[j:j+1+i])
        if isprime(p):
            if p > m:
                m = p
if m == -1:
    print("No prime found")
else:
    print(m)
#前面的語法