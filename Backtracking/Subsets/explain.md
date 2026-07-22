# Subsets

## 🔍 Problem Summary

You are given an array of unique integers and must return every possible subset of its elements, also known as the power set. The subsets can be returned in any order, but there must not be any duplicates.

The main challenge is systematically exploring every possible combination of elements. Since each element can either be included or excluded, every decision affects the subsets that can be formed.

---

## 🧠 Key Insight

For every element, there are exactly two choices: include it in the current subset or leave it out. By recursively making both decisions for every element, every possible subset is generated exactly once.

This naturally forms a decision tree where each path represents one unique subset.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Generate every possible combination of elements by checking all inclusion and exclusion possibilities.
- While this idea is correct, implementing it manually can become complicated. Backtracking provides a cleaner and more structured way to explore the same decision tree.

### 2. Better Approach

- Use depth-first search with backtracking to build one subset at a time.
- Starting from the first element, make two recursive calls: one that includes the current element and one that excludes it.
- When all elements have been considered, append a copy of the current subset to the result list.
- After exploring the branch where an element is included, remove it before exploring the branch where it is excluded.
- Since every element has two possible choices, the algorithm generates **2ⁿ** subsets. Copying each subset contributes to the overall work, resulting in a time complexity of **O(n × 2ⁿ)**. The recursion stack and current subset require **O(n)** extra space, excluding the space used for the output.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset[:])
                return

            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res
```
