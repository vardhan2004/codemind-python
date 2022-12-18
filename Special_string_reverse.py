n=input()
a=[]
b=[]
for i in n:
    if i.islower() or i.isupper():
        a.append(i)
    else:
        b.append(i)
d_a=[]
for i in range(-1,-len(a)-1,-1):
    d_a.append(a[i])
for i in b:
    ind=n.index(i)
    d_a.insert(ind,i)
res=''.join(d_a)
print(res)