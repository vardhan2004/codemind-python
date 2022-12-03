s=input()
a=s.split()
m=a[len(a)-1]
if min(m).isupper() and min(m).lower() in m:
    print(min(m).lower())
else:
    print(min(m))