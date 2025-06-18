#13.BMI計算
num =input()
parts = num.split()
ints = [int(x) for x in parts]
print(f"{ints[0]/((ints[1]*0.01)**2):.2f}")
#前面的語法