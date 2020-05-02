from operator import mul
from itertools import accumulate
class Solution:
    def solve(self, nums):
        prod= lambda x: list(accumulate(x,mul))
        acc = []
        res = []
        for n in nums:
            if n == 0 and acc:
                res.append(acc)
                acc = []
            elif n != 0:
                acc.append(n)
        if acc:
            res.append(acc)
        print(res)
        return max(max(prod(l) + prod(l[::-1])) for l in res)