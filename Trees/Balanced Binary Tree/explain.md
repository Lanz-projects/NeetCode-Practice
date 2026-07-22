# Balanced Binary Tree

## 🔍 Problem Summary

You are given the root of a binary tree and need to determine whether it is height-balanced.

A binary tree is considered balanced if, for every node, the heights of its left and right subtrees differ by no more than one. The challenge is verifying this condition efficiently for every node without repeatedly recalculating subtree heights.

---

## 🧠 Key Insight

A subtree's balance depends on two pieces of information: whether its left and right subtrees are already balanced and what their heights are.

By returning both the balance status and the height from each recursive call, the algorithm can determine whether the current subtree is balanced while computing its height in a single traversal.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- For every node, calculate the heights of its left and right subtrees.
- Check whether their height difference is at most one before repeating the process for every subtree.

This approach repeatedly computes subtree heights, leading to unnecessary work and a slower overall solution.

### 2. Better Approach

The solution performs a single depth-first traversal that returns both the balance status and the height of each subtree.

If the current node is `None`, the helper function returns that the subtree is balanced with a height of `0`. Otherwise, it recursively gathers the balance information and heights from the left and right subtrees.

The current subtree is balanced only if both child subtrees are balanced and the difference between their heights is no greater than one. The function then returns this balance status along with the height of the current subtree, which is one greater than the larger of the two child heights. The final answer is the balance status returned for the root.

Because each node is visited exactly once, the algorithm runs in **O(n)** time, where `n` is the number of nodes in the tree. The recursion requires **O(h)** space on the call stack, where `h` is the height of the tree. In the worst case of a completely unbalanced tree, this becomes **O(n)**, while for a balanced tree it is **O(log n)**.

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
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def dfs(root):
            if not root:
                return [True, 0]

            left = dfs(root.left)
            right = dfs(root.right)

            balanced = (left[0] and right[0]) and (abs(left[1] - right[1]) <= 1)
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]
```
