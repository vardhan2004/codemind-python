n=str(input())
cnt=0
for i in n:
    if i.islower()!=True and i.isupper()!=True and i.islower!=True and i!=' ':
        cnt+=1
print(cnt)