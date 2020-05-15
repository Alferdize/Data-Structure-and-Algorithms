class Solution:
    def solve(self, root):
        m = {}
        def aux(n, l):
            if n is not None: 
                if l not in m: m[l] = n.val
                aux(n.left, l + 1)
                aux(n.right, l + 1)
        aux(root, 0)
        return list(m.values())