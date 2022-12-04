r=int(input())
res=0
d=0
m=[]
for i in range(0,r):
    a=list(map(int,input().split()))[:r]
    m.append(a)
i=0
while i<r:
    f=str(i)+str(i)
    b=str(i)+str(r-i-1)
    if f==b:
        d=m[i][i]
    res+=m[i][i]+m[i][r-i-1]
    i+=1
print(res-d)
