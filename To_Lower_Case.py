n=input()
e=''
for i in n:
    if ord(i)>=97 and ord(i)<=122:
        e+=i
    else:
        e+=chr(ord(i)+32)
print(e)