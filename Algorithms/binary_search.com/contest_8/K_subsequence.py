class Solution(object):
    def solve(self, A, K):
        if not A:
            return 0
        freqmap = [[0]]
        for i in range(1, len(A)):
            ans_f = -1
            for f in range(len(freqmap) - 1, -1, -1):
                for h in freqmap[f]:
                    if abs(A[h] - A[i]) <= K:
                        ans_f = f
                        break
                if ans_f >= 0:
                    break
            
            ans_f += 1
            if ans_f >= len(freqmap):
                freqmap.append([i])
            else:
                freqmap[ans_f].append(i)
        return len(freqmap)