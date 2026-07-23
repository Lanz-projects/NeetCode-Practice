# Longest Common Subsequence

## 🔍 Problem Summary

Given two strings, find the length of their **longest common subsequence (LCS)**. A subsequence is formed by deleting characters without changing the order of the remaining characters.

The goal is to determine the maximum number of characters the two strings can share while preserving their relative order.

---

## 🧠 Key Insight

For every pair of positions `(i, j)`, if the characters match, they must be part of the LCS, so we add 1 and move diagonally. If they don't match, we try skipping a character from either string and take the better result.

This overlapping-subproblem structure makes **dynamic programming** the ideal solution.

---

## 🧩 Approaches Considered

### 1. Brute Force (Recursive)

- At each mismatch, recursively try skipping a character from either string.
- If characters match, include them in the subsequence.

**Why it's too slow:**

- Explores many of the same subproblems repeatedly.
- Time Complexity: **O(2^(m+n))**

### 2. Better Approach (Dynamic Programming)

- Create a 2D DP table where `dp[i][j]` stores the LCS length between `text1[i:]` and `text2[j:]`.
- Fill the table from the bottom-right toward the top-left.
- If characters match:
  - `dp[i][j] = 1 + dp[i + 1][j + 1]`
- Otherwise:
  - `dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])`

**Why it works:**

- Every state depends only on previously computed smaller subproblems.
- Each pair of indices is solved exactly once.

**Why it's better than brute force:**

- Time Complexity: **O(m × n)**
- Space Complexity: **O(m × n)**

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]
```
