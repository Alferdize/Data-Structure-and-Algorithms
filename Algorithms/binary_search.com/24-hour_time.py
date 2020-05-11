class Solution:
    def solve(self, s):
        # Write your code here
        (h, m), t = map(int, s[:-2].split(':')),s[-2:]
        if t == 'pm' and h < 12: h += 12
        if t == 'am': h %= 12
        return '%02d:%02d'%(h,m)