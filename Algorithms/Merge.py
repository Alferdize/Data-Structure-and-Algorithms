def merge(data, low, middle, high):
    n1 = middle - low + 1
    n2 = high - middle
    left = [0] * n1
    right = [0] * n2

    for i in range(n1):
        left[i] = data[low+i]

    for i in range(n2):
        right[i] = data[middle + 1 + i]
    i = 0
    j = 0
    k = low

    while i < n1 and j < n2:
        if left[i] <= right[j]:
            data[k] = left[i]
            i += 1
        else:
            data[k] = right[j]
            j += 1
        k += 1

    while j < n1:
        data[k] = right[j]
        j += 1
        k += 1


def merge_sort(data, low, high):
    if low < high:
        middle = (low + (high-1))//2
        merge_sort(data, low, middle)
        merge_sort(data, middle + 1, high)
        merge(data, low, middle, high)


data = [2, 3, 4, 1, 6, 8]
merge_sort(data, 0, len(data)-1)
print(data)
