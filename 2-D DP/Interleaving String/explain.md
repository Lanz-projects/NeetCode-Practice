# Interleaving String

## 🔍 Problem Summary

You are given three strings: `s1`, `s2`, and `s3`. Your task is to determine whether `s3` can be formed by interleaving the characters of `s1` and `s2` while preserving the original order of characters from each string.

The main challenge is deciding, at each position in `s3`, whether the next character should come from `s1` or `s2`. Since multiple valid choices may exist along the way, a simple greedy approach is not sufficient.

---

## 🧠 Key Insight

Instead of trying every possible interleaving independently, we can use dynamic programming to remember which combinations of positions in `s1` and `s2` can successfully form the remaining portion of `s3`.

If we know whether the suffix starting at a pair of indices `(i, j)` can build the remaining characters of `s3`, we can use that information to determine whether earlier positions are also valid. By building these answers from the end of the strings toward the beginning, every subproblem is solved only once.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Try every possible way of choosing the next character from either `s1` or `s2`.
- Continue recursively until all characters have been used or a mismatch is found.
- Since many of the same subproblems are explored repeatedly, this approach has exponential time complexity and quickly becomes too slow for larger inputs.

### 2. Better Approach

- First, check whether the combined lengths of `s1` and `s2` match the length of `s3`. If they do not, an interleaving is impossible.
- Create a 2D dynamic programming table where `dp[i][j]` represents whether the suffixes `s1[i:]` and `s2[j:]` can form the suffix `s3[i + j:]`.
- Initialize the bottom-right cell as `True` because two empty strings can always form an empty string.
- Iterate backward through both strings. At each position, check whether the next character in `s1` matches the corresponding character in `s3` and whether the remaining suffix is valid. Do the same for `s2`.
- If either choice leads to a valid state, mark the current cell as `True`.
- The final answer is stored in `dp[0][0]`. This fills each state exactly once, giving a time complexity of **O(m × n)** and a space complexity of **O(m × n)**, where `m` and `n` are the lengths of `s1` and `s2`.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = [[False for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True

        return dp[0][0]
```