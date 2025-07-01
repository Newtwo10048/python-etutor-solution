#16.Armstrong數
n = (input())
if int(n) == ((int(n[0])**3) + (int(n[1])**3) + (int(n[2])**3)):
    print("YES")
else:
    print("NO")
#注意 n = input() 的n是字串(string) ，如果n是int，則無法使用n[0]提出百位數