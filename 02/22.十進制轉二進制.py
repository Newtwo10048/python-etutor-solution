#22.十進制轉二進制
n =int(input())
if n>=0:
    print(0,end = "")
    for i in range(7):
        print((n//2**(6-i))%2,end = "")
    print()
else:
    n = (1 << 8) + n
    for i in range(8):
        print((n//2**(7-i))%2,end = "")
    print()
#可以用f-string
#正數print(f"{n:08b}")
#負數則先n = (1 << 8) + n再print(f"{n:08b}")