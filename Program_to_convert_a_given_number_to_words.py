n=int(input())
l=len(str(n))
dic_one={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight', 9 :'nine',10:'ten'}
dic_10={10:'ten',20:'twenty',30:'thirty',40:'fourty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',100:'hundred'}
dic_pos={2:'hundred',3:'thousand'}
dic_el={11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
if l<=3:
    a=100
if l>3:
    a=1000

e=[]
s=[]
k=0
if n<20:
    if n in dic_el:
        print(dic_el[n])
    elif n in dic_one:
        print(dic_one[n])
else:
    while n:
        d=n//a
    
    
        if n>=10000 and d in dic_one:
            e.append(dic_one[d]+' '+'thousand')
        elif n>=10000 and d>19 and d<101:
            m=(d%10)*10
            e.append(dic_10[m]+' '+'thousand')
        if n>1000:
            e.append(dic_one[d]+' '+'thousand')
        elif n>=100:
            e.append(dic_one[d]+' '+'hundred')
        elif n in dic_el:
            k=dic_el[n]
            e.append(k)
        r=n%a
  
        if r>19 and  r<101:
            g=(r//10)*10
            if r%10!=0:
                e.append(dic_10[g]+' '+dic_one[r%10])
            else:
                e.append(dic_10[g])
            break
        elif r>=1 and r<=19:
            if r in dic_one:
                k=dic_one[r]
                e.append(k)
                break
            else:
                if r in dic_el:
                    e.append(dic_el[r])
                    break
        a=a//10
        n=r
    print(*e)

