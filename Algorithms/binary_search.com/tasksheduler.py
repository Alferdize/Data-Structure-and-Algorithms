class Solution:
    def solve(self, nums, k):
        from collections import Counter
        c = Counter(nums)
        ans = 0
        lastsize = 0
        while c:
            lastsize = len(c)
            for x, _ in c.most_common(k+1):
                c[x] -= 1
                if c[x] == 0:
                    del c[x]
            ans += k+1
        return ans + lastsize - (k+1)