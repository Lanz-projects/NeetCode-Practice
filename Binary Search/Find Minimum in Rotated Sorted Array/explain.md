# Find Minimum in Rotated Sorted Array

## 🔍 Problem Summary

Given a sorted array of **unique** integers that has been rotated between `1` and `n` times, return the **minimum element** in the array.

Your solution must run in **O(log n)** time, so a linear scan is not acceptable.

---

## 🧠 Key Insight

Although the array has been rotated, **one half of the current search range is always sorted**.

By comparing the middle element with the rightmost element, we can determine which side contains the minimum:

- If `nums[mid] < nums[high]`, the minimum is in the **left half**, including `mid`.
- Otherwise, the minimum must be in the **right half**, excluding `mid`.

This allows us to repeatedly eliminate half of the remaining search space using binary search.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Scan through the entire array while keeping track of the smallest value.
- Return the minimum after examining every element.
- This works correctly but requires **O(n)** time, which does not satisfy the problem's constraints.

### 2. Better Approach

- Use two pointers representing the current search range.
- Repeatedly compute the middle index.
- Compare the middle element with the rightmost element:
  - If the middle element is smaller, the minimum is on the left side (including `mid`).
  - Otherwise, the minimum is on the right side.
- Continue narrowing the search range until only the minimum element remains.

Since the search space is halved on every iteration, the algorithm runs in **O(log n)** time while using **O(1)** extra space.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def findMin(self, nums):
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] < nums[high]:
                high = mid
            else:
                low = mid + 1

        return nums[high]
```
