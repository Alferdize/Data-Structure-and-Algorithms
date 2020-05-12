class Solution:
    def solve(self, words):
        # Write your code here
        m = max(map(len, words))
        ans = ['*' * (m + 4)]
        for word in words:
            line = ['* ', word, ' ' * (m - len(word)), ' *']
            ans.append("".join(line))
        ans.append(ans[0])
        return "\n".join(ans)