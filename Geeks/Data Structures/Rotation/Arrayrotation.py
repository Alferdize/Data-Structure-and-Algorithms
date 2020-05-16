def leftRotate(arr,d):
    for i in range(d):
        rotatebyOne(arr)

    
def rotatebyOne(arr):
    n = len(arr)
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i +1]
    arr[n-1] = temp


arr = [1, 2, 3, 4, 5, 6, 7]
leftRotate(arr,3)
print(arr)