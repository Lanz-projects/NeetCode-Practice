# Largest Rectangle in Histogram

## 🔍 Problem Summary

Given an array of integers `heights`, where each value represents the height of a histogram bar and each bar has a width of `1`, return the area of the **largest rectangle** that can be formed within the histogram.

The rectangle must consist of one or more consecutive bars, and its height is limited by the shortest bar included.

---

## 🧠 Key Insight

The key observation is that **every bar can potentially be the shortest bar in the largest rectangle.**

The challenge is determining how far each bar can extend to the left and right before encountering a shorter bar.

A **monotonic increasing stack** lets us efficiently track bars whose rectangles haven't been finalized yet. As soon as we encounter a shorter bar, we know exactly where the taller bars must end, allowing us to compute their maximum possible areas.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- For every bar, expand left and right until a shorter bar is encountered.
- Compute the rectangle area using that width and keep track of the maximum.
- Since this expansion is repeated for every bar, the overall time complexity is **O(n²)**.

### 2. Optimal Approach

- Maintain a **monotonic increasing stack** storing pairs of:
  - starting index
  - height
- As you iterate through the histogram:
  - If the current bar is shorter than the top of the stack, repeatedly pop taller bars.
  - For each popped bar:
    - Calculate its rectangle area using the current index as the right boundary.
    - Update the maximum area.
    - Carry its starting index forward so the current shorter bar can extend farther left.
- Push the current bar with its appropriate starting index.
- After processing all bars, compute the remaining rectangle areas using the end of the histogram as the right boundary.

Each bar is pushed and popped at most once, making the algorithm highly efficient.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea
```