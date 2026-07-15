# Combination Sum

## 🔍 Problem Summary

You are given an array of distinct integers and a target value. Your task is to return every unique combination of numbers that adds up to the target, where each candidate number may be used an unlimited number of times.

The main challenge is exploring all valid combinations without generating duplicates. Since numbers can be reused, the algorithm must carefully decide when to continue using the same candidate and when to move on to the next one.

---

## 🧠 Key Insight

At each candidate, there are two possible decisions: include it in the current combination or skip it and move to the next candidate. If a candidate is included, it remains available for future selections because it can be used multiple times.

Using backtracking allows every valid combination to be explored while pruning branches whose sums already exceed the target.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Generate every possible sequence of numbers and check whether its sum equals the target.
- This produces many unnecessary combinations and duplicate work, making it inefficient as the search space grows.

### 2. Optimal Approach

- Use depth-first search with backtracking to build one combination at a time.
- Keep track of the current candidate index, the current combination, and its running total.
- If the running total equals the target, add a copy of the current combination to the result.
- If the running total exceeds the target or all candidates have been considered, stop exploring that path.
- For each candidate, first choose to include it and recurse without advancing the index so it can be used again. After backtracking, recurse to the next candidate to explore combinations that do not include the current number.
- Backtracking ensures every valid combination is explored exactly once without duplicates. In the worst case, the search explores an exponential number of combinations, giving a time complexity of approximately **O(2ᵗ)**, where `t` is related to the target value, while the recursion stack and current combination require **O(t)** extra space.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur[:])
                return
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])

            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res
```
