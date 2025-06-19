#18.參加TOEIC
from decimal import Decimal, ROUND_HALF_UP
M =0
count9 =0
count67 =0
total = 0
num = int(input())
for i in range(num):
    n = int(input())
    if M<n:
        M = n
    if n<=700 and n>=600:
        count67 = count67 + 1
    elif n>=900:
        count9 = count9 + 1
    total = total + n
print(M)
print(count9)
print(count67)
total = Decimal(total) / num
print(total.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))
#前面的語法