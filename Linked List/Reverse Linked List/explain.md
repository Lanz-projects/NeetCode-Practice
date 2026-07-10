# Problem Title

## 🔍 Problem Summary

A short restatement of the problem **in your own words**.  
Focus on: what is being asked, what the inputs/outputs are, and what the core challenge is.

---

## 🧠 Key Insight

The single most important idea that unlocks the solution.  
(Example: “We need fast membership checks → use a set.”)

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- One or two bullets describing how it works
- Why it’s too slow or not ideal

### 2. Optimal Approach

- The strategy you chose
- Why it works
- Why it’s better than brute force

---

## 🧪 Final Code (Python)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
      prev = None
      curr = head

      while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
      return prev
```
