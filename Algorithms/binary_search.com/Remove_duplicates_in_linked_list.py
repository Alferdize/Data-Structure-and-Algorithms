
class Solution:
    def solve(self, head):
        seen = set()
        node = head
        while node:
            seen.add(node.val)
            while node.next and node.next.val in seen:
                node.next = node.next.next
            node = node.next
        return head