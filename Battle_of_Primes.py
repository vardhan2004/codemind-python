def prm(n):
    cnt=0
    for i in range(1,n+1):
        if n%i==0:
            cnt+=1
    if cnt==2:
        return True
    else :
        return False

def ans(n):
        p=prm(n)
        if p==True:
            return n
        else:
            return ans(n+1)



n1=int(input())
n2=int(input())
s=n1+n2
if prm(s)==True:
    res=ans(s+1)
    print(res-s)
else:
    res=ans(s)
    print(res-s)