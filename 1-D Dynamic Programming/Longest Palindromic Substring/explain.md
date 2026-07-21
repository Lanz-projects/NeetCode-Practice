# Longest Palindromic Substring

## 🔍 Problem Summary

You are given a string `s`. Your task is to find and return the longest substring that reads the same forwards and backwards.

A palindrome must consist of consecutive characters, so the main challenge is efficiently checking every possible palindrome without testing every substring.

---

## 🧠 Key Insight

Every palindrome has a center. Odd-length palindromes have a single character as their center, while even-length palindromes have two adjacent characters as their center.

By expanding outward from every possible center until the characters no longer match, we can find the longest palindrome without generating every substring.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Generate every possible substring and check whether each one is a palindrome.
- Since there are **O(n²)** substrings and checking each can take **O(n)** time, this approach runs in **O(n³)** time and is too slow for larger inputs.

### 2. Optimal Approach

- Treat every index as the center of an odd-length palindrome and every pair of adjacent indices as the center of an even-length palindrome.
- Expand outward while the left and right characters match.
- Whenever a longer palindrome is found, update the current best substring and its length.
- Repeat this process for every possible center and return the longest palindrome discovered.

There are **2n - 1** possible centers, and each expansion can take up to **O(n)** time in the worst case, giving an overall time complexity of **O(n²)**. Only a few variables are used during the search, so the extra space complexity is **O(1)**.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        resLen = 0

        for i in range(len(s)):
          # odd length
          l, r = i, i
          while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
              res = s[l:r+1]
              resLen = (r - l + 1)
            l -= 1
            r += 1

          # even length
          l, r = i, i + 1
          while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
              res = s[l:r +1]
              resLen = (r - l + 1)
            l -= 1
            r += 1
        return res
```
