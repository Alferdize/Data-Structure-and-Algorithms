import collections

class Node:
    __slots__ = 'children', 'end'
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.end = -1

class Solution(object):
    def solve(self, words):
        def dfs(node):
            if node.end >= 0:
                yield node.end
            for nei in node.children.values():
                yield from dfs(nei)
        
        def is_pali(s, i, j):
            return all(s[k] == s[i + j + ~k] for k in range(i, i + j >> 1))
        
        trie = Node()
        for i, word in enumerate(words):
            cur = trie
            for letter in word:
                cur = cur.children[letter]
            cur.end = i
        
        ans = 0
        for j, word in enumerate(words):
            # looking for words[i] + words[j] palindrome pair
            cur = trie
            for l_index, letter in enumerate(reversed(word)):
                if cur.end >= 0 and is_pali(word, 0, len(word) - l_index):
                    ans += 1
                cur = cur.children.get(letter, None)
                if cur is None: 
                    break
            else:
                for i in dfs(cur):
                    if i != j and is_pali(words[i], len(word), len(words[i])):
                        ans += 1
        return ans