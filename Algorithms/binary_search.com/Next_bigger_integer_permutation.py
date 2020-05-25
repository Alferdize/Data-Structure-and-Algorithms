class Solution:
    def solve(self, num):
        A = list(str(num))
        N = len(A)
        
        for i in range(N - 1, 0, -1):
            if A[i - 1] < A[i]:
                break
        else:
            A.sort()
            return int("".join(A))
        
        for j in range(N - 1, i - 1, -1):
            if A[j] > A[i - 1]:
                break
        
        A[j], A[i-1] = A[i-1], A[j]
        for k in range(i, N):
            k2 = N - 1 - (k - i)
            if k >= k2:
                break
            A[k], A[k2] = A[k2], A[k]
        return int("".join(A))