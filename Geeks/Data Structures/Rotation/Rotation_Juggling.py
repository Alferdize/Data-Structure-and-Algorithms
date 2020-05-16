def leftRotate(arr,d):
    n = len(arr)
    d = d % n
    gcd = gcd_func(d,n)
    for i in range(gcd):
        temp = arr[i]
        j = i
        while True:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp


def gcd_func(a,b):
    if b == 0:
        return a
    else:
        return gcd_func(b, a % b)



arr = [1, 2, 3, 4, 5, 6, 7]
leftRotate(arr,7)
print(arr)