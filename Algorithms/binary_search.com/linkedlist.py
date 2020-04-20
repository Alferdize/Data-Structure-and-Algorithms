# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        next = None
        curr = node.next
        node.next = None
        prev = node
        while(curr):
            if not curr.next:
                curr.next = prev
                prev = curr
                return prev
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            
        
        return prev