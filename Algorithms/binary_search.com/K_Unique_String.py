from collections import Counter
class Solution:
    def solve(self, s, k):
        counter=Counter(s)
        L = len(counter)
        if L<=k: return 0
        return sum(cnt for _,cnt in counter.most_common()[-(L-k):])