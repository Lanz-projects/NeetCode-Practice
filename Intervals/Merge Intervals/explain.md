# Merge Intervals

## 🔍 Problem Summary

You are given a list of intervals that may overlap. Merge every set of overlapping intervals and return a list containing only non-overlapping intervals.

The intervals are not guaranteed to be sorted, so the main challenge is identifying which intervals overlap and combining them while preserving the correct ordering.

---

## 🧠 Key Insight

Once the intervals are sorted by their starting times, any overlapping intervals will appear next to each other.

This allows us to process the intervals in a single pass, merging the current interval with the last interval in the result whenever they overlap.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Compare every interval with every other interval to find overlaps.
- Repeatedly merge overlapping intervals until no overlaps remain.
- This approach performs many unnecessary comparisons, making it inefficient for large inputs.

### 2. Better Approach

- Sort the intervals by their starting values.
- Initialize the result list with the first interval.
- Iterate through the remaining intervals.
- Compare the current interval's start with the ending value of the last merged interval.
- If they overlap, update the ending value of the last merged interval to the larger ending value.
- Otherwise, append the current interval as a new non-overlapping interval.

Sorting ensures overlapping intervals are processed consecutively, allowing every interval to be examined only once after sorting. The algorithm runs in **O(n log n)** time due to the initial sort, followed by a linear scan, and uses **O(n)** additional space for the output list.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda i: i[0])
        outputs = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = outputs[-1][1]

            if start <= lastEnd:
                outputs[-1][1] = max(lastEnd, end)
            else:
                outputs.append([start, end])

        return outputs
```
