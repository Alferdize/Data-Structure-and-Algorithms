T = int(input())
for i in range(1,T+1):
    N, M = list(map(int,input().split()))
    Arr = list(map(int,input().split()))
    substring = [i for i in range(M,0,-1)]
    cnt = 0
    for j in range(N-(M-1)):
        if Arr[j:j+M] == substring:
            cnt +=1
    print("Case #{}: {}".format(i,cnt))