def fun(s):
    al=[]
    na=[]
    v='aeiouAEIOU'
    for i in range(len(s)):
        if s[i].isalpha() and s[i] not in v:
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