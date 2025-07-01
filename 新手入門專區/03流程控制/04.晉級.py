#4.晉級
n =int(input())

count = 0
for i in range(n):
    num =input()
    parts = num.split()

    if int(int(parts[1])>=60):
        print(parts[0])
        count = count +1
if count>=n/2:
    print("晉級")
else:
    print("失敗")
#題目有問題