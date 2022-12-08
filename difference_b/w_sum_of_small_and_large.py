s=input()
a=s.split()
mi=0
ma=0
for i in a:
    mi+=ord(min(i))
    ma+=ord(max(i))
print(abs(mi-ma))