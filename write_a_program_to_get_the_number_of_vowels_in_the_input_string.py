s=input()
v='aeiouAEIOU'
cnt=0
for i in s:
    if i in v:
        cnt+=1
print(cnt)