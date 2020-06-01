class Solution:
    def solve(self, lst):
        n = len(lst)
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if lst[j] < lst[i]:
                    ans[i] += 1
        return ans