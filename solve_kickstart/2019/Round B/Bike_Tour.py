T = int(input())
for i in range(1,T+1):
    N = int(input())
    Arr = list(map(int,input().split()))
    out = 0
    for j in range(1,N-1):
        if Arr[j] > Arr[j-1] and Arr[j] > Arr[j+1]:
            out += 1
    print("Case #{}: {}".format(i,out))