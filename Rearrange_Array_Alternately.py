def fun(arr,n):
    arr.sort()
    large=n-1
    small=0
    temp=n*[0]
    flag=True
    for i in range(n):
        if flag is True:
            temp[i] = arr[large]
            large -= 1
        else:
            temp[i] = arr[small]
            small += 1
 
        flag = bool(1-flag)
    return temp
t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    res=fun(arr,n)
    print(*res)
