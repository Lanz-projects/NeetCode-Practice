from collections import defaultdict
class Solution(object):
    def isAnagram(self, s, t):
      if len(s) != len(t):
        return False
      
      counter1 = defaultdict(int)
      counter2 = defaultdict(int)
      
      for i in s:
        counter1[i] += 1
      for i in t:
        counter1[t] += 1  
        
      return counter1 == counter2