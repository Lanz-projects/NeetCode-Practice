# Design Add And Search Words Data Structure

## 🔍 Problem Summary

Design a data structure that supports adding words and searching for them later. The search operation must handle both exact characters and the wildcard character `'.'`, which can represent any single lowercase letter.

The main challenge is efficiently supporting wildcard searches without checking every stored word. A simple lookup is no longer enough because each `'.'` can match multiple possible characters.

---

## 🧠 Key Insight

A trie is well suited for storing words because each path represents a sequence of characters. Exact character searches simply follow the corresponding path through the trie.

When a `'.'` is encountered, the search branches into every possible child node at that position. A depth-first search explores each valid path until either a complete match is found or all possibilities have been exhausted.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Store every word in a list and compare each one against the search query character by character.
- This works, but every search may require checking all stored words, making wildcard searches especially inefficient.

### 2. Optimal Approach

- Store every word in a trie where each node contains a dictionary of child nodes and a flag indicating whether a complete word ends there.
- For `addWord`, traverse the trie, creating child nodes as needed, and mark the final node as a complete word.
- For `search`, use a depth-first search starting from the root.
- If the current character is a letter, continue down the matching child node. If it is `'.'`, recursively search every child node from that position.
- If the end of the search string is reached, return whether the current node marks the end of a stored word.
- Inserting a word takes **O(m)** time, where `m` is the word length. A normal search also runs in **O(m)** time, while wildcard searches may branch into multiple paths. In the worst case, the search can explore many nodes, though the problem limits the number of wildcards to at most two. The trie requires **O(n)** space overall, where `n` is the total number of characters inserted.

---

## 🧪 Final Code (Python)

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """

        def dfs(j, root):
            curr = root

            for i in range(j, len(word)):
                c = word[i]

                if c == ".":
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]

            return curr.word

        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
```
