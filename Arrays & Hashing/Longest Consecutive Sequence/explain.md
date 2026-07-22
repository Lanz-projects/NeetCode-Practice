# Longest Consecutive Sequence

## 🔍 Problem Summary

- Given an unsorted array of ints,
- return length of longest consecutive elements sequence
- Has to be in O(n)

---

## 🧠 Key Insight

The single most important idea that unlocks the solution.  
(Example: “We need fast membership checks → use a set.”)

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Sort the array and then scan through it, counting how long each consecutive streak is.
- Sorting alone costs **O(n log n)**, which violates the required **O(n)** time constraint, making this approach too slow.

### 2. Better Approach

- Convert the list into a hash set to allow **O(1)** membership checks, then iterate through each number and only begin counting when the number is the **start** of a sequence (i.e., `num - 1` is not in the set). From each valid start, expand forward (`num + 1`, `num + 2`, …) until the sequence ends.
- This works because each number is touched only a constant number of times: once when checking if it begins a sequence, and at most once more during forward expansion. Hash set lookups keep all operations constant time, giving a true **O(n)** runtime.
- It outperforms the brute force approach because it avoids sorting (`O(n log n)`) and avoids repeatedly scanning the same consecutive chains. By expanding only from true starting points, it eliminates all redundant work and achieves linear time.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def longestConsecutive(self, nums):
      numsSet = set(nums)
      longest = 0
      for num in numsSet:
          if (num - 1) not in numsSet:
              length = 1
              while (num + length) in numsSet:
                  length +=1
              longest = max(longest, length)
      return longest

```
