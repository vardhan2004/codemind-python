def fun(n,k):
    d=0
    if n==0 and k==1:
        return True
    while n:
        d+=1
        n//=10
    if d==k:
        return True
    else:
        return False
n,k=map(int,input().split())
arr=list(map(int,input().split()))
#print(k,arr)
cnt=0
for i in arr:
    if i<0:
        i=i*(-1)
    if fun(i,k)==True:
        cnt+=1
print(cnt)
