# Meeting Rooms

## 🔍 Problem Summary

You are given a list of meeting time intervals, each with a start and end time. Determine whether a person can attend every meeting without any scheduling conflicts.

Meetings that end exactly when another begins are allowed. The main challenge is efficiently detecting whether any two meetings overlap.

---

## 🧠 Key Insight

After sorting the meetings by their start times, any scheduling conflict can only occur between consecutive meetings.

This means we only need to compare each meeting with the one immediately before it. If a meeting starts before the previous one ends, a conflict exists and attending every meeting is impossible.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Compare every meeting with every other meeting to check for overlaps.
- If any pair overlaps, return `False`; otherwise, return `True`.
- This approach performs unnecessary comparisons, resulting in **O(n²)** time.

### 2. Better Approach

- Sort the meetings by their starting times.
- Iterate through the sorted list beginning with the second meeting.
- Compare the current meeting's start time with the previous meeting's end time.
- If the current meeting starts before the previous one ends, a scheduling conflict exists, so return `False`.
- If the loop completes without finding any overlaps, return `True`.

Sorting places potentially overlapping meetings next to each other, allowing a single linear scan to detect conflicts. The algorithm runs in **O(n log n)** time because of the initial sort and uses **O(1)** additional space.

---

## 🧪 Final Code (Python)

```python
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals):
        intervals.sort(key=lambda i: i.start)

        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]

            if i1.end > i2.start:
                return False

        return True
```
