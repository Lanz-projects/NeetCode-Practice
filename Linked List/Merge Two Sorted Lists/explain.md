# Merge Two Sorted Lists

## 🔍 Problem Summary

You are given the heads of two **sorted** singly linked lists.

Merge the two lists into a single sorted linked list by reusing the existing nodes, and return the head of the merged list.

The challenge is to merge the lists efficiently without creating new nodes or losing track of either list.

---

## 🧠 Key Insight

Since both linked lists are already sorted, we only need to repeatedly compare the current nodes of each list.

Whichever node has the smaller value is appended to the merged list, and its pointer advances. This process continues until one list is exhausted, after which the remaining nodes from the other list can be attached directly.

---

## 🧩 Approaches Considered

### 1. Brute Force

- Traverse both linked lists and copy all values into an array.
- Sort the array.
- Build a new linked list from the sorted values.
- While correct, this requires **O(m + n)** extra space and performs unnecessary sorting since the input lists are already sorted.

### 2. Optimal Approach

- Create a dummy node to simplify building the merged list.
- Maintain a `tail` pointer that always points to the last node in the merged list.
- While both lists have remaining nodes:
  - Compare the current values.
  - Attach the smaller node to the merged list.
  - Advance the pointer in the list from which the node was taken.
  - Move `tail` forward.
- Once one list is exhausted, attach the remaining nodes from the other list directly.

Since every node is visited exactly once, the algorithm runs in **O(m + n)** time using **O(1)** extra space.

---

## 🧪 Final Code (Python)

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1:
            tail.next = list1

        if list2:
            tail.next = list2

        return dummy.next
```