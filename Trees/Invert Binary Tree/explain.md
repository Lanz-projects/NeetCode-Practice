# Invert Binary Tree

## 🔍 Problem Summary

You are given the root of a binary tree and need to invert the tree by swapping the left and right child of every node.

The goal is to return the root of the inverted tree. The main challenge is ensuring that every node in the tree has its children swapped while preserving the overall tree structure.

---

## 🧠 Key Insight

Each node can be inverted independently by swapping its left and right children. Once the current node is swapped, the same operation can be applied recursively to its left and right subtrees.

Since every subtree is itself a binary tree, recursively performing the same operation naturally inverts the entire tree.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Traverse the tree and create an entirely new tree with every node's left and right children swapped.
- Return the newly constructed tree.

While this works, it requires additional memory to build a second tree when the original tree can be modified directly.

### 2. Optimal Approach

The solution uses a recursive depth-first traversal to invert the tree in place.

It first checks whether the current node is `None`. If so, the recursion stops because there is nothing to invert. Otherwise, it swaps the current node's left and right children using a temporary variable.

After swapping the children, the algorithm recursively inverts the new left subtree and the new right subtree. Since every node performs the same operation, the recursion eventually visits every node in the tree exactly once.

Because each node is processed a single time, the algorithm runs in **O(n)** time, where `n` is the number of nodes in the tree. The recursion uses **O(h)** space on the call stack, where `h` is the height of the tree. In the worst case of a completely unbalanced tree, this becomes **O(n)**, while for a balanced tree it is **O(log n)**.

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
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None

        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
```
