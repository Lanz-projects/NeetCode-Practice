# Group Anagram

## 🔍 Problem Summary

- Given an array of strings
- Group and return the anagrams in any order

---

## 🧠 Key Insight

Anagrams share the same canonical form.
If we convert each word into a signature that uniquely identifies its character composition (such as sorting the characters), then all anagrams will map to the same key.
A hashmap lets us group words by this signature in linear time.

---

## 🧩 Approaches Considered

### 1. Brute Force

- For each word, compare it with every other word to check if they are anagrams.
- Requires sorting or counting for each comparison → repeated work.
- **Time:** O(n² · k log k) (n = number of words, k = length of each word)
- **Why it’s not ideal:** You repeatedly compare words instead of grouping them efficiently.

---

### 2. Optimal Approach (Hashmap + Signature)

- Compute a signature for each word (e.g., sorted characters or a character count).
- Use a hashmap where the key is the signature and the value is the list of words.
- All anagrams map to the same key.
- **Time:** O(n · k log k) using sorted signature
- **Why it’s better:** No pairwise comparisons; grouping happens in a single pass.

---

## 🧪 Final Code (Python)

```python
from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
      groups = defaultdict(list)

      for word in strs:
        key = tuple(sorted(word))
        groups[key].append(word)

      return list(groups.values())

```
