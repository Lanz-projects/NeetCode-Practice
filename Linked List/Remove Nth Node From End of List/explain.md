# Remove Nth Node From End of List

## 🔍 Problem Summary

Given the head of a singly linked list and an integer `n`, remove the **n-th node from the end** of the list and return the head of the modified list.

The challenge is removing the correct node in a **single traversal** without first counting the total number of nodes.

---

## 🧠 Key Insight

Use two pointers separated by `n` nodes.

- Move the **right** pointer `n` steps ahead.
- Then move both pointers forward together until the right pointer reaches the end.
- At that point, the **left** pointer will be immediately before the node that needs to be removed.

Using a dummy node simplifies handling edge cases, such as removing the head of the list.

---

## 🧩 Approaches Considered

### 1. Brute Force

- Traverse the list once to determine its length.
- Compute the position of the node to remove from the beginning.
- Traverse the list again to that position and remove the node.
- While simple, this requires **two passes** through the list.

### 2. Optimal Approach

- Create a dummy node that points to the head.
- Initialize:
  - `right` at the head.
  - `left` at the dummy node.
- Move `right` forward `n` nodes.
- Move both pointers together until `right` reaches the end.
- `left` now points to the node immediately before the one to remove.
- Skip the target node by updating `left.next`.
- Return `dummy.next`, which correctly handles cases where the head is removed.

This solution only traverses the list once, resulting in **O(n)** time complexity with **O(1)** extra space.

---

## 🧪 Final Code (Python)

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next
```
