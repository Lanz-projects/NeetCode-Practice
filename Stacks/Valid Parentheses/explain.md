# Valid Parentheses

## 🔍 Problem Summary

We are given a string containing only the characters `()[]{}`.  
The task is to determine whether the parentheses form a **valid** sequence.  
A sequence is valid if:

- Every opening bracket has a corresponding closing bracket
- The types match (e.g., `(` with `)`)
- Brackets close in the correct last‑in, first‑out order

The output is a boolean indicating whether the entire string is valid.

---

## 🧠 Key Insight

Parentheses must close in the **reverse order** of how they were opened.  
A **stack** naturally models this behavior, allowing us to track open brackets and verify that each closing bracket matches the most recent opener.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Repeatedly remove valid pairs like `"()"`, `"[]"`, `"{}"` until no more can be removed
- If the string becomes empty, it is valid
- Inefficient because each removal requires scanning the entire string, leading to poor performance for long inputs

### 2. Better Approach

- Use a single stack to store opening brackets
- When encountering a closing bracket, check if it matches the top of the stack
- If it matches, pop; if not, the string is invalid
- Efficient because each character is processed once, giving linear time complexity

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{"}

        for char in s:
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False
```
