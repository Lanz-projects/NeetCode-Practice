# Partition Labels

## 🔍 Problem Summary

You are given a string `s` and need to divide it into as many partitions as possible such that each letter appears in at most one partition.

The partitions must remain in the original order and concatenate back into the original string. The main challenge is determining where a partition can safely end without splitting occurrences of the same character across multiple partitions.

---

## 🧠 Key Insight

A partition cannot end until it includes the last occurrence of every character seen so far.

By first recording the last index of each character, you can expand the current partition whenever you encounter a character whose last occurrence is farther to the right. Once the current index reaches the farthest required position, the partition is complete.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Try every possible way to split the string into partitions.
- For each partition, verify that no character appears in another partition.
- This requires checking many possible partition points, making it inefficient for longer strings.

### 2. Optimal Approach

- Make one pass through the string to record the last occurrence of every character.
- Traverse the string a second time while tracking:
  - `end`, the farthest last occurrence of any character seen so far.
  - `size`, the current partition's length.
- For each character, update `end` using its last occurrence.
- Increase the partition size as you move through the string.
- When the current index reaches `end`, all characters in the current partition have been fully contained, so record the partition size and begin a new one.

The first pass builds the last occurrence map, and the second pass determines partition boundaries greedily. The algorithm runs in **O(n)** time and uses **O(1)** additional space since there are at most 26 lowercase letters.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        lastIndex = {}

        for i, c in enumerate(s):
            lastIndex[c] = i

        res = []
        size = end = 0

        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])

            if i == end:
                res.append(size)
                size = 0

        return res
```