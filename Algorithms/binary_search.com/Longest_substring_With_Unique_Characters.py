class Solution:
    def solve(self, s):
        # Write your code here
        d = {}
        ans = l = 0
        for i,c in enumerate(s):
            if c in d: l = max(l,d[c] + 1)
            ans = max(ans, i - l + 1)
            d[c] = i
            
        return ans


# class Solution:
#     def solve(self, s):
#         # Write your code here
#         if len(s)==0:
#             return 0
#         if len(s)==1:
#             return 1
#         d=dict()
#         i=0
#         j=0
#         m=0
#         while j<len(s):
#             if d.get(s[j])==None:
#                 d[s[j]]=j
#             else:
#                 m=max(m,j-i)
#                 index=d[s[j]]+1
#                 for k in range(i,index):
#                     if d.get(s[k]) != None:
#                         d.pop(s[k])
#                 i=index
#                 d[s[j]]=j
#             j+=1
#         m=max(m,j-i)
#         return m