#15.質數列表與總和
def isprime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n% i ==0:
            return False
    return True
n = int(input())
p =1
i = 3
S = 2
print("2",end = "")
while p<n:
    if(isprime(i)):
        p = p + 1
        print(f",{i}",end = "")
        S = S + i    
    i = i + 1
print()
print(S)
# 提前輸出2，這樣f",{i}"迴圈才會很好寫