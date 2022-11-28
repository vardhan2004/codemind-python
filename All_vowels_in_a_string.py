s=str(input())
v='aeiou'
cnt=0
for i in v:
    if i in s:
        cnt+=1
if cnt==5:
    print('True')
else:
    print('False')