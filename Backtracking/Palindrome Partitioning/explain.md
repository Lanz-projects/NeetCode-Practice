# Palindrome Partitioning

## 🔍 Problem Summary

Given a string `s`, split it into substrings so that every substring in the partition is a palindrome.

Return every possible valid partition of the string. The main challenge is exploring all possible ways to split the string while ensuring that each chosen substring reads the same forward and backward.

---

## 🧠 Key Insight

Instead of generating every possible partition and checking it afterward, verify whether each substring is a palindrome before including it in the current partition.

By using backtracking, we only continue exploring partitions built from valid palindrome substrings. This prunes invalid paths early and efficiently generates every valid partition.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Generate every possible way to partition the string into substrings.
- After creating a partition, check whether every substring is a palindrome.
- This approach wastes time exploring many partitions that ultimately contain invalid substrings.

### 2. Optimal Approach

- Use backtracking to build one partition at a time.
- Starting from the current index, try every possible ending index to form a substring.
- Before adding the substring, check whether it is a palindrome using the helper function.
- If it is valid, add it to the current partition and recursively continue from the next index.
- When the end of the string is reached, add a copy of the completed partition to the results.
- After each recursive call, remove the last substring to restore the previous state and explore the next possibility.

Since only palindrome substrings are explored, the search avoids many unnecessary paths while still finding every valid partition. The algorithm runs in **O(n · 2ⁿ)** time in the worst case due to the number of possible partitions and repeated palindrome checks, and uses **O(n)** auxiliary space for the recursion stack and current partition, excluding the space needed for the output.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        part = []

        def backtracking(i):
            if i == len(s):
                res.append(part[:])
                return
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    part.append(s[i:j+1])
                    backtracking(j + 1)
                    part.pop()

        backtracking(0)
        return res

    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
```