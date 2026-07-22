# Combination Sum II

## 🔍 Problem Summary

You are given an array of candidate numbers, which may contain duplicates, and a target value. Return all unique combinations whose values sum to the target, where each candidate may be used at most once.

The main challenge is generating every valid combination while avoiding duplicates. Since the input can contain repeated numbers, the algorithm must ensure that identical combinations are not added to the result.

---

## 🧠 Key Insight

Sorting the candidates places duplicate values next to each other, making them easy to skip during the search. Backtracking then explores every valid combination while ensuring each number is used at most once.

After deciding not to use a candidate, any consecutive duplicates are skipped so that the same combination is not generated multiple times.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Generate every possible subset of the candidates and check whether its sum equals the target.
- Since duplicate values can produce identical combinations, additional work is needed to remove duplicates after the search, making this approach inefficient.

### 2. Better Approach

- Sort the candidate array so duplicate values are adjacent.
- Use depth-first search with backtracking to build one combination at a time.
- Keep track of the current index, the current combination, and its running total.
- If the running total equals the target, add a copy of the current combination to the result.
- If the running total exceeds the target or all candidates have been considered, stop exploring that path.
- First, include the current candidate and recurse to the next index since each number may only be used once. After backtracking, skip any consecutive duplicate values before exploring the branch that excludes the current candidate.
- Sorting combined with skipping duplicates ensures that each unique combination is generated exactly once. In the worst case, the search explores an exponential number of subsets, giving a time complexity of **O(2ⁿ)** after the initial **O(n log n)** sort, while the recursion stack and current combination require **O(n)** extra space.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()

        def dfs(i, cur, total):
            if target == total:
                res.append(cur[:])
                return
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            cur.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res
```
