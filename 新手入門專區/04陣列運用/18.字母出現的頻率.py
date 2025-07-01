#18.字母出現的頻率
s = input()
dp = [0] * 26
for i in range(len(s)):
    if "A" <= s[i] <= "Z":
        dp[ord(s[i])-65] = dp[ord(s[i])-65] + 1
    elif "a" <= s[i] <= "z":
        dp[ord(s[i])-97] = dp[ord(s[i])-97] + 1
print(dp[0],end="")
for i in range(1,26):
    print(f" {dp[i]}",end="")
print()
#前面的語法