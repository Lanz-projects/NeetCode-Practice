# Serialize And Deserialize Binary Tree

## 🔍 Problem Summary

Design two functions for a binary tree: one to convert the tree into a string (serialization) and another to rebuild the original tree from that string (deserialization).

The main challenge is preserving the tree's exact structure, including missing children, so that deserializing the string always reconstructs the original tree without losing any information.

---

## 🧠 Key Insight

A preorder depth-first traversal naturally visits every node in a consistent order. By also recording null children with a special marker, the serialized string contains enough information to uniquely reconstruct the entire tree.

During deserialization, reading the values in the same preorder order allows the tree to be rebuilt recursively, consuming one value at a time.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Store only the node values in a traversal order such as preorder or inorder.
- This does not preserve the tree's structure because missing children are not recorded, making it impossible to uniquely reconstruct the original tree.

### 2. Better Approach

- Perform a preorder depth-first traversal of the tree.
- For each node, append its value to the serialized result. If a node is `None`, append a special marker (`"N"`).
- Join the collected values into a comma-separated string.
- During deserialization, split the string back into a list of values and recursively process them in preorder.
- If the current value is `"N"`, return `None`. Otherwise, create a node and recursively build its left and right children.
- Because serialization and deserialization each visit every node exactly once, both operations run in **O(n)** time, where `n` is the number of nodes. The serialized output and recursive call stack require **O(n)** additional space.

---

## 🧪 Final Code (Python)

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None

            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
```
