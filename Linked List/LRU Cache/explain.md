# LRU Cache

## 🔍 Problem Summary

Design a data structure that supports the following operations in **O(1)** average time:

- `get(key)` returns the value associated with the key if it exists; otherwise returns `-1`.
- `put(key, value)` inserts or updates a key-value pair. If the cache exceeds its capacity, remove the **least recently used (LRU)** item.

The challenge is efficiently tracking both:

- Fast key lookups.
- The order in which items were most recently accessed.

---

## 🧠 Key Insight

No single data structure can efficiently support both requirements.

Instead, combine:

- A **hash map** for **O(1)** access to nodes by key.
- A **doubly linked list** to maintain usage order.

The linked list stores items from:

```
Left  -> Least Recently Used (LRU)
Right -> Most Recently Used (MRU)
```

Whenever a key is accessed or updated, move its node to the right end of the list. When the cache is full, remove the node at the left end.

---

## 🧩 Approaches Considered

### 1. Brute Force

- Store all key-value pairs in a list.
- On every `get()` or `put()`, search the list for the key.
- Move recently used items to the end of the list.
- When the cache is full, remove the first element.
- Since searching and moving elements both require linear time, operations take **O(n)**, which does not satisfy the problem requirements.

### 2. Optimal Approach

- Store each key in a hash map that points to its corresponding node in a doubly linked list.
- The linked list maintains items in order of recent use:
  - Left side = Least Recently Used.
  - Right side = Most Recently Used.
- For `get(key)`:
  - If the key exists, remove its node from its current position.
  - Reinsert it at the right end.
  - Return its value.
- For `put(key, value)`:
  - If the key already exists, remove the old node.
  - Insert the updated node at the right end.
  - If the cache exceeds its capacity:
    - Remove the leftmost node (the least recently used).
    - Delete its entry from the hash map.
- Using dummy head and tail nodes simplifies insertion and removal by eliminating edge cases.

Every operation on the hash map and doubly linked list takes **O(1)** time, so both `get()` and `put()` satisfy the required **O(1)** average time complexity.

---

## 🧪 Final Code (Python)

```python
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.cache = {}

        # Left = LRU, Right = Most Recent
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    # Remove a node from the linked list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # Insert a node at the right (most recently used)
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val

        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # Remove the least recently used node
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)
```
