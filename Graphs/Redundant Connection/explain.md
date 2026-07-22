# Redundant Connection

## 🔍 Problem Summary

You are given an undirected graph that originally formed a tree, but one additional edge has been added. This extra edge creates exactly one cycle in the graph.

Your task is to identify and return the edge that can be removed so the graph becomes a valid tree again. If multiple edges could be removed, return the one that appears last in the input.

---

## 🧠 Key Insight

As you process the edges one by one, keep track of which nodes already belong to the same connected component.

If an edge connects two nodes that are already connected, adding that edge would create a cycle, making it the redundant connection.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Remove each edge one at a time and perform a DFS or BFS to check whether the remaining graph is still connected and free of cycles.
- This requires repeatedly traversing the graph, making it much less efficient.

### 2. Better Approach

- Use a Union-Find (Disjoint Set Union) data structure to track connected components.
- Initially, every node is its own parent.
- For each edge, use the `find` function to determine the representative parent of both endpoints.
- If both nodes already share the same parent, they are already connected, so adding this edge creates a cycle. Return that edge immediately.
- Otherwise, merge the two components using `union`, applying path compression and union by rank to keep operations efficient.

Each edge is processed once, and each Union-Find operation runs in nearly constant time. The overall time complexity is **O(E · α(V))**, where `α` is the inverse Ackermann function, which is effectively constant in practice. The parent and rank arrays require **O(V)** space.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        N = len(edges)
        par = [i for i in range(N + 1)]
        rank = [1] * (N + 1)

        def find(n):
            if n != par[n]:
                par[n] = find(par[n])
            return par[n]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]

            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
```
