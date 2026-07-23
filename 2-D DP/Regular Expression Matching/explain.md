# Regular Expression Matching

## 🔍 Problem Summary

You are given an input string `s` and a pattern `p`. The pattern may contain normal characters, `.` which matches any single character, and `*` which matches zero or more occurrences of the character immediately before it.

Your task is to determine whether the entire string matches the pattern. The main challenge is correctly handling `*`, since it can either skip the preceding character entirely or match it multiple times.

---

## 🧠 Key Insight

The result depends only on the current positions in the string and the pattern. By treating each pair of indices as a subproblem, we can recursively determine whether the remaining portions match.

Since the same `(string index, pattern index)` combinations are encountered repeatedly, memoizing each result avoids redundant work and makes the recursive solution efficient.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Recursively try every possible interpretation of each `*`, deciding whether to use it zero times, one time, or multiple times.
- Because many of the same states are revisited, this approach has exponential time complexity and quickly becomes too slow.

### 2. Better Approach

- Use a recursive DFS where `(i, j)` represents whether `s[i:]` matches `p[j:]`.
- If both the string and pattern have been completely processed, return `True`. If only the pattern is exhausted, return `False`.
- Check whether the current characters match, accounting for the `.` wildcard.
- If the next pattern character is `*`, consider two possibilities: skip the `character*` pair entirely or, if the current characters match, consume one character from the string while keeping the pattern at the same position.
- If there is no `*`, simply advance both indices when the current characters match.
- Store the result for every `(i, j)` in a cache so each state is computed only once. Since there are at most **O(m × n)** unique states, the algorithm runs in **O(m × n)** time with **O(m × n)** space for the memoization cache, where `m` and `n` are the lengths of the string and pattern.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        cache = {}

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]

            if i >= len(s) and j >= len(p):
                return True

            if j >= len(p):
                return False

            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            if (j + 1) < len(p) and p[j + 1] == "*":
                cache[(i, j)] = (
                    dfs(i, j + 2) or
                    (match and dfs(i + 1, j))
                )
                return cache[(i, j)]

            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]

            cache[(i, j)] = False
            return False

        return dfs(0, 0)
```