from math import floor
class Solution:
    def solve(self, hour, minutes):
        # Write your code here
        am = minutes*6
        ah = minutes*.5 + (hour%12)*30
        x=abs(am-ah)
        return floor(x) if x <=180 else floor(360-x)