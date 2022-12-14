n=int(input())
row=[0 for i in range(n)]
a=[row.copy() for i in range(n)]
b=[row.copy() for i in range(n)]
d=[row.copy() for i in range(n)]
for i in range(n):
    l=list(map(int,input().split()))
    for j in range(n):
        a[i][j]=l[j]
for i in range(n):
    l=list(map(int,input().split()))
    for j in range(n):
        b[i][j]=l[j]
for i in range(n):
    for j in range(n):
        d[i][j]=abs(a[i][j]-b[i][j])
for i in d:
    print(*i)