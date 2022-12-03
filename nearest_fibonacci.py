n=int(input())
a,b,t=0,1,0
for i in range(n):
    f=a
    if a>n:
        break
    k=a
    t=a+b
    a=b
    b=t
if abs(n-k)<abs(n-f):
    print(k)
elif abs(n-k)>abs(n-f):
    print(f)
else:
    print(k,f)