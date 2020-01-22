def insertion(data):
    n = len(data)
    for i in range(1,n):
        key = data[i]
        j =i-1
        while j >= 0 and key < data[j]:
            data[j+1] = data[j]
            j-=1
        data[j+1] = key
    return data

print(insertion([2,3,4,1,6,8]))