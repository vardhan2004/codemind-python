def row_sum(d,r,c):
    r_s=[0 for i in range(r)]
    for i in range(r):
        for j in range(c):
            r_s[i]+=d[i][j]
    return r_s

r,c=map(int,input().split())
row=[0 for i in range(c)]
d=[row.copy() for i in range(r)]
for i in range(r):
    l=list(map(int,input().split()))
    for j in range(c):
        d[i][j]=l[j]
           
res=row_sum(d,r,c)
print(max(res))