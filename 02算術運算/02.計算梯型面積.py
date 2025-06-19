#2.計算梯型面積
num  =input()
parts = num.split()
ints = [int(x) for x in parts]

A = (ints[0] +ints[1]) * ints[2] /2
print(f"Trapezoid area:{A:.1f}")
#跟計算三角形一樣
