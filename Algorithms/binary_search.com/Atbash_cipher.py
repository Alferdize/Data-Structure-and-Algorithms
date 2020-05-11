from string import ascii_lowercase
class Solution:
    def solve(self, text):
        d = dict(zip(ascii_lowercase, ascii_lowercase[::-1]))
        return "".join(map(lambda c: d[c], text))
        
        
# class Solution:
#     def solve(self, text):
#         def reflect(c):
#             ci = ord(c) - ord('a')
#             ci = 25 - ci
#             return chr(ord('a') + ci)
        
#         return "".join(map(reflect, text))