# Word Search

## 🔍 Problem Summary

You are given a 2D grid of characters and a target word. Determine whether the word can be formed by moving through adjacent cells (up, down, left, or right), without using the same cell more than once in a single path.

The main challenge is exploring all possible paths while ensuring that each cell is used at most once during the construction of the word.

---

## 🧠 Key Insight

This problem is naturally solved with backtracking. Starting from each cell, recursively attempt to match the next character of the word by moving to neighboring cells.

A set keeps track of the cells currently in the path so they are not revisited. If a path fails, backtracking removes the cell from the set, allowing it to be used in other search paths.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Try every possible path through the grid without remembering which cells have already been used.
- This leads to many invalid paths and repeated work, making the search extremely inefficient.

### 2. Optimal Approach

- Iterate through every cell in the board as a possible starting position.
- Use a depth-first search to recursively match one character of the word at a time.
- Before continuing the search, verify that the current position is within bounds, has not already been used in the current path, and matches the expected character.
- Add the current cell to the path, recursively search in all four directions, and then remove the cell when backtracking.
- If all characters in the word are matched, return `True`. If no starting position succeeds, return `False`.
- In the worst case, the algorithm explores up to four directions for the first character and up to three directions for each remaining character, resulting in a time complexity of **O(m × n × 4 × 3^(L-1))**, where `m` and `n` are the board dimensions and `L` is the length of the word. The recursion stack and path set require **O(L)** extra space.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                (r, c) in path):
                return False

            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            path.remove((r, c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
```