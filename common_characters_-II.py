s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
cn=[]
for i in s1:
    if i in s2 and i.isalpha():
        if i not in cn:
            cn.append(i)
print(len(cn))