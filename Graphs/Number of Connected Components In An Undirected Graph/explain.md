# Number of Connected Components In An Undirected Graph

## 🔍 Problem Summary

You are given `n` nodes and a list of undirected edges that connect some pairs of nodes.

Your task is to determine how many connected components exist in the graph. A connected component is a group of nodes where every node can be reached from every other node in the same group. The main challenge is efficiently merging connected nodes without repeatedly traversing the graph.

---

## 🧠 Key Insight

Treat each node as its own separate component initially. Whenever an edge connects two different components, merge them into one.

A Union-Find (Disjoint Set Union) data structure makes these merges efficient by quickly determining whether two nodes already belong to the same component.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Build the graph and perform a DFS or BFS from every unvisited node to count connected components.
- Although this correctly solves the problem, repeatedly traversing the graph is less efficient than using Union-Find for dynamic component merging.

### 2. Optimal Approach

- Initialize every node as its own parent, meaning each node starts as a separate connected component.
- Use the `find` function with path compression to quickly locate the representative (root) of each component.
- For every edge, attempt to `union` the two endpoints. If they belong to different components, merge them and decrease the component count by one.
- If both nodes already share the same parent, they are already connected, so no merge is needed.
- After processing every edge, the remaining component count is the answer.

With path compression and union by rank, each Union-Find operation is nearly constant time. Processing all edges takes **O(E · α(V))** time, where `α` is the inverse Ackermann function, which is effectively constant in practice. The parent and rank arrays require **O(V)** space.

---

## 🧪 Final Code (Python)

```python
class Solution:
    def countComponents(self, n: int, edges):
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1

            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]

            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
        
            if p1 == p2:
                return 0
        
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
        
            return 1


        res = n

        for n1, n2 in edges:
            res -= union(n1, n2)

        return res
```
