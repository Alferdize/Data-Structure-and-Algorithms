T = int(input())

for j in range(1, T + 1):
    N = int(input())
    trace = 0
    rowcount = 0
    colcount = 0
    matrix = []
    for i in range(N):
        A = list(map(int,input().split()))
        trace += A[i]
        if sorted(A) != list(set(A)):
            rowcount += 1
        matrix.append(A.copy())
    rez = [[matrix[k][i] for k in range(N)] for i in range(N)] 
    for i in rez:
        if sorted(i) != list(set(i)):
            colcount += 1
    print("Case #{}: {} {} {}".format(j,trace,rowcount,colcount))


