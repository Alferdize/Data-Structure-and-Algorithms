# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node, k):
        head=node
        cur=head
        last=head
        l=0
        while cur:
            last=cur
            cur=cur.next
            l+=1
        k=(l-k)%l
        if not k: return head
        kth=head
        prev=last
        while k:
            prev=kth
            kth=kth.next
            k-=1
        prev.next=None
        last.next=h