# Distinct Subsequences

## 🔍 Problem Summary

You are given two strings, `s` and `t`. Your task is to determine how many distinct subsequences of `s` are exactly equal to `t`.

A subsequence is formed by deleting zero or more characters without changing the order of the remaining characters. The main challenge is that there are many different ways to choose which characters to keep, making a brute force search impractical.

---

## 🧠 Key Insight

At each character in `s`, there are only two possible choices: use it as part of the current match if it matches the next needed character in `t`, or skip it entirely.

Many of these decisions lead to the same remaining subproblem, so memoizing the result for each pair of indices allows us to solve every unique state only once.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Recursively try every possible subsequence of `s` and check whether it equals `t`.
- Since each character can either be included or skipped, the number of possible subsequences grows exponentially, making this approach too slow.

### 2. Better Approach

- Use a recursive DFS where `i` tracks the current position in `s` and `j` tracks the current position in `t`.
- If all characters in `t` have been matched, return `1` because a valid subsequence has been found.
- If `s` is exhausted before matching all of `t`, return `0`.
- When the current characters match, recursively consider both possibilities: use the character to match `t` or skip it and continue searching.
- If the characters do not match, simply skip the current character in `s`.
- Store each `(i, j)` result in a cache so repeated subproblems are solved only once. An additional early check returns `0` whenever there are not enough characters left in `s` to complete `t`.
- Since each pair of indices is computed at most once, the algorithm runs in **O(m × n)** time with **O(m × n)** space for the memoization cache, where `m` and `n` are the lengths of `s` and `t`.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dp = {}

        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            if len(s) - i < len(t) - j:
                return 0

            if s[i] == t[j]:
                dp[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                dp[(i, j)] = dfs(i + 1, j)

            return dp[(i, j)]

        return dfs(0, 0)
```
