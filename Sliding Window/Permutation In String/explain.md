# Permutation In String

## 🔍 Problem Summary

Given two strings `s1` and `s2`, determine whether **any permutation** of `s1` appears as a **substring** of `s2`.

A permutation contains the same characters as `s1`, just possibly in a different order.

Return `True` if such a substring exists; otherwise return `False`.

The challenge is efficiently checking every possible substring of `s2` without generating all permutations of `s1`.

---

## 🧠 Key Insight

A permutation of `s1` must:

- Have the **same length** as `s1`.
- Contain **exactly the same character frequencies**.

Instead of generating permutations, we slide a window of length `len(s1)` across `s2` and compare the character counts of the current window with those of `s1`.

If the frequency maps match, we've found a valid permutation.

---

## 🧩 Approaches Considered

### 1. Brute Force

- Generate every permutation of `s1`.
- Check whether each permutation appears as a substring of `s2`.
- Since `s1` has up to `n!` permutations, this approach becomes infeasible even for moderately sized strings.

### 2. Better Approach

- Build a frequency map for the characters in `s1`.
- Use a sliding window of length `len(s1)` over `s2`.
- As the window moves:
  - Add the new character entering the window.
  - Remove the character leaving the window.
  - Delete characters whose counts become zero to keep the maps comparable.
- After each shift, compare the two frequency maps.
- If they are equal, the current window is a permutation of `s1`, so return `True`.
- If no matching window is found, return `False`.

Since the alphabet consists of lowercase English letters, comparing the frequency maps is effectively constant time, giving an overall complexity of **O(n)**.

---

## 🧪 Final Code (Python)

```python
from collections import defaultdict

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False

        s1Count = defaultdict(int)
        window = defaultdict(int)

        for char in s1:
            s1Count[char] += 1

        l = 0

        for r in range(len(s2)):
            window[s2[r]] += 1

            if r - l + 1 > len(s1):
                window[s2[l]] -= 1
                if window[s2[l]] == 0:
                    del window[s2[l]]
                l += 1

            if window == s1Count:
                return True

        return False
```
