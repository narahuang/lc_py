class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        result = []
        intervals.sort()
        left = intervals[0][0]
        right = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0] <= right:
                right = max(right, interval[1])
            else:
                result.append([left, right])
                left = interval[0]
                right = interval[1]
        result.append([left, right])
        return result
