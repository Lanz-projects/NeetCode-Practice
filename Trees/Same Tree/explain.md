# Same Tree

## 🔍 Problem Summary

You are given the roots of two binary trees and must determine whether they are identical. Two trees are considered the same if they have the same structure and every corresponding node contains the same value.

The main challenge is verifying both the tree structure and node values simultaneously, since a difference in either means the trees are not the same.

---

## 🧠 Key Insight

Two trees are identical if their corresponding nodes match at every position. This naturally leads to a recursive comparison, where each pair of nodes is checked before recursively comparing their left and right children.

If both nodes are `None`, that portion of the trees matches. If one node is missing or the values differ, the trees cannot be the same.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Traverse both trees separately, store their structures and values, then compare the resulting representations.
- This works but requires additional memory to store both traversals before making the comparison.

### 2. Optimal Approach

- Recursively compare the corresponding nodes of both trees.
- If both nodes are `None`, return `True` since the current subtrees match.
- If one node is missing or their values differ, return `False`.
- Otherwise, recursively compare both left subtrees and both right subtrees.
- The trees are identical only if every recursive comparison succeeds. Since each pair of corresponding nodes is visited once, the algorithm runs in **O(n)** time, where `n` is the number of nodes, and uses **O(h)** space for the recursive call stack, where `h` is the height of the tree.

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

        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))
```
