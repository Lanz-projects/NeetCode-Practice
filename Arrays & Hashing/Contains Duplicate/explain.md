# Contains Duplicate

## 🔍 Problem Summary

- Given an int array
- If a value appears at least twice, return true
- Else return False, (Distinct)

---

## 🧠 Key Insight

Membership checking is the main operation.
A set provides O(1) average‑time lookups and inserts, making it ideal.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Compare each pair of element with eachother
- Time: O(n^2)
- Space: O(1)

### 2. List‑Based Approach

-Keep a list of seen values
-Checking membership in a list is O(n), so overall still O(n²)
-Time: O(n²)
-Space: O(n)

### 2. Better Approach

- Use a set to keep track of seen values
- Iterate through the array
- Check if the current element is in the set
- If yes, return True
- Else add value to set
- Time complexity of O(n)
- Space copmelxity of O(n)

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def containsDuplicate(self, nums):
      seen = set()
      for i in nums:
        if i in seen:
          return True
        else:
          seen.add(i)
      return False
```
