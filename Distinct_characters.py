s=input()
s=s.lower()
a=[]
for i in s:
    if i not in a and i.isalpha():
        a.append(i)
a.sort()
s=''.join(a)
print(s)