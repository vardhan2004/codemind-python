def palindrome(n):
    org1=n
    if n<0:
        n=n*(-1)
    org=n
    rev=0
    while n:
        r=n%10
        rev=rev*10+r
        n//=10
    if rev==org:
        return True
    else:
        return False

n=int(input())
for i in range(n):
    N=int(input())
    res=palindrome(N)
    print(res)