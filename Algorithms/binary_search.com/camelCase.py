class Solution:
    def solve(self, words):
        # Write your code here
        s=words.pop(0).lower()
        return s+"".join(w.capitalize() for w in words)