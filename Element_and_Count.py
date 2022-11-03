n=int(input())
arr=list(map(int,input().split()))
a=[]
cnt=0
for i in arr:
    if i not in a:
        print(i,arr.count(i),end=' ')
        a.append(i)

       
