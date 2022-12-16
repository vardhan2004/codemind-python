n=int(input())
ar=list(map(int,input().split()))
ev=0
od=0
for i in range(len(ar)):
    if i%2:
        od+=ar[i]
    else:
        ev+=ar[i]
if abs(od-ev)==0:
    print('YES')
else:
    print('NO')