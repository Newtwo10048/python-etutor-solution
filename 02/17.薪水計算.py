#17.薪水計算
num = input()
parts = num.split()
ints = [int(x) for x in parts]
print(round(60*ints[1]+60*ints[1]*1.33+(ints[0]-120)*ints[1]*1.66,1))
#前面的語法