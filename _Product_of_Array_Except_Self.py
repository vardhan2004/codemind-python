def fun(c,arr):
    p=1
    for i in arr:
        if i==c:
            continue
        p*=i
    return p
n=int(input())
arr=list(map(int,input().split()))
p=1
for i in arr:
    c=i
    res=fun(c,arr)
    print(res,end=' ')
        
    