#7.比大小
num = input()
parts = num.split()
ints = [int(x) for x in parts]

if ints[0]>ints[1]:
    if ints[2]>ints[0]:
        print(ints[2])
    else:
        print(ints[0])
else:
    if ints[2]>ints[1]:
        print(ints[2])
    else:
        print(ints[1])
#兩次比較就能得出大小
