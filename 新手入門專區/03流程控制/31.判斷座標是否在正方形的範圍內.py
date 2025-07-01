#31.判斷座標是否在正方形的範圍內
ints = [int(x) for x in input().split()]
if ints[0]>=0 and ints[0]<=100:
    if ints[1]>=0 and ints[1]<=100:
        print("inside")
    else:
        print("outside")
else:
    print("outside")
#前面的語法