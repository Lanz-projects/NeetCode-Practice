# Minimum Window Substring

## 🔍 Problem Summary

Given two strings `s` and `t`, find the **smallest substring of `s`** that contains **every character from `t`**, including duplicate characters.

If no such substring exists, return an empty string (`""`).

The challenge is finding the minimum valid window efficiently without checking every possible substring.

---

## 🧠 Key Insight

Use a **sliding window** to expand until all required characters are included, then shrink the window as much as possible while it remains valid.

To determine whether the current window is valid:

- Keep a frequency map of the characters required from `t`.
- Keep another frequency map for the current window.
- Track:
  - `need` = number of unique characters required.
  - `have` = number of unique characters whose required frequencies have been satisfied.

Once `have == need`, the window contains every required character, so we try to minimize it.

---

## 🧩 Approaches Considered

### 1. Brute Force

- Generate every possible substring of `s`.
- Count the characters in each substring.
- Check whether it contains every character from `t` with the required frequencies.
- Keep the smallest valid substring found.
- Since there are **O(n²)** substrings and validating each one requires additional work, this approach is far too slow.

### 2. Better Approach

- Build a frequency map for the characters in `t`.
- Use two pointers to maintain a sliding window over `s`.
- Expand the window by moving the right pointer:
  - Update the window's character counts.
  - If a required character reaches its needed frequency, increment `have`.
- Once all required characters are present (`have == need`):
  - Update the smallest valid window if the current one is shorter.
  - Shrink the window from the left while it remains valid.
  - If removing a character causes the window to no longer satisfy the required frequency, decrement `have`.
- Continue until the entire string has been processed.

Each character enters and leaves the window at most once, resulting in **O(m + n)** time complexity, where `m` and `n` are the lengths of `s` and `t`.

---

## 🧪 Final Code (Python)

```python
from collections import defaultdict
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if t == "":
            return ""

        countT, window = defaultdict(int), defaultdict(int)
        for c in t:
            countT[c] += 1

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] += 1

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
```
