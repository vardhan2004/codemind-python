n=input()
vo='aeiou'
s=''
for i in n:
    if i in vo:
        s+='V'
    else:
        s+='C'
c=''
res=''
for i in s:
    if i==c:
        continue
    c=i
    res+=i
print(res)
    
    
