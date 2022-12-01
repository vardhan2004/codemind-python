n=input()
dic={}
for i in n:
    dic[i]=n.count(i)
for k,v in dic.items():
    if k==' ':
        print(v)
