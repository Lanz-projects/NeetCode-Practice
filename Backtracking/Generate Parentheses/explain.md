# Generate Parentheses

## 🔍 Problem Summary

Given an integer `n` representing the number of pairs of parentheses, generate every possible combination of well-formed parentheses.

The output should contain all valid strings that use exactly `n` opening and `n` closing parentheses. The main challenge is generating only valid combinations without producing invalid ones that would need to be filtered out afterward.

---

## 🧠 Key Insight

A valid parentheses string can never contain more closing parentheses than opening parentheses at any point while it is being built.

By constructing each string one character at a time, we can stop exploring any path that would become invalid. This backtracking approach generates only well-formed combinations, avoiding unnecessary work and ensuring every completed string is a valid answer.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Generate every possible string of length `2n` consisting of `(` and `)`.
- Check each completed string to determine whether it is a valid parentheses sequence.
- This approach explores many invalid combinations, making it much slower than necessary.

### 2. Better Approach

- Use backtracking to build the parentheses string one character at a time.
- Keep track of how many opening and closing parentheses have been added so far.
- If fewer than `n` opening parentheses have been used, add `(` and continue exploring.
- If there are fewer closing parentheses than opening parentheses, add `)` and continue exploring.
- When both counts reach `n`, join the characters in the stack and add the completed string to the results.
- After each recursive call, remove the last character to restore the previous state before trying the next choice.

Since invalid prefixes are never explored, every recursive path can only produce valid parentheses combinations. The algorithm runs in **O(4ⁿ / √n)** time, which is proportional to the number of valid combinations generated, and uses **O(n)** auxiliary space for the recursion stack and current string (excluding the output).

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res
```
