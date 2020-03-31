case = int(input())

for i in range(case):
    N = int(input())
    data = list(map(int,input().split()))
    info = {}
    for i in range(N):
        info[chr(65+i)] = data[i]
    