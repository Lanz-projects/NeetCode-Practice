from collections import defaultdict

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False

        s1Count = defaultdict(int)
        window = defaultdict(int)

        for char in s1:
            s1Count[char] += 1

        l = 0

        for r in range(len(s2)):
            window[s2[r]] += 1

            if r - l + 1 > len(s1):
                window[s2[l]] -= 1
                if window[s2[l]] == 0:
                    del window[s2[l]]
                l += 1

            if window == s1Count:
                return True

        return False