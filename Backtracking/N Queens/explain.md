# N Queens

## 🔍 Problem Summary

Given an integer `n`, place `n` queens on an `n × n` chessboard so that no two queens can attack each other.

Return every distinct board configuration where each row contains exactly one queen and no two queens share the same row, column, or diagonal. The main challenge is efficiently exploring valid placements while avoiding configurations that violate these constraints.

---

## 🧠 Key Insight

Since each row must contain exactly one queen, we can place queens one row at a time while keeping track of which columns and diagonals are already occupied.

By using sets to record occupied columns, positive diagonals, and negative diagonals, we can determine whether a position is valid in constant time. Backtracking allows us to undo placements and explore every valid board configuration.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Try every possible way to place `n` queens on the board.
- After generating a complete board, check whether any queens attack each other.
- This approach explores an enormous number of invalid configurations, making it far too slow as `n` grows.

### 2. Better Approach

- Use backtracking to place one queen in each row.
- For each row, try placing a queen in every column.
- Before placing a queen, check whether its column, positive diagonal (`row + col`), or negative diagonal (`row - col`) is already occupied.
- If the position is valid, place the queen, mark its column and diagonals as occupied, and recursively process the next row.
- Once all `n` rows have been filled, convert the board into the required string format and add it to the results.
- After each recursive call, remove the queen and clear its column and diagonal entries so other placements can be explored.

Using sets makes each validity check **O(1)**, allowing the algorithm to prune invalid placements early instead of exploring impossible boards. The backtracking search runs in approximately **O(n!)** time in the worst case, with **O(n)** auxiliary space for the recursion stack and the tracking sets, excluding the space needed to store the solutions.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        col = set()
        posDiag = set()  # r + c
        negDiag = set()  # r - c

        res = []
        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            if n == r:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in col or (r - c) in negDiag or (r + c) in posDiag:
                    continue

                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res
```
