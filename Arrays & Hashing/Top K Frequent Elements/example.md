# Problem Title

## 🔍 Problem Summary

- Given an int array and int k,
- Return the k most freq eleemnts in any order
- Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

---

## 🧠 Key Insight

The key idea is that we don’t need to fully sort the elements by frequency.  
Instead, we can **bucket** numbers by how often they appear.  
Since frequencies range from 1 to n, a bucket array lets us retrieve the top k elements in linear time.

---

## 🧩 Approaches Considered

### 1. Brute Force

- Count frequencies, then sort the list of (number, frequency) pairs by frequency.
- Sorting dominates the runtime → **O(n log n)**.
- Too slow for the follow‑up requirement, which demands better than O(n log n).

---

### 2. Better Approach (Bucket Sort)

- Count frequencies using a hashmap.
- Create a bucket list where index = frequency and value = list of numbers with that frequency.
- Iterate buckets from highest frequency to lowest, collecting elements until we have k.
- **Time:** O(n)
- **Why it’s better:** Avoids sorting entirely; grouping by frequency lets us extract the top k in linear time.

---

## 🧪 Final Code (Python)

```python
from collections import defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
      counter = defaultdict(int)
      for i in nums:
        counter[i] += 1
      bucket = [[] for _ in range(len(nums) + 1)]
      for i, value in counter.items():
        bucket[value].append(i)
      result = []
      for freq in range(len(bucket)-1, -1, -1):
        for num in bucket[freq]:
          result.append(num)
          if len(result) == k:
            return result
      return []
```
