# Kth Largest Element In An Array

## 🔍 Problem Summary

Given an integer array `nums` and an integer `k`, return the `k`th largest element in the array.

The answer is based on the array's sorted order, not the `k`th distinct value. The main challenge is finding the desired element efficiently without fully sorting the array.

---

## 🧠 Key Insight

To determine the `k`th largest element, we do not need to keep every value in sorted order. We only need to track the largest `k` elements seen so far.

A min-heap of size `k` makes this efficient because the smallest value in the heap is always the current `k`th largest element.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Sort the entire array in descending order.
- Return the element at index `k - 1`.
- This works, but sorting the entire array takes more time than necessary when only one element is needed.

### 2. Better Approach (Min Heap)

- Create an empty min-heap.
- Iterate through each number in the array and add it to the heap.
- If the heap grows larger than `k`, remove the smallest element.
- After processing every number, the heap contains exactly the largest `k` elements.
- Since the smallest element in the heap is the `k`th largest overall, return the root of the heap.

The heap never stores more than `k` elements, so each insertion or removal takes **O(log k)** time. Processing all `n` elements gives an overall time complexity of **O(n log k)** while using **O(k)** extra space.

---

## ⚡ Alternative Approach: Quick Select

Another common solution is **Quick Select**, which is based on the partition step used in Quick Sort. Instead of sorting the entire array, it repeatedly partitions the array around a pivot until the pivot lands at the index corresponding to the `k`th largest element.

The algorithm converts the problem into finding the `(n - k)`th smallest element, partitions the array, and recursively searches only the side that could contain the answer.

### Complexity

- **Average Time:** **O(n)**
- **Worst-Case Time:** **O(n²)** (when poor pivots are consistently chosen)
- **Space:** **O(n)** (recursive implementation)

### Pros vs. Heap Approach

**Quick Select**

- ✅ Average-case **O(n)**, making it faster for a one-time query.
- ✅ Does not waste time maintaining a heap throughout the search.
- ❌ Worst-case performance is **O(n²)**.
- ❌ Modifies the input array during partitioning.
- ❌ More difficult to implement and reason about correctly.

**Min Heap**

- ✅ Guaranteed **O(n log k)** performance.
- ✅ Easy to implement using Python's `heapq`.
- ✅ Does not rely on pivot quality.
- ✅ Ideal for streaming problems or when elements are processed incrementally.
- ❌ Slightly slower than Quick Select on average for a single query.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        minHeap = []

        for n in nums:
            heapq.heappush(minHeap, n)
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return minHeap[0]
```

---

## 🧪 Alternative Code (Quick Select)

```python
class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l, r):
            pivot, p = nums[r], l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1

            nums[p], nums[r] = nums[r], nums[p]

            if p > k:
                return quickSelect(l, p - 1)
            elif p < k:
                return quickSelect(p + 1, r)
            else:
                return nums[p]

        return quickSelect(0, len(nums) - 1)
```
