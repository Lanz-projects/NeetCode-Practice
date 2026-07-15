# Subsets II

## 🔍 Problem Summary

You are given an integer array that may contain duplicate values and must return all possible subsets of the array. The result must not contain duplicate subsets, and the subsets may be returned in any order.

The main challenge is handling duplicate numbers. Without special care, different recursive paths can generate identical subsets, resulting in duplicate entries in the output.

---

## 🧠 Key Insight

Sorting the array places duplicate values next to each other, making them easy to identify during the search. When deciding not to include a value, any consecutive duplicates can be skipped so that the same subset is not generated multiple times.

This allows backtracking to explore every unique subset exactly once.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Generate all possible subsets and store them in a set to remove duplicates afterward.
- While this works, it creates duplicate subsets unnecessarily and requires additional work and memory to filter them out.

### 2. Optimal Approach

- Sort the array so duplicate values appear consecutively.
- Use backtracking to make two decisions for each element: include it in the current subset or exclude it.
- If all elements have been processed, add a copy of the current subset to the result list.
- After exploring the branch that includes the current value, backtrack and explore the branch that excludes it.
- Before exploring the exclusion branch, skip over any consecutive duplicate values so they are not considered as separate starting points for identical subsets.
- Since every unique subset must be generated, the algorithm runs in **O(n × 2ⁿ)** time in the worst case, where `n` is the length of the array. The recursion stack requires **O(n)** space, excluding the space used for the output.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[:])
                return

            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res
```
