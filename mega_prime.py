def prime(n):
    cnt=0
    for i in range(1,n+1):
        if n%i==0:
            cnt+=1
    if cnt==2:
        return True
    else:
        return False
def digit(n):
    c=0
    while n:
        c+=1
        n=n//10
    return c

n=int(input())
d=digit(n)
m=n

count=0
while n:
    r=n%10
    p=prime(r)
    if p==True:
        count+=1
    n=n//10

if d==count and prime(m)==True:
    print('Mega Prime')
else:
    print('Not Mega Prime')

        