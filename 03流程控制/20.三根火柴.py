#20.三根火柴
num = input()
parts = num.split()
ints = [int(x) for x in parts]

if ints[0]+ints[1]<=ints[2]:
    print("Not Triangle")
elif ints[0]+ints[2]<=ints[1]:
    print("Not Triangle")
elif ints[1]+ints[2]<=ints[0]:
    print("Not Triangle")
elif ints[0]**2==ints[1]**2+ints[2]**2:
    print("Right Triangle")
elif ints[1]**2==ints[0]**2+ints[2]**2:
    print("Right Triangle")
elif ints[2]**2==ints[0]**2+ints[1]**2:
    print("Right Triangle")
elif ints[0]**2>ints[1]**2+ints[2]**2:
    print("Obtuse Triangle")
elif ints[1]**2>ints[0]**2+ints[2]**2:
    print("Obtuse Triangle")
elif ints[2]**2>ints[0]**2+ints[1]**2:
    print("Obtuse Triangle")
elif ints[0]**2<ints[1]**2+ints[2]**2 and ints[1]**2<ints[0]**2+ints[2]**2 and ints[2]**2<ints[0]**2+ints[1]**2:
    print("Acute Triangle")
#這題需要注意判別順序：
#舉例：(1,1,2)這不是三角形(因為1+1=2)
#如果先判別是不是鈍角三角形(1**2 + 1**2 < 2**2)，就會被辨為鈍角
#所以判別順序：
#1.是否為三角形：
#2.是否其他三角形(順序不影響)