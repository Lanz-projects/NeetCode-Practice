# Linked List Cycle

## 🔍 Problem Summary

Given the head of a singly linked list, determine whether the list contains a **cycle**.

A cycle exists if following the `next` pointers eventually leads back to a previously visited node instead of reaching the end of the list.

Return `True` if a cycle exists; otherwise return `False`.

---

## 🧠 Key Insight

Use two pointers that move at different speeds.

- A **slow** pointer moves one node at a time.
- A **fast** pointer moves two nodes at a time.

If the linked list contains a cycle, the fast pointer will eventually catch up to the slow pointer. If the list has no cycle, the fast pointer will reach the end of the list.

---

## 🧩 Approaches Considered

### 1. Brute Force

- Traverse the linked list while storing every visited node in a hash set.
- If a node is encountered that has already been seen, a cycle exists.
- If the traversal reaches the end of the list, there is no cycle.
- This approach runs in **O(n)** time but requires **O(n)** extra space.

### 2. Optimal Approach

- Use Floyd's Cycle Detection Algorithm (also called the **Tortoise and Hare** algorithm).
- Initialize both the slow and fast pointers at the head.
- Move:
  - `slow` one step at a time.
  - `fast` two steps at a time.
- If the pointers ever meet, a cycle exists.
- If `fast` or `fast.next` becomes `None`, the list has no cycle.

This algorithm visits each node at most a constant number of times, giving **O(n)** time complexity while using only **O(1)** extra space.

---

## 🧪 Final Code (Python)

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
```
