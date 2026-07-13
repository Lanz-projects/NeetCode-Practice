# Kth Smallest Element in a BST

## 🔍 Problem Summary

You are given the root of a Binary Search Tree (BST) and an integer `k`. Return the value of the `k`th smallest node in the tree, where `k` is 1-indexed.

The main challenge is finding the `k`th smallest element efficiently without storing or sorting all of the node values. Since the tree is already a BST, its structure provides an ordering that can be leveraged.

---

## 🧠 Key Insight

A Binary Search Tree has the property that an in-order traversal (left, root, right) visits the nodes in ascending order.

Instead of storing every value, we can count each node as we visit it during the traversal. Once the `k`th node is visited, we immediately know it is the `k`th smallest value and can return it without processing the rest of the tree.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Perform a complete in-order traversal and store every node value in a list.
- Since the values are collected in sorted order, return the element at index `k - 1`.
- This approach works but uses unnecessary extra space because every value is stored, even though only one is needed.

### 2. Optimal Approach

- Use an iterative in-order traversal with a stack.
- Starting from the root, repeatedly move left, pushing each node onto the stack until reaching the leftmost node.
- Pop the top node from the stack, increment a counter, and check whether it is the `k`th node visited.
- If the counter equals `k`, return that node's value immediately.
- Otherwise, move to the node's right child and repeat the process.
- Because an in-order traversal of a BST visits nodes in ascending order, the `k`th visited node is guaranteed to be the `k`th smallest. This visits each node at most once, giving a time complexity of **O(h + k)** in the best case (or **O(n)** in the worst case), where `h` is the tree height, while the stack requires **O(h)** extra space.

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
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """

        n = 0
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            curr = curr.right
```
