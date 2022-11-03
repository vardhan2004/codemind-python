n=int(input())
arr=list(map(int,input().split()))
a=[]
cnt=0
for i in arr:
    if i not in a:
        a.append(i)
print(sum(a))
