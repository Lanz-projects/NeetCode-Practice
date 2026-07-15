# Letter Combinations of a Phone Number

## 🔍 Problem Summary

Given a string of digits from `2` to `9`, generate every possible letter combination that those digits could represent using the standard telephone keypad mapping.

Return all valid combinations in any order. The main challenge is exploring every possible choice for each digit while ensuring that every combination contains exactly one letter from each digit.

---

## 🧠 Key Insight

Each digit represents a small set of possible letters, so the problem can be viewed as choosing one letter for each position.

Backtracking allows us to build one combination at a time by selecting a letter for the current digit, recursively moving to the next digit, and collecting each completed combination once every digit has been processed.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Generate every possible sequence of letters without following the digit mapping, then filter out invalid combinations.
- This approach performs unnecessary work because it explores combinations that could never correspond to the given digits.

### 2. Optimal Approach

- Store the mapping from each digit to its corresponding letters in a dictionary.
- Use backtracking to process the digits from left to right.
- For the current digit, try each possible letter and append it to the current string.
- Recursively continue building the combination using the next digit.
- Once the current string has the same length as the input digits, add it to the results.

This approach systematically explores every valid letter choice without revisiting completed combinations. If there are `n` digits, the algorithm runs in **O(4ⁿ · n)** time in the worst case since each digit has up to four possible letters and building each result takes up to `n` characters. The recursion uses **O(n)** auxiliary space, excluding the space required for the output.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtracking(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return

            for c in digitToChar[digits[i]]:
                backtracking(i + 1, curStr + c)

        backtracking(0, "")
        return res
```
