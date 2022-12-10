s=input()
res=0
for i in s:
    if ord(i)>48 and ord(i)<58:
        res+=int(i)
print(res)