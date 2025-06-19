#22.判斷座標是否在圓形的範圍內
num = input()
parts = num.split()
ints = [int(x) for x in parts]

if ints[0]**2 + ints[1]**2<=10000:
    print("inside")
else:
    print("outside")
#前面的語法