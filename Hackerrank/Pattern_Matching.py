class Solution:
    def solve(self, text, pattern):
        def search(i, j, mapping):
            if i == len(text) or j == len(pattern):
                return i == len(text) and j == len(pattern)
            elif pattern[j] in mapping:
                word = mapping[pattern[j]]
                return (
                    text[i:i+len(word)] == word and
                    search(i + len(word), j + 1, mapping)
                )
            else:
                for end in range(i, len(text)):
                    word = text[i:end+1]
                    mapping[pattern[j]] = word
                    if search(i + len(word), j + 1, mapping):
                        return True
                    del mapping[pattern[j]]
            return False
        
        return search(0, 0, {})