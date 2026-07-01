# Trapping Rain Water

## 🔍 Problem Summary

Given an array where each value represents the height of a vertical bar in an elevation map. After rain falls, water can become trapped between bars if a taller bar exists on both the left and right sides.  
The task is to compute how many total units of water can be trapped across the entire map.

---

## 🧠 Key Insight

Water trapped at any index is determined by the **shorter** of the tallest bars on its left and right.  
If you know:

- the highest bar to the **left** of `i`, and
- the highest bar to the **right** of `i`,

then the water above index `i` is:

This reduces the problem to efficiently tracking left and right maximums — which can be done with a two‑pointer sweep that processes each index exactly once.

---

## 🧩 Approaches Considered

### 1. Brute Force

- For each index, scan leftward to find the tallest bar on the left, and scan rightward to find the tallest bar on the right.
- Compute trapped water using `min(leftMax, rightMax) - height[i]` for every index.
- **Why it’s too slow:**
  - Requires two full scans per index → **O(n²)** time.
  - Recomputes the same left/right maximums repeatedly.
  - Not feasible for large inputs.

---

### 2. Optimal Approach — Two Pointers

- Use two pointers (`l` and `r`) starting at the ends of the array.
- Track running `leftMax` and `rightMax` as you move inward.
- At each step, move the pointer at the **smaller** boundary because that side determines the water level.
- Add trapped water based on the difference between the current height and the corresponding max boundary.
- **Why it works:**
  - The smaller boundary limits the water height; moving the larger boundary cannot increase trapped water.
  - Each index is processed exactly once.
- **Why it’s better than brute force:**
  - Runs in **O(n)** time with **O(1)** extra space.
  - Efficiently maintains left/right maximums without repeated scanning.
  - Scales easily to very large elevation maps.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        result = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                result += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                result += rightMax - height[r]
        return result
```
