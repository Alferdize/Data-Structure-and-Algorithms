class Solution:
    def solve(self, intervals):
        # Write your code here
        intervals.sort(key=lambda x: x[1])
        last=None
        cnt=0
        while intervals:
            cur=intervals.pop(0)
            if not last or cur[0]>=last[1]:
                last=cur
                cnt+=1
        return cnt