# Insert Interval

## 🔍 Problem Summary

You are given a list of non-overlapping intervals sorted by their starting times, along with a new interval that needs to be inserted.

After inserting the new interval, return the updated list while maintaining the sorted order and merging any overlapping intervals. The main challenge is determining where the new interval belongs and combining it with any intervals it overlaps.

---

## 🧠 Key Insight

Since the intervals are already sorted and non-overlapping, we only need to process them once from left to right.

Each interval falls into one of three cases: it comes completely before the new interval, completely after it, or overlaps with it. Overlapping intervals can be merged by updating the new interval's start and end values as we scan through the list.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Insert the new interval into the list, sort all intervals, and then perform a full merge.
- This works correctly but performs unnecessary sorting even though the original intervals are already sorted.

### 2. Better Approach

- Iterate through the intervals from left to right.
- If the new interval ends before the current interval begins, insert the new interval into the result and append the remaining intervals.
- If the new interval starts after the current interval ends, add the current interval to the result since there is no overlap.
- Otherwise, the intervals overlap, so merge them by updating the new interval's start to the smaller starting value and its end to the larger ending value.
- If the loop finishes without inserting the new interval, append the merged interval to the result.

Because each interval is processed only once, the algorithm runs in **O(n)** time and uses **O(n)** additional space for the result list.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]

        res.append(newInterval)
        return res
```
