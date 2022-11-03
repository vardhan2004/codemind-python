n=int(input())
arr=list(map(int,input().split()))
a=[]
cnt=0
for i in arr:
    if arr.count(i)==i:
        cnt+=1
        if i not in a:
            a.append(i)
print(len(a))
        
