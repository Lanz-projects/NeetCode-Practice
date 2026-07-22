# Min Cost to Connect All Points

## 🔍 Problem Summary

You are given a set of points on a 2D plane. The cost of connecting any two points is their **Manhattan distance**. Your goal is to connect every point so that there is exactly one path between any pair of points (forming a tree) while minimizing the total connection cost.

The challenge is finding the minimum total cost without creating cycles.

---

## 🧠 Key Insight

This is a **Minimum Spanning Tree (MST)** problem.

Using **Prim's Algorithm**, we start from any point and repeatedly add the cheapest edge that connects a new point to the growing tree. By always choosing the smallest available connection, we guarantee the minimum total cost.

---

## 🧩 Approaches Considered

### 1. Brute Force

- Generate every possible way to connect all points into a tree.
- Compute the total cost for each valid tree.
- Return the minimum cost.
- Impractical because the number of possible spanning trees grows exponentially.

### 2. Better Approach

- Build a graph where every pair of points is connected by an edge weighted by their Manhattan distance.
- Use **Prim's Algorithm** with a min-heap.
- Start from any point and repeatedly choose the smallest-cost edge that connects an unvisited point.
- Keep adding points until every point has been included in the spanning tree.

---

## ⏱️ Time & Space Complexity

- **Time:** **O(N² log N)**
  - Building the complete graph takes `O(N²)`.
  - Heap operations across all edges contribute `O(N² log N)`.

- **Space:** **O(N²)**
  - The adjacency list stores every pair of points.
  - The heap and visited set require additional space.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        N = len(points)
        adj = {i: [] for i in range(N)}

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        res = 0
        visit = set()
        minHeap = [[0, 0]]  # [cost, point]

        while len(visit) < N:
            cost, i = heapq.heappop(minHeap)

            if i in visit:
                continue

            res += cost
            visit.add(i)

            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minHeap, [neiCost, nei])

        return res
```
