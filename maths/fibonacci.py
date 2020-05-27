n = int(input())
a, b = 0, 1

for _ in range(n):
    print(b, end=' ')
    a, b = b, a + b
