# Decode Ways

## 🔍 Problem Summary

You are given a string of digits representing an encoded message, where `"1"` maps to `'A'`, `"2"` to `'B'`, ..., and `"26"` to `'Z'`.

Your task is to determine how many different ways the entire string can be decoded. The main challenge is deciding whether to decode one digit or two digits at each position while correctly handling invalid cases such as numbers with leading zeros.

---

## 🧠 Key Insight

At every position in the string, there are at most two valid choices: decode the current digit by itself or decode the current and next digits together if they form a number between `10` and `26`.

By working backward through the string, we can compute the number of decoding ways from each position using the results already calculated for later positions.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Recursively try decoding one digit and two digits whenever both are valid.
- This repeatedly solves the same suffixes of the string, resulting in exponential running time.

### 2. Better Approach

- Use dynamic programming to store the number of decoding ways starting from each index.
- Initialize the base case by setting the position after the end of the string to `1`, representing one valid way to decode an empty suffix.
- Traverse the string from right to left.
- If the current character is `'0'`, there are no valid decodings starting from that position.
- Otherwise, begin with the number of ways obtained by decoding the current digit alone.
- If the current digit and the next digit form a valid number between `10` and `26`, add the number of ways from two positions ahead.
- After processing the entire string, the value stored at index `0` is the total number of valid decodings.

Each character is processed exactly once, so the algorithm runs in **O(n)** time. The dynamic programming table stores one value per index, resulting in **O(n)** space complexity.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = {len(s): 1}

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if (
                i + 1 < len(s)
                and (
                    s[i] == "1"
                    or s[i] == "2" and s[i + 1] in "0123456"
                )
            ):
                dp[i] += dp[i + 2]

        return dp[0]
```
