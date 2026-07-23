# Unique Paths

## 🔍 Problem Summary

Given an `m x n` grid, determine how many different ways a robot can travel from the **top-left** corner to the **bottom-right** corner if it can only move **right** or **down**.

The challenge is efficiently counting all possible paths without repeatedly solving the same subproblems.

---

## 🧠 Key Insight

The number of paths to any cell is simply the **sum of the paths from the cell below and the cell to the right**.

This naturally leads to **dynamic programming**, where we build the answer from the destination back to the start.

---

## 🧩 Approaches Considered

### 1. Brute Force (Recursive DFS)

- At each position, recursively try moving right and down.
- Count every path that reaches the destination.

**Why it's too slow:**

- Recomputes the same subproblems many times.
- Time Complexity: **O(2^(m+n))**

### 2. Better Approach (Dynamic Programming)

- Start from the bottom row, where every cell has exactly one path to the finish.
- Build each row from right to left.
- Each cell stores:
  - paths from the cell to its right
  - plus paths from the cell below.
- Only keep the previous row, reducing memory usage.

**Why it works:**

- Every path from a cell must begin by moving either **right** or **down**.
- By solving smaller subproblems first, every value is computed exactly once.

**Why it's better than brute force:**

- Time Complexity: **O(m × n)**
- Space Complexity: **O(n)**

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]
```
