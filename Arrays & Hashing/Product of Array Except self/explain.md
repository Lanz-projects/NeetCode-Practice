# Product of Array Except Self

## 🔍 Problem Summary

- Given an int aray (nums)
- Return an array (answer), where answer[i] is equal to product of all elemnts of given array
- Except nums[i]
- You must write an algorithm that runs in O(n) time and without using the division operation.

---

## 🧠 Key Insight

The key idea is that for each index `i`, the answer is:

product of all elements **to the left** of `i`  
×  
product of all elements **to the right** of `i`

Instead of recomputing these products from scratch for every index (which leads to O(n²)), we can **precompute all left products in one pass** and **all right products in another pass**, then combine them. This lets us reuse work and achieve O(n) time without using division.

---

## 🧩 Approaches Considered

### 1. Brute Force

- For each index `i`, compute the product of all elements **before** `i` and all elements **after** `i`.
- This requires two inner loops for every `i`:  
  one loop from `0 → i-1` and another from `i+1 → end`.
- **Time:** O(n²) because for each of the n positions, we scan almost the entire array again.
- **Why it’s not ideal:** We repeatedly recompute products from scratch for every index, doing a lot of duplicated work.

### 2. Optimal Approach (Prefix + Suffix Products)

- Build a `result` array where `result[i]` initially stores the **product of all elements to the left**.
- Then traverse from the right, maintaining a running suffix product, and multiply it into `result[i]`.
- **Time:** O(n)
- **Space:** O(1) extra (output array doesn’t count)
- **Why it’s better:** No repeated work, no division, handles zeros naturally.

---

## 🧪 Final Code (Python)

```python
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        result = [1] * n

        # Prefix products
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        # Suffix products
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result
```