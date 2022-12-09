s1=list(map(str,input().split()))
s2=list(map(str,input().split()))
l1=[]
l2=[]
for i in s1:
    l1.append(i.lower())
for i in s2:
    l2.append(i.lower())
for i in l2:
    if i in l1:
        print(i,end=' ')
