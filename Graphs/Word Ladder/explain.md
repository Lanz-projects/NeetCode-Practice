# Word Ladder

## 🔍 Problem Summary

You are given a starting word, an ending word, and a dictionary of valid words. You may transform one word into another by changing exactly one letter at a time, and every intermediate word must exist in the dictionary.

Your task is to determine the length of the shortest transformation sequence from the beginning word to the ending word. If no valid sequence exists, return `0`. The main challenge is efficiently finding neighboring words without comparing every pair of words.

---

## 🧠 Key Insight

Instead of checking every word to see if it differs by one letter, group words by intermediate patterns where one character is replaced with `'*'`.

Words that share the same pattern differ by only one letter in that position. This allows a Breadth-First Search (BFS) to quickly discover all valid transformations while guaranteeing the shortest sequence.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- For each word visited, compare it against every word in the dictionary to find those that differ by exactly one character.
- This requires many repeated comparisons, making the search much slower as the dictionary grows.

### 2. Optimal Approach

- First, build a mapping from wildcard patterns (such as `"h*t"` or `"*ot"`) to all words that match each pattern.
- Add the `beginWord` to the dictionary so it participates in the same pattern mapping.
- Perform a Breadth-First Search (BFS) starting from the `beginWord`.
- For each word removed from the queue, generate all of its wildcard patterns and visit every neighboring word associated with those patterns.
- Track visited words to avoid revisiting them, and process the BFS level by level. The first time the `endWord` is reached is guaranteed to be the shortest transformation sequence.

Building the pattern map takes **O(N × L)** time, where `N` is the number of words and `L` is the word length. The BFS also runs in **O(N × L)** time, giving an overall time complexity of **O(N × L)**. The pattern map, queue, and visited set require **O(N × L)** space.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0

        nei = collections.defaultdict(list)

        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                nei[pattern].append(word)

        visit = set([beginWord])
        q = collections.deque([beginWord])
        res = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return res

                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]

                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)

            res += 1

        return 0
```
