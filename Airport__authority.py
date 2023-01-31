n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
t=int(input())
p=0
for i in arr:
    if i<=t:
        p+=1
    else:
        p+=2
print(p)