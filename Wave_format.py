n=int(input())
arr=list(map(int,input().split()))
#print(arr)
arr.sort()
#print(arr)
a=arr[-1:-(n+1):-1]
#print(a)
i=0
j=1
while i<n and j<n:
    if a[i]>a[j]:
        temp=a[i]
        a[i]=a[j]
        a[j]=temp     
    i+=2
    j+=2
print(*a)
