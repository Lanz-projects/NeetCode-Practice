# House Robber

## 🔍 Problem Summary

You are given an array `nums` where each element represents the amount of money stored in a house along a street. You may rob any number of houses, but you cannot rob two adjacent houses because doing so triggers the alarm.

Your task is to determine the maximum amount of money that can be stolen without robbing neighboring houses. The main challenge is deciding at each house whether robbing it leads to a better overall profit than skipping it.

---

## 🧠 Key Insight

For every house, there are only two choices: rob it or skip it.

If you rob the current house, you must add its value to the best profit from two houses back. If you skip it, you keep the best profit from the previous house. The better of these two choices becomes the optimal result for the current position.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Recursively explore both choices at every house: rob it or skip it.
- This repeatedly solves the same subproblems, resulting in exponential running time.

### 2. Optimal Approach

- Maintain two variables:
  - `rob1` stores the maximum profit up to two houses back.
  - `rob2` stores the maximum profit up to the previous house.
- Iterate through the houses one by one.
- For each house, compute the better of:
  - Robbing the current house (`current value + rob1`)
  - Skipping the current house (`rob2`)
- Update the two variables to reflect the best results for the next iteration.
- After processing every house, `rob2` contains the maximum amount that can be robbed.

Each house is processed exactly once, so the algorithm runs in **O(n)** time. Since only two variables are maintained throughout the traversal, the extra space complexity is **O(1)**.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2
```