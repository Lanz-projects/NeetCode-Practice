# Daily Temperatures

## 🔍 Problem Summary

Given an array of daily temperatures, return an array where each element represents **how many days you must wait until a warmer temperature**.

- If a warmer temperature exists in the future, return the number of days until it occurs.
- If no warmer temperature exists, return `0` for that day.

The challenge is to solve this efficiently without repeatedly scanning the remaining temperatures for every day.

---

## 🧠 Key Insight

A brute-force solution looks **forward** from each day to find the next warmer temperature, leading to unnecessary repeated work.

Instead, think about what information actually needs to be remembered while scanning the array.

We only need to keep track of the days that **haven't yet found a warmer future temperature**. As we encounter new temperatures, they can immediately resolve one or more previous days waiting for a warmer temperature.

This naturally leads to using a **monotonic decreasing stack** that stores unresolved temperatures and their indices.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- For every day, scan forward through the remaining temperatures until a warmer day is found.
- Record the number of days waited, or `0` if no warmer day exists.
- This requires checking many future temperatures repeatedly.

Because of the nested scanning, the time complexity is **O(n²)**, which is too slow for large inputs.

### 2. Better Approach

- Maintain a **monotonic decreasing stack** containing pairs of:
  - temperature
  - index
- As you iterate through the temperatures:
  - While the current temperature is warmer than the temperature at the top of the stack:
    - Pop that previous day.
    - Compute the number of days waited using the index difference.
    - Store the result.
  - Push the current temperature and index onto the stack.
- Any indices left in the stack never encounter a warmer day, so their answers remain `0`.

This processes every temperature at most once when pushed and once when popped, giving an efficient linear-time solution.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t, i])

        return res
```
