class Solution:
    def solve(self, node):
        # Write your code here
        slow, fast = node, node
        vals = []
        while fast and fast.next:
            vals.append(slow.val)
            slow, fast = slow.next, fast.next.next
        ret = slow
        if fast:
            slow = slow.next
        while slow:
            slow.val += vals.pop()
            slow = slow.next
        return ret