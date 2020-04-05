from math import gcd

Test = int(input())

for i in range(Test):
    N, L = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = [-1] * (L + 1)
    for j in range(L):
        if gcd(A[i], A[i + 1]) != A[i]:
            B[i + 1] = gcd(A[i], A[i + 1])
            for k in range(j + 2, L + 1):
                B[k] = A[k - 1] // B[k - 1]
            for k in range(j , -1, -1):
                B[k] = A[k] // B[k+1]
            break
    vals = sorted(set(B))
    print(vals)
    res = ""
    for x in B:
        res += chr(ord('A') + vals.index(x))
    print("Case #{}: {}".format(i + 1, res))
            

    