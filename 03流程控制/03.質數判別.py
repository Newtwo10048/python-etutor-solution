#3.質數判別
def isprime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n% i ==0:
            return False
    return True

n =int(input())
if(isprime(n)):
    print("YES")
else:
    print("NO")
#前面的語法