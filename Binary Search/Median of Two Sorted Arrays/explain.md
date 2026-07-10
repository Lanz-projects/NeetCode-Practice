# Median of Two Sorted Arrays

## 🔍 Problem Summary

Given two sorted arrays `nums1` and `nums2`, return the **median** of the combined sorted array.

The challenge is that you **cannot simply merge the arrays**, since that would take **O(m + n)** time. Instead, the solution must run in **O(log(m + n))** time.

---

## 🧠 Key Insight

Instead of merging the arrays, we can **binary search the smaller array** to find a partition where:

- Every element on the left side is less than or equal to every element on the right side.
- The left partition contains exactly half of the combined elements.

Once the correct partition is found, the median can be computed directly from the elements surrounding the partition.

---

## 🧩 Approaches Considered

### 1. Brute Force

- Merge both sorted arrays into one sorted array.
- Return the middle element (or average of the two middle elements for an even-length array).
- While straightforward, merging requires **O(m + n)** time, which does not satisfy the required logarithmic runtime.

### 2. Optimal Approach

- Always perform binary search on the **smaller array** to minimize the search space.
- Partition both arrays so that:
  - The left partitions contain half of the total elements.
  - Every value on the left is less than or equal to every value on the right.
- At each binary search step:
  - Compute the partition indices for both arrays.
  - Compare the values surrounding each partition.
  - If the partition is invalid, move the search left or right accordingly.
- Once the correct partition is found:
  - If the total number of elements is odd, the median is the smallest value on the right side.
  - If the total number of elements is even, the median is the average of the largest value on the left side and the smallest value on the right side.

By only binary searching the smaller array, the algorithm achieves **O(log(min(m, n)))** time complexity, which satisfies the required **O(log(m + n))** runtime.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1

        while True:
            i = (l + r) // 2  # Partition in A
            j = half - i - 2  # Partition in B

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # Correct partition found
            if Aleft <= Bright and Bleft <= Aright:
                # Odd total length
                if total % 2:
                    return min(Aright, Bright)

                # Even total length
                return float(max(Aleft, Bleft) + min(Aright, Bright)) / 2

            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
```