# Word Search II

## 🔍 Problem Summary

You are given a 2D board of characters and a list of words. Return all words from the list that can be formed by connecting horizontally or vertically adjacent cells, without reusing the same cell within a single word.

The main challenge is efficiently searching for many words at once. Checking each word independently would repeatedly explore the same paths on the board, leading to unnecessary work.

---

## 🧠 Key Insight

A trie allows all of the target words to be stored in a single data structure, so shared prefixes are explored only once. As the board is traversed, the search only continues if the current sequence of characters exists as a prefix in the trie.

Combining the trie with backtracking prunes invalid paths early, making the search much more efficient than searching for each word separately.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- For every word in the list, perform a separate backtracking search on the board.
- Since many words share prefixes, this repeatedly explores the same paths, resulting in a significant amount of redundant work.

### 2. Optimal Approach

- Insert every word into a trie, where each node stores its children and whether it represents the end of a complete word.
- Start a depth-first search from every cell on the board.
- Before moving deeper, verify that the current character exists as a child of the current trie node. If it does not, stop exploring that path immediately.
- Keep track of the cells currently in the path so that no cell is used more than once for the same word.
- As characters are matched, move down the trie and build the current word. Whenever a trie node marks the end of a word, add it to the result set.
- After exploring all four directions, backtrack by removing the current cell from the visited set so it can be used in other searches.
- Building the trie takes **O(W × L)** time, where `W` is the number of words and `L` is the average word length. The board search prunes many invalid paths using the trie, making it much more efficient than searching each word independently. The trie requires **O(W × L)** space, while the recursion stack and visited set require up to **O(L)** additional space.

---

## 🧪 Final Code (Python)

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or
                r == ROWS or c == COLS or
                (r, c) in visit or
                board[r][c] not in node.children):
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.isWord:
                res.add(word)

            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)

            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)
```
