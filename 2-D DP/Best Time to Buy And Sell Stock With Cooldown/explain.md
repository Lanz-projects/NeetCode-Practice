# Best Time to Buy And Sell Stock With Cooldown

## 🔍 Problem Summary

A short restatement of the problem **in your own words**.  
Focus on: what is being asked, what the inputs/outputs are, and what the core challenge is.

---

## 🧠 Key Insight

The single most important idea that unlocks the solution.  
(Example: “We need fast membership checks → use a set.”)

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- One or two bullets describing how it works
- Why it’s too slow or not ideal

### 2. Better Approach

- The strategy you chose
- Why it works
- Why it’s better than brute force

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # State: Buying or Selling?
        # If Buy: i + 1
        # If Sell: i + 2 (needed for a cooldown day)

        dp = {} # key= (i, buying) val= max_profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i,buying)]
            
            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy,cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell,cooldown)
            return dp[(i,buying)]
        return dfs(0, True)
```
