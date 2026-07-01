class Solution(object):
    def twoSum(self, nums, target):
      map = {}
      for index, value in enumerate(nums):
          complement = target - value
          if complement in map:
              return [map[complement], index]
          else:
              map[value] = index
      return []