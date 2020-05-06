class Solution:
    def solve(self, n, friends):
        # Write your code here
        have_friends = [False]*(n)
        for x,y in friends:
            have_friends[x] = True
            have_friends[y] = True
        
        return all(have_friends)