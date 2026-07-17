# Jump Game

## 🔍 Problem Summary

You are given an array where each element represents the maximum number of steps you can jump forward from that index. Starting at the first index, determine whether it is possible to reach the last index.

The main challenge is deciding whether the available jumps are sufficient to bypass obstacles, such as positions with a jump length of `0`, without trying every possible path.

---

## 🧠 Key Insight

Instead of thinking about how to move forward, work backward from the last index.

Maintain the leftmost position that can reach the goal. If the current index can jump to or beyond that position, it becomes the new goal. If you can eventually move the goal all the way back to index `0`, then reaching the end is possible.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Try every possible jump from each position using recursion or backtracking.
- Return `True` if any path reaches the last index.
- This explores many duplicate paths and becomes exponential in the worst case, making it too slow for large inputs.

### 2. Optimal Approach

- Initialize the goal as the last index.
- Traverse the array from right to left.
- For each index, check whether the maximum jump from that position reaches or passes the current goal.
- If it does, update the goal to the current index.
- After processing the entire array, return `True` if the goal has moved back to index `0`; otherwise, return `False`.

This greedy strategy works because every time an index can reach the current goal, it becomes the new earliest position needed to reach the end. The algorithm processes the array only once, running in **O(n)** time and using **O(1)** additional space.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return True if goal == 0 else False
```
