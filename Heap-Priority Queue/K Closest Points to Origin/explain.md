# K Closest Points to Origin

## 🔍 Problem Summary

Given an array of points on a 2D plane and an integer `k`, return the `k` points that are closest to the origin `(0, 0)`.

The distance between points is measured using the Euclidean distance, but since only relative distances matter, comparing squared distances is sufficient. The main challenge is efficiently finding the `k` closest points without repeatedly searching the entire array.

---

## 🧠 Key Insight

Each point's distance from the origin can be computed independently, making a min-heap a natural choice for retrieving the closest points.

By storing each point along with its squared distance in a min-heap, we can always remove the nearest point in logarithmic time until we have collected `k` results.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Compute the distance for every point and sort the entire array by distance.
- Return the first `k` points after sorting.
- While correct, sorting all points performs more work than necessary when only the closest `k` points are needed.

### 2. Optimal Approach

- Compute the squared distance (`x² + y²`) for each point and store it with the point in a min-heap.
- Build the heap using all points.
- Repeatedly remove the smallest element from the heap until `k` points have been collected.
- Add each extracted point to the result list and return the completed list.

Using squared distances avoids the unnecessary square root calculation while preserving the correct ordering of distances. Building the heap takes **O(n)** time, and removing the closest point `k` times takes **O(k log n)** time, giving an overall complexity of **O(n + k log n)**. The heap requires **O(n)** additional space.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        minHeap = []

        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])

        heapq.heapify(minHeap)

        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1

        return res
```