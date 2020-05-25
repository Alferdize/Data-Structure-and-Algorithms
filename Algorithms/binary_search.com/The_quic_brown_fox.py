class Solution:
    def solve(self, words, s):
        string = [0] * len(s)
        for w in words:
            index = s.find(w)
            if index == -1: return False
            for j in range(index,index+len(w)):
                string[j] = 1
        return all(string)