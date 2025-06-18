#19.輾轉相除法
import math
num =input()
parts = num.split()
ints = [int(x) for x in parts]

print(math.gcd(ints[0],ints[1]))
#直接用math函式庫，math有math.lcm、math.exp(x)e的次方等等