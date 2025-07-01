#26.擲骰子遊戲
s =sum([int(x) for x in input().split()])
if s>9:
    print(f"{s} H")
else:
    print(f"{s} L")
#優化了一下，將：
#num = input()
#parts = num.split()
#ints = [int(x) for x in parts]
#整合成：
#ints = [int(x) for x in input().split()])