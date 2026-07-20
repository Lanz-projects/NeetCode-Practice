# Surrounded Regions

## 🔍 Problem Summary

You are given an `m x n` board containing `'X'` and `'O'` characters. A region is formed by horizontally or vertically connected `'O'` cells.

Your task is to capture every region that is completely surrounded by `'X'` cells by replacing its `'O'` cells with `'X'`. Any region connected to the border cannot be captured and must remain unchanged. The main challenge is distinguishing enclosed regions from those that are connected to the edge.

---

## 🧠 Key Insight

Instead of trying to identify which regions should be captured, first identify the regions that **cannot** be captured.

Any `'O'` connected to the border is guaranteed to remain `'O'`, so temporarily mark those cells. Afterward, every remaining `'O'` must be completely surrounded and can safely be changed to `'X'`.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Start a DFS or BFS from every `'O'` to determine whether its region reaches the border.
- This repeatedly explores the same regions, resulting in unnecessary work.

### 2. Optimal Approach

- Iterate over every border cell and start a Depth-First Search (DFS) from each border `'O'`.
- During the DFS, temporarily mark every connected `'O'` as `'T'` to indicate it cannot be captured.
- After all border-connected regions have been marked, traverse the board again and convert every remaining `'O'` to `'X'`, since those regions are fully enclosed.
- Finally, replace every temporary `'T'` back with `'O'` to restore the regions that should remain unchanged.

Each cell is visited at most a constant number of times, so the algorithm runs in **O(m × n)** time. The recursive DFS call stack requires **O(m × n)** space in the worst case.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            if (
                r < 0
                or r == ROWS
                or c < 0
                or c == COLS
                or board[r][c] != "O"
            ):
                return

            board[r][c] = "T"

            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if (
                    board[r][c] == "O"
                    and (r in [0, ROWS - 1] or c in [0, COLS - 1])
                ):
                    capture(r, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
```
