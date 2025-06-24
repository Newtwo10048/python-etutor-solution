#30.線段覆蓋長度
n = int(input())
st = []
for _ in range(n):
    l, r = map(int, input().split())
    st.append((l, r))
st.sort()
mer = []
s,e = st[0]

for i in range(1,n):
    l,r = st[i]
    if l <= e:#重疊
        e = max(e,r)
    else:#沒重疊
        mer.append((s,e))
        s,e =l,r
mer.append((s,e))
total = sum(r - l for l,r in mer)
print(total)
#map(int,input(),split())對右邊容器的元素執行左邊的函式