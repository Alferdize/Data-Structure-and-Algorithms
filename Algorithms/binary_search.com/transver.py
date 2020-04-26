class Solution:
    def solve(self, root):
        # Write your code here
        q = [root]
        ans = []
        for node in q:
            ans.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return ans