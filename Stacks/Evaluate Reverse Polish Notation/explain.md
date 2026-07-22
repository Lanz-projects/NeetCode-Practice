# Reverse Polish Notation

We are given an array of string tokens representing an arithmetic expression written in **Reverse Polish Notation (RPN)**.  
In RPN, operators come _after_ their operands, and expressions are evaluated using a stack.  
Each token is either:

- an integer, or
- one of the four operators: `+`, `-`, `*`, `/`

Our task is to evaluate the entire expression and return the final integer result.  
Division must truncate toward zero, and all operations are guaranteed to be valid.

---

## 🧠 Key Insight

Reverse Polish Notation naturally maps to a **stack-based evaluation**:

- Push numbers onto a stack
- When an operator appears, pop the top two numbers, apply the operator, and push the result back

This works because RPN ensures the correct order of operations without parentheses, and the stack always holds the most recent operands needed for each operator.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Evaluate the expression by repeatedly scanning the tokens and manually resolving operations in order.
- Too slow and complicated because Reverse Polish Notation requires nested operations, and repeatedly searching for operators leads to inefficient multi‑pass processing.

### 2. Better Approach

- Use a stack to evaluate the expression in a single pass.
- Push numbers onto the stack; when an operator appears, pop the top two numbers, apply the operator, and push the result back.
- Works because RPN guarantees the correct order of operations, and the stack always holds the most recent operands needed.
- More efficient and cleaner than brute force, achieving O(n) time with O(n) space.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for c in tokens:
          if c == "+":
            stack.append(stack.pop() + stack.pop())
          elif c == "-":
            a,b = stack.pop(), stack.pop()
            stack.append(b-a)
          elif c == "*":
            stack.append(stack.pop() * stack.pop())
          elif c == "/":
             a,b = stack.pop(), stack.pop()
             stack.append(int(float(b) / a))
          else:
            stack.append(int(c))
        return stack[0]
```
