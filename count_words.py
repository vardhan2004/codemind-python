def count(a):
    cnt=0
    v='aeiouAEIOU'
    if a[0] in v and a[len(a)-1] not in v:
        #print(a[0],a[len(a)-1])
        cnt+=1
    return cnt

a=input()
s=a.split()
c=0
for i in s:
    res=count(i)
    c+=res
    
print(c)

