# Merge Triplets to Form Target Triplet

## 🔍 Problem Summary

You are given a list of triplets and a target triplet. You may repeatedly merge two triplets by taking the maximum value at each position, and your goal is to determine whether the target triplet can be formed.

The main challenge is identifying which triplets can safely contribute to the target without introducing values that exceed the target in any position.

---

## 🧠 Key Insight

Any triplet that has a value larger than the target in any position can never be part of a valid solution.

Among the remaining valid triplets, all that matters is whether each position of the target can be matched by at least one triplet. If all three positions can be supplied independently, repeatedly taking coordinate-wise maximums will produce the target triplet.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Try every possible sequence of merge operations between triplets.
- Check whether any sequence eventually produces the target triplet.
- This explores far too many combinations of merges and is computationally infeasible.

### 2. Optimal Approach

- Iterate through every triplet.
- Ignore any triplet whose value exceeds the target in any position since it can never contribute to a valid answer.
- For each remaining triplet, compare its values with the corresponding values in the target.
- Whenever a value matches the target at a particular index, record that index in a set.
- After processing all triplets, return `True` if all three indices have been matched; otherwise, return `False`.

Each valid triplet can only increase values up to the target, so combining all matching coordinates is sufficient to determine whether the target can be formed. The algorithm scans the input once, running in **O(n)** time and using **O(1)** additional space since the set stores at most three indices.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        good = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)

        return len(good) == 3
```
