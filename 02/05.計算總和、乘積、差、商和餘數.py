#5.計算總和、乘積、差、商和餘數
num =input()
parts = num.split()

ints = [int(x) for x in parts]

print(f"{ints[0]}+{ints[1]}={sum(ints)}")
print(f"{ints[0]}*{ints[1]}={ints[0] * ints[1]}")
print(f"{ints[0]}-{ints[1]}={ints[0] - ints[1]}")
if ints[1]>0:
    print(f"{ints[0]}/{ints[1]}={ints[0] // ints[1]}...{ints[0] % ints[1]}")
else:
    print(f"{ints[0]}/{ints[1]}=-{ints[0] // (-1 * ints[1])}...{ints[0] % (-1 * ints[1])}")
#print(f"{x}"}，{}內會輸出x的值
#另test測資一會顯示錯誤
