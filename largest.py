# finding the larger of two numbers using arithmetic
a, b = int(input()), int(input())

c = ((a - b) ** 2) ** .5

print(int((a + b + c) / 2))
