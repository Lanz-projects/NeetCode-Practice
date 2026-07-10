# Merge K Sorted Lists

## 🔍 Problem Summary

You are given an array of `k` linked lists, where each linked list is already sorted in ascending order.

The goal is to merge all of these sorted linked lists into a single sorted linked list and return its head. The challenge is doing this efficiently, since repeatedly merging into one growing list or sorting all values again would perform unnecessary work.

---

## 🧠 Key Insight

Rather than merging every list into one sequentially, repeatedly merge the linked lists in pairs until only a single list remains.

Each merge combines two already sorted linked lists in linear time. By reducing the number of lists by about half after every round, the total amount of work stays balanced and avoids repeatedly traversing an increasingly large merged list.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Traverse every linked list and collect all node values into an array.
- Sort the array.
- Create a new linked list from the sorted values.

Although this produces the correct result, it ignores that the input lists are already sorted and spends extra time sorting all of the values.

### 2. Optimal Approach

The solution uses a divide-and-conquer strategy by repeatedly merging linked lists in pairs.

It first checks if the input is empty and returns `None` when there are no lists to merge. While more than one linked list remains, it processes the lists two at a time. Each pair is merged using the `mergeList` helper function, and the merged results are stored in a new list. After each round, the number of linked lists is roughly cut in half. This process continues until only one fully merged linked list remains.

The `mergeList` helper uses a dummy node and a tail pointer to efficiently merge two sorted linked lists. It repeatedly compares the current nodes from each list, appends the smaller node to the merged list, and advances the corresponding pointer. Once one list is exhausted, the remaining nodes from the other list are attached directly since they are already sorted.

Because every node is processed once during each merge level and there are approximately `log k` merge levels, the overall time complexity is **O(N log k)**, where `N` is the total number of nodes across all linked lists. The algorithm reuses the existing nodes and only maintains temporary references during merging, requiring **O(1)** extra space (excluding the list used to hold the merged pairs).

---

## 🧪 Final Code (Python)

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next
```
