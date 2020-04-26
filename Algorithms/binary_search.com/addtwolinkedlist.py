class Solution:
    def solve(self, l0, l1):
        head=l0
        carry=0            
        end=None
        while l0 and l1:
            carry,l0.val = divmod(l0.val+l1.val+carry, 10)
            l0=l0.next
            l1=l1.next
            end=l0 if l0 else end
        if carry:
            end.next=LLNode(carry)
        return head