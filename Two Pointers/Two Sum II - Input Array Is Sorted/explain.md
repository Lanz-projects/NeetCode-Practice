# Two Sum II - Input Array Is Sorted

## 🔍 Problem Summary

A short restatement of the problem **in your own words**.  
Focus on: what is being asked, what the inputs/outputs are, and what the core challenge is.

---

## 🧠 Key Insight

## The array is already **sorted**, which means we can determine whether we need a larger or smaller sum simply by adjusting pointers. This allows us to avoid extra data structures and meet the constant-space requirement. Instead of checking all pairs, we can use a **two-pointer technique**: one pointer at the start and one at the end, moving inward based on whether the current sum is too small or too large.

## 🧩 Approaches Considered

### 1. Brute Force

- Use two nested loops to check every possible pair `(i, j)` where `i < j`.
- For each pair, check whether `numbers[i] + numbers[j] == target`.
- **Why it’s not ideal:**
  - Time complexity is **O(n²)**.
  - Does not take advantage of the sorted property.
  - Too slow for large inputs and unnecessary given the problem constraints.

---

### 2. Optimal Approach — Two Pointers

- Place one pointer at the **start** of the array and one at the **end**.
- Compute the sum of the two pointed values:
  - If the sum is **less than** the target, move the left pointer right to increase the sum.
  - If the sum is **greater than** the target, move the right pointer left to decrease the sum.
  - If the sum matches the target, return the 1-indexed positions.
- **Why it works:**
  - The sorted order ensures predictable behavior when adjusting pointers.
  - We only scan the array once, moving pointers inward.
- **Why it’s better than brute force:**
  - Runs in **O(n)** time.
  - Uses **constant extra space**, as required.
  - Efficient, clean, and leverages the sorted structure perfectly.

---

## 🧪 Final Code (Python)

```python
# your solution here
```
