#15.電話費計算
n=int(input())
if n <=800:
    print(round(n*0.9,1))
elif n<1500:
    print(round(n*0.81,1))
else:
    print(round(n*0.711,1))
#前面的語法