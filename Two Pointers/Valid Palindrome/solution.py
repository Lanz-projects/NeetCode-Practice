class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        clean = []
        for char in s:
            if char.isalnum():
                clean.append(char.lower())
        clean = "".join(clean)
        
        start = 0
        end = len(clean) - 1
        while start <= end:
            if clean[start] != clean[end]:
                return False
            start += 1
            end -= 1
        return True