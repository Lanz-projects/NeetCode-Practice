# Valid Palindrome

## 🔍 Problem Summary

Given a string return true if palindrome
else False

---

## 🧠 Key Insight

We need to check whether the cleaned version of the string reads the same forward and backward.
The fastest way to compare both ends simultaneously is a two‑pointer technique: one pointer at the start, one at the end, moving inward.

## This avoids building new strings or reversing anything.

## 🧩 Approaches Considered

### 1. Brute Force

- Clean the string by removing all non‑alphanumeric characters and converting everything to lowercase.
- Create a reversed version of this cleaned string and compare the two.
- **Why it’s not ideal:**
  - Requires extra space for the cleaned string and its reverse.
  - Does unnecessary work when we can compare characters directly using pointers.

---

### 2. Better Approach — Two Pointers

- Use two pointers: one starting at the beginning, one at the end.
- Move both inward while skipping non‑alphanumeric characters.
- Compare characters directly without building new strings.
- **Why it works:**
  - Palindromes rely on symmetry, so checking both ends simultaneously is the most direct method.
- **Why it’s better than brute force:**
  - O(1) extra space.
  - Only one pass through the string, making it efficient for large inputs

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        clean = []
        for char in s:
            if char.isalnum():
                clean.append(char.lower())
        clean = "".join(clean)

        start = 0
        end = len(clean) - 1
        while start <= end:
            if clean[start] != clean[end]:
                return False
            start += 1
            end -= 1
        return True
```
