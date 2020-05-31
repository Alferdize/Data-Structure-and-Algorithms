class Solution:
    def solve(self, intervals, target):
        start, end = target
        left = []
        right = []

        for s, e in intervals:
            if end < s:
                right.append((s, e))
            
            elif start > e:
                left.append((s, e))
            
            else:
                start = min(start, s)
                end = max(end, e)
        
        left.append((start, end))
        return left + right