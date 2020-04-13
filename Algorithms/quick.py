import random
import time


def quic(A, low, high):
    if low < high:
        p = partition(A, low, high)
        quic(A, low, p-1)
        quic(A, p+1, high)


def partition(A, low,high):
    pivot = A[high]
    i = low
    for j in range(low,high):
        if A[j] < pivot:
            temp = A[j]
            A[j] = A[i]
            A[i] = temp
            i += 1
    temp = A[i]
    A[i] = A[high]
    A[high] = temp
    return i




A = [i for i in range(1000000)]
random.shuffle(A)
low = 0
high = len(A)-1
start = time.time()
quic(A, low, high)
print(time.time()-start)
