# Longest Substring Without Repeating Characters

## 🔍 Problem Summary

Given a string `s`, find the length of the **longest substring** that contains no repeated characters.

A **substring** consists of consecutive characters, so characters cannot be skipped.

The challenge is to efficiently find the longest valid substring without checking every possible substring.

---

## 🧠 Key Insight

Use a **sliding window** to represent the current substring without duplicate characters.

As you expand the window to the right, if a duplicate character is encountered, shrink the window from the left until the duplicate is removed.

This ensures the window always contains unique characters while allowing us to find the longest valid substring in a single pass.

---

## 🧩 Approaches Considered

### 1. Brute Force

- Generate every possible substring.
- Check whether each substring contains duplicate characters.
- Keep track of the longest valid substring found.
- Since there are **O(n²)** substrings and checking each one can take **O(n)** time, the overall complexity is **O(n³)**.

### 2. Optimal Approach

- Maintain a sliding window using two pointers:
  - `l` marks the beginning of the current substring.
  - `r` expands the substring one character at a time.
- Use a set to store the characters currently inside the window.
- If adding a new character creates a duplicate:
  - Remove characters from the left side of the window until the duplicate is gone.
- After each expansion, update the maximum window size.

Each character is added to and removed from the set at most once, resulting in an efficient **O(n)** time complexity with **O(min(n, k))** space, where `k` is the size of the character set.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            charSet.add(s[r])
            res = max(res, r - l + 1)

        return res
```