#12.成績分級
for i in range(int(input())):
    n = int(input())
    if n>=90 and n<=100:
        print("優等")
    elif n>=80 and n<=89:
        print("甲等")
    elif n>=70 and n<=79:
        print("乙等")
    elif n>=60 and n<=69:
        print("丙等")
    elif n>=0 and n<=60:
        print("不及格")
#前面的語法