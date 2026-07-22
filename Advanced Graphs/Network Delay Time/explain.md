# Network Delay Time

## 🔍 Problem Summary

You are given a directed, weighted graph representing a network of computers. Starting from node `k`, determine how long it takes for a signal to reach every node. If at least one node cannot be reached, return `-1`.

The challenge is finding the shortest path from one source node to every other node as efficiently as possible.

---

## 🧠 Key Insight

This is a **single-source shortest path** problem with **non-negative edge weights**, making **Dijkstra's Algorithm** the ideal solution.

Instead of exploring every possible path, always process the node with the currently smallest known travel time. Once a node is processed, its shortest distance is finalized. As soon as all nodes have been visited, the current travel time is the answer.

---

## 🧩 Approaches Considered

### 1. Brute Force

- Try every possible path from the starting node to every other node.
- Keep track of the shortest path found for each destination.
- Extremely inefficient because the number of possible paths grows exponentially.

### 2. Better Approach

- Build an adjacency list to represent the graph.
- Use a **min-heap (priority queue)** to always process the closest unvisited node.
- Keep a `visit` set so each node is finalized only once.
- Because Dijkstra processes nodes in increasing order of distance, **the moment all `n` nodes have been visited, the current distance is the maximum shortest-path distance**.
- If the heap becomes empty before all nodes are visited, some nodes are unreachable, so return `-1`.

---

## ⏱️ Time & Space Complexity

- **Time:** **O((V + E) log V)**
  - Each edge may be pushed into the priority queue.
  - Heap operations take `O(log V)`.

- **Space:** **O(V + E)**
  - The adjacency list stores all edges.
  - The heap and visited set together store up to `V` nodes.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def networkDelayTime(self, times, n, k):
        edges = collections.defaultdict(list)

        for u, v, w in times:
            edges[u].append((v, w))

        minHeap = [(0, k)]
        visit = set()

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)

            if n1 in visit:
                continue

            visit.add(n1)

            if len(visit) == n:
                return w1

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))

        return -1
```
