n =  [10, 15, 3, 7]
k = 17


def chech(n,k):
    for i in range(len(n)):
        num = n.pop()
        if k - num in n:
            return True
    return False

print(chech(n,k))

