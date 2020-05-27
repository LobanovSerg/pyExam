def selection_sort(array):
    n = len(array)
    while n > 1:
        sm = 0
        for i in range(n):
            if array[i] > array[sm]:
                sm = i
            array[n - 1], array[sm] = array[sm], array[n - 1]
        n -= 1
    return array

# enter numbers space separated
a = [int(_) for _ in input().split()]

print(selection_sort(a))
