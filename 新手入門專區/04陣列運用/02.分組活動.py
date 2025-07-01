#2.分組活動
n = int(input())
nums = input()
zu = int(input())
count = 1
print(nums[0],end="")
for i in range(1,n):
    if count % zu ==0:
        print(f" {nums[i]}",end = "")

    else:
        print(nums[i],end="")
    count = count +1
print()
#前面的語法