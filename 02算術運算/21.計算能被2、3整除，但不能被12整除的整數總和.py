#21.計算能被2、3整除，但不能被12整除的整數總和
n = int(input())
re =0
for i in range(n):
    if i%6==0:
        if i%12!=0:
            re = re +i
print(re)
#前面的語法