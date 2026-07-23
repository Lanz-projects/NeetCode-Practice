# Target Sum

## 🔍 Problem Summary

Given an array of integers, assign either a `'+'` or `'-'` sign to every number so that the resulting expression evaluates to the given target.

Return the total number of different sign assignments that produce the target sum.

---

## 🧠 Key Insight

Instead of tracking individual expressions, keep track of **how many ways** each possible running sum can be reached after processing each number.

This dynamic programming approach efficiently combines identical states instead of recomputing them.

---

## 🧩 Approaches Considered

### 1. Brute Force (Recursive)

- For each number, recursively choose either `+` or `-`.
- Count every expression whose final sum equals the target.

**Why it's too slow:**

- Explores every possible sign assignment.
- Time Complexity: **O(2ⁿ)**

### 2. Better Approach (Dynamic Programming with Hash Map)

- Let the hash map store:
  - **key:** current sum
  - **value:** number of ways to reach that sum.
- Start with one way to reach sum `0`.
- For each number:
  - Create a new map.
  - For every existing sum:
    - Add the current number.
    - Subtract the current number.
    - Accumulate the number of ways for both new sums.
- The answer is the number of ways to reach the target after processing every number.

**Why it works:**

- Different expressions can produce the same intermediate sum.
- By grouping these together, each state is computed only once per iteration.

**Why it's better than brute force:**

- Time Complexity: **O(n × S)**, where `S` is the range of reachable sums.
- Space Complexity: **O(S)**

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = defaultdict(int)
        dp[0] = 1

        for i in range(len(nums)):
            next_dp = defaultdict(int)
            for cur_sum, count in dp.items():
                next_dp[cur_sum + nums[i]] += count
                next_dp[cur_sum - nums[i]] += count
            dp = next_dp

        return dp[target]
```
