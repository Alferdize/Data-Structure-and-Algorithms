class Solution:
    def solve(self, arr):
        if not arr: return 0
        dp = {0:1}
        N = len(arr)
        for i in range(1, N):
            count = 0
            for j in range(i):
                if arr[i] > arr[j]:
                    count = max(count, dp[j])
            dp[i] = count + 1
        return max(dp.values())
            
        
        
        
# from itertools import islice, chain
# class Solution:
#     def solve(self, arr):
#         if len(arr) <= 1: return len(arr)
#         c = []
#         for i, x in enumerate(arr):
#             c.append(1+max(chain([0], (c[j] for j,y in enumerate(islice(arr,i)) if x > y))))
#         return max(c)