# Edit Distance

## 🔍 Problem Summary

You are given two strings, `word1` and `word2`. Your task is to determine the minimum number of operations needed to transform `word1` into `word2`.

The allowed operations are inserting a character, deleting a character, or replacing a character. The main challenge is finding the optimal sequence of operations without repeatedly solving the same subproblems.

---

## 🧠 Key Insight

The minimum number of operations for any pair of positions in the two strings depends only on the answers for the remaining suffixes.

By using dynamic programming, we can compute the minimum edits needed for every pair of indices starting from the ends of the strings and build up to the final answer without redundant calculations.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Recursively try every possible insert, delete, and replace operation until the strings match.
- Since each mismatch branches into multiple possibilities, many identical subproblems are recomputed, leading to exponential time complexity.

### 2. Better Approach

- Create a 2D dynamic programming table where `cache[i][j]` represents the minimum number of operations required to convert `word1[i:]` into `word2[j:]`.
- Initialize the last row and last column to handle cases where one string has already been exhausted. The remaining operations are simply inserting or deleting all remaining characters.
- Iterate backward through both strings.
- If the current characters already match, no operation is needed, so copy the value from the diagonal cell.
- Otherwise, consider the three allowed operations: delete a character, insert a character, or replace a character. Take the minimum of these three choices and add one for the current operation.
- After filling the table, the answer is stored in `cache[0][0]`. Since every state is computed once, the algorithm runs in **O(m × n)** time with **O(m × n)** space, where `m` and `n` are the lengths of the two strings.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        cache = [[float('inf') for j in range(len(word2) + 1)]
                 for i in range(len(word1) + 1)]

        for j in range(len(word2) + 1):
            cache[len(word1)][j] = len(word2) - j

        for i in range(len(word1) + 1):
            cache[i][len(word2)] = len(word1) - i

        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i + 1][j + 1]
                else:
                    cache[i][j] = 1 + min(
                        cache[i + 1][j],
                        cache[i][j + 1],
                        cache[i + 1][j + 1]
                    )

        return cache[0][0]
```
