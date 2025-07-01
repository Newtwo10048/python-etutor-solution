#22.英文斷字
width = int(input())
words = input().split()
lasp = width
for s in words:
    if lasp > len(s):
        if lasp - len(s)==0:
            print(f"{s}")
            lasp = width
        elif lasp - len(s)==1:
            print(f" {s}")
            lasp = width
        elif lasp - len(s)==2:
            print(f"  {s}")
            lasp = width
        else:
            if s == words[-1]:
                print(f"{s}")
            else:
                lasp = lasp - 1 -len(s)
                print(f"{s} ",end="")
    elif lasp == len(s):
        print(f"{s}")
        lasp = width
    else:
        print(f"{s[0:lasp-1]}-")
        print(f"{s[lasp-1:]} ",end="")
        lasp = width - ((len(s) + 2)-lasp)
    #print(f".{lasp}.",end="")
#可能題目有錯