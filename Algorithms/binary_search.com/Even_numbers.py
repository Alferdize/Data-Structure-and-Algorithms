# class Solution:
#     def solve(self, matrix):
#         # Write your code here
#         cnt =0
#         for i in matrix:
#             for j in i:
#                 if j % 2 ==0:
#                     cnt +=1
#         return cnt
        
class Solution:
    def solve(self, matrix):
        
# Write your code here
        res=0
        for i in matrix:
            for j in i:
                if j & 1 == 0:
                    res+=1
        return res