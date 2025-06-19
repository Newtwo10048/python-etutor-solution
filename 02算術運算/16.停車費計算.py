#16.停車費計算
n1 =input()
parts1 = n1.split()
ints1 = [int(x) for x in parts1]
n2 = input()
parts2 = n2.split()
ints2 = [int(x) for x in parts2]

h = ints2[0] - ints1[0]
m = h*60 + ints2[1] - ints1[1]
m = m//30
if m <=4:
    print(m*30)
elif m <= 8:
    print(120+(m-4)*40)
else:
    print(280+(m-8)*60)
#前面的語法