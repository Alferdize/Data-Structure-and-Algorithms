class Solution:
    def solve(self, coordinates):
        # Write your code here
        if len(coordinates) < 2:
            return False
        if len(coordinates) == 2:
            return True
        x1,y1 = coordinates[0]
        x2,y2 = coordinates[1]
        slope = (y2-y1)/(x2-x1)
        for i in range(len(coordinates[2:])):
            cur = coordinates[i]
            prev = coordinates[i-1]
            if slope != (cur[1] - prev[1])/(cur[0]-prev[0]):
                return False
        return True