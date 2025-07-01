#19.判斷是否能構成三角形
num =input()
parts = num.split()
ints = [int(x) for x in parts]
if ints[0]+ints[1]>ints[2]:
    if ints[0]+ints[2]>ints[1]:
        if ints[1]+ints[2]>ints[0]:
            print("fit")
        else:
            print("unfit")
    else:
        print("unfit")
else:
    print("unfit")
#前面的語法