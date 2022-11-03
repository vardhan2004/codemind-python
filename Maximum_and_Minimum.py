n=int(input())
arr=list(map(int,input().split()))
#print(arr)
a=[]
cnt=0
for i in arr:
    if arr.count(i)==i:
        cnt+=1
        a.append(i)
if cnt==0:
    print(-1)
else:
   print(min(a),max(a))
        
