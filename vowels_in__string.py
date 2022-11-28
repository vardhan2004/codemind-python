s=input()
vo='aAeEIiOoUu'
c=0
a=[]
for i in s:
    if i in vo and i not in a:
        a.append(i)
        c+=1
if c:
    print(*a)
else:
    print(-1)