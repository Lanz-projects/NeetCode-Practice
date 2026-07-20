# Rotting Oranges

## 🔍 Problem Summary

You are given an `m x n` grid where each cell is either empty (`0`), contains a fresh orange (`1`), or contains a rotten orange (`2`). Every minute, any fresh orange that is horizontally or vertically adjacent to a rotten orange also becomes rotten.

Your task is to determine the minimum number of minutes needed until no fresh oranges remain. If some fresh oranges can never become rotten, return `-1`.

---

## 🧠 Key Insight

All rotten oranges spread the infection at the same time, making this a perfect fit for a multi-source Breadth-First Search (BFS).

By placing every initially rotten orange into the queue, each BFS level represents one minute passing, and the first time a fresh orange is reached is the earliest it can become rotten.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Simulate each minute by repeatedly scanning the entire grid to find newly rotten oranges.
- This requires many unnecessary passes over the grid, making the solution much less efficient.

### 2. Optimal Approach

- First, count the number of fresh oranges and add every rotten orange to a queue.
- Perform a multi-source BFS, where each level of the queue represents one minute.
- For every rotten orange in the current level, rot each adjacent fresh orange, add it to the queue, and decrease the fresh orange count.
- Continue until there are no more oranges to process or all fresh oranges have become rotten.
- If every fresh orange is eventually infected, return the elapsed time. Otherwise, return `-1` because some oranges could never be reached.

Since each cell is processed at most once, the algorithm runs in **O(m × n)** time. The queue stores at most all cells in the grid, giving a worst-case space complexity of **O(m × n)**.

---

## 🧪 Final Code (Python)

```python
from collections import deque


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        q = deque()
        time, fresh = 0, 0

        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])

        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    # if in bounds and fresh, make rotten
                    if (
                        row < 0
                        or row == ROWS
                        or col < 0
                        or col == COLS
                        or grid[row][col] != 1
                    ):
                        continue

                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1

            time += 1

        return time if fresh == 0 else -1
```
