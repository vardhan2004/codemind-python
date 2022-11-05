n=int(input())
arr=list(map(int,input().split()))
a=[]
c=0
for i in arr:
    if i not in a and i%2!=0:
        a.append(i)
print(len(a))
