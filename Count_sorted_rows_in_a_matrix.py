def cnt_row_sort(M, n, m):
    cnt = 0
    for i in M:
        k = sorted(i)
        k.reverse()
        if i == sorted(i) or i == k:
            cnt += 1
    return cnt
n, m = map(int, input().split())
r = [0 for i in range(m)]
M = [r.copy() for i in range(n)]
for i in range(n):
    l = list(map(int,input().split()))
    for j in range(m):
        M[i][j] = l[j]
print(cnt_row_sort(M, n, m))