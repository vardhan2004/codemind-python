def fun(a):
    j=0
    b=[]
    b.append(a[len(a)-1])
    while j<=len(a)-2:
        b.append(a[j])
        j+=1
    return b
n,k,q=map(int,input().split())  
a=list(map(int,input().split()))
c=[]
for i in range(q):
       m=int(input())
       c.append(m)    
for i in range(k):
    rev=fun(a)
    a=rev
for i in c:
    print(rev[i])
    
       
