def quicsort(A, low, high):
    if low < high:
        p = partition(A, low, high)
        quicsort(A, low, p - 1)
        quicsort(A, p + 1, high)

def partition(A, low, high):
    pivot = A[high]
    i = low
    for j in range(low,high, 1):
        if A[j] < pivot:
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
            i += 1
    temp = A[i]
    A[i] = A[high]
    A[high] = temp
    return i


A = [1, 2, 4, 9, 3, 7]
low = 0
high = len(A)-1
quicsort(A, low, high)
print(A)
