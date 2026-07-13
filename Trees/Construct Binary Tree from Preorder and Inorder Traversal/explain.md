# Construct Binary Tree from Preorder and Inorder Traversal

## 🔍 Problem Summary

You are given two arrays representing the preorder and inorder traversals of the same binary tree. Your task is to reconstruct the original binary tree and return its root.

The main challenge is determining which nodes belong to the left and right subtrees at each step. By using the properties of preorder and inorder traversals together, the tree can be rebuilt recursively.

---

## 🧠 Key Insight

In a preorder traversal, the first value is always the root of the current subtree. Once that root is located in the inorder traversal, everything to its left belongs to the left subtree, and everything to its right belongs to the right subtree.

By recursively applying this process to the corresponding portions of both traversal arrays, the entire tree can be reconstructed.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Try every possible way of constructing a binary tree and compare its traversals to the given preorder and inorder arrays.
- While this would eventually find the correct tree, the number of possible binary trees grows exponentially, making the approach impractical.

### 2. Optimal Approach

- The first element in the preorder array is used to create the root node.
- Find that value in the inorder array to determine where the left subtree ends and the right subtree begins.
- Recursively build the left subtree using the corresponding slices of the preorder and inorder arrays.
- Recursively build the right subtree using the remaining portions of both arrays.
- Continue until there are no elements left, at which point the subtree is complete.
- Because each recursive call performs an `index()` lookup on the inorder array and creates new array slices, the overall time complexity is **O(n²)** in the worst case, while the recursive calls and sliced arrays require **O(n)** additional space.

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
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid + 1:])
        return root
```
