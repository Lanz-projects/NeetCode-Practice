# Car Fleet

## 🔍 Problem Summary

You’re given a target mile marker and a set of cars, each with a starting position and a speed.

All cars move toward the target, but no car is allowed to pass another. If a faster car catches up to a slower one, it must slow down and match that car’s speed — forming a car fleet.

A car fleet is defined as:

- A single car, or
- A group of cars that end up traveling together at the speed of the slowest car in the group.

Even if cars only catch up exactly at the target, they still count as part of the same fleet.

Your task is to determine how many distinct fleets reach the target.

---

## 🧠 Key Insight

The important observation is that **a car's arrival time at the target completely determines whether it forms a new fleet or joins an existing one.**

To make this work, process the cars from **closest to the target to farthest away**.

- If a car behind would arrive **sooner** than the fleet ahead, it catches up before reaching the target and becomes part of that fleet.
- If it would arrive **later**, it can never catch the fleet ahead and therefore starts a new fleet.

Instead of simulating movement, we only compare each car's time to reach the target.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Simulate every car moving toward the target over time.
- Continuously check whether faster cars catch slower cars and merge them into fleets.
- This requires repeatedly updating positions and checking collisions, making the simulation unnecessarily complicated and inefficient.

### 2. Optimal Approach

- Pair each car's position with its speed.
- Sort the cars by position so they can be processed from **closest to the target** to **farthest**.
- Compute each car's time to reach the target:
  - `(target - position) / speed`
- Maintain a stack of fleet arrival times.
- For each car:
  - Push its arrival time onto the stack.
  - If its arrival time is **less than or equal to** the fleet ahead, it catches that fleet, so remove it from the stack.
- The remaining times in the stack each represent one distinct fleet.

Because each car is processed once after sorting, the algorithm runs efficiently.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        pair = [[p, s] for p, s in zip(position, speed)]

        stack = []
        for p, s in sorted(pair)[::-1]:
            stack.append(float(target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
```