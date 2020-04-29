from collections import Counter
class Solution:
    def solve(self, nums, target):
        cnt = Counter([0])
        s = 0
        ans = 0
        for n in nums:
            s += n
            ans += cnt[s - target]
            cnt[s] += 1
        return ans