move = {
    "NORTH": lambda x,y: (x, y+1),
    "EAST": lambda x,y: (x+1, y),
    "SOUTH": lambda x,y: (x,y-1),
    "WEST": lambda x,y: (x-1, y)
}
class Solution:
    def solve(self, moves, x, y):
        # Write your code here
        tx,ty = 0, 0
        seen = {(tx,ty)}
        for m in moves:
            while (tx,ty) in seen:
                tx,ty = move[m](tx,ty)
            seen.add((tx,ty))
        return (x,y) == (tx,ty)