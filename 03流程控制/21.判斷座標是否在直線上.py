#21.判斷座標是否在直線上
num = input()
parts = num.split()
ints1 = [int(x) for x in parts]
num = input()
parts = num.split()
ints2 = [int(x) for x in parts]

if ints1[0]*ints2[0]+ints1[1]*ints2[1]+ints1[2]==0:
    print("YES")
else:
    print("NO")
#前面的語法