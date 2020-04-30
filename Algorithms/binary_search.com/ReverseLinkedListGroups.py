class Solution:
    def solve(self, node, k):
        
# Write your code here
        
        curr, head, prev = node, node, None
        
        while True:
            
            last_node_previous = prev 
# front part
            last_node_sublist = curr 
# last node after reversal will be
            i = 0
            
            while curr and i < k:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                i += 1
            
            if last_node_previous:
                last_node_previous.next = prev
            else:
                node = prev
            last_node_sublist.next = curr
            
            if not curr:
                break
            prev = last_node_sublist
            
        
        return node