def fun(arr):
    a=[]
    a.append(arr[-1])
    for i in range(len(arr)-1):
        a.append(arr[i])
    return a

t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    for i in range(k):
        res=fun(arr)
       
        arr=res
    print(*res)
    
