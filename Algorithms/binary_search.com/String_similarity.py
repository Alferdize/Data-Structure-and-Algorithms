class Solution:
    def solve(self, s, t, k):
        a,b = set(),set()
        for i in range(len(s)-k+1):
            a.add(s[i:i+k])
        for j in range(len(t)-k+1):
            b.add(t[j:j+k])
        return len(a&b)>0
        



class Solution:
    def solve(self, s, t, k):
        for i in range(len(s)-k+1):
            if s[i:i+k] in t:
                return True
        return False