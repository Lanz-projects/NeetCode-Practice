# Coin Change II

## 🔍 Problem Summary

Given a list of coin denominations and a target amount, determine **how many different combinations** of coins can make up that amount.

You may use each coin denomination **an unlimited number of times**, and the order of coins does **not** matter (e.g., `2 + 1 + 2` is the same combination as `2 + 2 + 1`).

---

## 🧠 Key Insight

Instead of finding the minimum number of coins, we count the number of ways to build each amount.

By processing one coin at a time, we ensure each unique combination is counted exactly once, avoiding duplicate permutations.

---

## 🧩 Approaches Considered

### 1. Brute Force (Recursive)

- For each coin, recursively choose whether to use it or move to the next coin.
- Count every valid combination that reaches the target amount.

**Why it's too slow:**

- Explores many repeated subproblems.
- Time Complexity: **Exponential**

### 2. Better Approach (Dynamic Programming)

- Let `dp[i]` represent the number of ways to make amount `i`.
- Initialize `dp[0] = 1` since there's one way to make amount 0 (choose no coins).
- Process each coin one at a time.
- For every amount that can include the current coin:
  - Add the number of ways to make the remaining amount.

**Why it works:**

- Each coin builds upon combinations formed by previously processed coins.
- Processing coins in the outer loop prevents counting different orderings of the same combination.

**Why it's better than brute force:**

- Time Complexity: **O(amount × number of coins)**
- Space Complexity: **O(amount)**

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(1, amount + 1):
                if i - coin >= 0:
                    dp[i] += dp[i - coin]

        return dp[-1]
```
