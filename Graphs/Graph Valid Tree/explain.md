# Graph Valid Tree

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
class Solution:
    def validTree(self, n: int, edges):
      if not n:
        return True

      adj = { i:[] for i in range(n) }
      for n1, n2 in edges:
        adj[n1].append(n2)
        adj[n2].append(n1)

      visit = set()
      def dfs(i, prev):
        if i in visit:
          return False
        visit.add(i)

        for j in adj[i]:
          if j == prev:
            continue
          if not dfs(j, i):
            return False
        return True
      return dfs(0, -1) and n == len(visit)
```
