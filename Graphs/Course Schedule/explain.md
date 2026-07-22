# Course Schedule

## 🔍 Problem Summary

You are given a number of courses and a list of prerequisite pairs, where each pair indicates that one course must be completed before another.

Your task is to determine whether it is possible to finish every course. The main challenge is detecting whether the prerequisite relationships contain a cycle, since any cycle makes it impossible to complete all required courses.

---

## 🧠 Key Insight

A course can only be completed if all of its prerequisites can also be completed. If, during a traversal, you encounter a course that is already being explored, you have found a cycle.

Using Depth-First Search (DFS) with a recursion stack allows cycles to be detected efficiently while memoizing completed courses to avoid repeated work.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- For every course, repeatedly explore all prerequisite chains without remembering previously processed results.
- This revisits the same prerequisite paths many times and performs unnecessary work, especially when multiple courses share prerequisites.

### 2. Better Approach

- Build an adjacency list that maps each course to its list of prerequisites.
- Perform a DFS starting from every course.
- Maintain a `visitSet` containing the courses currently in the recursion stack. If a course is encountered that is already in this set, a cycle exists, so return `False`.
- If a course has no remaining prerequisites, it can be completed immediately.
- After successfully processing all prerequisites for a course, remove it from the recursion stack and clear its prerequisite list. This memoizes the result so future DFS calls can return immediately.

Each course and prerequisite is processed at most once, so the algorithm runs in **O(V + E)** time, where `V` is the number of courses and `E` is the number of prerequisite pairs. The adjacency list and recursion stack require **O(V + E)** space.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visitSet = set()

        def dfs(crs):
            if crs in visitSet:
                return False

            if preMap[crs] == []:
                return True

            visitSet.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            visitSet.remove(crs)
            preMap[crs] = []

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True
```
