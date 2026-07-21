# Maximum Product Subarray

## 🔍 Problem Summary

You are given an integer array `nums`. Your task is to find the contiguous subarray whose product is the largest and return that product.

The main challenge is handling negative numbers and zeros. A negative value can turn the smallest product into the largest when multiplied by another negative number, while a zero breaks any ongoing subarray product.

---

## 🧠 Key Insight

Unlike the maximum sum subarray problem, the maximum product depends on both the current maximum and the current minimum products.

A negative number can swap these roles, so tracking both values at every step ensures that every possible maximum product is considered.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Generate every possible contiguous subarray and calculate its product.
- Since there are **O(n²)** subarrays and computing each product can take additional time, this approach is too slow for larger inputs.

### 2. Optimal Approach

- Initialize the result as the largest individual element since the answer could be a single value.
- Maintain two running values:
  - `curMax` stores the largest product ending at the current position.
  - `curMin` stores the smallest product ending at the current position.
- When processing each number, compute the new maximum and minimum products because multiplying by a negative number can swap them.
- If a zero is encountered, reset both running products since no subarray can continue through a zero.
- After updating the running values, update the overall maximum product if a larger value is found.

Each element is processed exactly once, so the algorithm runs in **O(n)** time. Only a few variables are maintained throughout the traversal, giving an extra space complexity of **O(1)**.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = max(nums)

        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue

            temp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(temp, n * curMin, n)

            res = max(res, curMax)

        return res
```
