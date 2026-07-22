# Minimum Interval to Include Each Query

## 🔍 Problem Summary

You are given a list of inclusive intervals and a list of queries. For each query, return the size of the smallest interval that contains that query value.

If no interval contains the query, return `-1` for that query. The main challenge is answering many queries efficiently without checking every interval against every query.

---

## 🧠 Key Insight

If we process queries in sorted order, we can add intervals to consideration as soon as their start value is less than or equal to the current query.

A min-heap can then keep track of candidate intervals by their size, while removing intervals that no longer contain the query. This ensures the heap top is always the smallest valid interval for the current query.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- For each query, scan every interval and check whether the query lies within the interval.
- Among all matching intervals, return the smallest interval size.
- This approach takes **O(n · m)** time for `n` intervals and `m` queries, which is too slow for large inputs.

### 2. Better Approach

- Sort the intervals by their starting value.
- Sort the queries, but keep track of their original positions by storing answers in a dictionary.
- Use a pointer to add all intervals whose start is less than or equal to the current query.
- Store candidate intervals in a min-heap as `(interval_size, right_end)`.
- Before answering the query, remove intervals from the heap whose right end is smaller than the query because they no longer contain it.
- If the heap is not empty, the top element gives the size of the smallest valid interval. Otherwise, the answer is `-1`.
- Build the final result array by mapping answers back to the original query order.

Sorting the intervals and queries takes **O(n log n + m log m)** time. Each interval is pushed and popped from the heap at most once, so the total heap work is **O((n + m) log n)**. The algorithm uses **O(n)** additional space for the heap.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def minInterval(self, intervals, queries):
        """
        :type intervals: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        intervals.sort()

        minHeap = []
        res, i = {}, 0

        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1

            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)

            res[q] = minHeap[0][0] if minHeap else -1

        return [res[q] for q in queries]
```
