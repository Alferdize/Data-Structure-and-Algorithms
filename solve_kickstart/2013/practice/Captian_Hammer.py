
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    m = int(input())
    arr = []
    for j in range(m):
        a = list(map(str, input().split()))
        arr.extend(a)
    arr.sort()
    if list(set(arr)) == arr:
        print("Case #{}: {}".format(i, "YES"))
    else:
        print("Case #{}: {}".format(i, "NO"))

