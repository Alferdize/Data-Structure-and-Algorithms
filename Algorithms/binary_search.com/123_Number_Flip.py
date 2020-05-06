class Solution:
    def solve(self, n):
        # Write your code here
        a = [int(c) for c in str(n)]
        for i, x in enumerate(a):
            if x != 3:
                a[i] = 3
                break
        return int("".join(map(str, a)))