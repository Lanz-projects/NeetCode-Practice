# Partition Equal Subset Sum

## 🔍 Problem Summary

You are given an integer array `nums`. Your task is to determine whether the array can be divided into two subsets whose sums are exactly equal.

The main challenge is deciding which elements belong in each subset. Since the two subsets must have the same sum, the problem becomes finding whether any subset adds up to half of the total sum.

---

## 🧠 Key Insight

If the total sum of the array is odd, it is impossible to split it into two equal subsets.

Otherwise, the goal is to determine whether a subset with sum equal to half of the total exists. By keeping track of all reachable subset sums as each number is processed, we can efficiently determine whether the target sum can be formed.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Recursively try placing every number into one of two subsets and compare their sums at the end.
- Since every element has two choices, this approach explores exponentially many possibilities.

### 2. Better Approach

- First, compute the total sum of the array. If it is odd, immediately return `False`.
- Set the target sum to half of the total.
- Use a set to store every subset sum that can currently be formed, beginning with only `0`.
- Process the numbers from right to left.
- For every existing sum, create two possibilities:
  - Keep the current sum unchanged.
  - Add the current number to the sum.
- If the target sum is reached during this process, return `True` immediately.
- After processing all numbers, check whether the target sum exists in the set of reachable sums.

Each number is combined with every reachable sum up to the target, resulting in **O(n × target)** time in the worst case. The set of reachable sums can contain up to **O(target)** values, so the extra space complexity is **O(target)**.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()

            for t in dp:
                if t + nums[i] == target:
                    return True

                nextDP.add(t + nums[i])
                nextDP.add(t)

            dp = nextDP

        return True if target in dp else False
```
