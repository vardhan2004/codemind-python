m, n = map(int, input().split())
pd = 0
row = [0 for i in range(n)]
M = [row.copy() for i in range(m)]
for i in range(m):
    lst = list(map(int, input().split()))
    for j in range(n):
        M[i][j] = lst[j]
        if i == j:
            pd += M[i][j]
            M[i][j] = None
i = 0
j = m - 1
while j >= 0:
    if M[i][j] != None:
        pd += M[i][j]
    i += 1
    j -= 1
print(pd)