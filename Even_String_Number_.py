from itertools import permutations
s=input()
d=[]
a=[]
for i in s:
    if ord(i)>47 and ord(i)<58 and i not in a:
        a.append(i)
for i in permutations(a,len(a)):
    r=''
    for j in i:
        r+=j
    #print(r)
    if int(r)%2==0:
        d.append(int(r))
if len(d)==0:
    print(-1)
else:
    print(max(d))
