s=input()
c=s[0]
for i in s:
    if i<c and i.isalpha():
        c=i
k=s[0]
for i in s:
    if i>k and i.isalpha():
        k=i
res=[]
res.append(c)
res.append(s.count(c))
res.append(k)
res.append(s.count(k))
print(*res)