#3.計算正方形面積
from decimal import Decimal, ROUND_HALF_UP

n = input()
for i in range(int(n)):
    e = input()
    A = Decimal(e) * Decimal(e)
    A = A.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
    print(A)
#四捨五入：
#import decimal 導入四捨五入模組
#from decimal import Decimal, ROUND_HALF_UP 這段為更精準地導入
#x.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP) x.quantiz(保留幾位,進位條件)
#Decimal("0.1")是保留小數第一位
#ROUND_HALF_UP是傳統四捨五入
