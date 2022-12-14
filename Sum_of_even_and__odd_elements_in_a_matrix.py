def sum_ev_od(d,r,c):
    even=0
    odd=0
    for i in range(r):
        for j in range(c):
            if d[i][j]%2==0:
                even+=d[i][j]
            else:
                odd+=d[i][j]
                
    print(even,odd)
    
n,m=map(int,input().split())
row=[0 for i in range(m)]
d=[row.copy() for i in range(n)]
for i in range(n):
    l=list(map(int,input().split()))
    for j in range(m):
        d[i][j]=l[j]
even=sum_ev_od(d,n,m)
