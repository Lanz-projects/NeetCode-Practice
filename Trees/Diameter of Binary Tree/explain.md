# Diameter of Binary Tree

## 🔍 Problem Summary

You are given the root of a binary tree and need to find its diameter.

The diameter is the length of the longest path between any two nodes in the tree, measured by the number of edges. The path does not necessarily have to pass through the root, making the challenge identifying the longest path anywhere in the tree.

---

## 🧠 Key Insight

The longest path through any node is determined by the height of its left subtree plus the height of its right subtree.

By calculating the height of each subtree during a depth-first traversal, you can simultaneously update the longest diameter seen so far without needing a separate pass through the tree.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- For every node, calculate the height of its left and right subtrees.
- Compute the diameter passing through that node and keep track of the largest value.

This approach repeatedly recalculates subtree heights, resulting in unnecessary work and a much slower overall solution.

### 2. Optimal Approach

The solution performs a single depth-first traversal of the tree while computing the height of each subtree.

A recursive helper function returns the height of the current subtree. If the current node is `None`, it returns `0`. Otherwise, it recursively computes the heights of the left and right subtrees.

Once both heights are known, the algorithm calculates the diameter passing through the current node by adding the left and right subtree heights together. If this value is larger than the current maximum diameter, it updates the stored result. Finally, the function returns the height of the current subtree by adding `1` to the larger of the two subtree heights.

Because each node is visited exactly once, the algorithm runs in **O(n)** time, where `n` is the number of nodes in the tree. The recursive calls require **O(h)** space on the call stack, where `h` is the height of the tree. In the worst case of a completely unbalanced tree, this becomes **O(n)**, while for a balanced tree it is **O(log n)**.

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
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        self.diameter = 0

        def dfs(curr):
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)

        dfs(root)
        return self.diameter
```
