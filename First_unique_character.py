s=input()
s=s.lower()
for i in s:
    if s.count(i)==1 and i.isalpha():
        print(i)
        break
else:
    print(-1)