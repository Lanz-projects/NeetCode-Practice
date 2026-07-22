# Cheapest Flights Within K Stops

## 🔍 Problem Summary

You are given a list of flights between cities, where each flight has a cost. Starting from a source city, find the **cheapest price** to reach a destination city using **at most `k` stops**.

If there is no valid route within the allowed number of stops, return `-1`.

---

## 🧠 Key Insight

This problem can be solved using a modified **Bellman-Ford Algorithm**.

Normally, Bellman-Ford relaxes all edges `n - 1` times to find the shortest paths. Here, we're only allowed to use at most `k + 1` flights (which corresponds to `k` stops), so we only perform **`k + 1` rounds of edge relaxation**.

Using a temporary copy of the prices array each round ensures that each iteration only uses paths with the allowed number of flights.

---

## 🧩 Approaches Considered

### 1. Brute Force

- Explore every possible path from the source to the destination.
- Track the total cost and number of stops.
- Return the cheapest valid path.
- Too slow because the number of possible routes grows exponentially.

### 2. Better Approach

- Initialize the minimum price to every city as infinity, except the source.
- Perform **`k + 1` iterations**:
  - Copy the current prices array.
  - Relax every flight using the prices from the previous iteration.
- Using a temporary array prevents a path from using more than one newly updated edge during the same iteration.
- After all iterations, the destination's price is the minimum cost using at most `k` stops.

---

## ⏱️ Time & Space Complexity

- **Time:** **O((K + 1) × E)**
  - Perform `k + 1` passes over all `E` flights.

- **Space:** **O(N)**
  - Store the current and temporary price arrays.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrices = prices[:]

            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue

                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p

            prices = tmpPrices

        return -1 if prices[dst] == float("inf") else prices[dst]
```
