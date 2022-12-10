def palindrome(st):
    res=''
    for i in range(-1,-len(st)-1,-1):
        res+=st[i]
    if st==res:
        return True
    else:
        return False
   
s=input()
s=s.lower()
a=s.split()
cnt=0
for i in a:
   res=palindrome(i)
   if res:
       cnt+=1
print(cnt)