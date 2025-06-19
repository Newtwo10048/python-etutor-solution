#28.判斷數值
def isprime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
n =int(input())
if n % 2==0:
    print("even",end="")
else:
    print("odd",end="")
if isprime(n):
    print(" prime")  
else:
    print()
#前面的代碼