#11.成績分級系統
n = int(input())
ints = [0]*5
for i in range(n):
    s = int(input())
    if s>=90:
        ints[0] = ints[0] + 1
    elif s>=80:
        ints[1] = ints[1] + 1
    elif s>=70:
        ints[2] = ints[2] + 1
    elif s>=60:
        ints[3] = ints[3] + 1
    else:
        ints[4] = ints[4] + 1
print(f"優等 {ints[0]}")
print(f"甲等 {ints[1]}")
print(f"乙等 {ints[2]}")
print(f"丙等 {ints[3]}")
print(f"不及格 {ints[4]}")
#前面的語法