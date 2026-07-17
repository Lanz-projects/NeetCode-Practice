# Jump Game II

## 🔍 Problem Summary

You are given an array where each element represents the maximum distance you can jump forward from that index. Starting at the first index, determine the minimum number of jumps required to reach the last index.

It is guaranteed that the last index is always reachable. The main challenge is finding the fewest jumps without exploring every possible path.

---

## 🧠 Key Insight

Treat each jump as expanding a range of indices that can currently be reached.

Within the current reachable range, determine the farthest position that can be reached with one additional jump. Once every index in the current range has been considered, make a jump and repeat the process using the newly expanded range.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Try every possible jump from each position using recursion or backtracking.
- Keep track of the minimum number of jumps needed to reach the last index.
- This explores many redundant paths and has exponential time complexity, making it impractical for large inputs.

### 2. Optimal Approach

- Maintain two pointers, `l` and `r`, representing the current range of indices reachable with the current number of jumps.
- For every index in this range, compute the farthest position that can be reached with one more jump.
- After scanning the entire range, update the range to begin just after the current one and end at the farthest reachable index.
- Increment the jump count each time the range expands.
- Continue until the current range reaches or passes the last index.

This greedy, level-by-level approach is similar to performing a breadth-first search on the array without explicitly building a graph. Every index is processed at most once, so the algorithm runs in **O(n)** time and uses **O(1)** additional space.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0

            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])

            l = r + 1
            r = farthest
            res += 1

        return res
```
