# Validate Binary Search Tree

## 🔍 Problem Summary

You are given the root of a binary tree and need to determine whether it satisfies the properties of a valid Binary Search Tree (BST).

In a valid BST, every node in the left subtree must have a value smaller than the current node, and every node in the right subtree must have a value larger. This rule must hold for every node in the tree, not just its immediate children. The challenge is ensuring that every node satisfies the constraints imposed by all of its ancestors.

---

## 🧠 Key Insight

Instead of only comparing a node with its parent, keep track of the valid range of values that each node is allowed to have.

As you traverse the tree, moving to the left child updates the upper bound, while moving to the right child updates the lower bound. If any node falls outside its allowed range, the tree is not a valid BST.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- For every node, traverse its entire left subtree to ensure all values are smaller and its entire right subtree to ensure all values are larger.
- Repeat this process recursively for every node in the tree.

Although this approach works, it repeatedly traverses the same subtrees, resulting in unnecessary work.

### 2. Optimal Approach

The solution uses a recursive depth-first search while maintaining the valid lower and upper bounds for each node.

The traversal begins at the root with bounds of negative infinity and positive infinity. At each node, the algorithm checks whether the node's value lies strictly between the current bounds. If it does not, the tree immediately fails the BST validation.

When recursively exploring the left subtree, the current node's value becomes the new upper bound because every value to the left must be smaller. Likewise, when exploring the right subtree, the current node's value becomes the new lower bound because every value to the right must be larger. The tree is valid only if both recursive calls return `True`.

Since each node is visited exactly once, the algorithm runs in **O(n)** time, where `n` is the number of nodes in the tree. The recursion requires **O(h)** space on the call stack, where `h` is the height of the tree. In the worst case of a completely unbalanced tree, this becomes **O(n)**, while for a balanced tree it is **O(log n)**.

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
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def valid(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False

            return valid(node.left, left, node.val) and valid(node.right, node.val, right)

        return valid(root, float('-inf'), float('inf'))
```
