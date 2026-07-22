# Valid Parenthesis String

## 🔍 Problem Summary

You are given a string containing `'('`, `')'`, and `'*'`. Determine whether the string can be interpreted as a valid parentheses sequence.

The `'*'` character is flexible—it can represent `'('`, `')'`, or an empty string. The main challenge is handling these multiple possibilities efficiently without trying every combination.

---

## 🧠 Key Insight

Instead of deciding what each `'*'` represents immediately, keep track of the range of possible unmatched left parentheses as you scan the string.

The minimum possible number of unmatched `'('` and the maximum possible number are updated for each character. As long as this range remains valid, there is at least one interpretation that could produce a balanced string.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Recursively try treating every `'*'` as `'('`, `')'`, or an empty string.
- Check whether any resulting string is a valid parentheses sequence.
- Since each `'*'` has three choices, this approach has exponential time complexity and quickly becomes impractical.

### 2. Better Approach

- Maintain two values:
  - `leftMin`, the minimum possible number of unmatched left parentheses.
  - `leftMax`, the maximum possible number of unmatched left parentheses.
- Traverse the string one character at a time.
- For `'('`, increment both values.
- For `')'`, decrement both values.
- For `'*'`, decrement `leftMin` (treating it as `')'` or empty) and increment `leftMax` (treating it as `'('`).
- If `leftMax` ever becomes negative, there are too many right parentheses, so return `False`.
- If `leftMin` becomes negative, reset it to `0` since the minimum number of unmatched left parentheses cannot be less than zero.
- After processing the string, return `True` only if `leftMin` is `0`, meaning a balanced interpretation exists.

By tracking only the range of possible unmatched left parentheses instead of every interpretation, the algorithm processes the string in **O(n)** time while using **O(1)** additional space.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1

            if leftMax < 0:
                return False

            if leftMin < 0:
                leftMin = 0

        return leftMin == 0
```
