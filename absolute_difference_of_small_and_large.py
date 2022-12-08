s=input()
a=s.split()
for i in a:
    ma=ord(min(i))
    mi=ord(max(i))
    print(abs(ma-mi),end=" ")
    