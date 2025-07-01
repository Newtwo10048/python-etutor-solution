#25.計算兩點距離
num =input()
parts = num.split()
ints1 = [int(x) for x in parts]
num =input()
parts = num.split()
ints2 = [int(x) for x in parts]
print(f"{((ints1[0]-ints2[0])**2+(ints1[1]-ints2[1])**2)**0.5:.2f}")
#前面的語法