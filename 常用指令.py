#嚴格四捨五入
from decimal import Decimal, ROUND_HALF_UP
total = Decimal(input())
total.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
#輸入單個整數
n = int(input())
#輸入多個整數
ints = [int(x) for x in input().split()]
#for迴圈
for i in range(n):
    print()
#判別質數
def isprime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n% i ==0:
            return False
    return True
