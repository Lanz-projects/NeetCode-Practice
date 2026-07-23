# Burst Balloons

## 🔍 Problem Summary

You are given an array of balloons where each balloon has a value. Bursting a balloon earns coins equal to the product of its value and the values of its current left and right neighbors. If a balloon has no neighbor on one side, that side is treated as having a value of `1`.

The goal is to determine the maximum number of coins that can be collected by choosing the best order to burst all the balloons. The challenge is that every burst changes the neighboring balloons, so each decision affects future coin values.

---

## 🧠 Key Insight

Instead of deciding which balloon to burst first, think about which balloon is burst **last** within a given range.

If the last balloon to burst in an interval is known, then its neighbors are fixed because everything inside the interval has already been removed. This allows each interval to be solved independently, making dynamic programming with memoization an effective solution.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Try every possible order of bursting balloons and calculate the total coins earned.
- Since there are factorially many possible orders, this approach becomes far too slow even for moderately sized inputs.

### 2. Better Approach

- Add virtual balloons with value `1` to both ends of the array so edge cases are handled uniformly.
- Use a recursive DFS where `dfs(l, r)` returns the maximum coins obtainable by bursting all balloons between indices `l` and `r`.
- For every balloon in the current interval, assume it is the **last** balloon to burst. The coins earned are the product of the balloon and its fixed neighbors, plus the best results from the left and right subintervals.
- Compute this value for every possible last balloon and keep the maximum result.
- Store the answer for each interval in a 2D memoization table so each subproblem is solved only once.
- Since there are **O(n²)** intervals and each interval considers up to **O(n)** possible last balloons, the algorithm runs in **O(n³)** time with **O(n²)** space.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = [1] + nums + [1]
        n = len(nums)

        dp = [[0] * n for _ in range(n)]

        def dfs(l, r):
            if l > r:
                return 0
            if dp[l][r] != 0:
                return dp[l][r]

            best = 0
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                best = max(best, coins)

            dp[l][r] = best
            return best

        return dfs(1, n - 2)
```