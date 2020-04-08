from itertools import permutations,combinations
T = int(input())

for i in range(T):
    N, K = list(map(int,input().split()))
    total = 0
    A = [j for j in range(1,N+1)]
    perm = permutations(A)
    collect = []
    for j in list(perm): 
        collect.append(list(j))
    comb = list(combinations(collect, N))
    print(len(comb))
    # for j in range(len(comb)):
    #     total = 0
    #     for k in range(N):
    #         total += comb[j][k][k]
    #     if total == K:
    #         collect = list(comb[j])
    #         break
    # if total == K:
    #     print("Case #{}: POSSIBLE".format(i+1))
    #     for j in collect:
    #         x = " ".join([str(elem) for elem in j])
    #         print(x)
    # else:
    #     print("Case #{}: IMPOSSIBLE".format(i+1))

