n, m = map(int, input().split())
r = [0 for i in range(m)]
M = [r.copy() for i in range(n)]
for i in range(n):
    l = list(map(int,input().split()))
    for j in range(m):
        M[i][j] = l[j]
k = [0, n - 1]
f = [0, m - 1]
ubs = 0
for i in range(n):
    for j in range(m):
        if i not in k and j not in f:
            ubs += M[i][j]
print(ubs)
