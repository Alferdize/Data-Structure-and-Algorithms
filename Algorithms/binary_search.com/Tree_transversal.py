class Solution:
    def solve(self, root, moves):
        # Write your code here
        stack= []
        cur = root
        for mov in moves:
            if mov == "LEFT":
                stack.append(cur)
                cur = cur.left
            if mov == "RIGHT":
                stack.append(cur)
                cur = cur.right
            if mov == "UP":
                cur = stack.pop()
        return cur.val