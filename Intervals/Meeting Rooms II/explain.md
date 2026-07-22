# Meeting Rooms II

## 🔍 Problem Summary

You are given a list of meeting time intervals, each with a start and end time. Determine the minimum number of meeting rooms required so that every meeting can take place without overlapping in the same room.

Meetings that end exactly when another begins can use the same room. The main challenge is efficiently tracking how many meetings are happening at the same time.

---

## 🧠 Key Insight

Rather than checking every pair of meetings, separate the start and end times into two sorted lists.

As you scan through the start times, compare each one with the earliest ending meeting. If a meeting starts before the earliest one ends, a new room is needed. Otherwise, a room has become available and can be reused.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Process meetings one at a time and search through existing rooms to find one that is available.
- Create a new room whenever no existing room can accommodate the meeting.
- This approach repeatedly checks room availability, making it inefficient as the number of meetings grows.

### 2. Better Approach

- Store all meeting start times in one array and all end times in another.
- Sort both arrays independently.
- Use two pointers to scan through the start and end times.
- If the next meeting starts before the earliest current meeting ends, allocate a new room by increasing the active meeting count.
- Otherwise, advance the end pointer because a room has become available, then decrease the active meeting count.
- Track the maximum number of simultaneously active meetings, which is the minimum number of rooms required.

Sorting the start and end times allows meetings to be processed in chronological order without explicitly assigning rooms. The algorithm runs in **O(n log n)** time due to sorting and uses **O(n)** additional space for the separate start and end arrays.

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
    def minMeetingRooms(self, intervals):
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res = count = 0
        s = e = 0

        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1

            res = max(res, count)

        return res
```
