# Lowest Common Ancestor in Binary Search Tree

## 🔍 Problem Summary

You are given the root of a Binary Search Tree (BST) along with two nodes, `p` and `q`. The goal is to find their lowest common ancestor (LCA).

The lowest common ancestor is the deepest node that has both `p` and `q` as descendants, where a node can also be a descendant of itself. The challenge is identifying this node efficiently by taking advantage of the BST's ordering property.

---

## 🧠 Key Insight

A Binary Search Tree guarantees that all values in the left subtree are smaller than the current node and all values in the right subtree are larger.

By comparing the values of `p` and `q` with the current node, you can determine whether both nodes lie on the left, both lie on the right, or are split across both sides. The first node where they split (or where one of them equals the current node) is the lowest common ancestor.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Traverse the tree to find the path from the root to `p` and the path from the root to `q`.
- Compare the two paths until they diverge, returning the last common node.

Although this works, it requires storing both paths and does not take full advantage of the Binary Search Tree structure.

### 2. Better Approach

The solution uses an iterative traversal that leverages the ordering property of a Binary Search Tree.

Starting at the root, it compares the values of `p` and `q` with the current node. If both values are greater than the current node's value, the lowest common ancestor must be in the right subtree, so the search moves right. If both values are smaller, the search continues in the left subtree.

When the two nodes no longer fall on the same side of the current node, or one of them matches the current node, the search has found the point where their paths diverge. That node is the lowest common ancestor and is immediately returned.

Because only one path from the root is explored, the algorithm runs in **O(h)** time, where `h` is the height of the tree. The iterative approach uses only a single pointer, resulting in **O(1)** extra space.

---

## 🧪 Final Code (Python)

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        curr = root

        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr
```
