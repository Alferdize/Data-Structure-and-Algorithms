class Solution:
    def solve(self, older, newer):
        # Write your code here
        A = list(map(int,older.split(".")))
        B = list(map(int,newer.split(".")))
        for a,b in zip (A,B):
            if a < b : return True
            if a > b : return False
        return False