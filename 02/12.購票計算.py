#12.購票計算
n = int(input())
print(f"NT10={n//10}")
n = n%10
print(f"NT5={n//5}")
print(f"NT1={n%5}")
#前面的語法