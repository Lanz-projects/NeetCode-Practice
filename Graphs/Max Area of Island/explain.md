# Max Area of Island

## 🔍 Problem Summary

You are given an `m x n` binary grid where `1` represents land and `0` represents water. Your task is to find the area of the largest island in the grid.

An island is formed by horizontally or vertically connected land cells. The main challenge is exploring each island completely while avoiding revisiting the same cells, then keeping track of the largest area found.

---

## 🧠 Key Insight

Instead of only determining whether an island exists, perform a traversal from each unvisited land cell and count how many cells belong to that connected component.

By computing the size of every island and keeping the maximum, each land cell is processed exactly once and the largest island can be found efficiently.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Start from every land cell and repeatedly explore all connected land without remembering which cells have already been processed.
- This causes the same islands to be traversed multiple times, making the solution much less efficient.

### 2. Better Approach

- Iterate through every cell in the grid.
- When a land cell that has not been visited is found, start a Depth-First Search (DFS) from that cell.
- The DFS marks each visited land cell and recursively explores all four neighboring directions.
- Each recursive call returns the size of the connected land it discovers, and adding these results together gives the total area of that island.
- After each DFS completes, compare its returned area with the current maximum and update the answer if necessary.

Since every cell is visited at most once, the algorithm runs in **O(m × n)** time. The visited set and recursive call stack require **O(m × n)** space in the worst case.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (
                r < 0
                or r == ROWS
                or c < 0
                or c == COLS
                or grid[r][c] == 0
                or (r, c) in visit
            ):
                return 0

            visit.add((r, c))
            return (
                1
                + dfs(r + 1, c)
                + dfs(r - 1, c)
                + dfs(r, c + 1)
                + dfs(r, c - 1)
            )

        maxArea = 0

        for r in range(ROWS):
            for c in range(COLS):
                maxArea = max(maxArea, dfs(r, c))

        return maxArea
```
