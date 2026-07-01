# Min Stack

## 🔍 Problem Summary

We need to design a special stack that supports all normal stack operations — `push`, `pop`, `top` — **plus** an additional operation: retrieving the minimum element currently in the stack.

The challenge is that **every operation must run in O(1) time**, including `getMin()`.  
This means we cannot scan the stack or recompute the minimum each time; we must maintain it efficiently as we push and pop.

---

## 🧠 Key Insight

A normal stack cannot tell us the minimum in O(1) time because the minimum changes whenever elements are added or removed.

The key idea is to maintain a **second stack** (`minStack`) that always stores the minimum value _up to that point_.  
Each push updates the minimum, and each pop removes the corresponding minimum.  
This ensures `getMin()` is always just the top of `minStack`.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Store all values in a single stack and compute the minimum by scanning the entire stack whenever `getMin()` is called.
- This is **too slow** because scanning takes O(n) time, violating the O(1) requirement.

### 2. Optimal Approach

- Maintain **two stacks**:
  - `stack` → stores all values normally
  - `minStack` → stores the minimum value at each level of the stack
- When pushing:
  - Compare the new value with the current minimum
  - Push the new minimum onto `minStack`
- When popping:
  - Pop from both stacks
- `getMin()` becomes O(1) because the minimum is always at the top of `minStack`.

This approach satisfies all constraints and keeps every operation constant time.

---

## 🧪 Final Code (Python)

```python
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack.append(value)
        val = min(val, self.minStack[-1] if self.minStack else val)
    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]

```
