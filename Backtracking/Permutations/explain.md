# Permutations

## 🔍 Problem Summary

You are given an array of distinct integers and must return every possible ordering of its elements. Each permutation should contain every number exactly once, and the results may be returned in any order.

The main challenge is generating every unique arrangement without missing any or producing duplicates. Since each position in a permutation can be filled by different elements, the number of possibilities grows rapidly.

---

## 🧠 Key Insight

A permutation can be built recursively by first generating all permutations of the remaining elements, then inserting the current element into every possible position within each smaller permutation.

By repeating this process until no elements remain, every possible ordering is generated exactly once.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Generate every possible ordering by trying all arrangements of the elements and filtering out duplicates if necessary.
- While correct, manually managing all possible swaps and ensuring uniqueness is more complicated than using a recursive construction.

### 2. Better Approach

- Recursively generate all permutations of the array excluding the first element.
- For each smaller permutation returned by the recursive call, insert the first element into every possible position.
- Add each newly formed permutation to the result list.
- Continue building upward until the original array has been reconstructed with all possible orderings.
- Since there are **n!** unique permutations and each one requires up to **O(n)** work to construct, the overall time complexity is **O(n × n!)**. The recursive call stack requires **O(n)** space, excluding the space needed to store the output.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]

        perms = self.permute(nums[1:])
        res = []

        for p in perms:
            for i in range(len(p) + 1):
                pCopy = p[:]
                pCopy.insert(i, nums[0])
                res.append(pCopy)

        return res
```
