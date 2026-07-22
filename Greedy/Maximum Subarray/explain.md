# Maximum Subarray

## 🔍 Problem Summary

Given an integer array `nums`, find the contiguous subarray with the largest possible sum and return that sum.

The subarray must consist of consecutive elements. The main challenge is finding the maximum sum without checking every possible subarray, which would be too slow for large inputs.

---

## 🧠 Key Insight

A negative running sum can never improve the sum of a future subarray.

As you scan through the array, keep a running sum of the current subarray. If that sum becomes negative, discard it and start a new subarray at the next element. This ensures every new subarray begins with the best possible starting point.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Generate every possible contiguous subarray and compute its sum.
- Keep track of the largest sum encountered.
- This approach examines **O(n²)** subarrays (or **O(n³)** if each sum is recomputed), making it too slow for large inputs.

### 2. Better Approach

- Maintain two variables:
  - `curSum`, representing the sum of the current subarray.
  - `maxSum`, storing the largest subarray sum found so far.
- Iterate through each number in the array.
- If the current running sum becomes negative, reset it to `0` since carrying a negative sum would only decrease future subarray sums.
- Add the current number to the running sum.
- Update the maximum sum whenever a larger subarray sum is found.
- Continue until every element has been processed.

This greedy strategy, commonly known as **Kadane's Algorithm**, guarantees that every element is processed only once. The algorithm runs in **O(n)** time and uses **O(1)** additional space.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSum = max(maxSum, curSum)

        return maxSum
```
