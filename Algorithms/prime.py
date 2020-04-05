import time

def findprime(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False

        p += 1

    sum = 0
    j = 26
    for p in range(n,2,-1):
        if prime[p]:
            j-=1
            print(p,chr(65+j))
        if chr(65+j)=="A":
            break
            
    return sum



if __name__ == "__main__":
    n = 103
    start = time.time()
    sum = findprime(n)
    print(sum)