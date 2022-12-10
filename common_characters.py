s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
n=[]
for i in s1:
    if i.isalpha() and i in s2:
        if i not in n:
            n.append(i)
if len(n)==0:
    print(-1)
else:
    n.sort()
    n=''.join(n)
    print(n)