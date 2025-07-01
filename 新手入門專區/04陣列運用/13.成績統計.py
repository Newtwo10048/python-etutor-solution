#13.成績統計
from decimal import Decimal, ROUND_HALF_UP
n = int(input())
ints = [0] * 3
for i in range(n):
    ints2 = [int(x) for x in input().split()]
    for j in range(3):
        ints[j] = ints[j] + ints2[j]
ints[0] = Decimal(ints[0])/n
ints[1] = Decimal(ints[1])/n
ints[2] = Decimal(ints[2])/n
ave = (ints[0]+ints[1]+ints[2])/3

print(ave.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP),end=" ")
print(ints[0].quantize(Decimal("0.1"), rounding=ROUND_HALF_UP),end=" ")
print(ints[1].quantize(Decimal("0.1"), rounding=ROUND_HALF_UP),end=" ")
print(ints[2].quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))
#前面的語法