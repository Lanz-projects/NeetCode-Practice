# Implement Trie (Prefix Tree)

## 🔍 Problem Summary

Design a Trie (Prefix Tree) data structure that efficiently stores a collection of strings. The trie must support inserting words, checking whether a complete word exists, and determining whether any stored word begins with a given prefix.

The main challenge is organizing the characters so that common prefixes are shared between words, allowing searches and prefix checks to be performed efficiently without scanning every stored string.

---

## 🧠 Key Insight

A trie represents each character as a node, with paths from the root corresponding to stored words. Words that share prefixes also share the same path through the tree, reducing redundant storage.

Each node keeps track of its child characters, while a separate flag marks whether a complete word ends at that node. This allows the trie to distinguish between a valid word and a prefix of a longer word.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Store every word in a list and perform a linear search for `search` and `startsWith`.
- While simple, each operation may require checking every stored word, making it inefficient as the dataset grows.

### 2. Better Approach

- Create a `TrieNode` that stores a dictionary of child nodes and a flag indicating whether a word ends at that node.
- For `insert`, start at the root and create child nodes for characters that do not already exist. After processing every character, mark the final node as the end of a word.
- For `search`, traverse the trie one character at a time. If any character is missing, return `False`; otherwise, return whether the final node is marked as the end of a word.
- For `startsWith`, traverse the trie in the same way, but only verify that the prefix exists without checking the end-of-word flag.
- Since each operation processes each character of the input exactly once, `insert`, `search`, and `startsWith` all run in **O(m)** time, where `m` is the length of the word or prefix. The trie requires **O(n)** space overall to store its nodes, where `n` is the total number of characters inserted.

---

## 🧪 Final Code (Python)

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```
