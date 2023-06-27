def cnt_col_sort(M, n, m):
    flag = True
    cnt = 0
    for i in range(m):
        ref = M[0][i]
        for j in range(1, n):
            if M[j][i] < ref:
                flag = False
            else:
                ref = M[j][i]
        if flag:
            cnt += 1
        else:
            flag = True
    return cnt
            
n, m = map(int, input().split())
r = [0 for i in range(m)]
M = [r.copy() for i in range(n)]
for i in range(n):
    l = list(map(int,input().split()))
    for j in range(m):
        M[i][j] = l[j]
print(cnt_col_sort(M,n,m))