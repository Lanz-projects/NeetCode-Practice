# Subtree of Another Tree

## 🔍 Problem Summary

You are given the roots of two binary trees, `root` and `subRoot`. The task is to determine whether `subRoot` appears as a subtree within `root`.

A subtree consists of a node in the original tree and all of its descendants. The challenge is finding a matching starting node and verifying that both the structure and node values of the two trees are identical.

---

## 🧠 Key Insight

A subtree match can only begin at a node whose value matches the root of `subRoot`. For each node in the main tree, check whether the entire subtree rooted at that node is identical to `subRoot`.

If it is not, recursively repeat the process for the left and right children until either a match is found or the entire tree has been searched.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Visit every node in the main tree as a possible starting point.
- For each node, compare the entire subtree with `subRoot`.

Although this approach may compare many subtrees, it is the straightforward way to solve the problem and forms the basis of the recursive solution.

### 2. Optimal Approach

The solution recursively searches the main tree while using a helper function to compare two trees for equality.

It first handles the base cases. If `subRoot` is empty, it is automatically a subtree, so the function returns `True`. If the main tree is empty but `subRoot` is not, there is no possible match, so it returns `False`.

For each node in the main tree, the algorithm calls `isSameTree` to determine whether the subtree rooted at that node is identical to `subRoot`. The helper recursively checks that both nodes exist, their values match, and their left and right subtrees are also identical.

If the current node is not a match, the algorithm continues searching by recursively checking the left and right subtrees of the main tree. The search stops as soon as a matching subtree is found.

In the worst case, `isSameTree` may be called for many nodes in the main tree, resulting in **O(m × n)** time, where `m` is the number of nodes in `root` and `n` is the number of nodes in `subRoot`. The recursive calls require **O(h)** space on the call stack, where `h` is the height of the main tree.

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
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))

    def isSameTree(self, r, s):
        if not r and not s:
            return True
        if r and s and r.val == s.val:
            return (self.isSameTree(r.left, s.left) and
                    self.isSameTree(r.right, s.right))
        return False
```
