from math import gcd

def leftRotate(arr,d):
    n = len(arr)
    d = d % n
    g_c_d = gcd(d,n)
    for i in range(g_c_d):
        j = i
        temp = arr[i]
        while 1:
            k = j +d
            if k >= n:
                k = k -n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp

arr = [1, 2, 3, 4, 5, 6, 7]
leftRotate(arr,9)
print(arr)