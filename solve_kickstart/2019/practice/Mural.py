T = int(input())
for i in range(1,T+1):
    N = int(input())
    A = list(map(int,list(input())))
    half = (N+1)//2
    count = sum(A[:half])
    temp = count
    for j in range(half,N):
        temp = temp + A[j] - A[j - half]
        count = max(count,temp)
    print("Case #{}: {}".format(i,count))