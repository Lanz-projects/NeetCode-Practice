class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key = lambda i: i[0])
        outputs = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = outputs[-1][1]

            if start <= lastEnd:
                outputs[-1][1] = max(lastEnd, end)
            else:
                outputs.append([start,end])
        return outputs