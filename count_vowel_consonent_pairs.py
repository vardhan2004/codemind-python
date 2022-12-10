s=input()
i=-1
j=0
cnt=0
v='aeiouAEIOU'
while i>(-len(s)-1)//2 and j<len(s)//2:
    if s[i].isalpha() and s[j].isalpha():
        if (s[i] in v and s[j] not in v) or (s[i] not in v and s[j] in v):
            cnt+=1
    i-=1
    j+=1
print(cnt)