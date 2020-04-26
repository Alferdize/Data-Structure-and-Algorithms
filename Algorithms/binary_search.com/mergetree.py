class Solution:
    def solve(self, node0, node1):
        # Write your code here
        if not node0:
            return node1
        elif not node1:
            return node0
        else:
            node0.val+=node1.val
            node0.left=self.solve(node0.left,node1.left)
            node0.right=self.solve(node0.right,node1.right)
            return node0