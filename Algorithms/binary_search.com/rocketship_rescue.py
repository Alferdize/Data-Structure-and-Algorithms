class Solution:
    def solve(self, weights, limit):
        # Write your code here
        weights.sort()
        i,j = 0, len(weights) -1
        ans = 0
        while i <= j:
            if weights[i] + weights[j] <= limit:
                i+=1
            j-=1
            ans +=1
        return ans