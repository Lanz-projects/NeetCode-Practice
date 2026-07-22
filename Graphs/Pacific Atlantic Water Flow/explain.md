# Pacific Atlantic Water Flow

## 🔍 Problem Summary

You are given an `m x n` grid where each cell represents the height of a piece of land. Water can flow from a cell to one of its four neighboring cells if the neighbor's height is less than or equal to the current cell's height.

The Pacific Ocean touches the top and left edges of the grid, while the Atlantic Ocean touches the bottom and right edges. Your task is to return all coordinates from which water can flow to **both** oceans. The main challenge is efficiently determining which cells can reach each ocean without repeatedly exploring the same paths.

---

## 🧠 Key Insight

Instead of starting a search from every cell, reverse the direction of the search by starting from each ocean's border.

By moving only to neighboring cells with equal or greater height, you identify every cell that can reach that ocean. The cells that appear in both searches are exactly the ones that can flow to both oceans.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Run a DFS or BFS from every cell to determine whether water can eventually reach both oceans.
- This repeats many of the same traversals, making the solution much less efficient.

### 2. Better Approach

- Perform two separate Depth-First Searches (DFS): one starting from every Pacific border cell and another starting from every Atlantic border cell.
- During each DFS, only move to neighboring cells whose height is **greater than or equal to** the current cell's height. This reverses the direction of water flow and finds every cell that can reach that ocean.
- Store the cells reachable from the Pacific in one set and the cells reachable from the Atlantic in another.
- After both traversals finish, iterate through the grid and collect every coordinate that appears in both sets.

Each cell is visited at most once during each DFS, so the algorithm runs in **O(m × n)** time. The two visited sets and the recursive call stack require **O(m × n)** space in the worst case.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if (
                (r, c) in visit
                or r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or heights[r][c] < prevHeight
            ):
                return

            visit.add((r, c))

            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res
```
