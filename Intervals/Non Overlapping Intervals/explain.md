# Non Overlapping Intervals

## 🔍 Problem Summary

You are given a list of intervals that may overlap. Remove the minimum number of intervals so that the remaining intervals are all non-overlapping.

Intervals that only touch at their endpoints are considered non-overlapping. The main challenge is deciding which intervals to remove when overlaps occur in order to maximize the number of intervals that can remain.

---

## 🧠 Key Insight

When two intervals overlap, keeping the interval that finishes first leaves the most room for future intervals.

By always retaining the interval with the smaller ending value, we minimize the chance of creating additional overlaps later in the scan. This greedy choice leads to the minimum number of removals.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Try removing different combinations of intervals and check whether the remaining intervals overlap.
- Keep track of the smallest number of removals that produces a valid set.
- This approach explores far too many possibilities and is impractical for large inputs.

### 2. Optimal Approach

- Sort the intervals by their starting values.
- Keep track of the ending value of the last interval that has been kept.
- Iterate through the remaining intervals.
- If the current interval starts after or exactly when the previous interval ends, keep it and update the ending value.
- Otherwise, an overlap occurs, so increment the removal count.
- To maximize the number of intervals that can fit afterward, keep the interval with the smaller ending value by updating `prevEnd` to the minimum of the two ending values.

Sorting allows the intervals to be processed in order, while the greedy decision ensures the fewest intervals are removed. The algorithm runs in **O(n log n)** time because of the initial sort, followed by a single linear scan, and uses **O(1)** additional space.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda i: i[0])

        res = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)

        return res
```
