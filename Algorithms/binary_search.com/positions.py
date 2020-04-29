from itertools import groupby
class Solution:
    def solve(self, positions):
       
        speed = [abs(a-b) for a, b in zip(positions, positions[1:])]
       
        return 1 + max(len([*g]) for _, g in groupby(speed))