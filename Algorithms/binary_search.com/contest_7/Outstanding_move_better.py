import bisect
class Solution:
    def solve(self, A):
        P = [0]
        base = 0
        for i, x in enumerate(A, 1):
            P.append(P[-1] + x)
            base += i * x
        
        def eval_at(j, x):
            return -j * x + P[j]
        def intersection(j1, j2):
            return (P[j2] - P[j1]) / (j2 - j1)
            
        hull = [-1]
        indexes = [0]
        for j in range(1, len(P)):
            while hull and intersection(indexes[-1], j) <= hull[-1]:
                hull.pop()
                indexes.pop()
            
            hull.append(intersection(indexes[-1], j))
            indexes.append(j)
        
        ans = base
        for i, x in enumerate(A):
            j = bisect.bisect(hull, x)
            j = max(j - 1, 0)
            ans = max(ans, base + eval_at(i, x) - eval_at(indexes[j], x))
        return ans % (10 ** 9 + 7)