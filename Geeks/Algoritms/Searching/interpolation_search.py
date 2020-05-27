def inperpolation(arr,x,n):
    low = 0
    high = n-1
    while low <= high and x >= arr[low] and x <= arr[high]:
        if low == high:
            if arr[low] == x:
                return low
            return -1
        pos = low + int(((float(high - low)/ (arr[high] - arr[low])) * (x  - arr[low])))
        
        if arr[pos] == x:
            return pos

        if pos < x:
            low = pos + 1
        else:
            high = pos - 1

    return -1
    



arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 
    34, 55, 89, 144, 233, 377, 610]

x = 55
N = len(arr)
result = inperpolation(arr,x,N)
print(result)