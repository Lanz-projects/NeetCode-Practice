# Binary Tree Maximum Path Sum

## 🔍 Problem Summary

You are given the root of a binary tree where each node contains an integer value. A path is any sequence of connected nodes, and it may begin and end at any node in the tree as long as each node is visited at most once.

The goal is to return the largest possible sum of values along any valid path. The main challenge is that the maximum path does not have to pass through the root and may include both the left and right subtrees of a node.

---

## 🧠 Key Insight

For each node, there are two different values to consider. One is the maximum path sum that can be extended upward to its parent, and the other is the maximum path sum that passes through the node by combining both its left and right subtrees.

A depth-first search allows us to compute both values during a single traversal. While each recursive call returns only one extendable path to its parent, we separately track the best complete path found anywhere in the tree.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Consider every possible path between every pair of nodes and calculate its sum.
- Since the number of possible paths grows rapidly as the tree becomes larger, this approach is far too slow for the given constraints.

### 2. Better Approach

- Perform a post-order depth-first search so each node is processed after its children.
- Recursively compute the maximum path sum that can be extended upward from the left and right children.
- Ignore any negative contributions by treating them as zero, since including them would only decrease the path sum.
- Update the global maximum using the current node plus both left and right contributions, representing the best path that passes through this node.
- Return the current node's value plus the larger of the two child contributions so the parent can continue building a valid path without creating a split.
- Since each node is visited exactly once, the algorithm runs in **O(n)** time, where `n` is the number of nodes. The recursive call stack requires **O(h)** space, where `h` is the height of the tree (up to **O(n)** in the worst case).

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
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res = [root.val]

        # return max path sum without split
        def dfs(root):
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # compute max path sum WITH split
            res[0] = max(res[0], root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]
```
