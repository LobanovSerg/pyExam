# checking the divisibility of one number by another
# using arithmetic

a, b = int(input()), int(input())

yes = 1- (a % b)
no = (((a % b) + 2) // ((a % b) + 1)) % 2

print('YES' * yes + 'NO' * no)
