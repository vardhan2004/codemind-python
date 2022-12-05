n=int(input())
arr=list(map(int,input().split()))
for i in arr:
    if arr.count(i)>=2:
        print(i)
        break