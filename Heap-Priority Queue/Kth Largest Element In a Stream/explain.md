# Kth Largest Element In a Stream

## 🔍 Problem Summary

Design a data structure that continuously tracks the `k`th largest element in a stream of integers.

The class is initialized with an integer `k` and an initial list of numbers. After each call to `add(val)`, return the current `k`th largest element among all values seen so far. The main challenge is efficiently updating the answer as new numbers are added without repeatedly sorting the entire stream.

---

## 🧠 Key Insight

Instead of storing every number in sorted order, we only need to keep track of the largest `k` elements seen so far.

A min-heap of size `k` makes this possible. The smallest value in the heap is always the `k`th largest overall, so each new value only requires updating the heap rather than reprocessing the entire stream.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Store every number that has been seen and sort the entire collection after each new value is added.
- Return the element at the appropriate position in the sorted list.
- This approach becomes inefficient because sorting is repeated after every insertion.

### 2. Optimal Approach

- Store the numbers in a min-heap and remove the smallest elements until only `k` remain.
- The heap always contains the current `k` largest values.
- When a new value is added, push it into the heap.
- If the heap grows larger than `k`, remove the smallest element.
- After these updates, the root of the min-heap is the `k`th largest element, so return it.

Since the heap never stores more than `k` elements, each insertion and removal takes **O(log k)** time. Initializing the heap takes **O(n + (n - k) log n)** in this implementation, and the data structure uses **O(k)** space.

---

## 🧪 Final Code (Python)

```python
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
```
