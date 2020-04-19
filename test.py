class Solution:
    def solve(self, nums):
        # Write your code here
        sum = 0
        data = nums[::-1].copy()
        prev = data.pop()
        if prev == len(nums):
            for i in range(len(nums)-1):
                sum = data.pop()
                if prev - sum in data:
                    prev = sum
                elif sum == 1:
                    break
                else:
                    return False
            return True
        else:
            return False


s1 = Solution()
print(s1.solve([7, 4, 3, 2, 1, 1, 1]))