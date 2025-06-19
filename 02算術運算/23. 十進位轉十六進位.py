#23. 十進位轉十六進位
n = int(input())
while n >= 16:
    if n//16==10:
        print("A",end="")
    elif n//16==11:
        print("B",end="")
    elif n//16==12:
        print("C",end="")
    elif n//16==13:
        print("D",end="")
    elif n//16==14:
        print("E",end="")
    elif n//16==15:
        print("F",end="")
    else:
        print(n//16,end="")
    n = n % 16
if n==10:
    print("A",end="")
elif n==11:
    print("B",end="")
elif n==12:
    print("C",end="")
elif n==13:
    print("D",end="")
elif n==14:
    print("E",end="")
elif n==15:
    print("F",end="")
else:
    print(n,end="")
print()
#前面的語法