# Best Time to Buy and Sell Stock

## 🔍 Problem Summary

You are given an array where `prices[i]` represents the price of a stock on the _i_-th day.

You may complete **exactly one transaction** by buying on one day and selling on a later day.

Return the **maximum profit** you can earn. If no profitable transaction is possible, return `0`.

The main challenge is finding the best buy and sell days in a single pass through the array.

---

## 🧠 Key Insight

As you scan through the prices, keep track of the **lowest price seen so far** (the best day to buy).

For each new price, calculate the profit you would make if you sold on that day. Update the maximum profit whenever you find a better one.

This allows us to find the answer in one pass without checking every possible pair of days.

---

## 🧩 Approaches Considered

### 1. Brute Force

- Try every possible pair of buy and sell days.
- For each pair where the sell day comes after the buy day, calculate the profit.
- Return the largest profit found.
- This requires checking every pair of days, resulting in **O(n²)** time complexity.

### 2. Optimal Approach

- Use two pointers:
  - `l` represents the best day to buy (lowest price seen so far).
  - `r` scans through future days looking for selling opportunities.
- If the current selling price is higher than the buying price:
  - Calculate the profit and update the maximum profit.
- If a lower price is found:
  - Move the buy pointer to the current day since it provides a better buying opportunity.
- Continue until every day has been processed.

This solution only traverses the array once, giving a time complexity of **O(n)** with **O(1)** extra space.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1

        return maxP
```
