class Solution:
    def solve(self, matrix, blocks):
        # Write your code here
        sb = set(blocks)
        index = {}
        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                if x in sb:
                    index[x] = (i,j)
        blocks = [index[x] for x in blocks]
        
        return sum(abs(a[0]-b[0]) + abs(a[1] - b[1]) for a,b in zip([(0,0)] + blocks, blocks))