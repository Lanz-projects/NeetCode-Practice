# Binary Tree Level Order Traversal

## 🔍 Problem Summary

You are given the root of a binary tree and need to return its level order traversal.

The output should contain a list of lists, where each inner list contains the values of the nodes at the same depth. The challenge is visiting the tree level by level rather than using the more common depth-first traversal.

---

## 🧠 Key Insight

A queue naturally processes nodes in the order they are discovered, making it ideal for breadth-first search (BFS).

By processing all nodes currently in the queue before moving on to the next set of children, each iteration corresponds to exactly one level of the tree.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Compute the height of the tree.
- For each level, perform a separate traversal to collect the nodes at that depth.

Although this approach works, it repeatedly traverses portions of the tree, resulting in unnecessary work.

### 2. Optimal Approach

The solution uses a breadth-first search (BFS) with a queue to traverse the tree one level at a time.

It starts by placing the root node into a queue. While the queue is not empty, it records the number of nodes currently in the queue, which represents all the nodes at the current level.

It then processes exactly that many nodes by removing them from the front of the queue. For each valid node, its value is added to the current level's list, and its left and right children are added to the queue for processing during the next iteration. After all nodes at the current level have been processed, the completed level is added to the result.

Since every node is visited exactly once, the algorithm runs in **O(n)** time, where `n` is the number of nodes in the tree. The queue stores at most one level of the tree at a time, requiring **O(w)** space, where `w` is the maximum width of the tree. In the worst case, this is **O(n)**.

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
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []

            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if level:
                res.append(level)

        return res
```
