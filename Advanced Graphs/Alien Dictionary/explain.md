# Alien Dictionary

## 🔍 Problem Summary

You are given a list of words that are already sorted according to the rules of an unknown alien language. Your task is to determine one valid ordering of the alien alphabet.

If the given word ordering is impossible (for example, a longer word appears before its own prefix), return an empty string. If multiple valid character orders exist, returning any one of them is acceptable.

---

## 🧠 Key Insight

The ordering of characters can be represented as a **directed graph**, where an edge `a → b` means character `a` must come before character `b`.

Once this graph is built, the problem becomes a **topological sort**. A DFS-based topological sort can also detect cycles—if a cycle exists, there is no valid character ordering.

---

## 🧩 Approaches Considered

### 1. Brute Force

- Try every possible ordering of the unique characters.
- Check whether each ordering correctly sorts all of the given words.
- Return the first valid ordering found.
- Far too slow since there are `k!` possible character orderings.

### 2. Better Approach

- Build a graph containing every unique character.
- Compare each pair of adjacent words:
  - The first differing characters determine an ordering constraint.
  - If the first word is longer but is a prefix of the second, the ordering is invalid.
- Perform a DFS-based topological sort.
- Use a `visited` map to detect cycles:
  - `True` = currently visiting (cycle detection)
  - `False` = fully processed
- Reverse the DFS finishing order to obtain the alien alphabet.

---

## ⏱️ Time & Space Complexity

- **Time:** **O(C + N × L)**
  - `C` = number of unique characters.
  - `N × L` = comparing adjacent words (`L` is average word length).
  - DFS visits every character and edge once.

- **Space:** **O(C + E)**
  - Graph stores all character relationships.
  - Visited map and recursion stack require additional space.

---

## 🧪 Final Code (Python)

```python
class Solution:
    def foreignDictionary(self, words):
        adj = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visited = {} # True = curr exploring, False = fully processed
        res = []

        def dfs(char):
            if char in visited:
                return visited[char]

            visited[char] = True

            for neighChar in adj[char]:
                if dfs(neighChar):
                    return True

            visited[char] = False
            res.append(char)

        for char in adj:
            if dfs(char):
                return ""

        res.reverse()
        return "".join(res)
```
