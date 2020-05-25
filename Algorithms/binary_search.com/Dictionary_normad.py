import string
from collections import defaultdict, deque
class Solution:
    def solve(self, dictionary, start, end):
        
        words = set(dictionary)
        q = deque([(start, 1)])
        seen = set()
        print(123)
        
        while q:
            x, d = q.popleft()
            # print(x, d)
            if x == end:
                return d
            elif x in seen:
                continue
            seen.add(x)
            for i in range(len(x)):
                for c in string.ascii_lowercase:
                    nb = x[:i] + c + x[i+1:]
                    if nb in words:
                        q.append((nb, d+1))
        
        return -1
