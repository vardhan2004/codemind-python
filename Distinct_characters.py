s=input()
s=s.lower()
#print(s)
a=[]
for i in s:
   if s.count(i)==1 and i.isalpha():
       a.append(i)
a.sort()
s=''.join(a)
print(s)