# Reconstruct Itinerary

## 🔍 Problem Summary

You are given a list of airline tickets where each ticket represents a flight from one airport to another. Starting from `"JFK"`, reconstruct the complete itinerary that uses **every ticket exactly once**.

If multiple valid itineraries exist, return the one with the **smallest lexical (alphabetical) order**.

---

## 🧠 Key Insight

This problem is asking for an **Eulerian Path**—a path that uses every edge exactly once.

Using **Hierholzer's Algorithm**, we repeatedly travel as far as possible, removing tickets as we use them. When we reach an airport with no remaining outgoing flights, we add it to the result while backtracking. Sorting each destination list in reverse order allows us to efficiently pop the lexicographically smallest destination.

---

## 🧩 Approaches Considered

### 1. Brute Force

- Try every possible itinerary using backtracking.
- Verify whether every ticket is used exactly once.
- Choose the lexicographically smallest valid itinerary.
- Too slow because the number of possible itineraries grows factorially.

### 2. Better Approach

- Build an adjacency list where each airport stores its destinations.
- Sort each destination list in **reverse lexicographical order** so the smallest airport can be popped in O(1).
- Use an iterative version of **Hierholzer's Algorithm** with a stack.
- When an airport has no remaining outgoing flights, add it to the answer.
- Reverse the final result since airports are added during backtracking.

---

## ⏱️ Time & Space Complexity

- **Time:** **O(E log E)**
  - Sorting the destination lists dominates the runtime.
  - DFS traversal itself visits each ticket exactly once.

- **Space:** **O(E + V)**
  - The graph stores every ticket once.
  - The stack and result list together hold at most all airports/tickets.

---

## 🧪 Final Code (Python)

```python
class Solution:
    def findItinerary(self, tickets):
        graph = collections.defaultdict(list)

        for src, des in tickets:
            graph[src].append(des)

        for src in graph:
            graph[src].sort(reverse=True)

        stack = ["JFK"]
        res = []

        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            else:
                res.append(stack.pop())

        return res[::-1]
```
