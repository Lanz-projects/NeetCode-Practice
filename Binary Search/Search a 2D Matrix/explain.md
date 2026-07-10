# Search a 2D Matrix

## 🔍 Problem Summary

Given m x n matrix:

- Each row sorted in non-decreasing order
- First int of each row is greater than last int of previous row
  Given target, return True if in matrix, else False
  Write in: O(log(m \* n))

---

## 🧠 Key Insight

The single most important idea that unlocks the solution.  
(Example: “We need fast membership checks → use a set.”)

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- One or two bullets describing how it works
- Why it’s too slow or not ideal

### 2. Optimal Approach

- The strategy you chose
- Why it works
- Why it’s better than brute force

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
```
