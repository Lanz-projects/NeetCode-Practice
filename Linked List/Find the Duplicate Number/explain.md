# Find the Duplicate Number

## 🔍 Problem Summary

You are given an array `nums` containing `n + 1` integers, where every integer is in the range `[1, n]`.

Exactly **one number is duplicated**, although it may appear more than twice.

Return the duplicated number **without modifying the array** and using only **constant extra space**.

The challenge is finding the duplicate while satisfying these strict constraints.

---

## 🧠 Key Insight

Treat the array like a **linked list**.

- Each index is a node.
- The value at each index points to the next node.

Since there are `n + 1` positions but only `n` possible values, the duplicate creates a **cycle** in this linked list.

Finding the duplicate becomes equivalent to finding the **entrance of the cycle**, which can be done using **Floyd's Cycle Detection Algorithm (Tortoise and Hare)**.

---

## 🧩 Approaches Considered

### 1. Brute Force

- Compare every pair of numbers to find the duplicate.
- Return the first repeated value.
- This requires **O(n²)** time and is too slow.

Other straightforward approaches, such as using a hash set or sorting the array, violate the problem constraints because they either use extra space or modify the input array.

### 2. Better Approach

- Treat the array as a linked list:
  - From index `i`, move to index `nums[i]`.
- Use two pointers:
  - `slow` moves one step at a time.
  - `fast` moves two steps at a time.
- The two pointers will eventually meet inside the cycle.
- Initialize a second slow pointer at the beginning of the array.
- Move both slow pointers one step at a time until they meet.
- Their meeting point is the **duplicate number**, which corresponds to the entrance of the cycle.

This algorithm runs in **O(n)** time while using only **O(1)** extra space and does not modify the input array.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow
```
