n = int(input())
arr = [[0]*n for _ in range(n)]

x, y = 0, 0

for k in range(1, n * n + 1):
    arr[x][y] = k
    if x <= y+ 1 and x + y< n - 1:
        y += 1
    elif x < y and x + y >= n - 1:
        x += 1
    elif x >= y and x + y > n - 1:
        y -= 1
    elif x > y + 1 and x + y <= n - 1:
        x -= 1

for i in range(n):
    print(*arr[i])
