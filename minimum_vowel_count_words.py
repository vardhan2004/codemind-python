def vow_count(n):
    a='aeiouAEIOU'
    cnt=0
    for i in n:
        if i in a:
            cnt+=1
    return cnt
        
s=input()
#print(s)
d=s.split()
b=[]
for i in d:
    c=vow_count(i)
    b.append(c)

print(b.count(min(b)))