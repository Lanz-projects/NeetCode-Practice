# House Robber II

## 🔍 Problem Summary

You are given an array `nums` where each element represents the amount of money in a house. Unlike the original problem, the houses are arranged in a circle, meaning the first and last houses are adjacent.

Your task is to determine the maximum amount of money that can be robbed without robbing two adjacent houses. The main challenge is handling the circular arrangement, since robbing the first house prevents robbing the last house.

---

## 🧠 Key Insight

Because the first and last houses cannot both be robbed, every valid solution falls into one of two cases: either the first house is excluded or the last house is excluded.

By solving the original House Robber problem on these two linear subarrays and taking the larger result, the circular constraint is eliminated.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Recursively explore every combination of robbing or skipping houses while checking that adjacent houses are never robbed.
- The circular dependency greatly increases the number of possibilities, making this approach exponential.

### 2. Optimal Approach

- Reuse the linear House Robber algorithm as a helper function.
- Compute the maximum profit in two separate scenarios:
  - Rob from the second house through the last house.
  - Rob from the first house through the second-to-last house.
- Also compare against the value of the first house to correctly handle the edge case where the input contains only one house.
- The helper function maintains two variables representing the best profits from the previous one and two houses, updating them as it scans through the array.
- The larger of the two linear solutions is the maximum amount that can be robbed from the circular arrangement.

The helper function runs in **O(n)** time, and it is called twice, so the overall time complexity remains **O(n)**. Since only a few variables are maintained during each traversal, the extra space complexity is **O(1)** (excluding the sliced arrays created by this implementation).

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2
```
