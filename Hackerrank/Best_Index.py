T = int(input())
Arr = list(map(int,input().split()))
k = 2
start = 1
while start <= T:
    start += k
    k += 1
start -= k - 1
k -= 2
s = sum(Arr[:start])    
ms = s
for i in range(1, T):
    s -= Arr[i - 1]    
    if start < T:
        s += Arr[start]
        start += 1
    else:
        k -= 1
        s -= sum(Arr[T - k:T])
        start -= k
    if s > ms:
        ms = s
print(ms)