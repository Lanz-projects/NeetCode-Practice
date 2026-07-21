# Min Cost Climbing Stairs

## 🔍 Problem Summary

You are given an array `cost` where `cost[i]` represents the cost of stepping on the `i`th stair. After paying the cost of a step, you may climb either one or two stairs at a time.

You may begin on step `0` or step `1`. Your task is to determine the minimum total cost required to reach the top of the staircase. The main challenge is choosing the cheapest sequence of one-step and two-step moves.

---

## 🧠 Key Insight

The minimum cost to reach a given step depends only on the minimum costs of the next one or two steps.

By working backward from the top, each step can be updated to store the minimum total cost required to reach the end from that position.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Recursively try both possible moves (one step or two steps) from every position and compute the total cost for each path.
- This repeatedly solves the same subproblems, resulting in exponential running time.

### 2. Optimal Approach

- Append a `0` to the end of the array to represent reaching the top without paying an additional cost.
- Traverse the array backward, updating each step's cost by adding the smaller of the costs from the next one or two steps.
- After the traversal, each element stores the minimum cost needed to reach the top starting from that step.
- Since you may begin on either step `0` or step `1`, return the smaller of those two values.

Each step is processed exactly once, so the algorithm runs in **O(n)** time. Because the input array is updated in place without using additional data structures, the extra space complexity is **O(1)**.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.append(0)

        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])
```
