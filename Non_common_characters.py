s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
cnt=0
c=[]
for i in s1:
    if i.isalpha() and i not in s2:
        if i not in c:
            c.append(i)
for i in s2:
    if i.isalpha() and i not in s1:
        if i not in c:
            c.append(i)
print(len(c))