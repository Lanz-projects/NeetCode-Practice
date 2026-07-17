# Hand of Straights

## 🔍 Problem Summary

You are given an array of card values and an integer `groupSize`. Determine whether all of the cards can be rearranged into groups of exactly `groupSize` consecutive values.

Each card must be used exactly once. The main challenge is ensuring that every group starts with the smallest available card while correctly handling duplicate values.

---

## 🧠 Key Insight

Every valid group must begin with the smallest unused card.

By keeping track of each card's frequency and always starting from the current smallest value, you can greedily build consecutive groups. If any required card is missing or cards are removed out of order, forming valid groups becomes impossible.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Try every possible way to partition the cards into groups of consecutive values.
- Verify whether every card is used exactly once.
- This explores far too many possible arrangements and is not feasible for large inputs.

### 2. Optimal Approach

- First, check whether the total number of cards is divisible by `groupSize`. If not, immediately return `False`.
- Count the frequency of every card value using a hash map.
- Store all unique card values in a min-heap so the smallest available card can always be accessed efficiently.
- While the heap is not empty, begin a new group using the smallest remaining card.
- For each value in the consecutive sequence:
  - Verify the card exists.
  - Decrease its frequency.
  - If its count reaches zero, it must also be the smallest value in the heap before removing it. Otherwise, the cards cannot be grouped correctly.
- If every group is successfully formed, return `True`.

Using a frequency map together with a min-heap guarantees groups are always built from the smallest available card, preventing invalid ordering. Building the frequency map takes **O(n)** time, while heap operations result in an overall time complexity of **O(n log n)**. The algorithm uses **O(n)** additional space for the hash map and heap.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if len(hand) % groupSize:
            return False

        count = {}
        for i in hand:
            count[i] = 1 + count.get(i, 0)

        minHeap = list(count.keys())
        heapq.heapify(minHeap)

        while minHeap:
            first = minHeap[0]

            for i in range(first, first + groupSize):
                if i not in count:
                    return False

                count[i] -= 1

                if count[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)

        return True
```
