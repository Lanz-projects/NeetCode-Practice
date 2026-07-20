# Clone Graph

## 🔍 Problem Summary

You are given a reference to a node in a connected, undirected graph. Each node contains a value and a list of its neighboring nodes.

Your task is to create and return a deep copy of the entire graph. The main challenge is correctly recreating every node and its connections without duplicating nodes or getting stuck in cycles.

---

## 🧠 Key Insight

As you traverse the graph, create each node only once and store a mapping from the original node to its cloned counterpart.

Whenever you encounter a node you've already cloned, simply reuse the existing copy instead of creating another one. This naturally handles cycles while preserving the graph's structure.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Recursively copy every neighbor without keeping track of previously cloned nodes.
- This fails on graphs with cycles because the same nodes are revisited indefinitely, leading to infinite recursion and duplicate copies.

### 2. Optimal Approach

- Use a Depth-First Search (DFS) to traverse the graph.
- Maintain a dictionary that maps each original node to its cloned node.
- When visiting a node for the first time, create its clone and store it in the dictionary before exploring its neighbors.
- Recursively clone each neighbor and append the cloned neighbors to the current node's neighbor list.
- If a node has already been cloned, immediately return the existing copy instead of creating another one.

Since every node and edge is visited only once, the algorithm runs in **O(V + E)** time, where `V` is the number of vertices and `E` is the number of edges. The dictionary and recursive call stack require **O(V)** space.

---

## 🧪 Final Code (Python)

```python
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node) if node else None
```
