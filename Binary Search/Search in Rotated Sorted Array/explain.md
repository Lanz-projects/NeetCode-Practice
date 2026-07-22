# Search in Rotated Sorted Array

## 🔍 Problem Summary

You are given an array of **distinct integers** that was originally sorted in ascending order but has been rotated at an unknown pivot.

Given a target value, return its index if it exists in the array; otherwise, return `-1`.

The challenge is to find the target in **O(log n)** time, so we cannot simply scan through the array.

---

## 🧠 Key Insight

Even though the array has been rotated, **at least one half of the current search range is always sorted.**

By determining which half is sorted, we can check whether the target lies within that range:

- If it does, continue searching that half.
- Otherwise, search the other half.

This allows us to eliminate half of the remaining elements on every iteration, just like standard binary search.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Iterate through every element until the target is found.
- Return its index if found; otherwise return `-1`.
- This requires **O(n)** time, which does not satisfy the required logarithmic runtime.

### 2. Better Approach

- Use two pointers representing the current search range.
- Repeatedly compute the middle index.
- If the middle element is the target, return its index.
- Otherwise:
  - Determine whether the **left half** is sorted.
    - If it is, check whether the target lies within that half.
      - If so, search left.
      - Otherwise, search right.
  - If the left half is not sorted, then the **right half** must be sorted.
    - Check whether the target lies within the right half.
      - If so, search right.
      - Otherwise, search left.
- Continue until the target is found or the search range becomes empty.

Since one half of the search space is discarded on every iteration, the algorithm runs in **O(log n)** time while using **O(1)** extra space.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target and target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1
```
