

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        # Write your code here
        import collections
        q = collections.deque()
        q.append((root, 0, 0))
        curr_depth = max_width = left = 0
       
        while q:
            node, depth, pos = q.popleft()
           
            if node.left:
                q.append((node.left, depth+1, pos*2))
            if node.right:
                q.append((node.right, depth+1, pos*2 + 1))
           
            if curr_depth != depth:
                curr_depth = depth
                left = pos
           
            max_width = max(max_width, pos-left+1)
       
        return max_width