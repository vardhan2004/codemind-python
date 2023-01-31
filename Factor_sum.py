def fact(n):
    f=0
    for i in range(1,n+1):
        if n%i==0:
            f+=i
    return f

arr=list(map(int,input().split(",")))
a=[]
for i in arr:
    sum=fact(i)
    if sum in arr:
        a.append(i)
a.sort()
if len(a)==0:
    print(-1)
else:
    print(*a)