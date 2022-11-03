n=int(input())
arr=list(map(int,input().split()))
k=int(input())
a=[]
c=0
for i in arr:
    if arr.count(i)==k:
        c+=1
        if i not in a:
            a.append(i)
            print(i,end=' ')
if c==0:
    print(-1)