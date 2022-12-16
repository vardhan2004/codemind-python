a=list(map(int,input().split()))[:3]
b=list(map(int,input().split()))[:3]
a_c=0
b_c=0
for i in range(3):
    if a[i]>b[i]:
        a_c+=1
    elif a[i]<b[i]:
        b_c+=1
print(a_c,b_c)