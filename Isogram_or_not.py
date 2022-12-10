s=input()
cnt=0
for i in s:
    if s.count(i)==1:
        cnt+=1
if cnt==len(s):
    print(True)
else:
    print(False)