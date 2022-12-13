def fun(n,k):
    n=str(n)
    if len(n)==k:
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
