class Solution:
    def solve(self, nums):
        extval, ans = [], "" 
        l = len(str(max(nums))) + 1
        for i in nums: 
            temp = str(i) * l 
            extval.append((temp[:l:], i)) 
        extval.sort(reverse = True) 
        for i in extval: 
            ans += str(i[1]) 
        return ans


# import functools
# class Solution:
#     def solve(self, snippets):
#         snippets = [str(s) for s in snippets]
#         mlen = max(len(s) for s in snippets) * 2  # double the length of the longest snippet
#         return ''.join(sorted(snippets, reverse=True, key=lambda s: s*(mlen//len(s)+1)))