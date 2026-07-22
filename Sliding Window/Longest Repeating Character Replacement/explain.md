# 424. Longest Repeating Character Replacement

## 🔍 Problem Summary

You are given a string `s` consisting of uppercase English letters and an integer `k`.

You may replace **at most `k` characters** in the string with any other uppercase letter.

Return the length of the **longest substring** that can be made up of the same character after performing at most `k` replacements.

The challenge is determining whether a substring can be converted into a single repeated character without trying every possible replacement.

---

## 🧠 Key Insight

For any substring, only the characters that **aren't the most frequent character** need to be replaced.

If:

```
window_size - (frequency of the most common character) <= k
```

then the current window is valid because we can replace all of the other characters.

This allows us to use a **sliding window**, expanding when the window is valid and shrinking when it is not.

---

## 🧩 Approaches Considered

### 1. Brute Force

- Generate every possible substring.
- Count the frequency of every character in each substring.
- Check whether the substring can be made into a single repeated character using at most `k` replacements.
- Since there are **O(n²)** substrings and counting frequencies takes additional work, this approach is too slow.

### 2. Better Approach (O(26n))

- Use a sliding window with two pointers.
- Maintain a frequency map of the characters currently inside the window.
- At every step:
  - Expand the window by adding the next character.
  - Compute the highest character frequency using `max(count.values())`.
  - If the number of characters that would need replacing exceeds `k`, shrink the window from the left.
- Since there are only **26 uppercase English letters**, computing `max(count.values())` is effectively constant time.
- This results in a practical time complexity of **O(26n)**, which simplifies the implementation while remaining very efficient.

---

## ⚡ Even Better Optimization (O(n))

The previous solution recomputes:

```python
max(count.values())
```

every time the window changes.

Although this only scans **26 letters**, we can avoid even that by maintaining a variable `maxf` that stores the largest frequency ever seen in the current window.

As the window expands:

- Update `maxf = max(maxf, count[s[r]])`.
- Never decrease `maxf` when shrinking the window.
- Even if `maxf` becomes slightly outdated, the algorithm remains correct because an overestimated maximum frequency can only delay shrinking the window—it never causes us to miss the correct answer.

This improves the theoretical runtime from **O(26n)** to **O(n)**, though the practical difference is very small. The **O(26n)** version is often easier to understand and remember.

---

## 🧪 Final Code (Python)

This is the **O(26n)** solution (recommended for clarity).

```python
from collections import defaultdict

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = defaultdict(int)
        res = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] += 1

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
```

This is the **O(n)** optimization.

```python
from collections import defaultdict

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = defaultdict(int)
        res = 0
        l = 0
        maxf = 0

        for r in range(len(s)):
            count[s[r]] += 1
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
```

- Why it works
- Why it’s better than brute force

---

## 🧪 Final Code (Python)

This is the O(26n) solution (main)

```python
from collections import defaultdict
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        count = defaultdict(int)
        res = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] += 1

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

```

This is the O(n) solution

```python
from collections import defaultdict
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        count = defaultdict(int)
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] += 1
            maxf = max(maxf, count[s[r]])
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

```
