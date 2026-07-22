# 3Sum

## 🔍 Problem Summary

We are given an integer array and must return **all unique triplets** `[nums[i], nums[j], nums[k]]` such that:

- `i`, `j`, and `k` are all different indices
- The sum of the three values is exactly `0`
- The output must not contain duplicate triplets, even if the array contains repeated numbers

The order of triplets and the order of elements inside each triplet does not matter.

---

## 🧠 Key Insight

The array can be sorted, and once sorted, each triplet can be found by:

1. Fixing one number (`nums[i]`)
2. Using a **two‑pointer technique** to find two other numbers that sum to `-nums[i]`

Sorting is the key that unlocks everything:

- It allows us to avoid duplicates cleanly
- It allows us to use the same two‑pointer strategy from Two Sum II
- It reduces the search space from O(n³) to O(n²)

This transforms the problem from “three nested loops” into “one loop + two pointers.”

---

---

## 🧩 Approaches Considered

### 1. Brute Force

- Use **three nested loops** to check every possible triplet `(i, j, k)`.
- For each combination, check whether `nums[i] + nums[j] + nums[k] == 0`.
- Store valid triplets in a set to avoid duplicates.
- **Why it’s not ideal:**
  - Time complexity is **O(n³)** — far too slow for large inputs.
  - Requires extra space to track duplicates.
  - Does not leverage any structure in the array.

### 2. Better Approach — Sorting + Two Pointers

- First, sort the array so that duplicates are adjacent and pointer movement becomes predictable.
- Iterate through the array, fixing one value `nums[i]` at a time. This value acts as the first element of the potential triplet.
- For each fixed `i`, use a two‑pointer search (`left` and `right`) to find two additional numbers that sum to `-nums[i]`.
- If the sum is too small, move the left pointer right to increase it.
- If the sum is too large, move the right pointer left to decrease it.
- When a valid triplet is found, add it to the result and skip over any duplicate values to avoid repeated triplets.
- **Why it works:**
  - Sorting allows us to efficiently skip duplicates and ensures pointer movement always moves toward or away from the target sum in a predictable way.
  - The two‑pointer technique reduces the inner search from O(n²) to O(n).
- **Why it’s better than brute force:**
  - Runs in **O(n²)** instead of O(n³).
  - Avoids duplicate triplets without needing extra data structures.
  - Clean, efficient, and leverages sorted order perfectly.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()

        for index, a in enumerate(nums):
            if index > 0 and nums[index] == nums[index - 1]:
              continue

            l, r = index + 1, len(nums) - 1
            while l < r:
                threeSum =  a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    result.append([a,nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return result
```
