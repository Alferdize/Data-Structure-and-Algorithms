case = int(input())
for i in range(case):
    N,K = list(map(int, input().split()))
    M = list(map(int, input().split()))
    difference = 0
    for j in range(len(M)-1):
        diff = M[j+1] - M[j]
        if diff > difference:
            difference = diff
    for j in range(len(M)-1):
        diff
