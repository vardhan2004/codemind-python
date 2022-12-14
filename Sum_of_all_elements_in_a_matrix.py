n,m=map(int,input().split())
row=[0 for i in range(m)]
d=[row.copy() for i in range(n)]
res=0
for i in range(n):
    l=list(map(int,input().split()))
    for j in range(m):
        res+=l[j]
print(res)