#20.字根與子字串
ss = input()
dic = {}
for i in range(len(ss)):
    dic[ss[i]] = i
s = input()
re = False
for i in range(len(s)-len(ss)+1):
    a = True
    for j in range(len(ss)):
        if ss[len(ss)-j-1] != s[i+len(ss)-j-1]:
            a = False
    if a:
        re = True
    else:
        if s[i+len(ss)-j-1] in dic:
            i = i + dic[s[i+len(ss)-j-1]]
        else:
            i = i + len(ss)
if re:
    print("YES")
else:
    print("NO")
#前面的語法，但是使用了Boyer-Moore由子字串的尾部開始比對，錯了就根據dic裡給索引值平移到一下次比對的位置。