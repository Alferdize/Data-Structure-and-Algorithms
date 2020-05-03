class Solution:
    def solve(self, node):
        # Write your code here
        while node.next:
            if node.val >= node.next.val:
                return False
            node = node.next
        return True