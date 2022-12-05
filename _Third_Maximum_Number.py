n=int(input())
l=list(map(int,input().split()))
if n==3:
    print(min(l))
elif n<3:
    print(max(l))
else:
    l.remove(max(l))
    c=max(l)
    l.remove(max(l))
    if max(l)==c:
        print(min(l))
    else:
        print(max(l))