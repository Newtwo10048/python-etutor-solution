#11.氣象預報
for i in range(int(input())):
    n = int(input())
    if n>=0 and n<=60:
        if n>37:
            print("避免外出")
        else:
            print("可依需要待在戶外")
    if n>=70 and n<=500:
        if n>150:
            print("避免外出")
        else:
            print("可依需要待在戶外")
#題目有問題