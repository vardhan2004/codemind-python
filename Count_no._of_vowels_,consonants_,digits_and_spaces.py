s=input()
v='aeiou'
v_c,c_c,d_c,w_s=0,0,0,0
for i in s:
    if i in v:
        v_c+=1
    elif i.isalpha():
        c_c+=1
    elif i.isdigit():
        d_c+=1
    else:
        w_s+=1
print('Vowels:',v_c)
print('Consonants:',c_c)
print('Digits:',d_c)
print('White spaces:',w_s)