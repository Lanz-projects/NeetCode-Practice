# Search a 2D Matrix

## 🔍 Problem Summary

Given an `m x n` matrix where:

- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.

Given a target value, return `True` if the target exists in the matrix; otherwise, return `False`.

The required time complexity is **O(log(m \* n))**, so we need to leverage the matrix's sorted structure instead of scanning every element.

---

## 🧠 Key Insight

Although the input is a 2D matrix, it behaves like one large sorted array because:

- Each row is individually sorted.
- Every row starts with a value greater than the previous row's last value.

This allows us to perform **binary search twice**:

1. First, binary search over the rows to find the only row that could contain the target.
2. Then, perform another binary search within that row.

By repeatedly cutting the search space in half, we efficiently locate the target without visiting every element.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Iterate through every row and every element until the target is found.
- Return `True` if found; otherwise return `False`.
- This examines every element in the worst case, resulting in **O(m × n)** time.

### 2. Better Approach

- First, binary search the rows:
  - If the target is larger than the row's last element, search lower rows.
  - If the target is smaller than the row's first element, search higher rows.
  - Otherwise, the target must be in that row if it exists.
- Once the correct row is found, perform a standard binary search within that row.
- Return `True` if the target is found; otherwise return `False`.

Each binary search runs in logarithmic time, giving an overall complexity of **O(log m + log n)**, which is equivalent to **O(log(m × n))**.

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
