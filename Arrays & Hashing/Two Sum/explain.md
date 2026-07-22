# Two Sum

## 🔍 Problem Summary

- Given an array of intergs, and a target (int)
- Find two indices where the two values add up to the sum
- Return the indicies
- Only one valid solution

---

## 🧠 Key Insight

For each number, we need to quickly check whether its complement has already been seen.
A hashmap gives O(1) lookups and O(1) inserts, making it the ideal data structure.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Check each pair, and see if they add up to the target
- Time: O(n^2)
- Space: O(n)

### 2. Better Approach

- Use a hashmap to store the complements
- Iterate through, and check the complement of the curr value and the target, and check to see if its in the hashmap,
- If so, return the list of the current index, and the index of the complement
- Else, add the current value in the hashmap as a key, and set the value to be it's index
- If no applicable values found, return []

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def twoSum(self, nums, target):
      map = {}
      for index, value in enumerate(nums):
          complement = target - value
          if complement in map:
              return [map[complement], index]
          else:
              map[value] = index
      return []
```
