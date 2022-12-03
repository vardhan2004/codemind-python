def pairs(a):
    i=0
    j=-1
    v='aeiouAEIOU'
    cnt=0
    while i<=len(a)//2 and j>=-(len(a))//2:
        if (a[i ] in  v and a[j] not in v) or (a[i ] not in  v and a[j] in v):
            #print(a[i],a[j])
            cnt+=1
        i+=1
        j-=1
    return cnt
        
    

a=input()
s=a.split()
c=0
for i in s:
    p=pairs(i)
    c+=p
print(c)

