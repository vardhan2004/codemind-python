def fun(a):
    j=0
    b=[]
    b.append(a[len(a)-1])
    while j<=len(a)-2:
        b.append(a[j])
        j+=1
    return b
n=int(input())
a=list(map(int,input().split()))
p=int(input())
c=[]
for i in range(p):
    res=fun(a)
    a=res
print(*a)
       
