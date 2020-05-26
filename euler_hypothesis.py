# refutation of the Euler hypothesis

n = 150
array = [i ** 5 for i in range(n)]

for a in range(1, n):
    print(a)
    for b in range(a, n):
        for c in range(b, n):
            for d in range(c, n):
                total = array[a] + array[b] + array[c] + array[d]
                if total in array:
                    print(a, b, c, d, array.index(total))
                    exit(0)
