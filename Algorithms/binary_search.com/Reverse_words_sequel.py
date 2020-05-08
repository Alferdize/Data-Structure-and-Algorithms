from itertools import groupby
class Solution:
    def solve(self, sentence, delimiters):
        words=[]
        ans=""
        for k,g in groupby(sentence, lambda x: x in delimiters):
            if not k:
                words.append("".join(g))
        
        for k,g in groupby(sentence, lambda x: x in delimiters):
            if k:
                ans+="".join(g)
            else:
                ans+=words.pop()
        return ans