class Solution:
    def solve(self, words):
        # Write your code here
        first = ""
        counts = []
        count = 0
        for item in words:
            if item[0] == first:
                count += 1
            else:
                counts.append(count)
                count = 1
                first = item[0]
        counts.append(count)
        return max(counts)