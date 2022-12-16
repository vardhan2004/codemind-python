n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    if l.count(i)==1:
        a.append(i)
if len(a)==0:
    print(-1)
else:
    print(max(a))