# Number of Islands

## 🔍 Problem Summary

You are given an `m x n` grid where each cell is either `"1"` (land) or `"0"` (water). Your task is to determine how many separate islands exist in the grid.

An island consists of horizontally or vertically connected land cells surrounded by water. The main challenge is counting each island exactly once without revisiting the same land multiple times.

---

## 🧠 Key Insight

Once you discover an unvisited land cell, you have found a new island. From that starting point, traverse all connected land cells and mark them as visited so they are not counted again.

By exploring an entire connected component before continuing the scan, each island contributes exactly one to the final count.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Start from every land cell and repeatedly search its neighboring land without keeping track of previously explored cells.
- This leads to revisiting the same island many times, making the solution unnecessarily inefficient and difficult to manage.

### 2. Optimal Approach

- Iterate through every cell in the grid.
- Whenever an unvisited land cell is found, increment the island count and perform a Breadth-First Search (BFS) starting from that cell.
- During the BFS, add each visited land cell to a `visit` set and explore its four neighboring cells (up, down, left, and right).
- Continue until every connected land cell has been visited. Once the BFS finishes, the entire island has been processed, so the outer loop continues searching for the next unvisited island.

Since each cell is visited at most once, the algorithm runs in **O(m × n)** time. The `visit` set and BFS queue together require **O(m × n)** space in the worst case.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (
                        r in range(rows)
                        and c in range(cols)
                        and grid[r][c] == "1"
                        and (r, c) not in visit
                    ):
                        q.append((r, c))
                        visit.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1

        return islands
```
