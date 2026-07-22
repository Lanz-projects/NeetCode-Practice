# Swim In Rising Water

## 🔍 Problem Summary

You are given an `n × n` grid where each cell's value represents its elevation. As time passes, the water level rises to match the current time `t`. You can move between adjacent cells only if **both cells' elevations are at most `t`**.

Return the **minimum time** needed to travel from the top-left corner to the bottom-right corner.

---

## 🧠 Key Insight

This is a **shortest path** problem where the "cost" of a path is **the maximum elevation encountered**, not the sum of elevations.

Using **Dijkstra's Algorithm**, always explore the path with the smallest current maximum elevation. For each move, the new cost becomes `max(current_time, neighbor_elevation)`. The first time we reach the destination, we've found the minimum possible time.

---

## 🧩 Approaches Considered

### 1. Brute Force

- Try every possible path from the start to the finish.
- For each path, compute the highest elevation encountered.
- Return the path with the smallest maximum elevation.
- Exponential time due to the enormous number of possible paths.

### 2. Better Approach

- Treat each cell as a graph node.
- Use a **min-heap** to always process the cell reachable with the smallest current required water level.
- Store `(time, row, col)` in the heap, where `time` is the maximum elevation seen so far.
- Visit each cell once, updating neighboring cells with `max(current_time, neighbor_height)`.
- As soon as the destination is popped from the heap, return its time.

---

## ⏱️ Time & Space Complexity

- **Time:** **O(N² log N)**
  - There are `N²` cells.
  - Each heap operation costs `O(log(N²)) = O(log N)`.

- **Space:** **O(N²)**
  - The visited set and priority queue can each store up to `N²` cells.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        visit = set()
        minHeap = [[grid[0][0], 0, 0]]  # (time/max-height, row, col)
        visit.add((0, 0))

        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        while minHeap:
            t, r, c = heapq.heappop(minHeap)

            if r == N - 1 and c == N - 1:
                return t

            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc

                if (
                    neiR < 0 or neiC < 0 or
                    neiR == N or neiC == N or
                    (neiR, neiC) in visit
                ):
                    continue

                visit.add((neiR, neiC))
                heapq.heappush(
                    minHeap,
                    [max(t, grid[neiR][neiC]), neiR, neiC]
                )
```
