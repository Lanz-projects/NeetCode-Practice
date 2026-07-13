# Same Tree

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
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if not p and not q:
            return True
        if (not p or not q) or (p.val != q.val):
            return False

        return (self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))

```
