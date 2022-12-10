def fun(key,ar):
    j=1
    cnt=0
    while j<len(ar):
        if key in ar[j]:
            cnt+=1
        j+=1
    return cnt
s=input()
s=s.lower()
a=s.split()
k=a[0]
j=1
cnt=0
c=[]
for i in k:
    res=fun(i,a)
    if res==len(a)-1:
        cnt+=1
        c.append(i)
if cnt==0:
    print(-1)
else:
    c=''.join(c)
    print(min(c))
    