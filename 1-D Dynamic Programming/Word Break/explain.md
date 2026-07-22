# Word Break

## 🔍 Problem Summary

You are given a string `s` and a dictionary of valid words `wordDict`. Your task is to determine whether the entire string can be split into one or more dictionary words.

Words from the dictionary may be reused multiple times. The main challenge is deciding where to split the string without repeatedly checking the same suffixes.

---

## 🧠 Key Insight

Whether a position can successfully start a valid segmentation depends on whether any dictionary word matches at that position and whether the remaining suffix can also be segmented.

By working backward through the string, each position can be determined using results that have already been computed.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Recursively try every possible split of the string and check whether each piece exists in the dictionary.
- This repeatedly recomputes the same suffixes, leading to exponential running time.

### 2. Better Approach

- Create a dynamic programming array where `dp[i]` indicates whether the substring starting at index `i` can be segmented into dictionary words.
- Initialize the position after the last character as `True`, since an empty suffix is already successfully segmented.
- Traverse the string from right to left.
- For each position, check every word in the dictionary.
- If a word matches the substring starting at the current index and the remaining suffix is valid, mark the current position as `True`.
- Once a valid match is found, stop checking additional words for that position.
- The value at `dp[0]` indicates whether the entire string can be segmented.

For each position, every dictionary word may be checked, and comparing a word takes time proportional to its length. This results in a time complexity of **O(n × m × l)**, where `n` is the length of the string, `m` is the number of dictionary words, and `l` is the maximum word length. The dynamic programming array requires **O(n)** space.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i:i + len(w)] == w:
                    dp[i] = dp[i + len(w)]

                if dp[i]:
                    break

        return dp[0]
```
