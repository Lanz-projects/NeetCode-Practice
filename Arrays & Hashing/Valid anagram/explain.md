# Problem Title

## 🔍 Problem Summary

-Given two strings

- Check if s1 and s2 are anagrams
- If so, return True
- Else False

---

## 🧠 Key Insight

Since anagrams are the same length, and same freq of letters
we can create a counter to compare them.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Check the length
- Then check every character in s1 and try to find a match unused character in s2
- Time: O(n^2)
- Space: O(n)

### 2. Optimal Approach

- Check the length
- Use a counter (defaultdict), to keep track of freq of characters
- Iterate through each string, and increase the counter where the key is the character, and the value is the frequency.
- Return whether counter1 == counter 2
- Time complexity: O(n)
- Space: O(n)

---

## 🧪 Final Code (Python)

```python
from collections import defaultdict
class Solution(object):
    def isAnagram(self, s, t):
      if len(s) != len(t):
        return False

      counter1 = defaultdict(int)
      counter2 = defaultdict(int)

      for i in s:
        counter1[i] += 1
      for i in t:
        counter1[t] += 1

      return counter1 == counter2
```
