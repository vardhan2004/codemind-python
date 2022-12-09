s=input()
#print(s)
k=[]
a=[]
for i in range(len(s)):
    if s[i].isalpha():
        k.append(s[i])
    else:
        a.append(i)
k.sort()
for i in a:
    k.insert(i,s[i])
s=''.join(k)
print(s)