# Container With Most Water

## 🔍 Problem Summary

You’re given an array where each element represents the height of a vertical line drawn at that index. By choosing any two lines, they form the sides of a container, and the x‑axis acts as the base. Your goal is to pick the pair of lines that traps the maximum amount of water, which depends on both the distance between the lines and the shorter line’s height. You must return that maximum possible area.

---

## 🧠 Key Insight

The amount of water between two lines is determined by:

# Area

(right index−left index)×min⁡(height[left],height[right])
To maximize this, you don’t need to check every pair. The key observation is:

The limiting factor is always the shorter line.

Therefore, if you want a better chance at increasing the area, you should move the pointer at the shorter line inward, hoping to find a taller line that increases the minimum height.

## 🧩 Approaches Considered

### 1. Brute Force

- Check every possible pair of lines `(i, j)` and compute the container area using  
  `(j - i) * min(height[i], height[j])`.
- Track the maximum area found across all pairs.
- **Why it’s not ideal:**
  - Time complexity is **O(n²)** — far too slow for arrays up to 100,000 elements.
  - Wastes time checking pairs that cannot possibly improve the result.
  - Does not use any insight about how area changes when pointers move.

---

### 2. Optimal Approach — Two Pointers

- Place one pointer at the **left** end and one at the **right** end of the array.
- Compute the area formed by the two lines.
- Move the pointer at the **shorter** line inward, since the shorter height limits the area.
- Continue updating the maximum area while adjusting pointers.
- **Why it works:**
  - The minimum of the two heights determines the container’s height; moving the taller line cannot increase this minimum.
  - Always moving the shorter line maximizes the chance of finding a taller line and increasing the area.
  - Ensures all meaningful candidate pairs are explored.
- **Why it’s better than brute force:**
  - Runs in **O(n)** instead of O(n²).
  - Uses a mathematically sound rule to avoid unnecessary checks.
  - Clean, efficient, and scales to very large inputs.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = (r - l) * min(height[l],height[r])
            result = max(result, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return result
```
