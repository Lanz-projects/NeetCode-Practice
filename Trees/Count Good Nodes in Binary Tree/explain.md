# Count Good Nodes in Binary Tree

## 🔍 Problem Summary

You are given the root of a binary tree and need to count how many nodes are considered "good."

A node is good if there is no node with a greater value along the path from the root to that node. The challenge is keeping track of the maximum value seen so far while traversing each path through the tree.

---

## 🧠 Key Insight

As you move from the root to a node, the only information needed is the largest value encountered along that path.

By carrying this maximum value during a depth-first traversal, you can immediately determine whether the current node is good and then update the maximum before continuing to its children.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- For every node, trace the path back to the root.
- Find the maximum value along that path and determine whether the current node is at least as large.

Although this works, it repeatedly traverses the same paths, resulting in unnecessary work.

### 2. Optimal Approach

The solution uses a recursive depth-first search while passing the maximum value seen on the current root-to-node path.

The traversal begins at the root, using the root's value as the initial maximum. For each node, it compares the node's value with the current maximum. If the node's value is greater than or equal to the maximum seen so far, it is counted as a good node.

The maximum value is then updated before recursively exploring the left and right subtrees. Each recursive call returns the number of good nodes found in its subtree, and these counts are added together to produce the final answer.

Since every node is visited exactly once, the algorithm runs in **O(n)** time, where `n` is the number of nodes in the tree. The recursion requires **O(h)** space on the call stack, where `h` is the height of the tree. In the worst case of a completely unbalanced tree, this becomes **O(n)**, while for a balanced tree it is **O(log n)**.

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
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node, maxVal):
            if not node:
                return 0

            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res

        return dfs(root, root.val)
```