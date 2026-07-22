# Reverse Nodes In K Group

## 🔍 Problem Summary

You are given the head of a linked list and an integer `k`. The task is to reverse the nodes of the list in groups of `k` and return the modified linked list.

If the final group contains fewer than `k` nodes, it should remain unchanged. The challenge is to reverse the nodes themselves without modifying their values while correctly reconnecting each reversed group to the rest of the list.

---

## 🧠 Key Insight

Instead of trying to reverse the entire list at once, process the linked list one group of `k` nodes at a time.

Before reversing a group, first verify that it contains exactly `k` nodes. Once confirmed, reverse only that section in place and reconnect it to the previous and next portions of the list. Repeating this process produces the final result while leaving any incomplete group untouched.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Copy the nodes or their values into an array.
- Reverse every group of `k` elements in the array.
- Rebuild the linked list from the modified array.

Although this approach is easier to reason about, it uses extra memory and does not satisfy the requirement of modifying the linked list by rearranging the nodes themselves.

### 2. Better Approach

The solution uses a dummy node along with pointers to process the linked list one group at a time.

A helper function first locates the `k`th node from the current group's starting position. If fewer than `k` nodes remain, the algorithm stops because the remaining nodes should stay in their original order.

When a complete group is found, the algorithm stores the node immediately after the group and reverses the pointers within the group using the standard linked list reversal technique. It keeps track of the previous node and the current node, updating each node's `next` pointer until the entire group has been reversed.

After the reversal is complete, the newly reversed group is connected back to the previous portion of the list, and the pointer marking the previous group advances to the end of the reversed group. This process repeats until there are no more complete groups to reverse.

Since each node is visited a constant number of times, the algorithm runs in **O(n)** time, where `n` is the number of nodes in the linked list. The reversal is performed in place using only a few pointer variables, so the extra space complexity is **O(1)**.

---

## 🧪 Final Code (Python)

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            # reverse group
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
```
