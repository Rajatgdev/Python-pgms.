def insertion_sort(a):
    i = 1
    while i < len(a):
        j = i
        while a[j] < a[j - 1] and j > 0:
            a[j], a[j - 1] = a[j - 1], a[j]
            j = j - 1
        i = i + 1


list = [2, 56, 32, 4, 9, 18]
insertion_sort(list)
print(list)
