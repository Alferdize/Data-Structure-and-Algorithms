def findprime(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p*p,n+1,p):
                prime[i] = False
        p += 1
    
    j = 26
    primes = {
    }
    numbers = []
    for i in range(n,2,-1):
        if prime[i]:
            j -= 1
            primes[i] = chr(65+j)
            numbers.append(i)
        if chr(65+j) == "A":
            break
    return primes, numbers


T = int(input())
for j in range(T):
    N, L = list(map(int,input().split()))
    prime,numbers = findprime(N)
    A = list(map(int,input().split()))
    fact  = []
    print(prime)
    # for i in numbers:
    #     if A[0] % i == 0:
    #         if A[1] % i ==0:
    #             fact.append(int(A[0] / i))
    #             fact.append(i)
    #             break
    #         else:
    #             fact.append(i)
    #             fact.append(int(A[0] / i))
    #             break
    # div = fact[1]
    # for i in range(1,L):
    #     fact.append(int(A[i]/div))
    #     div = int(A[i]/div)
    
    # print("Case #{}: ".format(j+1),end="")
    # for i in fact:
    #     print(prime[i],end="")
