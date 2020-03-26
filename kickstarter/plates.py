case = int(input())

import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline


def lmi():
    return list(map(int, input().split()))


def llmi(n):
    return [lmi() for _ in range(n)]


def solve():
    N, K, P = list(map(int, input().strip().split()))
    X = llmi(N)
    dp = [[0] * (P + 1) for _ in range(N + 1)]
    print("Enumerate",X)
    print("Dp",dp)
    for i, plates in enumerate(X):
        print("Enumerate : ",i)
        _sum_b = 0
        for j in range(K + 1):
            print("Joker ",j)
            # j is plate count
            if j:
                _sum_b += plates[j - 1]
            for v in range(P + 1):
                if v - j < 0 or v - j > P:
                    continue
                dp[i + 1][v] = max(dp[i + 1][v], dp[i][v - j] + _sum_b)
                print("Data {} : {} : {} : {} ".format(v,j,P,_sum_b))
                print("Finale {}: {}".format(i+1,dp))

    return dp[N][-1]


for i in range(case):
    print('Case #{}:'.format(i+1), solve(), flush=True)
