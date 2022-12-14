r,c=map(int,input().split())
row=[0 for i in range(c)]
a=[row.copy() for j in range(r)]
d=[0 for j in range(c)]
for i in range(r):
    l=list(map(int,input().split()))
    for j in range(c):
        a[i][j]=l[j]
for i in range(c):
    for j in range(r):
        d[i]+=a[j][i]
print(*d)