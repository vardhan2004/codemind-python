def max_col(m,r,c):
    m_c=[0 for i in range(c)]
    for i in range(c):
        c=0
        for j in range(r):
            if m[j][i]>c:
                c=m[j][i]
        print(c)
    
                

r,c=map(int,input().split())
row=[0 for i in range(c)]
m=[row.copy() for i in range(r)]
for i in range(r):
    l=list(map(int,input().split()))
    for j in range(c):
        m[i][j]=l[j]
res=max_col(m,r,c)
