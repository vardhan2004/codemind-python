s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
a=[0]*26
for i in s1:
    asc=ord(i)-97
    a[asc]+=1
for i in s2:
    asc=ord(i)-97
    a[asc]-=1
for i in a:
    if i!=0:
        print('False')
        break
else:
    print('True')