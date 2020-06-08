# Recursion!!!
def fib_pos(x):
    if x == 1 or x == 2:
        return 1
    else:
        return fib_pos(x - 1) + fib_pos(x - 2)

print(fib_pos(int(input())))
