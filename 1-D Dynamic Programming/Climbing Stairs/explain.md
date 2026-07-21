# Climbing Stairs

## 🔍 Problem Summary

You are given an integer `n` representing the number of steps in a staircase. At each move, you may climb either `1` or `2` steps.

Your task is to determine how many distinct ways there are to reach the top. The main challenge is recognizing that the number of ways to reach a step depends on the number of ways to reach the previous two steps.

---

## 🧠 Key Insight

To reach a given step, the final move must have come from either one step below or two steps below.

This means the number of ways to reach the current step is simply the sum of the ways to reach the previous two steps, forming the same recurrence as the Fibonacci sequence.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Recursively try taking either one step or two steps from every position until reaching the top.
- This recomputes the same subproblems many times, leading to exponential running time.

### 2. Optimal Approach

- Keep track of the number of ways to reach the previous two steps using two variables.
- Iterate from the bottom of the staircase toward the top, updating these values based on the recurrence relation.
- At each iteration, the current number of ways is the sum of the previous two values.
- By storing only the last two results instead of an entire array, the solution uses constant extra space while still computing the answer efficiently.

The loop processes each step exactly once, so the algorithm runs in **O(n)** time. Since only two variables are maintained throughout the computation, the space complexity is **O(1)**.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one
```
