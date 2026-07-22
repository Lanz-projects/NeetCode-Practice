# Find Median From Data Stream

## 🔍 Problem Summary

Design a data structure that supports continuously adding numbers from a data stream and efficiently returning the median of all numbers seen so far.

The median should update after each insertion, and queries should be answered quickly without sorting the entire collection every time. The main challenge is maintaining the numbers in a way that allows fast insertions while keeping the median readily available.

---

## 🧠 Key Insight

The median naturally divides the numbers into two halves: a smaller half and a larger half.

By maintaining a max-heap for the smaller half and a min-heap for the larger half, we can always keep the middle values at the tops of the heaps. Rebalancing the heaps after each insertion ensures their sizes differ by at most one, making the median easy to retrieve.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Store every number in a list and sort it whenever the median is requested.
- Return the middle element (or average of the two middle elements).
- This approach repeatedly sorts the data, making median queries inefficient as the stream grows.

### 2. Better Approach

- Maintain two heaps:
  - A max-heap (`small`) containing the smaller half of the numbers.
  - A min-heap (`large`) containing the larger half.
- Insert each new number into the max-heap.
- If the largest value in the max-heap is greater than the smallest value in the min-heap, move it to the min-heap to preserve ordering.
- Rebalance the heaps whenever one heap becomes larger than the other by more than one element.
- To find the median:
  - Return the top of the larger heap if the heaps have different sizes.
  - Otherwise, return the average of the two heap tops.

Each insertion performs a constant number of heap operations, resulting in **O(log n)** time. Retrieving the median only examines the heap tops, so it runs in **O(1)** time. The two heaps together store every inserted number, requiring **O(n)** space.

---

## 🧪 Final Code (Python)

```python
class MedianFinder(object):

    def __init__(self):
        self.small, self.large = [], []  # max-heap, min-heap

    def addNum(self, num):
        heapq.heappush(self.small, -num)

        # ensure ordering: max(small) <= min(large)
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # rebalance heaps
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-self.small[0] + self.large[0]) / 2.0
```
