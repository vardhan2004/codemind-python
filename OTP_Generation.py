n=input()
e=''
for i in n:
    i=int(i)
    if i%2:
        e+=str(i**2)
print(e)
