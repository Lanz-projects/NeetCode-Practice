# Course Schedule II

## 🔍 Problem Summary

You are given a number of courses and a list of prerequisite pairs, where each pair specifies that one course must be completed before another.

Your task is to return a valid order in which all courses can be completed. If no such ordering exists because of a cycle in the prerequisite graph, return an empty list. The main challenge is producing a valid topological ordering while detecting cycles.

---

## 🧠 Key Insight

A course should only be added to the final ordering after all of its prerequisites have already been processed.

Using a Depth-First Search (DFS), you can detect cycles with a recursion stack while building the course order by adding each course only after its prerequisite chain has been fully explored.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Try every possible ordering of the courses and check whether it satisfies all prerequisite relationships.
- The number of possible orderings grows extremely quickly, making this approach impractical even for small inputs.

### 2. Better Approach

- Build an adjacency list that maps each course to its list of prerequisites.
- Perform a DFS from every course while maintaining two sets:
  - `cycle` tracks the courses currently in the recursion stack to detect cycles.
  - `visit` tracks courses that have already been fully processed.
- If a course is encountered that is already in the `cycle` set, a cycle exists, so return an empty list.
- After all prerequisites for a course have been processed successfully, remove it from the recursion stack, mark it as visited, and append it to the output list.
- Once every course has been explored, the output list represents a valid order in which all courses can be completed.

Each course and prerequisite is visited at most once, so the algorithm runs in **O(V + E)** time, where `V` is the number of courses and `E` is the number of prerequisite pairs. The adjacency list, recursion stack, visited sets, and output list require **O(V + E)** space.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        output = []
        visit, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False

            if crs in visit:
                return True

            cycle.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return output
```
