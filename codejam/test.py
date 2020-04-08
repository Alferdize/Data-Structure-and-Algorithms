import random
import math
import itertools

def latin_square2(items, shuffle=True, forward=False):
    sign = -1 if forward else 1
    result = [items[sign * i:] + items[:sign * i] for i in range(len(items))]
    if shuffle:
        random.shuffle(result)
    return result

T = int(input())
for i in range(1,T+1):
    N , K = list(map(int,input().split()))
    items = list(range(1, N + 1))
    random.shuffle(items)
    total = 0
    matrix = []
    for j in range(math.factorial(N)*math.factorial(N+1)):
        rows1 = latin_square2(items)
        k = 0
        total = 0
        if rows1 not in matrix:
            matrix.append(rows1)
            for row in rows1:
                total += row[k]
                k+=1
            if total == K:
                break
    if total == K:
        print("Case #{}: POSSIBLE".format(i+1))
        for row in rows1:
            x = " ".join([str(elem) for elem in row])
            print(x)
    else:
        print("Case #{}: IMPOSSIBLE".format(i+1))
