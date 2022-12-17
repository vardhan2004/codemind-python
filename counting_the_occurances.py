n=input()
k=input()
if k not in n:
    print(-1)
else:
    cnt=0
    for i in n:
        if k in i:
            cnt+=1
    print(cnt)