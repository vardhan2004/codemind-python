def mar(M, n, m):
    r = [0]*n
    for i in range(n):
        r[i] = sum(M[i])
    return max(r)
def mac(M, n, m):
    c = [0]*m
    for i in range(m):
        co = 0
        for j in range(n):
            co += M[j][i]
        c[i] = co
    return max(c)
n, m = map(int, input().split())
r = [0 for i in range(m)]
M = [r.copy() for i in range(n)]
for i in range(n):
    l = list(map(int,input().split()))
    for j in range(m):
        M[i][j] = l[j]
print(max(mar(M,n,m), mac(M, n, m)))