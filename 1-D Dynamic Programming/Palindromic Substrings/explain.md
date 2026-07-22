# Palindromic Substrings

## 🔍 Problem Summary

You are given a string `s`. Your task is to count how many substrings of `s` are palindromes.

A palindrome is a string that reads the same forwards and backwards, and a substring must consist of consecutive characters. The main challenge is counting every palindromic substring efficiently without generating every possible substring.

---

## 🧠 Key Insight

Every palindrome has a center. Odd-length palindromes have one center character, while even-length palindromes have a center between two characters.

By expanding outward from each possible center, every palindromic substring is discovered exactly once, allowing us to count them efficiently.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Generate every possible substring and check whether each one is a palindrome.
- Since there are **O(n²)** substrings and each palindrome check can take **O(n)** time, this approach runs in **O(n³)** time.

### 2. Better Approach

- Iterate through every index in the string.
- Treat each index as the center of an odd-length palindrome and each adjacent pair as the center of an even-length palindrome.
- Use a helper function to expand outward while the characters on both sides match.
- Every successful expansion represents a unique palindromic substring, so increment the count.
- Sum the counts from all odd and even centers to obtain the final answer.

There are **2n - 1** possible centers, and each expansion can take up to **O(n)** time in the worst case, resulting in an overall time complexity of **O(n²)**. Since only a few variables are used during the expansion, the extra space complexity is **O(1)**.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0

        for i in range(len(s)):
            res += self.countPali(s, i, i)
            res += self.countPali(s, i, i + 1)

        return res

    def countPali(self, s, l, r):
        res = 0

        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1

        return res
```
