from collections import defaultdict
class Solution:
    def solve(self, matrix, k):
        cum=[[defaultdict(int) for _ in matrix[0]] for _ in matrix]
        cum[0][0][matrix[0][0]]+=1
        for i in range(1,len(matrix)):
            for v in cum[i-1][0].keys():
                cum[i][0][v + matrix[i][0]]+=cum[i-1][0][v]
        for j in range(1,len(matrix[0])):
            for v in cum[0][j-1].keys():
                cum[0][j][v+matrix[0][j]]+=cum[0][j-1][v]
        for i in range(1,len(matrix)):
            for j in range(1,(len(matrix[0]))):
                for v in cum[i-1][j].keys():
                    cum[i][j][v + matrix[i][j]]+=cum[i-1][j][v]
                for v in cum[i][j-1].keys():
                    cum[i][j][v+matrix[i][j]]+=cum[i][j-1][v]
        return cum[-1][-1][k] % (10**9 +  7)