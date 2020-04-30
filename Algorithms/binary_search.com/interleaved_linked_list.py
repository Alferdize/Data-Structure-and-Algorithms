class Solution:
    def solve(self, l0, l1):
        # Write your code here
        if l0:
            l0.next = self.solve(l1,l0.next)
        else:
            return l1
        return l0