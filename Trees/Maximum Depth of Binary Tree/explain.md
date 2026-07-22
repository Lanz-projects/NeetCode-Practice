# Maximum Depth of Binary Tree

## 🔍 Problem Summary

You are given the root of a binary tree and must determine its maximum depth. The depth of a tree is the number of nodes along the longest path from the root down to any leaf node.

The main challenge is exploring every branch of the tree while keeping track of the deepest path. Since the longest path could be in either the left or right subtree, both must be considered.

---

## 🧠 Key Insight

The depth of a tree can be defined recursively. The depth of a node is one plus the greater of the depths of its left and right subtrees.

By recursively computing the depth of each subtree, the maximum depth of the entire tree naturally builds up from the leaf nodes to the root.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Traverse every possible path from the root to each leaf while manually tracking the current depth.
- Although this finds the correct answer, it requires additional bookkeeping and is less elegant than using the recursive structure of the tree.

### 2. Better Approach

- Use recursion to compute the maximum depth of each subtree.
- If the current node is `None`, return `0` since an empty tree has no depth.
- Otherwise, recursively calculate the depths of the left and right subtrees.
- Return `1` plus the larger of the two depths to account for the current node.
- Since every node is visited exactly once, the algorithm runs in **O(n)** time, where `n` is the number of nodes. The recursive call stack requires **O(h)** space, where `h` is the height of the tree (up to **O(n)** in the worst case).

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
    def maxDepth(self, root):
        if not root:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```
