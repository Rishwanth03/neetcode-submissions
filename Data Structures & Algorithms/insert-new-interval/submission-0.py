class Solution:
    def insert(self, intervals, newInterval):
        result = []

        new_start, new_end = newInterval

        for start, end in intervals:

            # 1. Current interval is completely before newInterval
            if end < new_start:
                result.append([start, end])

            # 2. Current interval is completely after newInterval
            elif start > new_end:
                result.append([new_start, new_end])
                new_start, new_end = start, end

            # 3. Intervals overlap
            else:
                new_start = min(new_start, start)
                new_end = max(new_end, end)

        # Add newInterval / merged interval
        result.append([new_start, new_end])

        return result