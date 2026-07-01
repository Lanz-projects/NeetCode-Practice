from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
      groups = defaultdict(list)
      
      for word in strs:
        key = tuple(sorted(word))
        groups[key].append(word)
      
      return list(groups.values())
      