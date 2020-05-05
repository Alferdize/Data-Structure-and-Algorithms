class Solution:
    def solve(self,matrix):
        def solution(matrix,y,x,seen):
            if (y,x) in seen: return seen[(y,x)]
            if y == 0 or x ==0 :
                return sum(sum(q[:x+1]) for q in matrix[:y+1]) == 0
            ans =0 
            if matrix[y-1][x] == 0:
                ans += solution(matrix, y -1, x , seen)
            if matrix[y][x-1] == 0:
                ans += solution(matrix, y, x-1 , seen)
            seen[(y,x)] = ans
            return ans%1000000007
        return solution(matrix,len(matrix)-1,len(matrix[0])-1, {})%1000000007