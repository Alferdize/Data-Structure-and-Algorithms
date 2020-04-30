class Solution:
    def solve(self, node):
        # Write your code here
        current = node
        while current and current.next:
            #swap values
            next = current.next
            current.val, next.val = next.val, current.val
            current = next.next
            
        return node