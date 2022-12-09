def fun(s):
    al=[]
    na=[]
    for i in range(len(s)):
        if s[i].isalpha():
            al.append(s[i])
        else:
            na.append(i)
    al.sort()
    for i in na:
        al.insert(i,s[i])
    s=''.join(al)
    return s
s=list(map(str,input().split()))
for i in s:
    res=fun(i)
    print(res,end=' ')