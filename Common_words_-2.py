s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
s1=s1.split()
s2=s2.split()
c=0
a=[]
for i in s1:
    if s1.count(i)==1:
        if i in s2 and s2.count(i)==1:
            a.append(i)
            c+=1
print(len(a))