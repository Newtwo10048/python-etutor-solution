#3.輸出反向數字
num = input()
for i in range(4):
    if i!=3:
        print(num[(3-i)],end=",")
    else:
        print(num[3-i])
#if 空格 加 條件式加 :
#else 也是加 :
#if i!=3:
#else:
#for i in range(n):
#i 是變數，從0到n-1。
