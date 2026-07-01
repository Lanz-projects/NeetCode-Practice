from collections import defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
      counter = defaultdict(int)
      for i in nums:
        counter[i] += 1
      bucket = [[] for _ in range(len(nums) + 1)]
      for i, value in counter.items():
        bucket[value].append(i)
      result = []
      for freq in range(len(bucket)-1, -1, -1):
        for num in bucket[freq]:
          result.append(num)
          if len(result) == k:
            return result
      return []