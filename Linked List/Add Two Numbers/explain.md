# Add Two Numbers

## 🔍 Problem Summary

You are given two non-empty linked lists representing two non-negative integers.

- Each node contains a single digit.
- The digits are stored in **reverse order**, so the head contains the least significant digit.

Add the two numbers and return the sum as a linked list in the same reversed format.

The challenge is correctly handling different list lengths and carrying digits when a sum exceeds `9`.

---

## 🧠 Key Insight

Process both linked lists **digit by digit**, just like performing addition by hand.

For each position:

- Add the two digits (using `0` if one list has ended).
- Include any carry from the previous addition.
- Store the current digit in the result list.
- Carry the tens digit to the next iteration.

Continue until both lists and the carry have been fully processed.

---

## 🧩 Approaches Considered

### 1. Brute Force

- Convert each linked list into its corresponding integer.
- Add the two integers together.
- Convert the resulting integer back into a linked list.
- While this works conceptually, it relies on converting potentially very large numbers and does not naturally follow the linked list representation.

### 2. Optimal Approach

- Create a dummy node to simplify building the result list.
- Traverse both linked lists simultaneously.
- At each step:
  - Read the current digit from each list (or `0` if a list has ended).
  - Add the digits along with the current carry.
  - Create a new node containing the ones digit.
  - Update the carry with the tens digit.
- Continue while either list still has nodes or a carry remains.
- Return the node following the dummy node.

Each node is processed exactly once, giving **O(max(m, n))** time complexity with **O(max(m, n))** space for the output list.

---

## 🧪 Final Code (Python)

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        curr = dummy

        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # Calculate the current digit and carry
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10

            curr.next = ListNode(val)

            # Move pointers forward
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
```
