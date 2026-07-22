# Task Scheduler

## 🔍 Problem Summary

You are given a list of CPU tasks and a cooling interval `n`. The same task cannot be executed again until at least `n` intervals have passed, although the CPU may execute other tasks or remain idle during that time.

Return the minimum number of CPU intervals required to complete every task. The main challenge is scheduling tasks to minimize idle time while always respecting the cooling constraint.

---

## 🧠 Key Insight

At any point, the best task to execute is the one with the highest remaining frequency that is not currently cooling down.

A max-heap efficiently selects the next task with the greatest remaining count, while a queue tracks tasks that are cooling down and the time when they can be executed again. Together, these data structures simulate the Better schedule.

---

## 🧩 Approaches Considered

### 1. Brute Force (if applicable)

- Simulate every possible task ordering while checking whether each task satisfies the cooling requirement.
- Choose the schedule with the fewest idle intervals.
- This approach explores far too many possible schedules and quickly becomes impractical.

### 2. Better Approach

- Count how many times each task appears.
- Store the remaining task frequencies in a max-heap (implemented using negative values).
- Process one CPU interval at a time.
- Remove the task with the highest remaining frequency from the heap and execute it.
- If the task still has remaining occurrences, place it into a queue along with the time when it becomes available again.
- At each interval, check whether the front of the queue has finished cooling. If so, move it back into the heap.
- Continue until both the heap and cooling queue are empty.

The heap always chooses the most valuable available task, while the queue guarantees that tasks cannot be reused before their cooling period expires. Building the frequency map and heap takes **O(m)** time, where `m` is the number of distinct tasks, and each task is inserted and removed from the heap at most once per occurrence. This results in an overall time complexity of **O(n log m)**, where `n` is the total number of tasks, with **O(m)** extra space for the heap, queue, and frequency map.

---

## 🧪 Final Code (Python)

```python
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        queue = deque()  # [-cnt, idleTime]

        while maxHeap or queue:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    queue.append([cnt, time + n])

            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])

        return time
```
