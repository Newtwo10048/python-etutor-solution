#12.期末成績
n = int(input())
m = 0
mn = 101
ave =0
p = 0
for i in range(n):
    num = int(input())
    if num>m:
        m = num
    elif num<mn:
        mn = num
    ave = ave + num 
    if num >= 60:
        p = p + 1
print(f"Max:{m}")
print(f"Min:{mn}")
print(f"Average:{round(ave/n,1)}")
print(f"Pass:{p}")
#前面的語法