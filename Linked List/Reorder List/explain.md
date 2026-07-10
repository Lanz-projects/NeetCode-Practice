# Reorder List

## 🔍 Problem Summary

Given the head of a singly linked list, reorder the nodes so they appear in the following pattern:

```
L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...
```

You must **rearrange the existing nodes** by changing their pointers—you are **not allowed to modify the node values**.

The challenge is performing this reordering efficiently and **in-place**.

---

## 🧠 Key Insight

The reordering can be broken into **three simple steps**:

1. Find the middle of the linked list.
2. Reverse the second half of the list.
3. Merge the first half and the reversed second half by alternating nodes.

Each step can be done in linear time, resulting in an efficient in-place solution.

---

## 🧩 Approaches Considered

### 1. Brute Force

- Store every node in an array.
- Use two pointers (one at the beginning and one at the end) to reconnect the nodes in the required order.
- While this approach is straightforward, it requires **O(n)** extra space to store the nodes.

### 2. Optimal Approach

- Use the slow and fast pointer technique to find the middle of the linked list.
- Reverse the second half of the list in-place.
- Merge the two halves:
  - Take one node from the first half.
  - Then one node from the reversed second half.
  - Repeat until all nodes have been connected.
- Since the nodes are rearranged directly, no additional data structures are needed.

This approach visits each node only a constant number of times, resulting in **O(n)** time complexity with **O(1)** extra space.

---

## 🧪 Final Code (Python)

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None
        Do not return anything, modify head in-place instead.
        """

        # Find the middle
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        second = slow.next
        prev = slow.next = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # Merge the two halves
        first, second = head, prev

        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
```