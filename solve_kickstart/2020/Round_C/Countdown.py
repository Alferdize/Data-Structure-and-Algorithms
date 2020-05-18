T = int(input())
for i in range(1,T+1):
    N, M = list(map(int,input().split()))
    Arr = list(map(int,input().split()))
    cnt = 0
    series = 0
    for j in range(len(Arr)):
        if Arr[j] == M:
            series =1
        elif series > 0 and j > 0 and Arr[j -1] == Arr[j] + 1:
            series += 1
        else:
            series = 0
        if series == M:
            cnt += 1
    print("Case #{}: {}".format(i,cnt))