T = int(input())
for i in range(T):
    N = int(input())
    total = sum(j * (N-j) for j in range(N) )
    print(2 * total)