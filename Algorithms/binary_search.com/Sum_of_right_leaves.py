class Solution:
    def solve(self, root):
        # Write your code here
        def solution(root, right=False):
            if not root:
                return 0
            elif not root.left and not root.right and right:
                return root.val
            return solution(root.left, False) + solution(root.right, True)
        return solution(root)