#20.最大質數問題
def isprime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n% i ==0:
            return False
    return True
n =int(input())
re = 2
for i in range(n):
    if(isprime(i)):
        re = i
print(re)
#這裡題目要的小於不包含該數，isprime(i+1)是錯的