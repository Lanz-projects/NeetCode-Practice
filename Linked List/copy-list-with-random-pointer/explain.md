# Copy List with Random Pointer

## 🔍 Problem Summary

You are given the head of a linked list where each node has:

- A `next` pointer to the next node.
- A `random` pointer that can point to **any node** in the list or `None`.

Create a **deep copy** of the entire list, meaning every node in the new list must be a brand new node with the same values and the same `next` and `random` relationships.

None of the pointers in the copied list may reference nodes from the original list.

---

## 🧠 Key Insight

Each original node must correspond to exactly one copied node.

A hash map can store this relationship:

```
original node → copied node
```

Once every copied node has been created, we can use the map to correctly assign both the `next` and `random` pointers.

---

## 🧩 Approaches Considered

### 1. Brute Force

- For every node, search the original list to determine where its `random` pointer points.
- Then search the copied list again to find the corresponding copied node.
- Since each random pointer may require scanning the list, this results in **O(n²)** time complexity.

### 2. Optimal Approach

- Use a hash map to associate every original node with its copied node.
- Perform two passes through the list:
  1. Create a copy of every node and store the mapping.
  2. Use the mapping to assign each copied node's `next` and `random` pointers.
- Initializing the map with `{None: None}` allows both pointers to be assigned without needing special cases for `None`.

This approach visits each node a constant number of times, resulting in **O(n)** time complexity with **O(n)** extra space.

---

## 🧪 Final Code (Python)

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        oldToCopy = {None : None}

        curr = head

        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next

        curr = head

        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next

        return oldToCopy[head]
```
