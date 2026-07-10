# Koko Eating Bananas

## 🔍 Problem Summary

Koko has `n` piles of bananas, where `piles[i]` is the number of bananas in the *i*-th pile.

She has `h` hours before the guards return, and she must finish all the bananas before then.

Koko chooses an eating speed `k` (bananas per hour). Each hour:

- She picks one pile.
- She eats `k` bananas from that pile.
- If the pile has fewer than `k` bananas, she eats the entire pile and does nothing else for that hour.

Koko wants to eat **as slowly as possible** while still finishing every pile within `h` hours.

Your task is to return the **minimum integer eating speed `k`** that allows her to finish on time.

---

## 🧠 Key Insight

The key observation is that **the answer isn't one of the piles—it's a speed.**

As the eating speed increases:

- The total number of hours needed can only stay the same or decrease.
- This creates a **monotonic relationship**, making the possible speeds searchable with binary search.

Instead of searching through the piles, we binary search the range of possible speeds and determine whether a given speed is fast enough.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Try every possible eating speed from `1` up to the largest pile.
- For each speed, compute how many hours Koko would need to finish all piles.
- Return the first speed that finishes within `h` hours.
- While correct, this can require checking many unnecessary speeds, making it inefficient for large inputs.

### 2. Optimal Approach

- The minimum possible speed is `1`, and the maximum possible speed is the size of the largest pile.
- Use binary search over this range of possible speeds.
- For each candidate speed:
  - Compute the total hours required by summing `ceil(pile / speed)` for every pile.
  - If the total hours are less than or equal to `h`, the speed works, so try searching for an even smaller speed.
  - Otherwise, search for a larger speed.
- Continue until the smallest valid speed is found.

Each binary search step checks all piles once, resulting in an efficient solution with time complexity **O(n log m)**, where `m` is the size of the largest pile.

---

## 🧪 Final Code (Python)

```python
import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            hours = 0

            for p in piles:
                hours += math.ceil(float(p) / k)

            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1

        return res
```