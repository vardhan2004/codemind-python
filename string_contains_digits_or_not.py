def fun(s):
    for i in s:
        if ord(i)>=48 and ord(i)<=57:
            return 'Yes'
    else:
        return "No"
    
N=int(input())
for i in range(N):
    st=input()
    res=fun(st)
    print(res)