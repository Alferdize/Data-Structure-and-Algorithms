def solve(self, root):        # Write your code here
    def trv(node):  # return height of a node
        if node is None:
            return [0, True]
        else:
            lh = trv(node.left)
            rh = trv(node.right)
            return [max(lh[0], rh[0])+1, abs(lh[0]-rh[0]) <= 1 and lh[1] and rh[1]]

    return trv(root)[1]
