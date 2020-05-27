a, b, c = float(input()), float(input()), float(input())

discriminant = b ** 2 - 4 * a * c

if discriminant < 0:
    print("No roots")
elif discriminant == 0:
    print(-b / (2 * a))
else:
    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)
    print(min(x1, x2), max(x1, x2))
