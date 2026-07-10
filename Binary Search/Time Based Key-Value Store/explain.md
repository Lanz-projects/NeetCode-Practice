# Time Based Key-Value Store

## 🔍 Problem Summary

Design a data structure that stores multiple values for the same key at different timestamps.

You need to support two operations:

- `set(key, value, timestamp)` stores a value for a key at a specific timestamp.
- `get(key, timestamp)` returns the value associated with the **largest timestamp that is less than or equal to the given timestamp**.

If no such timestamp exists, return an empty string (`""`).

The challenge is to efficiently retrieve the correct historical value without scanning every stored timestamp.

---

## 🧠 Key Insight

The timestamps for each key are added in **strictly increasing order**.

This means each key's values are naturally stored in sorted order by timestamp, allowing us to use **binary search** to quickly find the latest timestamp that does not exceed the requested timestamp.

Instead of searching every stored value, binary search reduces each lookup to **O(log n)**.

---

## 🧩 Approaches Considered

### 1. Brute Force

- Store every `(value, timestamp)` pair for each key in a list.
- When `get()` is called, scan the list from the end (or beginning) until finding the largest timestamp that is less than or equal to the target timestamp.
- This works correctly but requires **O(n)** time for every lookup, which becomes inefficient as more values are stored.

### 2. Optimal Approach

- Store each key in a dictionary that maps to a list of `[value, timestamp]` pairs.
- Since timestamps are guaranteed to be inserted in increasing order, each list remains sorted automatically.
- During `get()`:
  - Retrieve the list for the given key.
  - Use binary search to find the largest timestamp that is less than or equal to the requested timestamp.
  - Keep track of the latest valid value found while searching.
- Return the stored value if one exists; otherwise return an empty string.

Each `set()` operation runs in **O(1)** time, while each `get()` operation runs in **O(log n)** due to binary search.

---

## 🧪 Final Code (Python)

```python
class TimeMap(object):

    def __init__(self):
        self.store = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        res = ''
        values = self.store.get(key, [])

        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2

            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1

        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key, value, timestamp)
# param_2 = obj.get(key, timestamp)
```
