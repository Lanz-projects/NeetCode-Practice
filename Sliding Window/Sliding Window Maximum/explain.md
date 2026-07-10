# Sliding Window Maximum

## 🔍 Problem Summary

Given an array `nums` and an integer `k`, find the **maximum value** in every sliding window of size `k` as the window moves from left to right.

Return an array containing the maximum element for each window.

The challenge is efficiently finding each window's maximum without repeatedly scanning all `k` elements.

---

## 🧠 Key Insight

Maintain a **monotonic decreasing deque** that stores the indices of useful elements in the current window.

The deque is kept in decreasing order of values, so:

- The front of the deque always contains the index of the current window's maximum.
- Smaller elements behind a larger one are removed because they can never become the maximum while the larger element remains in the window.

This allows every element to be added and removed at most once.

---

## 🧩 Approaches Considered

### 1. Brute Force

- For every window of size `k`, scan all `k` elements to find the maximum.
- Repeat this for every possible window.
- Since each of the roughly `n` windows requires `O(k)` work, the total time complexity is **O(nk)**, which is too slow for large inputs.

### 2. Optimal Approach

- Use a deque to store **indices** rather than values.
- As the window expands:
  - Remove indices from the back whose values are smaller than the current value, since they can never become the maximum.
  - Add the current index to the back of the deque.
- Remove the front index if it has moved outside the current window.
- Once the window reaches size `k`:
  - The front of the deque is the maximum for that window.
  - Record the value and slide the window forward.

Since each index is inserted and removed from the deque at most once, the algorithm runs in **O(n)** time with **O(k)** extra space.

---

## 🧪 Final Code (Python)

```python
from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        output = []
        q = deque()
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1

            r += 1

        return output
```
