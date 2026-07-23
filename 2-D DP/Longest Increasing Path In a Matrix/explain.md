# Longest Increasing Path In a Matrix

## 🔍 Problem Summary

You are given an `m x n` matrix of integers. Starting from any cell, you may move up, down, left, or right, but only to a cell containing a strictly larger value.

Your goal is to find the length of the longest possible increasing path in the matrix. The main challenge is that many paths overlap, so repeatedly exploring the same cells would result in a large amount of redundant work.

---

## 🧠 Key Insight

The longest increasing path starting from a particular cell is always the same, regardless of how that cell was reached. This means we can compute the answer for each cell once and reuse it whenever it appears in another search.

By combining depth-first search with memoization, each cell stores the length of its longest increasing path after it has been computed, avoiding repeated calculations.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Start a DFS from every cell and recursively explore every possible increasing path.
- Since many searches revisit the same cells and recompute identical paths, the runtime grows exponentially and becomes impractical for larger matrices.

### 2. Better Approach

- Use a DFS to compute the longest increasing path starting from each cell.
- Before exploring neighboring cells, check whether the current result has already been computed. If so, return the cached value immediately.
- From each cell, recursively explore the four directions, but only continue if the neighboring value is strictly greater than the current value.
- Store the longest path length for each cell in a dictionary so future searches can reuse it instead of recomputing it.
- Iterate through every cell in the matrix, treating each one as a potential starting point, and keep track of the maximum path length found.
- Because each cell is fully processed only once and each DFS considers at most four neighbors, the algorithm runs in **O(m × n)** time with **O(m × n)** additional space for the memoization table and recursion stack.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}

        def dfs(r, c, prevVal):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or
                    matrix[r][c] <= prevVal):
                return 0

            if (r, c) in dp:
                return dp[(r, c)]

            res = 1
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))

            dp[(r, c)] = res
            return res

        longest = 0
        for r in range(ROWS):
            for c in range(COLS):
                longest = max(longest, dfs(r, c, -1))

        return longest
```
