import math 

log = False


def algorithm(n, k):
    if k < n or k > n * n or k == n + 1 or k == n * n + 1 \
        or n == 3 and k not in (3, 6, 9):
        return "IMPOSSIBLE", None
    else:
        r = int(k / n)
        diagonal = [r] * n
        if k % n > 0:
            delta = k - r * n
            diagonal[0] += 1
            delta -= 1
            if delta > 0:
                j = 1
                print(delta)
                while delta > 0 and j < n:
                    loc = min(delta, n - diagonal[j])
                    diagonal[j] += loc
                    delta -= loc
                    j += 1
            else:
                till = int(n - 1)
                for j in range(1, till, 2):
                    if j < n -1 and r > 1 and r < n:
                        delta = min(int((r + j) % r), n - r)
                        diagonal[j] -= delta
                        diagonal[j + 1] += delta
        flags = [None] * 2 * n
        flags_mark = [None] * n
        for i in range(2 * n):
            flags[i] = [0] * n
        clear  = [0] * n
        square = [None] * n
        for i in range(n):
            flags_mark[i] = [0] * 2 * n
            square[i] = [0] * n
            square[i][i] = diagonal[i]
            flags[i][diagonal[i] - 1] = 1
            flags[n + 1][diagonal[i] - 1] = 1
            clear[diagonal[i] - 1] += 1 
        l_diagonal_sort = [(en[1],en[0]) for en in enumerate(clear) if en[1] > 0]
        l_diagonal_sort.sort(reverse=True)
        ch = True
        print(l_diagonal_sort)


            
    return flags, diagonal


def accept():
    T= int(input())
    for i in range(1, T+1):
        N, K = list(map(int,input().split()))
        res , sqr = algorithm(N, K)
        
        print("Case #{}: {}".format(sqr, res))



if __name__ == "__main__":
    accept()