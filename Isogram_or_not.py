def res(s):
    dic = {}
    for i in s:
        if i in dic:
            return False
        else:
            dic[i] = 1
    return True
s = input()
print(res(s))