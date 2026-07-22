# Coin Change

## 🔍 Problem Summary

You are given an array `coins` representing different coin denominations and an integer `amount` representing the target value you want to make.

Your task is to return the minimum number of coins needed to make up the target amount. If it is impossible to form the amount using the given coins, return `-1`. The main challenge is efficiently finding the Better combination without trying every possible set of coins.

---

## 🧠 Key Insight

The minimum number of coins needed for a given amount can be built from the solutions to smaller amounts.

By computing the answer for every amount from `0` up to the target, each new value can be determined using previously computed results instead of repeatedly solving the same subproblems.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Recursively try every possible combination of coins until the target amount is reached.
- Since many of the same amounts are recomputed repeatedly, this approach has exponential running time and becomes impractical for larger targets.

### 2. Better Approach

- Create a dynamic programming array where `dp[i]` stores the minimum number of coins needed to make amount `i`.
- Initialize every value to an impossible large number, except `dp[0]`, which is `0` because no coins are needed to make an amount of zero.
- Iterate through every amount from `1` to the target.
- For each amount, try every coin denomination. If the coin can contribute to the current amount, update the minimum using `1 + dp[amount - coin]`.
- After filling the table, check whether the target amount was successfully updated. If not, return `-1`; otherwise, return the minimum number of coins stored for the target.

The dynamic programming table has `amount + 1` entries, and each entry considers every coin denomination, resulting in **O(amount × number of coins)** time. The DP array stores one value for each amount, so the space complexity is **O(amount)**.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return dp[amount] if dp[amount] != amount + 1 else -1
```
