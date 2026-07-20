# Walls And Gates

## 🔍 Problem Summary

You are given an `m x n` grid where each cell is either a wall (`-1`), a gate (`0`), or an empty room (`INF`). Your task is to update every empty room with the distance to its nearest gate.

If an empty room cannot reach any gate, it should remain unchanged. The main challenge is finding the shortest distance to the closest gate for every room without performing unnecessary repeated searches.

---

## 🧠 Key Insight

Instead of starting a search from every empty room, start from every gate at the same time.

By performing a multi-source Breadth-First Search (BFS), the first time an empty room is reached is guaranteed to be its shortest distance to a gate, since BFS explores locations level by level.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Run a BFS from every empty room to find the nearest gate.
- This repeatedly explores the same areas of the grid, making the solution much slower than necessary.

### 2. Optimal Approach

- Initialize a queue with every gate in the grid before starting the search.
- Perform a multi-source BFS, expanding outward from all gates simultaneously.
- As each room is reached for the first time, mark it as visited, update its distance, and add its neighboring rooms to the queue.
- Because BFS processes cells level by level, the first distance assigned to a room is guaranteed to be the shortest possible distance to any gate.

Since each room is added to the queue at most once, the algorithm runs in **O(m × n)** time. The queue and visited set together require **O(m × n)** space in the worst case.

---

## 🧪 Final Code (Python)

```python
from collections import deque


class Solution:
    def wallsAndGates(self, rooms):
        ROWS, COLS = len(rooms), len(rooms[0])
        visit = set()
        q = deque()

        def addRoom(r, c):
            if (
                r < 0
                or r == ROWS
                or c < 0
                or c == COLS
                or (r, c) in visit
                or rooms[r][c] == -1
            ):
                return

            visit.add((r, c))
            q.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    visit.add((r, c))
                    q.append([r, c])

        dist = 0

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist

                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)

            dist += 1
```
