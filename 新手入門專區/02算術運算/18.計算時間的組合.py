#18.計算時間的組合
n = int(input())
print(f"{n//86400} days")
n = n%86400
print(f"{n//3600} hours")
n = n%3600
print(f"{n//60} minutes")
print(f"{n%60} seconds")
#前面的語法