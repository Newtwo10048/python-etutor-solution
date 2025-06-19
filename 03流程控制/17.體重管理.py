#17.體重管理
for i in range(int(input())):
    n = int(input())
    if n>=28:
        print("肥胖")
    elif n>=24:
        print("體重過重")
    elif n>=18.5:
        print("正常")
    else:
        print("體重過輕")
#前面的語法