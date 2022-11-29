import math as m
def prime(n):
    s=int(m.sqrt(n))
    if n==1:
        return False
    for i in range(2,s+1):
        if n%i==0:
            return False
    else:
        return True
def reverse(n):
    rev=0
    while n:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
 

def fun(n):
    if prime(reverse(n))==True and prime(n)==True:
        return 'circular prime'
    elif prime(n)==True and prime(reverse(n))==False:
        return 'prime but not a circular prime'
    else:
        return 'not prime'
n=int(input())
res=fun(n)
print(res)