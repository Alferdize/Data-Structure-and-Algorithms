class Solution:
    def solve(self, root, lo, hi):
        # Write your code here
        def solution(node):
            if node:
                if lo > node.val:
                    return solution(node.right)
                if hi < node.val:
                    return solution(node.left)
                if node.left:
                    node.left = solution(node.left)
                if node.right:
                    node.right = solution(node.right)
                return node
        return solution(root)