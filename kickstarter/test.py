from math import gcd
T = int(input())
for j in range(T):
    N, L = list(map(int,input().split()))
    A = list(map(int,input().split()))
    fact = []
    x = gcd(A[0],A[1])
    fact.append(A[0]//x)
    fact.append(x)
    for i in range(2,L+1):
        fact.append(A[i-1]//fact[i-1])
    numbers = sorted(set(fact))
    res = ""
    for i in fact:
        res += chr(ord("A") + numbers.index(i))
    print("Case #{}: {}".format(j+1,res))