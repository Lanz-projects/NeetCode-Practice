# Longest Increasing Subsequence

## 🔍 Problem Summary

You are given an integer array `nums`. Your task is to find the length of the longest subsequence whose elements are in strictly increasing order.

Unlike a subarray, a subsequence does not need to consist of consecutive elements. The main challenge is deciding which elements to include while preserving their original order.

---

## 🧠 Key Insight

The longest increasing subsequence starting at a given index depends on the longest increasing subsequences that begin at later indices.

By working backward through the array, each position can determine its best subsequence length by looking at all larger values that come after it.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Recursively explore every possible subsequence and keep track of the longest increasing one.
- Since every element can either be included or excluded, this approach has exponential running time.

### 2. Better Approach

- Create a dynamic programming array `LIS` where `LIS[i]` stores the length of the longest increasing subsequence starting at index `i`.
- Initialize every position to `1` because every element can always form a subsequence by itself.
- Traverse the array from right to left.
- For each element, check every element that comes after it.
- If a later element is larger than the current one, update the current value using `1 + LIS[j]`.
- After filling the DP array, the largest value represents the length of the overall longest increasing subsequence.

The outer loop processes every element, and the inner loop compares it with every later element, resulting in **O(n²)** time. The dynamic programming array stores one value for each element, so the extra space complexity is **O(n)**.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return max(LIS)
```
