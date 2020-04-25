class Solution:
    def solve(self, preorder, inorder):
        ranks = {v:i for i,v in enumerate(inorder)}
        it = (Tree(v) for v in preorder)
        root = next(it)
        
        stack = [root]
        for n in it:
            if stack and ranks[n.val] < ranks[stack[-1].val]:
                stack[-1].left = n
                stack.append(n)
            else:
                while stack and ranks[n.val] > ranks[stack[-1].val]:
                    curr = stack.pop()
                curr.right = n
                stack.append(n)
        print(root)
            
        
        return root