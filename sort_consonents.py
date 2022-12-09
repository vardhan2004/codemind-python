def sort_v(s):
    al=[]
    av=[]
    vowel='aeiouAEIOU'
    for i in range(len(s)):
        if s[i].isalpha() and s[i] not in vowel:
            al.append(s[i])
        else:
            av.append(i)
    al.sort()
    for i in av:
        al.insert(i,s[i])
    s=''.join(al)
    return s
s=list(map(str,input().split()))
for i in s:
    res=sort_v(i)
    print(res,end=' ')