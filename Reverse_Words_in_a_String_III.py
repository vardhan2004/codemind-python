def fun(s):
    e=s[-1:-len(s)-1:-1]
    return e
l=list(map(str,input().split()))
for i in l:
    rev=fun(i)
    print(rev,end=' ')