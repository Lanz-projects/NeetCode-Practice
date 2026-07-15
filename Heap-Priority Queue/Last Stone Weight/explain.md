# Last Stone Weight

## 🔍 Problem Summary

You are given an array where each element represents the weight of a stone. On each turn, the two heaviest stones are smashed together.

If the stones have equal weight, both are destroyed. Otherwise, the lighter stone is destroyed and the heavier stone is replaced with the difference of their weights. Return the weight of the final remaining stone, or `0` if no stones remain. The main challenge is efficiently finding and updating the two heaviest stones after each smash.

---

## 🧠 Key Insight

The only stones that matter on each turn are the two heaviest ones, making a priority queue the ideal data structure.

Since Python's `heapq` implements a min-heap, storing the stone weights as negative values allows it to behave like a max-heap. This lets us repeatedly remove the two largest stones and insert the remaining difference efficiently.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Repeatedly sort the array to find the two heaviest stones.
- Smash them together, update the array, and repeat until one or no stones remain.
- This approach performs unnecessary sorting after every operation, making it inefficient.

### 2. Optimal Approach

- Convert every stone weight to a negative value and build a heap.
- On each iteration, remove the two largest stones by popping the two smallest negative values.
- If the stones have different weights, push the negative value representing their difference back into the heap.
- Continue until at most one stone remains.
- If the heap is empty, return `0`; otherwise, return the absolute value of the remaining stone.

Building the heap takes **O(n)** time, and each smash performs heap operations that take **O(log n)** time. Since there can be at most `n - 1` smashes, the overall time complexity is **O(n log n)**, while the heap requires **O(n)** space.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])
```
